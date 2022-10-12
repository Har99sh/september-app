<template lang="">
<div>
  <b-form inline>
    <label class="sr-only" for="inline-form-input-name">Email</label>
    <b-form-input
      id="inline-form-input-name"
      class="mb-2 mr-sm-2 mb-sm-0"
      placeholder="email@sm.com"
      v-model="email"
    ></b-form-input>
    <label class="sr-only" for="inline-form-input-username">Password</label>
    <b-input-group prepend="*" class="mb-2 mr-sm-2 mb-sm-0">
      <b-form-input v-model="password" type="password" id="inline-form-input-password" placeholder="****"></b-form-input>
    </b-input-group>
    <b-button type="submit"  variant="primary" @click="authenticate">Login</b-button>
  </b-form>
  </div>
</template>
<script>
import { useAuthStore } from '../../controller/store/auth.store';
export default {
    name: "LoginUser",
    data() {
      return {
        email: "",
        password: ""
      }   
    },
    methods: {
      authenticate() {
        const authStore = new useAuthStore();
        let login_data = {
          "email": this.email,
          "password": this.password
        }
        console.log(login_data)
        authStore.login(login_data);
      }
    }
}
</script>
<style scoped>

.modal-header {
  background-color: rgba(120, 166, 200, 1);
}

#contenidoDelLogin {
  background-color: rgb(49, 103, 137, 1);
}

#botonDeLogin {
  background-color: rgba(120, 166, 200, 1);
  color: white; 
}
#logCancel {
  background-color: rgba(120, 166, 200, 1);
  color: white;
}
    
</style>