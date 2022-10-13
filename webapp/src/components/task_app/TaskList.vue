<template>
    <div>   
        <div class="d-flex justify-content-around w-100">
            <b-button variant="info" @click="filter_task('all')">All</b-button>
            <b-button variant="success" @click="filter_task('done')">Done</b-button>
            <b-button variant="primary" @click="filter_task('todo')">To Do</b-button>       
        </div>
        <div class="container py-5 task-table" v-if="task_list.length !== 0" >
            <table class="table mb-0 ">
                <thead>
                    <tr>
                        <th scope="col">Task</th>
                        <th scope="col">Due on</th>
                        <th scope="col">Description</th>
                        <th scope="col">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="fw-normal" v-for="task in task_list" :key="task.id">
                        <th>
                            <span class="ms-2">{{task.title}}</span>
                        </th>                   
                        <td>
                            <span class="ms-2">{{task.due_date.slice(0, -13)}}</span>
                        </td>
                        <td class="align-middle">
                            <b-button  v-b-modal="'modal'+task.id" >+</b-button>
                        </td>
                        <td class="align-middle">
                            <div>
                                <b-button-toolbar key-nav aria-label="Toolbar with button groups">
                                    <b-button-group class="mx-1">
                                    <b-button variant="danger">Comment</b-button>
                                    <b-button :variant="done_style(task.is_completed)" 
                                        @click="markAsDone(task.id)"
                                        :disabled="task.is_completed">
                                        Done
                                    </b-button>
                                    </b-button-group>
                                </b-button-toolbar>
                            </div>
                        </td>
                        <div>
                        <b-modal :id="'modal'+task.id" hide-backdrop hide-footer scrollable :title="task.title">
                            <p class="my-4">
                                <strong> Due on {{task.due_date.slice(0, -13)}}</strong>
                            </p>
                            <p class="my-4">
                                {{task.description}}
                            </p>
                            <b-button-toolbar key-nav aria-label="Toolbar with button groups">
                                <b-button-group class="d-flex justify-content-evenly">
                                <b-button variant="outline-danger">Comment</b-button>
                                <b-button :variant="done_style(task.is_completed)" 
                                        @click="taskStore.markAsDone(task.id)"
                                        :disabled="task.is_completed">
                                        Done
                                </b-button>
                                </b-button-group>
                            </b-button-toolbar>
                        </b-modal>
                    </div>
                    </tr>
                </tbody>
            </table>
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
</div>
</template>
<script>

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
        markAsDone(id) {
            this.taskStore.markAsDone(id);
            this.task_list = this.taskStore.undone_task_list;
            this.updateView();
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
        getMyTasks() {
            this.taskStore.getMyTasks()
            this.task_list = this.taskStore.undone_task_list;
        },
        updateView() {
            this.$forceUpdate();
        }
    },
    beforeMount() {
        this.getMyTasks();
    }
}
</script>

<style>
.all-tasks-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
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