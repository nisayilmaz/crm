<template>
  <div class="card mb-4 projects-table" :style="mainStyle">
    <div class="card-header pb-0">
      <h6>Fırsatlar</h6>
      <div v-if="this.filter === '0'" class="accordion accordion-flush" id="accordionFlushExample">
        <div class="accordion-item">
          <h4 class="accordion-header">
            <button class="ps-0 accordion-button collapsed " type="button" data-bs-toggle="collapse"
              data-bs-target="#addProject" aria-expanded="false" aria-controls="flush-collapseOne">
              Fırsat Ekle <i class="fa fa-plus ms-2" aria-hidden="true"></i>
            </button>
          </h4>
          <div id="addProject" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
            <div class="accordion-body">
              <form class="row">
                <div class="col-4">
                  <div class="mb-3">
                    <label for="client" class="form-label">Son Kullanıcı*</label>
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
                    <label for="product" class="form-label">Ürün*</label>
                    <select v-model="product" class="form-select" id="product">
                      <option selected>Ürün Seçin</option>
                      <option v-for="product in products" :key="product.id" :value="product.id"> {{product.name}} </option>
                    </select>
                  </div>
                  <div class="mb-3">
                    <label for="count" class="form-label">Adet*</label>
                    <input v-model="count"  type="text" class="ps-0 form-control" id="count">
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
                    <label for="poc" class="form-label">POC*</label>
                    <select v-model="poc" class="form-select" id="poc">
                      <option selected></option>
                      <option value="1"> Toplantı Aşaması </option>
                      <option value="2"> POC Talebi </option>
                      <option value="3"> POC Aşaması </option>
                      <option value="4"> POC Gerçekleştirildi </option>
                      <option value="5"> Yaklaşık Maliyet </option>
                      <option value="6"> Alım Aşaması </option>
                      <option value="7"> Pazarlık Aşaması </option>
                      <option value="8"> Gerçekleşti </option>
                      <option value="9"> Kapandı </option>
                      <option value="10"> Kaybedildi </option>
                    </select>
                  </div>
                  <div class="mb-3">
                    <label for="endDate" class="form-label">Tahmini Kapanış Tarihi</label>
                    <input v-model="endDate" type="date" class="ps-0 form-control" id="endDate">
                  </div>
                    <div class="mb-3">
                        <label for="probability" class="form-label">Olasılık*</label>
                        <vue-slider id="probability"
                                    v-model="probability"
                                    :data="probValues"
                                    :marks="false"
                        ></vue-slider>
                    </div>
                </div>
                <div class="col-4">
                  <div class="mb-3">
                    <label for="tenderDate" class="form-label">İhale Tarihi</label>
                    <input v-model="tenderDate" type="date" class="ps-0 form-control" id="tenderDate">
                  </div>
                  <div class="mb-3">
                      <label for="budget" class="form-label">Bütçe*</label>
                      <input v-model="budget" type="text" class="ps-0 form-control" id="budget">
                  </div>
                  <div class="mb-3">
                    <label for="explanation" class="form-label">Açıklama</label>
                    <input v-model="explanation" type="text" class="ps-0 form-control" id="explanation">
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
      <div class="table table-striped table-responsive p-0 ">
        <table class="table align-items-center justify-content-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Son Kullanıcı
              </th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                İş Ortağı
              </th>
                <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                    Account Manager
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
                Detay
              </th>
                <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(project, i) in projects" :key="i">
              <td  class="align-middle text-center">
                  <span v-if="projectDetails[i].client" class="text-xs font-weight-bold">
                    <router-link :to="{ name: 'CompanyDetail', params: { id: projectDetails[i].client.id}}" target="_blank">{{ projectDetails[i].client?.name }}</router-link>
                    </span>
                  <span v-else class="text-xs font-weight-bold">
                      -
                    </span>

              </td>
              <td class="align-middle text-center">
                <span v-if="projectDetails[i].partner" class="text-xs font-weight-bold">
                    <router-link :to="{ name: 'CompanyDetail', params: { id: projectDetails[i].partner.id}}" target="_blank">{{ projectDetails[i].partner?.name }}</router-link>
                    </span>
                  <span v-else class="text-xs font-weight-bold">
                      -
                    </span>
              </td>
                <td class="align-middle text-center">
                    <span  class="text-xs font-weight-bold">{{ projectDetails[i].user?.first_name }} {{ projectDetails[i].user?.last_name }}</span>

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
                <span class="text-xs font-weight-bold">{{ project?.budget }}$</span>

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
                <span class="text-xs font-weight-bold">
                    <Popper :hover="true">
                      <vsud-progress
                              :percentage="project?.probability"
                      />
                      <template #content>
                        <div>%{{ project?.probability }}</div>
                      </template>
                    </Popper>
                   </span>

              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">
                    <Popper :hover="true">
                      <i class="far fa-question-circle"></i>
                      <template #content>
                        <div>{{ project?.info }}</div>
                      </template>
                    </Popper>
                    </span>
              </td>
                <td class="align-middle text-center">
                    <span class="text-xs font-weight-bold">
                        <router-link :to="{ name: 'bill', params: { id: project.id} }" target="_blank"><i class="fa fa-external-link"></i></router-link>
                    </span>
                </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<style>
