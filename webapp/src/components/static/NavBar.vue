<template >
    <nav class="navbar navbar-expand-lg bg-light">
       <div class="container-fluid">
          <router-link class="navbar-brand" to="/">J4W</router-link>

          <div v-if="is_logged" class="d-flex" id="navbarTogglerDemo02">
             <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                   <router-link class="nav-link active" to="/login">Login</router-link>
                </li>
                <li class="nav-item">
                   <router-link class="nav-link active" to="/register-company">SignUp</router-link>
                </li>
             </ul>
          </div>

         <div v-else class="d-flex" id="navbarTogglerDemo02">
             <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                   <b-button  v-b-modal.time_tracker_modal class="nav-link">Start timer</b-button>
                </li>
                <li class="nav-item">
                   <router-link class="nav-link active" to="/" @click="logout">Logout</router-link>
                </li>
             </ul>

              <b-modal id="time_tracker_modal" centered title="Start your shift?" data-bs-backdrop="static" hide-footer hide-backdrop content-class="shadow">
                  <div class="modal-header modal-dialog-centered">
                     <h1 class="modal-dialog modal-dialog-centered">{{running_time}}</h1>
                  </div>
                  <b-button type="button" v-if="!is_running" class="btn btn-primary paused boton-color" id="play-pause" @click="startTimer">
                     Start Timer
                  </b-button>

                  <b-button type="button" class="btn btn-primary paused" id="play-pause" v-else @click="stopTimer">
                     Stop Timer
                  </b-button>
            </b-modal>
          </div>

       </div>
    </nav>
</template>

<script>
import {useAuthStore} from '../../controller/store/auth.store';
import { shiftStore } from '../../controller/store/shift_api.store';
export default {
   data() {
      return{
         authStore: new useAuthStore(),
         total_time: null,
         running_time: 0,
         start_time: null,
         finish_time: null,
         is_running: false,
         time_interval: null,
         shiftStore : new shiftStore
      }
   },
   computed: {
      is_logged() {
         return this.authStore.isLoggedIn();
      }
   },
   methods: {
      logout(){
         this.authStore.logout()
      },
      startTimer() {
         // Send post request to api /start-timer
         this.shiftStore.startShift()
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
         this.shiftStore.endShift()
         this.is_running = false;
         this.running_time = 0;
         clearInterval(this.time_interval);
      }
   }
}
</script>
<style>
.boton.color {
   background-color: rgba(49, 103, 137, 1);
}
</style>
