import Vue from 'vue'
import VueRouter from 'vue-router'
import ApplicationFormView from '../views/ApplicationFormView.vue'
import ApplicationsView from '../views/ApplicationsView.vue'


Vue.use(VueRouter)

const routes = [
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
