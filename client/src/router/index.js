import Vue from 'vue';
import Router from 'vue-router';
import Mot from '../components/Mot.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/',
      name: 'Mot',
      component: Mot,
    },
  ],
});
