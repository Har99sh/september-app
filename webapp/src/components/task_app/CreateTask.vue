<template>
<div class="style-body">
    <div v-if="task_not_created" @click="try_again">Task was not created properly, please try again.</div>
    <main>
        <div class="modal modal-signin position-static d-block py-5" tabindex="-1" role="dialog" id="modalSignin">
            <div class="modal-dialog" role="document">
                <div class="modal-content rounded-4 shadow" id="contenidoDelLogin">
                    <div class="modal-header p-3 pb-3 border-bottom-0">
                       <p class="fw-bold mb-0 fs-5">New Task</p>
                       <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body p-4 pt-2s">
                    <form class="">
                        <div class="form-floating mb-3 ">
                            <input type="text" class="form-control rounded-10" id="floatingInput" placeholder="Task title" v-model="title">
                            <label for="floatingInput">Task Title</label>
                        </div>
                        <div class="form-floating mb-3 ">
                            <textarea type="textarea" rows="15" class="form-control textarea-description rounded-10"  placeholder="Task title" v-model="description" />
                            <label for="floatingInput">Description</label>
                        </div>
                        <div class="form-floating mb-3 ">
                            <input type="date" class="form-control rounded-10" id="floatingInput" placeholder="Task title" v-model="due_date">
                            <label for="floatingInput">Due Date</label>
                        </div>
                        <div class="form-floating mb-3 ">
                            <b-form-select v-model="employee_id" @input="tell_me">
                                <b-form-select-option :value="null" disabled>-- Please select an option --</b-form-select-option>
                                <b-form-select-option v-for="employee in employee_list" :key="employee.id" :value="employee.id">{{employee.name +' '+employee.surname}}</b-form-select-option>
                            </b-form-select>
                            <label for="floatingInput">Assign to</label>
                        </div>
                        <div>
                            <div class="log  btn btn-lg rounded-3 btn-md " id="botonDeLogin" @click="create_task">Assign</div>
                        </div>

                    </form>
                </div>
                </div>
            </div>
        </div>
    </main>
</div>
    


</template>
<script>
import axios from 'axios';
import { TaskStore } from '../../controller/store/task_api.store';
export default {
    name: 'CreateTask',
    data() {
        return {
            title : "",
            description: "",
            due_date: "",
            employee_id: "",
            assignee:"",
            assigned_by: "1111",
            company_id: "1111",
            is_completed : false,
            task_not_created: false,
            employee_list : [],
            taskStore: new TaskStore
        }
    },
    methods: {
        create_task() {
            this.taskStore.create_task({
                title : this.title,
                description: this.description,
                due_date: this.due_date,
                employee_id: this.employee_id,
                assigned_by_id: this.assigned_by,
                company_id: this.company_id,
                is_completed : this.is_completed,
            })
            // .then(() => {
            //     this.$router.push({path: '/tasks'});
            // })
            // .catch(() => {
            //     this.task_not_created = true;
            // })
        },
        try_again() {
            this.task_not_created = false;
        },
        tell_me(person) {
            console.log(person);
            console.log(this.employee_id)
        }
    },
    mounted() {
        const path = `http://127.0.0.1:5000/employee/1111`;
        axios.get(path)
        .then(response => this.employee_list = response.data)
        .catch(error => console.log(error))
    },
}
</script>
<style scoped>

.task-form-container{
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.task-form-container .form-floating {
    width: 600px;
}
.task-form-container .textarea-description {
    height: 150px;
}

.assign-button {
    width: 60px;
    height: 40px;
    text-align: center;
}
</style>