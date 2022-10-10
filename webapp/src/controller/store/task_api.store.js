import { defineStore } from "pinia";
import { authApi , api_user_id} from "../api_auth/api_auth";

export const TaskStore = defineStore({
    id:"task_store",
    state: ()=> ({
        user_id : api_user_id,
    }),
    actions: {
        getMyTasks() {
            return authApi.get('tasks/mine/' + this.user_id)
        }
    }
})