from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from .models import Company, People, Project
from .serializers import *
from knox.auth import TokenAuthentication as KnoxTokenAuthentication


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
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
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
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        print(request.data)
        data = {
            'client': request.data.get('client'),
            'partner': request.data.get('partner'),
            'registration_date': request.data.get('registration_date'),
            'exp_end_date': request.data.get('exp_end_date'),
            'tender_date': request.data.get('tender_date'),
            'info': request.data.get('info'),
            'status': request.data.get('status'),
            'count': request.data.get('count'),
            'client_contact': request.data.get('client_contact'),
            'partner_contact': request.data.get('partner_contact'),
            'product': request.data.get('product'),
            'budget': request.data.get('budget'),
            'poc_request': request.data.get('poc_request'),
            'probability': request.data.get('probability'),
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

class ProductApiView(APIView):
    authentication_classes = [KnoxTokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
