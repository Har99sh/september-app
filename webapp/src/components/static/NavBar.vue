<template>
    <nav class="navbar navbar-expand-lg bg-light">
       <div class="container-fluid">
          <router-link class="navbar-brand" to="/">J4W</router-link>
          <div class="d-flex" id="navbarTogglerDemo02">
             <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                   <router-link class="nav-link active" to="/login">Login</router-link>
                </li>
                <li class="nav-item">
                   <router-link class="nav-link active" to="/register/company">SignUp</router-link>
                </li>
             </ul>
          </div>
       </div>
    </nav>
</template>
<script>
export default {
    
}
</script>
<style>
    
</style>