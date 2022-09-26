<template lang="">
    <div>
        {{user_list}}
    </div>
</template>
<script>
import axios from 'axions';
export default {
    name:"AllEmployees",
    data() {
        return {
            user_list:[],
        }
    },
    methods: {
        get_all_employees() {
            const path = "http://127.0.0.1:5000/users"
            axios.get(path, )
            .then(response => user_list = response)
        }
    }
}
</script>
<style lang="">
    
</style>