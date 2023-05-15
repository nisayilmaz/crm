<template>
    <div class="card mb-4">
        <div class="card-header pb-0">
            <h6>Projects table</h6>
            <div class="accordion accordion-flush" id="accordionFlushExample">
                <div class="accordion-item">
                    <h4 class="accordion-header">
                        <button class="ps-0 accordion-button collapsed " type="button" data-bs-toggle="collapse"
                                data-bs-target="#addUser" aria-expanded="false" aria-controls="flush-collapseOne">
                            Kullanıcı Ekle
                        </button>
                    </h4>
                    <div id="addUser" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                        <div class="accordion-body">
                            <form class="row">
                                <div class="col-4">
                                    <div class="mb-3">
                                        <label for="username" class="form-label">Kullanıcı Adı</label>
                                        <input v-model="username" type="text" class="ps-0 form-control" id="username">
                                    </div>
                                </div>
                                <div class="col-4">
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
            username: "",
            password: "",
        }
    },
    async created() {

    },
    methods: {
        async addUser(e) {
            e.preventDefault();
            await axios.post(`http://${window.location.hostname}:5000/api/auth/register/`, {
                username: this.username,
                password: this.password,
                email: ""
            });

            this.username = "";
            this.password = "";
        },
    },

};
</script>
