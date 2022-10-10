<template>
<div class="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark sidebar-admin" style="width: 280px;">
    <hr>
        <ul class="nav nav-pills flex-column mb-auto">
            <li>
                <b-card-title>My Dashboard</b-card-title>
                <b-button @click="changeTab('my-info')" class="nav-link text-white">
                    My Info
                </b-button>
            </li>
            <li>
                <b-card-title>Manage employees</b-card-title>
                <b-button @click="changeTab('see-employees')" class="nav-link text-white">
                    See Employees
                </b-button>
                <b-button @click="changeTab('see-employees')" class="nav-link text-white">
                    Add Employee
                </b-button>
            </li>
            <li>
                <b-card-title>Task App</b-card-title>
                <b-button  @click="changeTab('my-tasks')" class="nav-link text-white">
                    My Tasks
                </b-button>
                <b-button @click="changeTab('create-task')" class="nav-link text-white">
                    Assign Task
                </b-button>
                <b-button @click="changeTab('team-tasks')" class="nav-link text-white">
                    Team Tasks
                </b-button>
            </li>
        </ul>
    <hr>
  </div>
</template>
<script>
export default {
    name : "TheSideBar",
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
    .sidebar-admin {
        height: 90vh;
        position: sticky;
    }
</style>