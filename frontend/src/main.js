/*
=========================================================
* Vite Soft UI Dashboard - v1.0.0
=========================================================
* Product Page: https://creative-tim.com/product/vite-soft-ui-dashboard
* Copyright 2022 Creative Tim (https://www.creative-tim.com)
Coded by www.creative-tim.com
* Licensed under MIT (https://github.com/creativetimofficial/vite-soft-ui-dashboard/blob/556f77210e261adc3ec12197dab1471a1295afd8/LICENSE.md)
=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/ 

import { createApp } from 'vue'
import App from './App.vue'
import store from "./store";
import router from "./router";
import "./assets/css/nucleo-icons.css";
import "./assets/css/nucleo-svg.css";
import SoftUIDashboard from "./soft-ui-dashboard";
import axios from "axios";
import Popper from "vue3-popper";
import messages from "@intlify/unplugin-vue-i18n/messages";
import {createI18n} from "vue-i18n";

const i18n = createI18n({
    legacy: false,
    globalInjection: true,
    locale: "tr",
    fallbackLocale: "tr",
    availableLocales: ["en", "tr"],
    messages: messages,
});

router.beforeEach(async (to, from, next) => {
    var isAuthenticated = true // check if user is authenticated
    try{
        const response = await axios.get(`http://${window.location.hostname}:5000/api/auth/check/`, {headers: {
                Authorization : `${localStorage.getItem("accessToken")}`
            }});

        if(response.data?.role) {
            store.state.role = response.data.role;
        }
    }
    catch(err){
        isAuthenticated = false
    }
    if(to.name === 'Users' && store.state.role !== 1) {
        next('/dashboard')
    }
    else if (to.meta.requiresAuth && !isAuthenticated) {
        next('/sign-in')
    } else {
        next()
    }

})
    const renderApp = () => {
        createApp(App)
        .component("Popper", Popper)
        .use(store)
        .use(router)
        .use(SoftUIDashboard)
        .use(i18n)
            .mount('#app')
      };
     
    renderApp();
