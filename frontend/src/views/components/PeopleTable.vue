<template>
    <div class="card mb-4">
      <div class="card-header pb-0">
        <h6>Kişiler</h6>
        <div class="accordion accordion-flush" id="accordionFlushExample">
          <div class="accordion-item">
            <h4 class="accordion-header">
              <button class="ps-0 accordion-button collapsed " type="button" data-bs-toggle="collapse" data-bs-target="#addPeople" aria-expanded="false" aria-controls="flush-collapseOne">
                  Kişi Ekle
              </button>
            </h4>
            <div id="addPeople" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
              <div class="accordion-body row">
                <div class="col-6">
                    <div class="mb-3">
                        <label for="name" class="form-label">Ad</label>
                        <input v-model="first_name" type="text" class="ps-0 form-control" id="firstName">
                    </div>

                    <div class="mb-3">
                        <label for="surname" class="form-label">Soyad</label>
                        <input v-model="last_name" type="text" class="ps-0 form-control" id="lastName">
                    </div>

                    <div class="mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input v-model="email" type="text" class="ps-0 form-control" id="email">
                    </div>
                    <button type="submit" class="btn btn-primary pull-right" @click="addPerson">Ekle</button>

                </div>
                <div class="col-6">
                    <div class="mb-3">
                        <label for="phone" class="form-label">Telefon</label>
                        <input v-model="phone" type="text" class="ps-0 form-control" id="phone">
                    </div>

                    <div class="mb-4">
                        <label for="company" class="form-label">Kurum</label>
                        <select id="client" v-model="company" class="form-select"  >
                            <option selected>Kurum Seçin</option>
                            <option v-for="company in companies" :key="company.id" :value="company.id">{{company.name}}</option>
                        </select>
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
                <th
                  class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                  Ad 
                </th>
                <th
                  class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">
                  Soyad
                </th>
                <th
                  class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">
                  Email
                </th>
                <th
                  class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">
                  Telefon
                </th>
                <th
                  class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">
                  Kurum
                </th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="person in people" :key="person.id">
                <td>
                  <div class="d-flex px-2">
                    <div class="my-auto">
                      <h6 class="mb-0 text-sm">{{person.first_name}}</h6>
                    </div>
                  </div>
                </td>
                <td>
                  <p class="text-sm font-weight-bold mb-0">{{person.last_name}}</p>
                </td>
                <td>
                  <span class="text-xs font-weight-bold">{{person.email}}</span>
                </td>
                <td >
                    <span class="me-2 text-xs font-weight-bold">{{person.phone}}</span>
                </td>
                <td class="align-middle">
                    <span class="me-2 text-xs font-weight-bold">{{ getCompanyName(person.company) }}</span>

                </td>
                <td class="align-middle">
                    <a class="me-4 text-secondary font-weight-bold text-xs" >
                        <i class="far fa-edit"></i>
                    </a>

                    <a class="me-4 text-secondary font-weight-bold text-xs" @click="deletePerson($event, person.id)">
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
    name: "PeopleTable",
    components: {
    },
    data() {
      return {
        companies : [],
        people : [],
        first_name : "",
        last_name : "",
        email : "",
        phone: "",
        company: ""
      }
    },
    async created() {
        const companiesRes = await axios.get(`http://${window.location.hostname}:5000/api/kurumlar/`);
        if (companiesRes.data.status === "success") {
            this.companies = companiesRes.data.data;
        }
        const people = await axios.get(`http://${window.location.hostname}:5000/api/kisiler/`);
        this.people = people.data.data;
    },
    methods: {
      async addPerson(e) {
        e.preventDefault();
        const response = await axios.post(`http://${window.location.hostname}:5000/api/kisiler/`, {
          first_name : this.first_name,
          last_name : this.last_name,
          phone : this.phone,
          email : this.email,
          company : this.company
        },
            {
            headers: {
                'Content-Type': 'application/json',
            }
        });
        let lastId =  response.data.data.id;
        const personRes = await axios.get(`http://${window.location.hostname}:5000/api/kisiler/${lastId}`);
        this.people.push(personRes.data.data);
        this.first_name = "";
        this.last_name = "";
        this.email = "";
        this.phone = "";
        this.company = "";
      },
      async deletePerson(e, id) {
          e.preventDefault();
          await axios.delete(`http://${window.location.hostname}:5000/api/kisiler/${id}`);
          this.people = this.people.filter(person => person.id !== id);
      },
      getCompanyName(companyId) {
          if(!Array.isArray(this.companies)) return " "
          const comp = this.companies.find(c => c.id === companyId);
          return comp ? comp.name : " ";
      },
    }
  };
  </script>
  