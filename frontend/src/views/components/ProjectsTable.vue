<template>
  <div class="card mb-4">
    <div class="card-header pb-0">
      <h6>Projects table</h6>
      <div class="accordion accordion-flush" id="accordionFlushExample">
        <div class="accordion-item">
          <h4 class="accordion-header">
            <button class="ps-0 accordion-button collapsed " type="button" data-bs-toggle="collapse"
              data-bs-target="#addProject" aria-expanded="false" aria-controls="flush-collapseOne">
              Proje Ekle
            </button>
          </h4>
          <div id="addProject" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
            <div class="accordion-body">
              <form class="row">
                <div class="col-4">
                  <div class="mb-3">
                    <label for="client" class="form-label">Son Kullanıcı</label>
                    <select v-model="client" class="form-select" id="client" @change="dropdownListener">
                      <option selected>Kurum Seçin</option>
                      <option v-for="client in clients" :id="client.id" :value="client.id">{{ client.name }}</option>
                    </select>
                  </div>
                  <div class="mb-3">
                    <label for="partner" class="form-label">İş Ortağı</label>
                    <select v-model="partner" class="form-select" id="partner" @change="dropdownListener">
                      <option selected>Kurum Seçin</option>
                      <option v-for="partner in partners" :id="partner.id" :value="partner.id">{{ partner.name }}</option>
                    </select>
                  </div>
                  <div class="mb-3">
                    <label for="startDate" class="form-label">Fırsat Tarihi</label>
                    <input v-model="startDate" type="date" class="ps-0 form-control" id="startDate">
                  </div>
                  <div class="mb-3">
                    <label for="product" class="form-label">Ürün</label>
                    <select v-model="product" class="form-select" id="product">
                      <option selected>Ürün Seçin</option>
                      <option v-for="product in products" :key="product.id" :value="product.id"> {{product.name}} </option>
                    </select>
                  </div>
                  <div class="mb-3">
                    <label for="count" class="form-label">Adet</label>
                    <input v-model="count" @blur="v$.count.$touch" type="text" class="ps-0 form-control" id="count">
<!--                      <span v-if="v$.count.$error">
                        {{ v$.count.$errors[0].$message }}
                      </span>-->
                  </div>
                </div>
                <div class="col-4">
                  <div class="mb-3">
                    <label for="client_contact" class="form-label">İlgili Kişi</label>
                    <select v-model="clientContact" class="form-select" id="client_contact">
                      <option selected></option>
                      <option v-for="emp in clientEmployees" :id="emp.id" :value="emp.id"> {{ emp.first_name }} {{ emp.last_name }}
                      </option>
                    </select>
                  </div>

                  <div class="mb-3">
                    <label for="partner_contact" class="form-label">Proje Sorumlusu</label>
                    <select v-model="partnerContact" class="form-select" id="partner_contact">
                      <option selected></option>
                      <option v-for="emp in partnerEmployees" :id="emp.id" :value="emp.id"> {{ emp.first_name }} {{ emp.last_name}}
                      </option>
                    </select>
                  </div>

                  <div class="mb-3">
                    <label for="poc" class="form-label">POC</label>
                    <select v-model="poc" class="form-select" id="poc">
                      <option selected></option>
                      <option value="Y"> Evet </option>
                      <option value="N"> Hayır </option>
                    </select>
                  </div>

                  <div class="mb-3">
                    <label for="endDate" class="form-label">Tahmini Kapanış Tarihi</label>
                    <input v-model="endDate" type="date" class="ps-0 form-control" id="endDate">
                  </div>

                  <div class="mb-3">
                    <label for="budget" class="form-label">Bütçe</label>
                    <input v-model="budget" type="text" class="ps-0 form-control" id="budget">
                  </div>
                </div>
                <div class="col-4">
                  <div class="mb-3">
                    <label for="tenderDate" class="form-label">İhale Tarihi</label>
                    <input v-model="tenderDate" type="date" class="ps-0 form-control" id="tenderDate">
                  </div>

                  <div class="mb-3">
                    <label for="probability" class="form-label">Olasılık</label>
                    <input v-model="probability" type="text" class="ps-0 form-control" id="probability">
                  </div>

                  <div class="mb-3">
                    <label for="explanation" class="form-label">Açıklama</label>
                    <input v-model="explanation" type="text" class="ps-0 form-control" id="explanation">
                  </div>

                  <div class="mb-3">
                    <label for="status" class="form-label">Durum</label>
                    <input v-model="status" type="text" class="ps-0 form-control" id="status">
                  </div>
                </div>
              </form>
              <button @click="addProject" type="submit" class="btn btn-primary">Ekle</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
        <table class="table align-items-center justify-content-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Son Kullanıcı
              </th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                İş Ortağı
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ">
                Fırsat Tarihi
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Ürün
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Adet
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Bütçe
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                POC
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Tahmini Kapanış Tarihi
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                İlgili Kişi
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Proje Sorumlusu
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                İhale Tarihi
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Olasılık
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Açıklama
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Durum
              </th>
                <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(project, i) in projects" :key="i">
              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ projectDetails[i].client?.name }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ projectDetails[i].partner?.name }}</span>
              </td>
              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ project?.registration_date }}</span>
              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ projectDetails[i].product?.name }}</span>
              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ project?.count}}</span>
              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ project?.budget }}</span>
              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ project?.poc_request }}</span>
              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ project?.exp_end_date }}</span>
              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{projectDetails[i].client_contact?.first_name}} {{ projectDetails[i].client_contact?.last_name}}</span>
              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{projectDetails[i].partner_contact?.first_name}} {{ projectDetails[i].partner_contact?.last_name}}</span>
              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ project?.tender_date }}</span>
              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ project?.probability }}</span>
              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ project?.info }}</span>
              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ project?.status }}</span>
              </td>
                <td class="align-middle text-center">
                    <a class="me-4 text-secondary font-weight-bold text-xs" >
                        <i class="far fa-edit"></i>
                    </a>

                    <a href="javascript:;" class="me-4 text-secondary font-weight-bold text-xs" @click="deleteProject($event, project?.id)">
                        <i class="far fa-trash-alt me-2"></i>
                    </a>
                </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import { useVuelidate } from '@vuelidate/core'
