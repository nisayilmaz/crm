<template>
    <div class="card h-100">
        <div class="p-3 pb-0 card-header">
            <div class="row">
                <div class="col-md-8 d-flex align-items-center">
                    <h6 class="mb-0">Kurum Detayı</h6>
                </div>
                <div class="col-md-4 text-end">
<!--                    <a class="btn btn-link text-danger text-gradient px-3 mb-0" href="javascript:;">-->
<!--                        <i @click="this.deleteProject($event,project.id)"-->
<!--                           class="far fa-trash-alt me-2" aria-hidden="true"></i>-->
<!--                    </a>-->
<!--                    <a v-if="!edit" href="javascript:;">-->
<!--                        <i @click="this.clickEdit"-->
<!--                           class="text-sm fa fa-pencil-square-o text-secondary"-->
<!--                        ></i>-->
<!--                    </a>-->
<!--                    <a v-if="edit" href="javascript:;">-->
<!--                        <i @click="this.cancelEdit"-->
<!--                           class="text-sm fa fa-ban text-secondary"-->
<!--                        ></i>-->
<!--                    </a>-->
                </div>
            </div>
        </div>
        <div v-if="!edit" class="p-3 card-body">
            <p class="text-sm">
                <strong class="text-dark">Kurum Adı:</strong>&nbsp;
                <span> {{ company?.name }} </span>
            </p>
            <ul class="list-group">
                <li class="pt-0 text-sm border-0 list-group-item ps-0">
                    <strong class="text-dark">Adres:</strong>&nbsp;
                    <span v-if="company?.address !== '' ">{{ company?.address }}</span>
                    <span v-else>-</span>
                </li>
                <li class="text-sm border-0 list-group-item ps-0">
                    <strong class="text-dark">Telefon:</strong>&nbsp;
                    <span v-if="company?.phone !== '' ">{{ company?.phone }}</span>
                    <span v-else>-</span>
                </li>
                <li class="text-sm border-0 list-group-item ps-0">
                    <strong class="text-dark">Email:</strong>&nbsp;
                    <span v-if="company?.email !== '' "> {{ company?.email }}</span>
                    <span v-else>-</span>
                </li>
            </ul>
        </div>
    </div>
    <people-table class="mt-3" :company_filter="company?.id"/>
    <projects-table class="mt-3" :filter="company?.id"/>

</template>

<script>
import axios from "axios";
import users from "@/views/Users.vue";
import moment from "moment/moment";
import VueSlider from "vue-slider-component";
import 'vue-slider-component/theme/default.css';
import Swal from 'sweetalert2'
import PeopleTable from "@/views/components/PeopleTable.vue";
import ProjectsTable from "@/views/components/ProjectsTable.vue";

export default {
    name: "ProjectCard",
    components: {
        VueSlider,
        PeopleTable,
        ProjectsTable
    },
    props: ['id'],

    data() {
        return {
            company : null
        }
    },
    async created() {
        const companyRes = await axios.get(`http://${window.location.hostname}:5000/api/kurumlar/${this.id}`, {
            headers: {
                Authorization : `${localStorage.getItem("accessToken")}`
            }
        });
        this.company = companyRes.data.data
    },
    computed: {

    },
    methods: {

    },

};
</script>
