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
                  <b-form autocomplete="off">
                     <div class="form-floating mb-3 ">
                        <b-form-input type="text" class="form-control rounded-10" v-model="name" id="firstname"></b-form-input>
                        <label for="firstname">Name</label>
                     </div>
                     <div class="form-floating mb-3">
                        <b-form-input type="text" class="form-control rounded-3" v-model="surname" id="surname"></b-form-input>
                        <label for="surname">Last name</label>
                     </div>                    
                      <div class="form-floating mb-3">
                        <b-form-input type="text" class="form-control rounded-3" v-model="dni" id="dni" ></b-form-input>
                        <label for="dni">DNI</label>
                     </div>
                     <div class="form-floating mb-3">
                        <b-form-input type="email" class="form-control rounded-3" id="email"
                               placeholder="name@example.com" autocomplete="off" v-model="email" ></b-form-input>
                        <label for="email">E-mail</label>
                     </div>
                     <div class="form-floating mb-3">
                        <b-form-input type="password" class="form-control rounded-3" id="password" v-model="password" placeholder="***********" autocomplete="off"></b-form-input>
                        <label for="password">Password</label>
                     </div>
                      <b-form-checkbox v-model="is_admin" >Admin</b-form-checkbox>
                     <div class=" btn-toolbar d-flex justify-content-evenly">
                        <b-button class="log btn btn-lg rounded-3 btn-md botonDeSubmit" @click="register">Submit</b-button>
                     </div>
                  </b-form>
               </div>
            </div>
         </div>
      </div>
   </main>
    </div>
</template>
<script>
import { useAdminStore } from '../../controller/store/admin.store';
export default {
   data() {
      return  {
         user_data :{
            name: "Name",
            surname: "Surname",
            dni:"ID",
            email: "employee@email.com",
            password:"*****",
            is_admin: false,
         }
      }
   },
  methods: {
     register() {
      console.log("componnet clco")
      let data =  {
         name: this.name,
            surname: this.surname,
               email: this.email,
               password: this.password,
               is_admin: this.is_admin || false,
               dni: this.dni
         };
         console.log(data)
         let store  = useAdminStore()
         console.log(store)
         store.register(data)
      // console.log(data)
      // await this.adminStore.registerEmployee(data);
      // console.log("hello")

      // this
    },
  },
};
</script>
<style scoped>
</style>