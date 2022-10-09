import {createApp, h} from 'vue'
import App from './App.vue'
import router from "./router/routes";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import BootstrapVue3 from 'bootstrap-vue-3'
import $ from 'jquery'
import auth_data from './controller/auth'
  
const app = createApp({
  render: () => h(App),
})
app.use(auth_data)
app.use(BootstrapVue3)
app.use($)
app.use(router) 
app.mount("#app");