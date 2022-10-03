<template>
    <div>
    <main>
      <div class="modal modal-signin position-static d-block py-5" tabindex="-1" role="dialog" id="modalSignin">
         <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow" id="contenidoDelLogin">
               <div class="modal-header p-3 pb-3 border-bottom-0">
                  <p class="fw-bold mb-0 fs-5">Register</p>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
               </div>
               <div class="modal-body p-4 pt-2s">
                  <form class="">
                     <div class="form-floating mb-3 ">
                        <input type="Name" class="form-control rounded-10" id="floatingInput" placeholder="Name" v-model="name">
                        <label for="floatingInput">Name</label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="Lastname" class="form-control rounded-3" id="floatingInput"
                           placeholder="Last Name" v-model="surname">
                        <label for="floatingInput">Last Name</label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="text" class="form-control rounded-3" id="floatingInput" placeholder="DNI" v-model="dni">

                        <label for="floatingInput">DNI</label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="E-mail" class="form-control rounded-3" id="floatingInput"
                           placeholder="name@example.com" v-model="email">
                        <label for="floatingInput">E-mail </label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="password" class="form-control rounded-3" id="floatingPassword"
                           placeholder="Password" v-model="password">
                        <label for="floatingPassword">Password</label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="confirm-password" class="form-control rounded-3" id="floatingPassword"
                           placeholder="Password" v-model="password">
                        <label for="floatingPassword">Confirm your Password</label>
                     </div>
                     <div class="form-check mb-3">
                        <input type="checkbox" class="form-check-input" id="is_admin" v-model="is_admin">
                        <label class="floating-input" for="is_admin">Admin?</label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="text" class="form-control rounded-3" id="floatingInput" placeholder="Company Id" v-model="company_id">

                        <label for="floatingInput">Company ID</label>
                     </div>
                     <div class=" btn-toolbar d-flex justify-content-evenly">
                        <button class="log  btn btn-lg rounded-3 btn-md" id="botonDeLogin" @click="submit">Register</button>
                        <button class="logcancel  btn btn-lg rounded-3 btn-md" id="logCancel" type="submit"> Cancel</button>
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
import axios from "axios";
export default {
   data() {
      return  {
         user_data :{
            name: "",
            surname: "",
            dni:"",
            email: "",
            password:"",
            is_admin: null,
            company_id:"",
         }
      }
   },
  methods: {
    submit: function () {
      const path = "http://127.0.0.1:5000/register";
      axios
        .post(path, {
            name: this.name,
            surname: this.surname,
            email: this.email,
            password: this.password,
            is_admin: this.is_admin,
            company_id:this.company_id,
            dni: this.dni
        })
        .then((response) => {
          console.log(response);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
<style>
.modal-header {
  background-color: rgba(120, 166, 200, 1);
}

.modal-content {
  background-color: rgb(49, 103, 137, 1);
}

.botonDeSubmit {
  background-color: rgba(120, 166, 200, 1);
  color: rgb(0, 0, 0); 
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