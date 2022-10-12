<template>
    <div class="tab-to-show">
        <EmployeeRegisterForm v-if="active_tab == 'register-employee'"/>
        <CreateTask v-if="active_tab == 'create-task'"/>
        <AdminTasksView v-if="active_tab == 'team-tasks'"/>
        <TaskList v-if="active_tab == 'my-tasks'"/>
        <MyInfo v-if="active_tab == 'my-info'"/>
        <AllEmployees v-if="active_tab=='see-employees'"/>
    </div>
</template>

<script>

import TaskList from "../task_app/TaskList.vue";
import AdminTasksView from "../task_app/AdminTasksView.vue";
import CreateTask from "../task_app/CreateTask.vue";
import MyInfo from '../common/MyInfo.vue'
import EmployeeRegisterForm from "../forms/EmployeeRegisterForm.vue";
import AllEmployees from './AllEmployees.vue'

export default {
    name: "TabsToShow",
    components: {EmployeeRegisterForm, CreateTask, AdminTasksView, TaskList, MyInfo, AllEmployees},
    props: ['active_tab'],
}
</script>

<style>
    .tab-to-show {
        width: 100%;
        display: flex;
        justify-content: center;
        align-content: center;
    }
</style>