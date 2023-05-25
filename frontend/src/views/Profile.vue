<template>
    <div class="card mb-4">
        <div class="container">
            <div class="row">

                <div class="mt-4 col-md-12 col-xl-12 mt-md-0">
                    <profile-card :project="project"/>
                </div>
            </div>

            <div class="mt-4 row">
                <div class="col-12">
                    <div class="mb-4 card">
                        <div class="p-3 pb-0 card-header">
                            <h6 class="mb-1">Notlar</h6>
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
import ProfileCard from "./components/ProfileCard.vue";
import VsudAvatar from "../components/VsudAvatar.vue";
import ProjectsCard from "./components/ProjectOverviewCard.vue";
import axios from "axios";

export default {
    name: "ProfileOverview",
    components: {
        VsudSwitch,
        ProfileCard,
        VsudAvatar,
        ProjectsCard,
    },
    props: ['id'],

    data() {
        return {
            project : {},
            notes: []

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
    }
};
</script>
