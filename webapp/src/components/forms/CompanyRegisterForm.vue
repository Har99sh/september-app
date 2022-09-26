<template>
  <div>
      <form>
         <input type="text" v-model="name" placeholder="name">
         <input type="text" v-model="surname" placeholder="surname">
         <input type="email" v-model="email" placeholder="email">
         <input type="password" v-model="password" placeholder="password">
         <input type="checkbox" v-model="is_admin">
         <input type="text" v-model="company_id" placeholder="1111">
         <input type="text" v-model="dni" placeholder="111111">
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
            surname: "",
            email: "",
            password:"",
            is_admin: null,
            company_id:"",
            dni:""
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

<style>
</style>