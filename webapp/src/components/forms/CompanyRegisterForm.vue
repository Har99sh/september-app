<template>

   <div>
      <section class="vh-100" style="background-color: #696969;">
         <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
               <div class="col col-xl-10">
                  <div class="card" style="border-radius: 1rem;">
                     <div class="row g-0">
                        <div class="col-md-6 col-lg-5 d-none d-md-block">
                           <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/img1.webp"
                              alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" />
                        </div>
                        <div class="col-md-6 col-lg-7 d-flex align-items-center">
                           <div class="card-body p-4 p-lg-5 text-black">
                              <b-form>
                                 <div class="d-flex align-items-center mb-3 pb-1">
                                     <i class="fas fa-cubes fa-2x me-3" style="color: #ff6219;"></i>
                                     <span class="h1 fw-bold mb-0">Just4Work</span>
                                 </div>

                                 <h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Register</h5>
                                 <div class="form-outline mb-4">
                                    <b-form-input class="form-control rounded-10" type="Name" id="floatingInput" placeholder="Name"></b-form-input>
                                    <label class="form-label" for="floatingInput">Name</label>
                                 </div>

                                 <div class="form-outline mb-4">
                                    <b-form-input class="form-control rounded-10" type="Lastname" id="floatingInput" placeholder="Cif"></b-form-input>
                                    <label class="form-label" for="floatingInput">Cif</label>
                                 </div>

                                 <div class="form-outline mb-4">
                                    <b-form-input
                                       id="floatingInput"
                                       class="form-control rounded-10"
                                       placeholder="email@sm.com"
                                       type="E-mail" 
                                       v-model="email"
                                       >
                                    </b-form-input>
                                    <label class="form-label rounded-3" for="floatingInput">Email address</label>
                                 </div>

                                 <div class="form-outline mb-4">
                                     <b-form-input v-model="password" type="Mobile" class="form-control rounded-3" id="floatingInput" placeholder="Telephone"></b-form-input>
                                     <label class="form-label" for="floatingInput">Telephone</label>
                                 </div>

                                 <div class="pt-1 mb-4">
                                    <b-button class="log btn btn-lg rounded-3 btn-md botonDeSubmit " type="submit" @click="submit">Login</b-button>
                                 </div>

                                 <div class="classTerms">
                                    <div><a class="small text-muted" href="#!">Forgot password?</a></div>
                                    <div><a href="#!" class="small text-muted">Terms of use.</a></div>
                                    <div><a href="#!" class="small text-muted">Privacy policy</a></div>
                                 </div>
                              </b-form>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </section>
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

.classTerms {
   display: flex;
   justify-content: space-between;
}
.classTerms a:link, a:visited, a:active a:focus a:hover {
   text-decoration:none;
    color: black;
}
</style>

