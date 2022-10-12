<template>
<div class="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark sidebar-user" style="width: 280px;">
    <hr>
        <ul class="nav nav-pills flex-column mb-auto">
            <li>
                <b-card-title>My Dashboard</b-card-title>
                <b-button @click="changeTab('my-info')" class="nav-link text-white">
                    My Info
                </b-button>
            </li>
            <li>
                <b-card-title>Task App</b-card-title>
                <b-button  @click="changeTab('my-tasks')" class="nav-link text-white">
                    My Tasks
                </b-button>                
            </li>
        </ul>
    <hr>
  </div>
</template>
<script>
export default {
    name : "TheSideBarUser",
    data() {
        return{};
    },
    methods: {
        changeTab(tab) {
            this.$emit('change-tab', tab)
        }
    },
}
</script>
<style scoped>
    .sidebar-user {
        height: 90vh;
    }
</style>