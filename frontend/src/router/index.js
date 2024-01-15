import Vue from 'vue'
import VueRouter from 'vue-router'
import ApplicationView from '../views/ApplicationView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/apply',
    name: 'ApplicationView',
    component: ApplicationView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
