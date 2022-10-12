<template>
   <div>
      <nav class="navbar navbar-expand-lg bg-light">
         <div class="container-fluid">
            <router-link class="navbar-brand" to="/">J4W</router-link>
            <div class="d-flex" id="navbarTogglerDemo02">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
               <li class="nav-item">
               <router-link v-b-modal.modal-1 class="nav-link active" to="/login">Check</router-link>
               </li>
               <li class="nav-item">
               <router-link class="nav-link active" to="/register-company" @click="logout()" >Logout</router-link>
               </li>
            </ul>
         </div>
      </div>
   </nav>

      <b-modal id="modal-1" centered title="text-center" data-bs-backdrop="static" hide-footer hide-backdrop content-class="shadow">
         <div class="modal-header modal-dialog-centered">
            <h1 class="modal-dialog modal-dialog-centered">{{running_time}}</h1>
         </div>
         <div class="modal-body display-1 text-tipe" id="stopwatch" >
            {{runningTime}}
         </div>

         <b-button type="button" v-if="!is_running" class="btn btn-primary paused boton-color" id="play-pause" @click="startTimer">
            Start Timer
         </b-button>

         <b-button type="button" class="btn btn-primary paused" id="play-pause" v-else @click="stopTimer">
            Stop Timer
         </b-button>
     </b-modal>
   </div>
</template>

<script>
   import deleteToken from "../../LocalStorageService";
   export default {
      name: 'App',
      data() {
         return {
         total_time: null,
         running_time: 0,
         start_time: null,
         finish_time: null,
         is_running: false,
         time_interval: null,
         }
      },
   methods: {
      logout() {
         deleteToken();
      },
      startTimer() {
         // Send post request to api /start-timer
         this.is_running = true;
         this.start_time = Date.now() - this.running_time;
         this.time_interval = setInterval(()=> {
         this.running_time = Date.now() - this.start_time;
         this.calculateTime(this.running_time);
         }, 1000)
      },
      calculateTime(runningTime) {
           const total_seconds = Math.floor(runningTime / 1000);
           const total_minutes = Math.floor(total_seconds / 60);
           const total_hours = Math.floor(total_minutes / 60);
           const display_seconds = (total_seconds % 60).toString().padStart(2, "0");
           const display_minutes = total_minutes.toString().padStart(2, "0");
           const display_hours = total_hours.toString().padStart(2, "0");
           this.running_time =  `${display_hours}:${display_minutes}:${display_seconds}`
      },
      stopTimer(){
         //Send post request api to stop timer
         this.is_running = false;
         this.running_time = 0;
         clearInterval(this.time_interval);
      }
   }
}
</script>
 
<style>
#app {
   font-family: Avenir, Helvetica, Arial, sans-serif;
   -webkit-font-smoothing: antialiased;
   -moz-osx-font-smoothing: grayscale;
   text-align: center;
   color: rgba(49, 103, 137, 1);
   margin-top: 60px;
}
.boton.color {
   background-color: rgba(49, 103, 137, 1);
}
 </style>