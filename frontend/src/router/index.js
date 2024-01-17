import Vue from 'vue'
import VueRouter from 'vue-router'
import ApplicationFormView from '../views/ApplicationFormView.vue'
import ApplicationsView from '../views/ApplicationsView.vue'
import LandingView from '../views/LandingView.vue'
import NotFoundView from '../views/NotFoundView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'LandingView',
    component: LandingView
  },
  {
    path: '/apply',
    name: 'ApplicationFormView',
    component: ApplicationFormView
  },
  {
    path: '/applications',
    name: 'ApplicationView',
    component: ApplicationsView
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
