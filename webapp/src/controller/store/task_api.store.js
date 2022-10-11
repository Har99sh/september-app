import { defineStore } from "pinia";
import { useApiStore } from "./api.store";

export const TaskStore = defineStore({
    id:"task_store",
    state: ()=> ({
        user_id : null,
        task_list : [],
        api: null,
    }),
    actions: {
        initialise() {
            const store = useApiStore();
            store.createApiInstance();
            this.user_id = store.user_id;
            this.api = store.api;
        },
        getMyTasks() {
            if (this.user_id == null)
                this.initialise();
            this.api.get('tasks/mine/' + this.user_id)
            .then((response) => {
                this.task_list = response.data
            })
            .catch(error => console.log(error))  
            return this.task_list;
        },
        create_task(data) {
            if (this.user_id == null)
                this.initialise();
            this.api.post('tasks/create', data)
         }
    }
})