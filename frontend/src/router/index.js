import Vue from 'vue'
import VueRouter from 'vue-router'
import ApplicationFormView from '../views/applications/ApplicationFormView.vue'
import ApplicationsView from '../views/applications/ApplicationsView.vue'
import AddBookView from '../views/library/AddBookView.vue'
import LandingView from '../views/other/LandingView.vue'
import NotFoundView from '../views/other/NotFoundView.vue'


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
  {
    path: '/addbook',
    name: 'AddBookView',
    component: AddBookView
  },
  {
    path: '*',
    name: 'NotFoundView',
    component: NotFoundView
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
