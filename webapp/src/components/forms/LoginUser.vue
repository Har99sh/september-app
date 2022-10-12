<template lang="">
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

                              <h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign into your account</h5>

                              <div class="form-outline mb-4">
                                      <b-form-input
                                        id="inline-form-input-name"
                                        class="form-control form-control-lg"
                                        placeholder="email@sm.com"
                                        v-model="email"
                                      ></b-form-input>
                                  <label class="form-label" for="form2Example17">Email address</label>
                              </div>

                              <div class="form-outline mb-4">
                                  <b-form-input v-model="password" type="password" class="f" id="inline-form-input-password" placeholder="****"></b-form-input>
                                  <label class="form-label" for="form2Example27">Password</label>
                              </div>

                              <div class="pt-1 mb-4">
                                      <b-button class="btn btn-dark btn-lg btn-block" type="submit" @click="authenticate">Login</b-button>
                              </div>

                              <a class="small text-muted" href="#!">Forgot password?</a>
                              <a href="#!" class="small text-muted">Terms of use.</a>
                              <a href="#!" class="small text-muted">Privacy policy</a>
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