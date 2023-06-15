<template>
    <div class="card mb-4">
        <div class="card-header pb-0">
            <h6>Kullanıcılar</h6>
            <div class="accordion accordion-flush" id="accordionFlushExample">
                <div class="accordion-item">
                    <h4 class="accordion-header">
                        <button class="ps-0 accordion-button collapsed " type="button" data-bs-toggle="collapse"
                                data-bs-target="#addUser" aria-expanded="false" aria-controls="flush-collapseOne">
                            Kullanıcı Ekle <i class="fa fa-plus ms-2" aria-hidden="true"></i>
                        </button>
                    </h4>
                    <div id="addUser" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                        <div class="accordion-body">
                            <form class="row">
                                <div class="col-4">
                                    <div class="mb-3">
                                        <label for="name" class="form-label">Ad</label>
                                        <input v-model="first_name" type="text" class="ps-0 form-control" id="name">
                                    </div>
                                    <div class="mb-3">
                                        <label for="surname" class="form-label">Soyad</label>
                                        <input v-model="last_name" type="text" class="ps-0 form-control" id="surname">
                                    </div>
                                    <div class="mb-3">
                                        <label for="email" class="form-label">Email</label>
                                        <input v-model="email" type="text" class="ps-0 form-control" id="email">
                                    </div>
                                </div>
                                <div class="col-4">
                                    <div class="mb-4">
                                        <label for="role" class="form-label">Rol</label>
                                        <select id="role" v-model="role" class="form-select"  >
                                            <option selected>Rol Seçin</option>
                                            <option value="1">Admin</option>
                                            <option value="2">Account Manager</option>
                                        </select>
                                    </div>
                                    <div class="mb-3">
                                        <label for="password" class="form-label">Şifre</label>
                                        <input v-model="password" type="text" class="ps-0 form-control" id="password">
                                    </div>
                                </div>
                            </form>
                            <button @click="addUser" type="submit" class="btn btn-primary">Ekle</button>
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
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="user in users" :key="user.id">
                        <td>
                            <div class="d-flex px-2">
                                <div class="my-auto">
                                    <h6 class="mb-0 text-sm">{{user.first_name}}</h6>
                                </div>
                            </div>
                        </td>
                        <td>
                            <p class="text-sm font-weight-bold mb-0">{{user.last_name}}</p>
                        </td>
                        <td>
                            <span class="text-xs font-weight-bold">{{user.email}}</span>
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
import vsudAlert from "@/components/VsudAlert.vue";
export default {
    name: "UsersTable",
    components: {
        vsudAlert
    },
    data() {
        return {
            companies : [],
            users: [],
            first_name : "",
            last_name : "",
            role: "",
            email: "",
            password: "",
        }
    },
    async created() {
        const companiesRes = await axios.get(`http://${window.location.hostname}:5000/api/kurumlar/`,
            {headers: {
                    Authorization : `${localStorage.getItem("accessToken")}`
                }});
        if (companiesRes.data.status === "success") {
            this.companies = companiesRes.data.data;
        }

        try {
            const usersRes = await axios.get(`http://${window.location.hostname}:5000/api/auth/kullanicilar`,
                {headers: {
                        Authorization : `${localStorage.getItem("accessToken")}`
                    }});
            this.users = usersRes.data.data
        }
        catch (err) {
        }
    },
    methods: {
        async addUser(e) {
            try {
                e.preventDefault();
                const resp = await axios.post(`http://${window.location.hostname}:5000/api/auth/register/`, {
                    password: this.password,
                    email: this.email,
                    role: this.role,
                    first_name : this.first_name,
                    last_name : this.last_name
                });
                this.users.push(resp.data.user)
            }
            catch (err){
            }
            this.email = "";
            this.password = "";
            this.first_name = ""
            this.last_name = ""
            this.company = ""
        },
        getCompanyName(companyId) {
            if(!Array.isArray(this.companies)) return " "
            const comp = this.companies.find(c => c.id === companyId);
            return comp ? comp.name : " ";
        },
        async deletePerson(e, id) {
            e.preventDefault();
            try {
                await axios.delete(`http://${window.location.hostname}:5000/api/auth/kullanicilar/${id}`, {
                    headers: {
                        Authorization : `${localStorage.getItem("accessToken")}`
                    }
                });
                this.users = this.users.filter(person => person.id !== id);
            }
            catch (err) {
            }
        },
    },
};
</script>
