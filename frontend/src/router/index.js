import { createRouter, createWebHashHistory } from "vue-router";
import Dashboard from "@/views/Dashboard.vue";
import SignIn from "@/views/SignIn.vue";
import Projects from "@/views/Projects.vue";
import Companies from "@/views/Companies.vue";
import Partners from "@/views/Partners.vue";
import People from "@/views/People.vue";
import Users from "@/views/Users.vue";
import ProjecctDetail from "@/views/ProjectDetail.vue";

const routes = [
  {
    path: "/",
    name: "/",
    redirect: "/dashboard",
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/kurumlar",
    name: "Companies",
    component: Companies,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/is-ortaklari",
    name: "Partners",
    component: Partners,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/firsatlar",
    name: "Projects",
    component: Projects,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/kisiler",
    name: "People",
    component: People,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/hesaplar",
    name: "Users",
    component: Users,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/sign-in",
    name: "Sign In",
    component: SignIn,
  },
  {
    path: "/firsat/:id",
    name: "bill",
    component: ProjecctDetail,
    props: true

  },
];

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes,
  linkActiveClass: "active",
});

export default router;
