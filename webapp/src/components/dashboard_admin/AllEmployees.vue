<template lang="">
    <div class="container py-5 task-table">
        <table class="table mb-0 ">
            <thead>
                <tr>
                    <th scope="col">Employee Name</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr class="fw-normal" v-for="employee in employee_list" :key="employee.id">
                    <th>
                        <span class="ms-2">{{employee.name + ' ' + employee.surname}}</span>
                    </th>
                    <td class="align-middle">
                        <div>
                            <b-button-toolbar key-nav aria-label="Toolbar with button groups">
                                <b-button-group class="mx-1">
                                    <b-button variant="primary"> Assign Task </b-button>
                                    <b-button variant="danger">Delete </b-button>
                                    <b-button  v-b-modal="'modal'+employee.id" >+</b-button>
                                </b-button-group>
                            </b-button-toolbar>
                        </div>
                    </td>
                    <div>
                    <b-modal :id="'modal'+employee.id" hide-backdrop hide-footer scrollable :title="employee.name + ' ' + employee.surname">
                        <p class="my-4">
                            {{employee.id}}
                        </p>
                         <!-- Using value -->
                        <b-button v-b-toggle.task-list class="m-1">See tasks</b-button>
                        <b-button v-b-toggle.shift-logs class="m-1">See tasks</b-button>
                        <!-- Element to collapse -->
                        <b-collapse id="task-list">
                            <b-list-group>
                                    <b-list-group-item v-for="task in employee_list.tasks" :key="task.id">Cras justo odio</b-list-group-item>
                            </b-list-group>
                        </b-collapse>
                        <b-collapse id="shift-logs">
                            <b-list-group>
                                    <b-list-group-item v-for="log in employee_list.shifts_logs" :key="log.id">Cras justo odio</b-list-group-item>
                            </b-list-group>
                        </b-collapse>
                    </b-modal>
                </div>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
import { TaskStore } from '../../controller/store/task_api.store';
export default {
    name:"AllEmployees",
    data() {
        return {
            employee_list:[],
            taskStore: new TaskStore,
        }
    },
    mounted() {
        this.taskStore.getEmployeeList();
        this.employee_list = this.taskStore.employee_list;
        console.log(this.employee_list)
    },
}
</script>
<style lang="">
    
</style>