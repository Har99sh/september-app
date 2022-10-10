<template>
    <div class="all-tasks-container" v-if="task_list.length !== 0" >
        <div class="d-flex justify-content-around w-50">
            <b-button variant="info" @click="filter_task('all')">All</b-button>
            <b-button variant="success" @click="filter_task('done')">Done</b-button>
            <b-button variant="primary" @click="filter_task('todo')">To Do</b-button>   
            <label for="sort_by">Sort By</label>
            <b-form-select @input="sort_task" id="sort_by" class="w-50">
                <b-form-select-option  value="due_date"> Due Date </b-form-select-option>
            </b-form-select>        
        </div>
        <div class="card w-75" v-for="task in task_list"  :key="task.id" >
            <div class="card-body" :id="task.id">
                <h5 class="card-title">{{task.title}}</h5>
                <p class="card-text" >Due on {{task.due_date}}</p>
                <b-collapse :id="'collapse'+task.id" class="mt-2">
                    <b-card>
                        <p class="card-text">{{task.description}}</p>
                    </b-card>
                </b-collapse>
                <div class="task-actions">
                    <b-button v-b-toggle="'collapse'+task.id" class="m-1">Description</b-button>
                    <b-button class="m-1" 
                              :variant="done_style(task.is_completed)" 
                              @click="markAsDone(task.id)"
                              :disabled="task.is_completed">
                            Mark As Done 
                    </b-button>
                </div>
            </div>
        </div>
    </div>
    <!--Show this if there are no tasks in the database-->
    <div v-else>
        <b-card
            overlay
            img-src="https://picsum.photos/900/250/?image=3"
            img-alt="Card Image"
            text-variant="white"
            title="You do not have any tasks at the moment">
        </b-card>
    </div>
</template>
<script>
import axios from 'axios';
import {TaskStore} from '../../controller/store/task_api.store'
export default {
    name : 'TaskList',
    data() {
        return {
            task_list: [],
            master_list:[],
            there_are_task : false,
            axios_base_path: "http://127.0.0.1:5000/tasks/",
            date: "",
            show_description: false,
            description_text: "DESCRIPTION",
            mark_as_done:"",
            taskStore: new TaskStore,
        }
    },
    methods: {
        getTasks() {
            this.taskStore.getMyTasks();
            // console.log(this.authStore)
            // const path = "http://127.0.0.1:5000/tasks/mine/"+this.authStore.user.user_id;
            // const token = this.authStore.getToken();
            // axios.get(path, { headers: {"Authorization" : 'Bearer ' + token}})
            // .then(response => {
            //     this.master_list = response.data
            //     this.task_list = response.data.filter((task) => task.is_completed == false);
            // })
            // .catch(err => {
            //     console.log(err)
            // })
        },
        markAsDone(id) {
            //this.getTaskId();
            console.log(id)
            const path = this.axios_base_path + 'done/' + id;
            axios.put(path)
            .then(response => console.log(response))
            .catch(error => console.log(error))
        },
        done_style(done){
            if (done) {
                return "success";
            }
            else {
                return "primary";
            }
        },
        filter_task(type) {
            if (type == "all") {
                this.task_list = this.master_list;
            } else if (type == "done") {
                this.task_list = this.master_list.filter((task) => task.is_completed == true);
            } else if (type == "todo") {
                this.task_list = this.master_list.filter((task) => task.is_completed == false);
            }  
        },
        sort_task(sort_by) {
            if (sort_by == "due_date") {
                this.task_list = this.task_list.sort((a,b) => new Date(a.due_date) - new Date(b.due_date));
            }
        }
    },
    computed:{
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
    align-content: center;
    flex-direction: column;
    row-gap: 10px;
    width: 100%;
}
.task-actions {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}
.task-action{
    background-color: darkgray;
    padding: 2px 3px;
    width: fit-content;
    height: 30px;
    text-align: center;
}
.d-none {
    display: none;
}

</style>