import { defineStore } from "pinia";
import { useApiStore } from "./api.store";

export const TaskStore = defineStore({
    id:"task_store",
    state: ()=> ({
        user_id : null,
        company_id: null,
        task_list : [],
        api: null,
        done_task_list:[],
        undone_task_list:[],
        company_tasks: [],
        empoyee_list: [],
    }),
    getters: {
        doneTasks: (state) => state.done_task_list = state.task_list.filter((task) => task.is_completed == true),
        undoneTasks: (state) => state.undone_task_list = state.task_list.filter((task) => task.is_completed == true),
        notDeletedTasks: (state, id) => state.done_task_list = state.done_task_list.filter(task => task.id !== id)
    },
    actions: {
        initialise() {
            const store = useApiStore();
            store.createApiInstance();
            this.user_id = store.user_id;
            this.api = store.api;
            this.company_id = store.company_id;
        },
        getMyTasks() {
            if (this.user_id == null)
                this.initialise();
            this.api.get('tasks/mine/' + this.user_id)
                .then((response) => {
                    this.task_list = response.data;
                    this.undone_task_list = this.task_list.filter((task) => task.is_completed == true);
                })
                .catch(error => console.log(error))  
        },
        create_task(data) {
            if (this.api == null)
                this.initialise();
            this.api.post('tasks/create', data)
        },
        markAsDone(task_id) {
            if (this.api == null) {
                this.initialise();
            }
            this.api.post('tasks/done', {"id": task_id})
            .then(() => {
                this.undone_task_list = this.task_list.filter((task) => task.is_completed == false);
            })
            .catch(err => console.log(err))
            .finally(()=> console.log("done or not done"))
        },
        getCompanyTasks() {
            if (this.user_id == null)
                this.initialise();
            this.api.get('tasks/company/' + this.company_id)
            .then((response) => {
                console.log(response.data)
                this.company_tasks = response.data;
            })
            .catch(error => console.log(error))
            this.getEmployeeList();
        },
        deleteTask(id) {
            if (this.user_id == null)
                this.initialise();
            this.api.delete('tasks/delete/' + id)
            .then((response) => {
                console.log(response)
            })
            .catch(error => console.log(error))
        },
        getEmployeeList() {
            if (this.user_id == null)
                this.initialise();

            this.api.get('/employee/'+this.company_id)
                .then(response => {
                    this.employee_list = response.data
                    console.log(response)
                })
                .catch(error => console.log(error))
        }
    }
})