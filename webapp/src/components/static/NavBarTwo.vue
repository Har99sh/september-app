<template>
    <nav class="navbar navbar-expand-lg bg-light">
       <div class="container-fluid">
          <router-link class="navbar-brand" to="/">J4W</router-link>
          <div class="d-flex" id="navbarTogglerDemo02">
             <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                   <router-link class="nav-link active" to="/login">Check</router-link>
                </li>
                <li class="nav-item">
                   <router-link class="nav-link active" to="/register-company" @click="logout()">Logout</router-link>
                </li>
             </ul>
          </div>
       </div>
    </nav>
</template>
<script>
import deleteToken from '../../LocalStorageService'
export default {
    methods: {
       logout() {
         deleteToken()
       }
    }
}
</script>
<style>
    
</style>