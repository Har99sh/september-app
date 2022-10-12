<template lang="">
    <div class="container py-5 task-table">
        <table class="table mb-0 ">
            <thead>
                <tr>
                    <th scope="col">Team Member</th>
                    <th scope="col">Task</th>
                    <th scope="col">Description</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr class="fw-normal" v-for="task in tasks" :key="task.id">
                    <th>
                        <span class="ms-2">{{task.name + ' ' + task.surname}}</span>
                    </th>
                    <td class="align-middle">
                        <span>{{task.title}}</span>
                    </td>
                    <td class="align-middle">
                        <b-button  v-b-modal="'modal'+task.id" >+</b-button>
                    </td>
                    <td class="align-middle">
                        <div>
                            <b-button-toolbar key-nav aria-label="Toolbar with button groups">
                                <b-button-group class="mx-1">
                                <b-button variant="primary">Edit</b-button>
                                <b-button variant="danger" @click="taskStore.deleteTask(task.id)">Delete</b-button>
                                <b-button variant="success">Done</b-button>
                                </b-button-group>
                            </b-button-toolbar>
                        </div>
                    </td>
                    <div>
                    <b-modal :id="'modal'+task.id" hide-backdrop hide-footer scrollable :title="task.title">
                        <p class="my-4">
                            {{task.description}}
                        </p>
                        <b-button-toolbar key-nav aria-label="Toolbar with button groups">
                            <b-button-group class="d-flex justify-content-evenly">
                            <b-button variant="primary">Edit</b-button>
                            <b-button variant="danger" @click="taskStore.deleteTask(task.id)">Delete</b-button>
                            <b-button variant="success">Done</b-button>
                            </b-button-group>
                        </b-button-toolbar>
                    </b-modal>
                </div>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
import { TaskStore } from '../../controller/store/task_api.store'
export default {
    name: "AdminTasksView",
    data() {
        return {
            taskStore: new TaskStore,
            tasks: [],
            employee_list:[]
        }
    },
   mounted() {
       this.taskStore.getCompanyTasks();
       this.tasks = this.taskStore.company_tasks;
       this.employee_list = this.taskStore.employee_list;
   }
}
</script>
<style>
    .task-table {
        max-height: 600px;
        overflow-y: scroll;
    }
</style>