<template>
    <div class="card mb-4 people-table" :style="mainStyle">
      <div class="card-header pb-0">
        <h6>Kişiler</h6>
        <div v-if="company_filter === '0'" class="accordion accordion-flush" id="accordionFlushExample">
          <div class="accordion-item">
            <h4 class="accordion-header">
              <button class="ps-0 accordion-button collapsed " type="button" data-bs-toggle="collapse" data-bs-target="#addPeople" aria-expanded="false" aria-controls="flush-collapseOne">
                  Kişi Ekle <i class="fa fa-plus ms-2" aria-hidden="true"></i>
              </button>
            </h4>
            <div id="addPeople" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
              <div class="accordion-body row">
                <div class="col-6">
                    <div class="mb-3">
                        <label for="name" class="form-label">Ad*</label>
                        <input v-model="first_name" type="text" class="ps-0 form-control" id="firstName">
                    </div>

                    <div class="mb-3">
                        <label for="surname" class="form-label">Soyad*</label>
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
                        <label for="company" class="form-label">Kurum*</label>
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
          <div class="row">
              <div class="col-3 ms-3">
                  <input v-if="company_filter === '0'" class="ps-0 form-control text-xs" v-model="search">
              </div>
          </div>
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
              <tr v-for="person in filteredData" :key="person.id">
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
  import Swal from "sweetalert2";
  import {axiosInstance} from "@/utils/utils";
  export default {
    name: "PeopleTable",
    props: {
      company_filter :{
          type:String,
          default:0
      }
    },
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
        company: "",
        search: "",
        loading : true,
        filter: parseInt(this.company_filter)
      }
    },
    async created() {
        this.loading = true
        const companiesRes = await axiosInstance.get(`/kurumlar/`);
        if (companiesRes.data.status === "success") {
            this.companies = companiesRes.data.data;
        }
        const people = await axiosInstance.get(`/kisiler/`);
        this.people = people.data.data;
        if(this.company_filter !== '0') {
            this.people = this.people.filter(person => person.company === parseInt(this.company_filter))
        }
        this.loading = false
    },
      computed: {
        mainStyle() {
            return {
                opacity: this.loading ? 0 : 1
            }
        },
        filteredData() {
            return this.people.filter(person => {
                return (person?.first_name + person?.last_name + this.getCompanyName(person?.company)).toString().toLowerCase().includes(this.search.toLowerCase())})
        }
      },
    methods: {
      async addPerson(e) {
        e.preventDefault();
        try {
            const response = await axiosInstance.post(`/kisiler/`, {
                    first_name : this.first_name,
                    last_name : this.last_name,
                    phone : this.phone,
                    email : this.email,
                    company : this.company
                });
            let lastId =  response.data.data.id;
            const personRes = await axiosInstance.get(`/kisiler/${lastId}`);
            this.people.push(personRes.data.data);
        }
        catch (err) {
            Swal.fire(
                'Hata',
                'Kişi Eklenemedi!',
                'error'
            )
        }
        this.first_name = "";
        this.last_name = "";
        this.email = "";
        this.phone = "";
        this.company = "";
      },
      async deletePerson(e, id) {
          e.preventDefault();
          Swal.fire({
              title: 'Bu kişiyi silmek istediğinize emin misiniz?',
              text: "Bu işlem geri alınamaz ve kişiyle ilişkili tüm fırsatlar da silinir.",
              icon: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: 'Sil',
              cancelButtonText:'İptal'
          }).then(async (result) => {
              if (result.isConfirmed) {
                  await axiosInstance.delete(`/kisiler/${id}`);
                  this.people = this.people.filter(person => person.id !== id);
              }
          })

      },
      getCompanyName(companyId) {
          if(!Array.isArray(this.companies)) return " "
          const comp = this.companies.find(c => c.id === companyId);
          return comp ? comp.name : " ";
      },
    }
  };
  </script>

<style lang="scss">
.people-table{
  transition: opacity linear 0.1s;
}
</style>