<template>
  <div class="container top-0 position-sticky z-index-sticky">
    <div class="row">
      <div class="col-12">
        <navbar
          is-blur="blur blur-rounded my-3 py-2 start-0 end-0 mx-4 shadow"
          btn-background="bg-gradient-success"
          :dark-mode="true"
        />
      </div>
    </div>
  </div>
  <main class="mt-0 main-content main-content-bg">
    <section>
      <div class="page-header min-vh-75">
        <div class="container">
          <div class="row">
            <div class="mx-auto col-xl-4 col-lg-5 col-md-6 d-flex flex-column">
              <div class="mt-8 card card-plain">
                <div class="pb-0 card-header text-start">
                  <h3 class="font-weight-bolder text-info text-gradient">Hoş Geldiniz</h3>
                  <p class="mb-0">Email ve şifre ile giriş yapınız.</p>
                </div>
                <div class="card-body">
                    <span v-if="error" style="color: red"> Lütfen email ve şifrenizi kontrol edin.</span>

                    <form role="form" class="text-start">
                    <label>Email</label>
                    <vsud-input v-model:value="username" type="email" placeholder="Email" name="email" />
                    <label>Şifre</label>
                    <vsud-input v-model:value="password" type="password" placeholder="Şifre" name="password" />
                    <div class="text-center">
                      <vsud-button @click="login"
                        class="my-4 mb-2"
                        variant="gradient"
                        color="info"
                        full-width
                      >GİRİŞ YAP</vsud-button >
                    </div>
                  </form>
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="oblique position-absolute h-100 d-md-block d-none me-n8">
                <div
                  class="login-img bg-cover oblique-image position-absolute fixed-top ms-auto h-100 z-index-0 ms-n6"
                  :style="{
                    backgroundImage:
                      `url(${logo})`,
                  }"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import Navbar from "@/examples/PageLayout/Navbar.vue";
import AppFooter from "@/examples/PageLayout/Footer.vue";
import VsudInput from "@/components/VsudInput.vue";
import VsudButton from "@/components/VsudButton.vue";
import bgImg from "@/assets/img/curved-images/curved9.jpg"
import logo from "@/assets/img/tr7_logo_big.png"
import axios from "axios";
const body = document.getElementsByTagName("body")[0];

export default {
  name: "SigninPage",
  components: {
    Navbar,
    AppFooter,
    VsudInput,
    VsudButton,
  },
  data() {
    return {
      bgImg,
      logo,
      username: "",
      password :"",
      error: false
    }
  },
  beforeMount() {
    this.$store.state.hideConfigButton = true;
    this.$store.state.showNavbar = false;
    this.$store.state.showSidenav = false;
    this.$store.state.showFooter = false;
    body.classList.remove("bg-gray-100");
  },
  beforeUnmount() {
    this.$store.state.hideConfigButton = false;
    this.$store.state.showNavbar = true;
    this.$store.state.showSidenav = true;
    this.$store.state.showFooter = true;
    body.classList.add("bg-gray-100");
  },
    methods: {
        async login(e) {
            e.preventDefault();
            try {
                const response = await axios.post(`http://${window.location.hostname}:5000/api/auth/login/`, {
                    username:this.username,
                    password:this.password,
                });
                if(response.data?.token) {
                    window.localStorage.setItem("accessToken", `Token ${response.data.token}`);
                    this.$router.push('/dashboard');
                }
                if(response.data?.role) {
                    this.$store.state.role = response.data.role;
                }
            }
            catch (error) {
                this.error = true
            }
        },
    }
};
</script>
