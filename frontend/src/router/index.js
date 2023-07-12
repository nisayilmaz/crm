import {createRouter, createWebHashHistory, createWebHistory} from "vue-router";
import Dashboard from "@/views/Dashboard.vue";
import SignIn from "@/views/SignIn.vue";
import Projects from "@/views/Projects.vue";
import Companies from "@/views/Companies.vue";
import Partners from "@/views/Partners.vue";
import People from "@/views/People.vue";
import Users from "@/views/Users.vue";
import ProjectDetail from "@/views/ProjectDetail.vue";
import FinishedProjects from "@/views/FinishedProjects.vue";
import CompanyDetail from "@/views/components/CompanyDetail.vue";

const routes = [
  {
    path: "/",
    name: "/",
    redirect: "/log-in",
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
    //Todo: Kurumun ingilizcesi?
    path: "/companies",
    name: "Companies",
    component: Companies,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/partners",
    name: "Partners",
    component: Partners,
    meta: {
      requiresAuth: true
    }
  },
  {
    //Todo: firsatın ingilizcesi???
    path: "/opportunities",
    name: "Projects",
    component: Projects,
    meta: {
      requiresAuth: true
    }
  },
  {
    //Todo: firsatın ingilizcesi???

    path: "/gerceklesen-firsatlar",
    name: "FinishedProjects",
    component: FinishedProjects,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/people",
    name: "People",
    component: People,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/accounts",
    name: "Users",
    component: Users,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/log-in",
    name: "Log In",
    component: SignIn,
  },
  {
    path: "/opportunity/:id",
    name: "Opportunities",
    component: ProjectDetail,
    props: true

  },
  {
    path: "/company/:id",
    name: "CompanyDetail",
    component: CompanyDetail,
    props: true

  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  linkActiveClass: "active",
});

export default router;
