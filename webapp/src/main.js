import {createApp, h} from 'vue'
import App from './App.vue'
import router from "./router/routes";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
  
  const app = createApp({
    render: () => h(App),
  })
  //app.use(BootstrapVue)
  app.use(router)
  
  app.mount("#app");