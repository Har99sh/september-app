<template>
    <div class="style-body">
    <main>
      <div class="modal modal-register position-static d-block py-5" tabindex="-1" role="dialog" id="modalRegister">
         <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
               <div class="modal-header p-3 pb-3 border-bottom-0">
                  <p class="fw-bold mb-0 fs-5">Register Employee</p>
               </div>
               <div class="modal-body p-4 pt-2s">
                  <form class="">
                     <div class="form-floating mb-3 ">
                        <input type="Name" class="form-control rounded-10" placeholder="Name" v-model="name" id="firstname">
                        <label for="firstname">Name</label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="Lastname" class="form-control rounded-3" v-model="surname" id="surname" placeholder="Last Name">
                        <label for="surname">Last name</label>
                     </div>                    
                      <div class="form-floating mb-3">
                        <input type="ID" class="form-control rounded-3" v-model="dni" id="dni" placeholder="X------">
                        <label for="surname">DNI</label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="E-mail" class="form-control rounded-3" id="email"
                           placeholder="name@example.com">
                        <label for="email">E-mail</label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="password" class="form-control rounded-3" id="password" v-model="password" placeholder="***********">

                        <label for="password">Password</label>
                     </div>
                      <b-form-checkbox v-model="is_admin" >Admin</b-form-checkbox>
                     <div class=" btn-toolbar d-flex justify-content-evenly">
                        <button class="log btn btn-lg rounded-3 btn-md botonDeSubmit" type="submit" @click="submit">Submit</button>
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
<style scoped>
</style>