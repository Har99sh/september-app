<template lang="">
<div>
    <main>
      <div class="modal modal-signin position-static d-block py-5" tabindex="-1" role="dialog" id="modalSignin">
         <div class="modal-dialog" role="document">
           <div class="modal-content rounded-4 shadow" id="contenidoDelLogin">
             <div class="modal-header p-3 pb-3 border-bottom-0">
               <p class="fw-bold mb-0 fs-5">Sign in to your account</p>
               <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
             </div>
             <div class="modal-body p-4 pt-2s">
               <form class="">
                 <div class="form-floating mb-3">
                   <input type="Name" class="form-control rounded-10" id="floatingInput" placeholder="email" v-model="email">
                   <label for="floatingInput">User</label>
                 </div>
                 <div class="form-floating mb-3">
                     <input type="password" class="form-control rounded-10" id="floatingPassword" placeholder="Password" v-model="password">
                     <label for="floatingPassword">Password</label>
                   </div>
                 <div class="btn-toolbar d-flex justify-content-evenly">
                     <div  class="log  btn btn-lg rounded-3 btn-md botonDeLogin" id="botonDeLogin" @click="authenticate">Login</div>
                     <button class="btn btn-lg rounded-3 btn-md" id="logCancel" type="submit">Cancel</button>
                 </div>
               </form>
             </div>
           </div>
         </div>
     </div>
    </main>
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
        authStore.login(login_data);
      }
    }
}
</script>
<style>

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