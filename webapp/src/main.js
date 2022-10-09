import {createApp, h} from 'vue';

import App from './App.vue';
import {createPinia} from 'pinia';
import router from "./router/routes";

import BootstrapVue3 from 'bootstrap-vue-3';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';




//let auth_service = new AuthService();
const app = createApp({
  render: () => h(App),
})
app.use(createPinia()).use(BootstrapVue3).use(router).mount("#app");