.popper{
    max-width: 300px;
    white-space: break-spaces;

}
:root {
    --popper-theme-background-color: #333333;
    --popper-theme-background-color-hover: #333333;
    --popper-theme-text-color: #ffffff;
    --popper-theme-border-width: 0px;
    --popper-theme-border-style: solid;
    --popper-theme-border-radius: 6px;
    --popper-theme-padding: 32px;
    --popper-theme-box-shadow: 0 6px 30px -6px rgba(0, 0, 0, 0.25);
}

</style>
<script>
import axios from "axios";
import moment from "moment";
import VueSlider from "vue-slider-component";
import 'vue-slider-component/theme/default.css';
import VsudProgress from "@/components/VsudProgress.vue";
import {th} from "vuetify/locale";
import Swal from "sweetalert2";
import projects from "@/views/Projects.vue";
import {axiosInstance} from "@/utils/utils";
export default {
  name: "ProjectsTable",
  components: {
      VsudProgress,
      VueSlider
  },
  props: {
      filter : {
          type: String,
          default : 0
      }
  },
  data() {
    return {
      clients: [],
      partners: [],
      projects: [],
      people: [],
      users:[],
      clientEmp: [],
      partnerEmp: [],
      products: [],
      client: null,
      partner: null,
      startDate: null,
      product: null,
      poc: null,
      endDate: null,
      clientContact: null,
      partnerContact: null,
      tenderDate: null,
      explanation: null,
      probability: 0,
      count : null,
      budget: null,
      probValues : [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
      user:null,
      loading:true
    }
  },
  async created() {
    this.loading = true
    const clientsResp = await axiosInstance.get(`/kurumlar/rol/client`);
    if(clientsResp.data.data){
      this.clients = clientsResp.data.data;
    }
    const partnersRes = await axiosInstance.get(`/kurumlar/rol/partner`);
    if(partnersRes.data.data){
      this.partners = partnersRes.data.data;
    }

    const productRes = await axiosInstance.get(`/urunler`);
        this.products = productRes.data?.data;

    const projectsRes = await axiosInstance.get(`/firsatlar`);
    if(projectsRes) {
        this.projects = projectsRes.data.data;
        this.formatObj(this.projects);
        this.projects = this.projects.filter(project => project.poc_request !== 'Gerçekleşti');
        if (this.filter !== "0") {
            this.projects = this.projects.filter(project => project.client === this.filter || project.partner === parseInt(this.filter))
        }

    }
    const peopleResp =  await axiosInstance.get(`/kisiler`);
    this.people = peopleResp.data.data

    const usersRes = await axiosInstance.get(`/auth/kullanicilar`);
    if(usersRes.data.data){
        this.users = usersRes.data.data;
    }
    this.loading = false

  },
  computed: {
    mainStyle() {
        return {
            opacity: this.loading ? 0 : 1
        }
    },
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
            const user = this.users.find(usr => usr.id === project?.registered_by);
            return { client, partner, client_contact, partner_contact, product, project, user };
        });
      }
  },
   methods: {
    async addProject(e) {
      e.preventDefault();
      try {
          const response = await axiosInstance.post(`/firsatlar`, {
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
              probability: this.probability,
              count: this.count,
              budget: this.budget
          });
          let lastId = response.data.data.id;
          const projectsRes = await axiosInstance.get(`/firsatlar/${lastId}`);
          this.formatObj(projectsRes.data.data)
          this.projects.push(projectsRes.data.data);
          this.client = null
          this.partner = null
          this.startDate = null
          this.product = null
          this.poc = null
          this.endDate = null
          this.clientContact = null
          this.partnerContact = null
          this.tenderDate = null
          this.explanation = null
          this.probability = 0
          this.count = null
          this.budget = null
          this.user = null
      }
      catch (err) {
          Swal.fire(
              'Hata',
              'Fırsat Eklenemedi!',
              'error'
          )
      }

    },

    formatDate(dateInput, format = 'DD.MM.YYYY') {
      return moment(dateInput).format(format)
    },

    formatPoc(poc) {
      let options = { 1: "Toplantı Aşaması", 2: "POC Talebi",3: "POC Aşaması", 4: "POC Gerçekleştirildi",5: "Yaklaşık Maliyet", 6: "Alım Aşaması",7: "Pazarlık Aşaması", 8: "Gerçekleşti", }
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
  },
  watch: {
    client: {
      handler() {
        this.clientContact = null;
      },
      immediate: false
    },
    partner: {
        handler() {
            this.partnerContact = null;
        },
        immediate: false
    },
  }
};
</script>

<style lang="scss">
.projects-table{
  transition: opacity linear 0.07s;
}
</style>