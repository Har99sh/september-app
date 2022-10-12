<template>
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
                                    <b-button  :v-b-modal="'modal'+employee.id" >+</b-button>
                                </b-button-group>
                            </b-button-toolbar>
                        </div>
                    </td>
                    <div>
                    <b-modal :id="'modal'+employee.id" hide-backdrop hide-footer scrollable :title="employee.name + ' ' + employee.surname">
                        <p class="my-4">
                            {{employee.email}}
                        </p>
                         <!-- Using value -->
                        <b-button v-b-toggle="'task-list'" class="m-1">See tasks</b-button>
                        <!-- Element to collapse -->
                        <b-collapse id="task-list">
                            <b-list-group>
                                    <b-list-group-item>Cras justo odio</b-list-group-item>
                                    <b-list-group-item>Dapibus ac facilisis in</b-list-group-item>
                                    <b-list-group-item>Morbi leo risus</b-list-group-item>
                                    <b-list-group-item>Porta ac consectetur ac</b-list-group-item>
                                    <b-list-group-item>Vestibulum at eros</b-list-group-item>
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
export default {
    name: 'EmployeeCard',
    props: {
        employee_list: {
            type : Array,
            required: true
        }
    },
    data(){
        return{}
    }
}
</script>
<style>
    
</style>