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
                            <h6 class="mb-1">Notlar</h6>
                            <div class="accordion accordion-flush" id="addNoteAccordion">
                                <div class="accordion-item">
                                    <h4 class="accordion-header">
                                        <button class="ps-0 accordion-button collapsed " type="button" data-bs-toggle="collapse"
                                                data-bs-target="#addNote" aria-expanded="false" aria-controls="flush-collapseOne">
                                            Not Ekle
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
                                                </div>
                                            </form>
                                            <button @click="addNote" type="submit" class="btn btn-primary">Ekle</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="p-3 card-body">
                            <div class="row">
                                <div class="mb-4 col-xl-3 col-md-3 mb-xl-0" v-for="note in notes" :key="note.id">
                                    <projects-card
                                            :title="note.title"
                                            :description="note.note"
                                            :date= "note.creation_date"
                                    />
                                </div>
                            </div>
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

export default {
    name: "ProjectDetail",
    components: {
        VsudSwitch,
        VsudAvatar,
        ProjectsCard,
        ProjectCard
    },
    props: ['id'],

    data() {
        return {
            project : {},
            notes: [],
            note: "",
            title:""
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
                    project: this.project.id
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
                alert(err)
            }
        },
    }
};
</script>
