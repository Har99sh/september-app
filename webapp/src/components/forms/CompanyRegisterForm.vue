<template>
  <div>
    <main>
      <div class="modal modal-signin position-static d-block py-5" tabindex="-1" role="dialog" id="modalSignin">
         <div class="modal-dialog" role="document">
            <div class="modal-content rounded-4 shadow">
               <div class="modal-header p-3 pb-3 border-bottom-0">
                  <p class="fw-bold mb-0 fs-5">Company Register</p>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
               </div>
               <div class="modal-body p-4 pt-2s">
                  <form class="">
                     <div class="form-floating mb-3 ">
                        <input type="Name" class="form-control rounded-10" id="floatingInput" placeholder="Name">
                        <label for="floatingInput">Name</label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="Lastname" class="form-control rounded-3" id="floatingInput"
                           placeholder="Last Name">
                        <label for="floatingInput">Cif</label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="E-mail" class="form-control rounded-3" id="floatingInput"
                           placeholder="name@example.com">
                        <label for="floatingInput">E-mail</label>
                     </div>
                     <div class="form-floating mb-3">
                        <input type="Mobile" class="form-control rounded-3" id="floatingInput" placeholder="Mobile">

                        <label for="floatingInput">Movile</label>
                     </div>
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
            cif: "",
            email: "",
            telephone:""
         }
      }
   },
  methods: {
    submit: function () {
      const path = "http://127.0.0.1:5000/register-company";
      axios
        .post(path, {
            name: this.name,
            cif: this.cif,
            email: this.email,
            telephone: this.telephone
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
</style>

