<template>
  <div class="card mb-4">
    <div class="card-header pb-0">
      <h6>{{title}}</h6>
      <div class="accordion accordion-flush" id="accordionFlushExample">
        <div class="accordion-item">
          <h4 class="accordion-header">
            <button class="ps-0 accordion-button collapsed " type="button" data-bs-toggle="collapse"
              data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
              Kurum Ekle
            </button>
          </h4>
          <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
            <div class="accordion-body row">
              <div class="col-6">
                  <div class="mb-3">
                      <label for="name" class="form-label">Kurum İsmi</label>
                      <input v-model="name" type="text" class="ps-0 form-control" id="name">
                  </div>
                  <div class="mb-3">
                      <label for="phone" class="form-label">Telefon</label>
                      <input v-model="phone" type="text" class="ps-0 form-control" id="phone">
                  </div>
                  <button @click="addCompany" type="submit" class="btn btn-primary">Ekle</button>
              </div>
              <div class="col-6">
                <div class="mb-3">
                    <label for="email" class="form-label">Email</label>
                    <input v-model="email" type="text" class="ps-0 form-control" id="email">
                </div>
                <div class="mb-3">
                    <label for="address" class="form-label">Adres</label>
                    <input v-model="address" type="text" class="ps-0 form-control" id="address">
                </div>
              </div>
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
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Kurum</th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Email</th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Telefon</th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Adres</th>
              <th class="text-secondary opacity-7"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="company in companies" :key="company.id">
              <td>
                <div class="d-flex px-2 py-1">
                  <div class="d-flex flex-column justify-content-center">
                    <h6 class="mb-0 text-sm"> {{ company.name }}</h6>
                    <!-- <p class="text-xs text-secondary mb-0">{{company.email}}</p> -->
                  </div>
                </div>
              </td>
              <td>
                <p class="text-xs font-weight-bold mb-0">{{ company.email }}</p>
              </td>
              <td class="align-middle text-sm">
                <p class="text-xs font-weight-bold mb-0">{{ company.phone }}</p>
              </td>
              <td class="align-middle text-sm">
                <p class="text-xs font-weight-bold mb-0">{{ company.address }}</p>
              </td>
              <td class="align-middle">
                <a class="me-4 text-secondary font-weight-bold text-xs" >
                  <i class="far fa-edit"></i>
                </a>

                <a href="javascript:;" class="me-4 text-secondary font-weight-bold text-xs" @click="deleteCompany($event, company.id)"> 
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
export default {

  name: "CompaniesTable",
  components: {
  },
  props: {
      type: String,
  },
  data() {
      return {
          companies: [],
          name: "",
          phone: "",
          email: "",
          address: ""
      };
  },
  computed: {
      title() {
          if(this.type === 'client') {
              return 'Kurumlar'
          }
          else if(this.type === 'partner') {
              return 'İş Ortakları'
          }
      },
  },
  async created() {
      try {
          const response = await axios.get(`http://${window.location.hostname}:5000/api/kurumlar/rol/${this.type}`, {
              headers: {
                  Authorization : `${localStorage.getItem("accessToken")}`
              }
          });
          if (response.status === 200) {
              if (!Array.isArray(response.data.data)){
                  this.companies = []
              }
              else {
                  this.companies = response.data.data;
              }
          }
      }
      catch (err) {
        console.log("log in")
      }


  },
  methods: {
    async addCompany(e) {
      e.preventDefault();
      try {
          const response = await axios.post(`http://${window.location.hostname}:5000/api/kurumlar/`, {
              name: this.name,
              role: this.type,
              email: this.email,
              address: this.address,
              phone: this.phone
          }, {headers: {
              Authorization : `${localStorage.getItem("accessToken")}`
          }});
          this.companies.push(response.data.data)
          this.name = ""
          this.phone = ""
          this.email= ""
          this.address= ""
      }
      catch (error) {

        alert(error)
      }
    },

    async deleteCompany(e, id) {
      e.preventDefault();
      await axios.delete(`http://${window.location.hostname}:5000/api/kurumlar/${id}`, {
          headers: {
              Authorization : `${localStorage.getItem("accessToken")}`
          }});
      this.companies = this.companies.filter(company => company.id !== id);
    },
  }
};
</script>