<template>
    <div class="task-form-container">

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
            <input type="text" class="form-control rounded-10" id="floatingInput" placeholder="Task title" v-model="assignee">
            <label for="floatingInput">Assign to</label>
        </div>

        <div class="assign-button" @click="create_task">Assign</div>

    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: 'CreateTask',
    data() {
        return {
            title : "",
            description: "",
            due_date: "",
            employee_id: "1111",
            assignee:"",
            assigned_by: "1111",
            company_id: "1111",
            is_completed : false
        }
    },
    methods: {
        create_task() {
            const path = "http://127.0.0.1:5000/tasks/create";
            axios
            .post(path, {
                title : this.title,
                description: this.description,
                due_date: this.due_date,
                employee_id: this.employee_id,
                assigned_by_id: this.assigned_by,
                company_id: this.company_id,
                is_completed : this.is_completed,
            })
            .then(response => {
                console.log(response)
            })
            .catch(err => {
                console.error(err)
            })
        }
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