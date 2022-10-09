<template lang="">
    <div>
        <EmployeeRegisterForm v-if="active_tab == 'register-employee'"/>
        <CreateTask v-if="active_tab == 'create-task'"/>
        <AdminTasksView v-if="active_tab == 'team-tasks'"/>
        <TaskList v-if="active_tab == 'my-tasks'"/>
        <MyInfo v-if="active_tab == 'my-info'"/>
    </div>
</template>
<script>
import TaskList from "../task_app/TaskList.vue";
import AdminTasksView from "../task_app/AdminTasksView.vue";
import CreateTask from "../task_app/CreateTask.vue";
import MyInfo from '../common/MyInfo.vue'
import EmployeeRegisterForm from "../forms/EmployeeRegisterForm.vue";
export default {
    name: "TabsToShow",
    components: {EmployeeRegisterForm, CreateTask, AdminTasksView, TaskList, MyInfo},
    props: ['active_tab']
}
</script>
<style lang="">
    
</style>