import {createApp, h} from 'vue'
import App from './App.vue'
import router from "./router/routes";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import $ from 'jquery'
  
  const app = createApp({
    render: () => h(App),
  })
  app.use($)
  app.use(router) 
  app.mount("#app");