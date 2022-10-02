<template>
  <div>
      <form>
         <input type="text" v-model="name" placeholder="name">
         <input type="text" v-model="cif" placeholder="cif">
         <input type="email" v-model="email" placeholder="email">
         <input type="telephone" v-model="telephone" placeholder="telephone">
         <!-- <input type="text" v-model="company_id" placeholder="1111"> -->
         <input type="submit" @click="submit">
      </form>
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
  
</style>

