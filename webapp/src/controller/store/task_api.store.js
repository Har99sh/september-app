import { defineStore } from "pinia";
import { authApi, api_user } from "../api_auth/api_auth";

export const TaskStore = defineStore({
    id:"task_store",
    state: ()=> ({
        user_id : api_user.user_id,
        task_list : [],
    }),
    actions: {
        getMyTasks() {
            console.log(api_user.token)
            authApi.get('tasks/mine/' + this.user_id)
            .then((response) => console.log(response.data))
            .catch(error => console.log(error))
        }
    }
})