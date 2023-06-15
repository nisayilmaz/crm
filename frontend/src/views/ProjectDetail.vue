<template>
    <div class="card mb-4">
        <div class="container">
            <div class="row">

                <div class="mt-4 col-md-12 col-xl-12 mt-md-0">
                    <project-card :project="project"/>
                </div>
            </div>

            <div class="mt-4 row">

                <div class="col-12">
                    <div class="mb-4 card">
                        <div class="p-3 pb-0 card-header">
<!--                            <h6 class="mb-1">Notlar</h6>-->
                            <nav-pill/>

                            <div class="accordion accordion-flush" id="addNoteAccordion">
                                <div class="accordion-item">
                                    <h4 class="accordion-header">
                                        <button class="ps-0 accordion-button collapsed " type="button" data-bs-toggle="collapse"
                                                data-bs-target="#addNote" aria-expanded="false" aria-controls="flush-collapseOne">
                                            Not Ekle <i class="fa fa-plus ms-2" aria-hidden="true"></i>
                                        </button>
                                    </h4>
                                    <div id="addNote" class="accordion-collapse collapse" data-bs-parent="#addNoteAccordion">
                                        <div class="accordion-body">
                                            <form class="row">
                                                <div class="col-4">
                                                    <div class="mb-3">
                                                        <label for="title" class="form-label">Başlık</label>
                                                        <input v-model="title" type="text" class="ps-0 form-control" id="title">
                                                    </div>
                                                    <div class="mb-3">
                                                        <label for="note" class="form-label">Not</label>
                                                        <input v-model="note" type="text" class="ps-0 form-control" id="note">
                                                    </div>
                                                    <div class="mb-3">
                                                        <label for="type" class="form-label">Kategori</label>
                                                        <select v-model="type" class="form-select" id="partner">
                                                            <option value="1">Arama</option>
                                                            <option value="2">Yüzyüze Görüşme</option>
                                                            <option value="3">İş Ortağı İle Görüşme</option>
                                                            <option value="4">E-posta</option>
                                                        </select>
                                                    </div>
                                                </div>
                                            </form>
                                            <button @click="addNote" type="submit" class="btn btn-primary">Ekle</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="card-body pt-4 p-3">
                            <ul class="list-group">
                                <li v-for="note in notes" :key="note.id" class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg">
                                    <div class="d-flex flex-column">
                                        <h6 class="mb-3 text-sm">{{note.title}}</h6>
                                        <span class="mb-2 text-xs">Tarih:
                                            <span class="text-dark font-weight-bold ms-sm-2">{{note.creation_date}}</span>
                                        </span>
                                        <span class="mb-2 text-xs">
                                              Kategori:
                                              <span class="text-dark ms-sm-2 font-weight-bold">{{note.category}}</span>
                                        </span>
                                        <span class="text-xs">
                                              Not:
                                              <span class="text-dark ms-sm-2 font-weight-bold">{{note.note}}</span>
                                        </span>
                                    </div>
                                    <div class="ms-auto text-end">
                                        <a class="btn btn-link text-danger text-gradient px-3 mb-0" href="javascript:;">
                                            <i class="far fa-trash-alt me-2" aria-hidden="true"></i>
                                        </a>
                                    </div>
                                </li>

                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import VsudSwitch from "@/components/VsudSwitch.vue";
import ProfileCard from "./components/ProjectCard.vue";
import VsudAvatar from "../components/VsudAvatar.vue";
import ProjectsCard from "./components/ProjectOverviewCard.vue";
import axios from "axios";
import ProjectCard from "@/views/components/ProjectCard.vue";
import Swal from "sweetalert2";
import NavPill from "./components/NavPill.vue";

export default {
    name: "ProjectDetail",
    components: {
        VsudSwitch,
        VsudAvatar,
        ProjectsCard,
        ProjectCard,
        NavPill
    },
    props: ['id'],

    data() {
        return {
            project : {},
            notes: [],
            note: "",
            title:"",
            type: ""
        };
    },
    async created() {
        const projectsRes = await axios.get(`http://${window.location.hostname}:5000/api/firsatlar/${this.id}`, {
            headers: {
                Authorization : `${localStorage.getItem("accessToken")}`
            }
        });
        this.project = projectsRes.data.data

        const notesRes = await axios.get(`http://${window.location.hostname}:5000/api/notlar/${this.id}`, {
            headers: {
                Authorization : `${localStorage.getItem("accessToken")}`
            }
        });
        this.notes = notesRes.data.data
    },
    methods : {
        async addNote(e) {
            e.preventDefault()
            try {
                const response = await axios.post(`http://${window.location.hostname}:5000/api/notlar/`, {
                    title: this.title,
                    note: this.note,
                    project: this.project.id,
                    category: this.type
                }, {
                    headers: {
                        Authorization: `${localStorage.getItem("accessToken")}`
                    }
                });
                if(response.data.data){
                    this.notes.splice(0, 0, response.data.data);
                    this.notes.join()
                }
            }catch (err) {
                Swal.fire(
                    'Hata',
                    'Not Eklenemedi!',
                    'error'
                )
            }
        },
    }
};
</script>
