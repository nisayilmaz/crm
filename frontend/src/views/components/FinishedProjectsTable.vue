<template>
  <div class="card mb-4">
    <div class="card-header pb-0">
      <h6>Gerçekleşen Fırsatlar</h6>

    </div>
    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
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
                Fatura Tarihi
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
                Bitiş Tarihi
              </th>

              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Fatura Miktarı
              </th>

                <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                    Sözleşme
                </th>
                <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(project, i) in projects" :key="i">
              <td  class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ projectDetails[i].client?.name }}</span>

              </td>
              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ projectDetails[i].partner?.name }}</span>

              </td>
                <td class="align-middle text-center">
                    <span  class="text-xs font-weight-bold">{{ projectDetails[i].manager?.first_name }} {{ projectDetails[i].manager?.last_name }}</span>

                </td>
                <td class="align-middle text-center">
                    <span class="text-xs font-weight-bold">{{ project?.invoice_date }}</span>
                </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ projectDetails[i].product?.name }}</span>
              </td>

              <td class="align-middle text-center">
                <span  class="text-xs font-weight-bold">{{ project?.count}}</span>

              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ project?.budget }}$</span>

              </td>

              <td class="align-middle text-center">
                <span  class="text-xs font-weight-bold">{{ project?.end_date }}</span>

              </td>

              <td class="align-middle text-center">
                <span class="text-xs font-weight-bold">{{ project?.invoice_amount }}</span>
              </td>

                <td class="align-middle text-center">
                    <a style="cursor: pointer" @click="download(project.id)" class="text-xs font-weight-bold">Sözleşme İndir</a>
                </td>

<!--                <td class="align-middle text-center">-->
<!--                    <span class="text-xs font-weight-bold">-->
<!--                        <router-link :to="{ name: 'bill', params: { id: project.id} }" target="_blank"><i class="fa fa-external-link"></i></router-link>-->
<!--                    </span>-->
<!--                </td>-->
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

export default {
  name: "FinishedProjectsTable",
  components: {
      VsudProgress,
      VueSlider
  },
  data() {
    return {
      clients: [],
      partners: [],
      projects: [],
      people: [],
      users:[],
      products: [],
      client: "",
      partner: "",
      invoiceDate: "",
      product: "",
      endDate: "",
      count : "",
      budget: "",
      user:""
    }
  },
  async created() {
    const clientsResp = await axios.get(`http://${window.location.hostname}:5000/api/kurumlar/rol/client`,{
            headers: {
                Authorization : `${localStorage.getItem("accessToken")}`
            }
      });
    if(clientsResp.data.data){
      this.clients = clientsResp.data.data;
    }
    const partnersRes = await axios.get(`http://${window.location.hostname}:5000/api/kurumlar/rol/partner`, {
        headers: {
            Authorization : `${localStorage.getItem("accessToken")}`
        }
    });
    if(partnersRes.data.data){
      this.partners = partnersRes.data.data;
    }

    const productRes = await axios.get(`http://${window.location.hostname}:5000/api/urunler`, {
        headers: {
            Authorization : `${localStorage.getItem("accessToken")}`
        }
    });
        this.products = productRes.data?.data;

    const projectsRes = await axios.get(`http://${window.location.hostname}:5000/api/sonlanan/`, {
        headers: {
            Authorization : `${localStorage.getItem("accessToken")}`
        }
    });
    if(projectsRes) {
        this.projects = projectsRes.data.data;
        this.formatObj(this.projects);
    }
    const peopleResp =  await axios.get(`http://${window.location.hostname}:5000/api/kisiler`, {
        headers: {
            Authorization : `${localStorage.getItem("accessToken")}`
        }
    });
    this.people = peopleResp.data.data

    const usersRes = await axios.get(`http://${window.location.hostname}:5000/api/auth/kullanicilar`,{
        headers: {
            Authorization : `${localStorage.getItem("accessToken")}`
        }
    });
    if(usersRes.data.data){
        console.log(usersRes.data.data)
        this.users = usersRes.data.data;
    }
  },
  computed: {

      projectDetails() {
        return this.projects.map(project => {
            const client = this.clients.find(c => c.id === project?.client);
            const partner = this.partners.find(c => c.id === project?.partner);
            const product = this.products.find(prod => prod.id === project?.product);
            const manager = this.users.find(user => user.id === project?.registered_by)

            return { client, partner, product, project,manager };
        });
      }
  },
   methods: {

    formatDate(dateInput, format = 'DD.MM.YYYY') {
      return moment(dateInput).format(format)
    },

    async download(id) {
          let response = await axios.get(`http://${window.location.hostname}:5000/api/download/${id}`, {
              responseType:"blob",
              Authorization: `${localStorage.getItem("accessToken")}`,

          })
        let filename = "sozlesme.pdf"
        if (typeof response.headers["content-disposition"] === "string") {
            let regex = /filename="([^"]+)"/.exec((response.headers["content-disposition"]))
            if(regex) {
                filename = regex[1]
            }
        }

          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', filename);
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
          window.URL.revokeObjectURL(url);
        },
    formatObj(projList) {
       if(Array.isArray(projList)){
           for (const project of projList) {
               if (project.end_date) {
                   project.end_date = this.formatDate(project.end_date)
               }
               if (project.invoice_date) {
                   project.invoice_date = this.formatDate(project.invoice_date)
               }
           }
       }
      else {
           if (projList.end_date) {
               projList.end_date = this.formatDate(projList.end_date)
           }
           if (projList.invoice_date) {
               projList.invoice_date = this.formatDate(projList.invoice_date)
           }
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
            this.clientContact = null;
        },
        immediate: false
    },
  }
};
</script>
