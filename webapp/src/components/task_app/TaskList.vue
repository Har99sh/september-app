<template>
    <div class="all-tasks-container" v-if="task_list.length !== 0" >
        <div class="card w-75" v-for="task in task_list"  :key="task.id" >
            <div class="card-body" v-bind:id="task.id">
                <h5 class="card-title">{{task.title}}</h5>
                <p class="card-text">{{task.description}}</p>
                <p class="card-text">Due on {{task.due_date}}</p>
                <div class="task-actions">
                    <div class="mark-as-done task-action" 
                        v-bind:data-task_id="task.id"
                        @click="markAsDone()">
                        DONE
                    </div>
                    <div class="mark-as-rejected task-action">REJECT</div>
                </div>
            </div>
        </div>
    </div>
    <!--Show this if there are no tasks in the database-->
    <div v-else>There are no tasks!</div>
</template>
<script>
import axios from 'axios';
export default {
    name : 'TaskList',
    data() {
        return {
            task_list: [],
            there_are_task : false,
            axios_base_path: "http://127.0.0.1:5000/tasks/",
            task_id : "",
        }
    },
    methods: {
        getTasks() {
            const path = "http://127.0.0.1:5000/tasks";
            axios.get(path)
            .then(response => {
                this.task_list = response.data;
                console.log(this.task_list)
            })
            .catch(err => {
                console.log(err)
            })
        },
        getTaskId() {
            let done_btn = document.querySelector(".mark-as-done");
            let id = done_btn.dataset.task_id;
            this.task_id = id;
            console.log(document.querySelector(".card-body").id)
        },
        markAsDone() {
            this.getTaskId();
            console.log(this.task_id)
            const path = this.axios_base_path + 'done/' + this.task_id;
            axios.put(path)
            .then(response => console.log(response))
            .catch(error => console.log(error))
        }
    },
    created() {       
        this.getTasks();
    },
}
</script>
<style scoped>
.all-tasks-container {
    display: flex;
    justify-content: center;
    flex-direction: column;
    width: 100%;
}
.task-actions {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}
.task-action{
    background-color: darkgray;
    width: 60px;
    height: 30px;
    text-align: center;
}
</style>