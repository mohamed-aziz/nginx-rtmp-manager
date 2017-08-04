import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Home from '@/components/Home'
import Player from '@/components/Player'
import Jobs from '@/components/Jobs'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/jobs',
      name: 'Jobs',
      component: Jobs
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/player/:name',
      name: 'Player',
      component: Player
    }
  ]
})