import {required, email,helpers, minLength} from '@vuelidate/validators'
export default {
  name: "ProjectsTable",
  components: {
  },
  setup () {
      return { v$: useVuelidate() }
  },
  data() {
    return {
      clients: [],
      partners: [],
      projects: [],
      people: [],
      clientEmp: [],
      partnerEmp: [],
      products: [],
      client: "",
      partner: "",
      startDate: "",
      product: "",
      poc: "",
      endDate: "",
      clientContact: "",
      partnerContact: "",
      tenderDate: "",
      explanation: "",
      status: "",
      probability: "",
      count : "",
      budget: "",
    }
  },
    /*validations () {
        return {
            count: {
                required: helpers.withMessage('This field is required', required),
                minLength: minLength(4),
            },
            status: { required },
        }
    },*/
  async created() {
    const clientsResp = await axios.get(`http://${window.location.hostname}:5000/api/kurumlar/rol/client`);
    if(clientsResp.data.data){
      this.clients = clientsResp.data.data;
    }
    const partnersRes = await axios.get(`http://${window.location.hostname}:5000/api/kurumlar/rol/partner`);
    if(partnersRes.data.data){
      this.partners = partnersRes.data.data;
    }

    const productRes = await axios.get(`http://${window.location.hostname}:5000/api/urunler`);
        this.products = productRes.data?.data;

    const projectsRes = await axios.get(`http://${window.location.hostname}:5000/api/firsatlar`);
    if(projectsRes) {
      this.projects = projectsRes.data.data;
      this.formatObj(this.projects);
    }
    const peopleResp =  await axios.get(`http://${window.location.hostname}:5000/api/kisiler`);
    this.people = peopleResp.data.data
  },
  computed: {
    clientEmployees() {
      if (!Array.isArray(this.people)) return []
      return this.people.filter(person => person.company === this.client)
    },
    partnerEmployees() {
      if (!Array.isArray(this.people)) return []
      return this.people.filter(person => person.company === this.partner)
    },
      projectDetails() {
        return this.projects.map(project => {
            const client = this.clients.find(c => c.id === project?.client);
            const partner = this.partners.find(c => c.id === project?.partner);
            const client_contact = this.people.find(person => person.id === project?.client_contact);
            const partner_contact = this.people.find(person => person.id === project?.partner_contact);
            const product = this.products.find(prod => prod.id === project?.product);
            return { client, partner, client_contact, partner_contact, product, project };
        });
      }
  },
   methods: {
    async addProject(e) {
      e.preventDefault();
      const response = await axios.post(`http://${window.location.hostname}:5000/api/firsatlar`, {
          client: this.client,
          partner: this.partner,
          registration_date: this.startDate,
          product: this.product,
          poc_request: this.poc,
          exp_end_date: this.endDate,
          client_contact: this.clientContact,
          partner_contact: this.partnerContact,
          tender_date: this.tenderDate,
          info: this.explanation,
          status: this.status,
          probability: this.probability,
          count: this.count,
          budget: this.budget
      });
      let lastId = response.data.data.id;
      const projectsRes = await axios.get(`http://${window.location.hostname}:5000/api/firsatlar/${lastId}`);
      this.formatObj(projectsRes.data.data)
      console.log(projectsRes.data.data)
      this.projects.push(projectsRes.data.data);
      this.client = "";
      this.partner = "";
    },

    formatDate(dateInput, format = 'DD.MM.YYYY') {
      return moment(dateInput).format(format)
    },

    formatPoc(poc) {
      let options = { Y: "Evet", N: "Hayır" }
      poc = options[poc]
      return poc
    },
    formatObj(projList) {
       if(Array.isArray(projList)){
           for (const project of projList) {
               if (project.registration_date) {
                   project.registration_date = this.formatDate(project.registration_date)
               }
               if (project.exp_end_date) {
                   project.exp_end_date = this.formatDate(project.exp_end_date)
               }
               if (project.tender_date) {
                   project.tender_date = this.formatDate(project.tender_date)
               }
               project.poc_request = this.formatPoc(project.poc_request)
           }
       }
      else {
           if (projList.exp_end_date) {
               projList.registration_date = this.formatDate(projList.registration_date)
           }
           if (projList.exp_end_date) {
               projList.exp_end_date = this.formatDate(projList.exp_end_date)
           }
           if (projList.tender_date) {
               projList.tender_date = this.formatDate(projList.tender_date)
           }
           projList.poc_request = this.formatPoc(projList.poc_request)
       }
    },
     async deleteProject(e, id) {
         e.preventDefault();
         await axios.delete(`http://${window.location.hostname}:5000/api/firsatlar/${id}`);
         this.projects = this.projects.filter(project => project.id !== id);
     },
  },
  watch: {
    client: {
      handler() {
        this.clientContact = null;
      },
      immediate: false
    },
  }
};
</script>
