from datetime import date

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth, ExtractMonth
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from .models import Company, People, Project, FinishedProject
from .serializers import *
from knox.auth import TokenAuthentication as KnoxTokenAuthentication
from knox.models import AuthToken
import os


class CompanyApiView(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'role': request.data.get('role'),
            'email': request.data.get('email'),
            'phone': request.data.get('phone'),
            'address': request.data.get('address'),
        }
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'failed', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CompanyByRoleList(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CompanySerializer

    def get(self, request, role):
        try:
            companies = Company.objects.filter(role=role)
            serializer = CompanySerializer(companies, many=True)
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'failed', 'data': []}, status=status.HTTP_204_NO_CONTENT)


class CompanyApiDetailView(APIView):
    # authentication_classes = [KnoxTokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
            serializer = CompanySerializer(company, many=False)
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'failed', 'data': []}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
            company.delete()
            return Response({'status': 'success', 'data': []}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'failed', 'data': []}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        instance = Company.objects.get(pk=pk)
        if not instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name', None),
            'email': request.data.get('email', None),
            'phone': request.data.get('phone', None),
            'address': request.data.get('address', None),

        }
        non_empty_data = {}
        for key, value in data.items():
            if value:
                non_empty_data[key] = value
        serializer = CompanySerializer(instance=instance, data=non_empty_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeopleApiView(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email'),
            'phone': request.data.get('phone'),
            'company': request.data.get('company')
        }
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'failed', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PeopleApiDetailView(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        try:
            person = People.objects.get(pk=pk)
            serializer = PeopleSerializer(person, many=False)
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'failed', 'data': []}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        try:
            person = People.objects.get(pk=pk)
            person.delete()
            return Response({'status': 'success', 'data': []}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'failed', 'data': []}, status=status.HTTP_204_NO_CONTENT)


class ProjectApiView(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        user = None
        if token:
            token = token.split(" ")[1]
            user = AuthToken.objects.get(token_key=token[0:8]).user
        role = None
        if user:
            role = user.role

        if role == 1:
            projects = Project.objects.all()
        elif role == 2:
            projects = Project.objects.filter(registered_by=user)
        serializer = ProjectSerializer(projects, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        user = None
        if token:
            token = token.split(" ")[1]
            user = AuthToken.objects.get(token_key=token[0:8]).user
        data = {
            'client': request.data.get('client'),
            'partner': request.data.get('partner'),
            'registration_date': request.data.get('registration_date'),
            'exp_end_date': request.data.get('exp_end_date'),
            'tender_date': request.data.get('tender_date'),
            'info': request.data.get('info'),
            'count': request.data.get('count'),
            'client_contact': request.data.get('client_contact'),
            'partner_contact': request.data.get('partner_contact'),
            'product': request.data.get('product'),
            'budget': request.data.get('budget'),
            'poc_request': request.data.get('poc_request'),
            'probability': request.data.get('probability'),
            'registered_by': user.id
        }
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'failed', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProjectApiDetailView(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project, many=False)
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'failed', 'data': []}, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            project.delete()
            return Response({'status': 'success', 'data': []}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'failed', 'data': []}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        instance = Project.objects.get(pk=pk)
        if not instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'client': request.data.get('client', None),
            'partner': request.data.get('partner'),
            'registration_date': request.data.get('registration_date', None),
            'exp_end_date': request.data.get('exp_end_date', None),
            'tender_date': request.data.get('tender_date', None),
            'info': request.data.get('info', None),
            'count': request.data.get('count', None),
            'client_contact': request.data.get('client_contact', None),
            'partner_contact': request.data.get('partner_contact', None),
            'product': request.data.get('product', None),
            'budget': request.data.get('budget', None),
            'poc_request': request.data.get('poc_request', None),
            'probability': request.data.get('probability', None),
            'registered_by': request.data.get('registered_by', None),
        }
        non_empty_data = {}
        for key, value in data.items():
            if value:
                non_empty_data[key] = value
        serializer = ProjectSerializer(instance=instance, data=non_empty_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductApiView(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)


class NotesApiView(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'note': request.data.get('note'),
            'project': request.data.get('project'),
            'category': request.data.get('category')
        }
        serializer = NotesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'failed', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class NotesApiDetailView(APIView):
    # authentication_classes = [KnoxTokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, *args, **kwargs):
        notes = Notes.objects.filter(project=pk)
        notes = notes.order_by("-creation_date")
        serializer = NotesSerializer(notes, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            note = Notes.objects.get(pk=pk)
            note.delete()
            return Response({'status': 'success', 'data': []}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'status': 'failed', 'data': []}, status=status.HTTP_204_NO_CONTENT)


class Statistics(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        companies = Company.objects
        client_cnt = companies.filter(role="client").count()
        partner_cnt = companies.filter(role="partner").count()
        projects = Project.objects.all()
        project_cnt = projects.count()
        budget = projects.aggregate(Sum('budget'))
        current_year = date.today().year
        finished_projects = FinishedProject.objects.all()
        fin_cnt = finished_projects.count()

        sales_by_month = finished_projects.filter(invoice_date__year=current_year) \
            .annotate(month=ExtractMonth('invoice_date')) \
            .values('month') \
            .annotate(count=Sum('invoice_amount')) \
            .values('month', 'count')

        registration_by_month = projects.filter(registration_date__year=current_year) \
            .annotate(month=ExtractMonth('registration_date')) \
            .values('month') \
            .annotate(count=Count('pk')) \
            .values('month', 'count')

        sales = [0] * 12
        registration =[0] * 12
        for item in sales_by_month:
            if item.get("month", None) is not None:
                sales[item.get("month", 0) - 1] = item.get("count", 0)

        for item in registration_by_month:
            if item.get("month", None) is not None:
                registration[item.get("month", 0) - 1] = item.get("count", 0)

        data = {
            "client_cnt": client_cnt,
            "partner_cnt": partner_cnt,
            "project_cnt": project_cnt,
            "fin_cnt": fin_cnt,
            "total_budget": budget["budget__sum"],
            "monthly_sales": sales,
            "monthly_reg": registration
        }
        return Response({'status': 'success', 'data': data}, status=status.HTTP_200_OK)


class FinishedProjectApiView(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        user = None
        if token:
            token = token.split(" ")[1]
            user = AuthToken.objects.get(token_key=token[0:8]).user
        role = None
        if user:
            role = user.role
        if role == 1:
            projects = FinishedProject.objects.all()
        elif role == 2:
            projects = FinishedProject.objects.filter(registered_by=user)
        serializer = FinishedProjectSerializer(projects, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'client': request.data.get('client'),
            'partner': request.data.get('partner'),
            'count': request.data.get('count'),
            'product': request.data.get('product'),
            'budget': request.data.get('budget'),
            'invoice_date': request.data.get('invoice_date'),
            'invoice_amount': request.data.get('invoice_amount'),
            'agreement': request.FILES.get('file', None),
            'end_date': request.data.get('end_date'),
            'project': request.data.get('project'),
            'registered_by': request.data.get('registered_by'),
        }
        serializer = FinishedProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)

        return Response({'status': 'failed', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def download(request, pk):
    proj = FinishedProject.objects.get(pk=pk)
    file_handle = proj.agreement.open()
    file_name = os.path.basename(str(file_handle))
    # send file
    response = FileResponse(file_handle, content_type='application/pdf')
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, responseType, Content-Disposition'
    response['Content-Disposition'] = 'attachment; filename="' + file_name + '"'
    response['Content-Length'] = proj.agreement.size
    return response
