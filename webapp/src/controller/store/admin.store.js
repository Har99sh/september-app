import { defineStore } from "pinia";
import { useApiStore } from "./api.store";

export const useAdminStore= defineStore({
    id:"adminStore",
    state: ()=> ({
        admin_id : null,
        company_id: null,
        api: null,
    }),
    actions: {
        initialise() {
            const apiStore = useApiStore();
            apiStore.createApiInstance();
            this.admin_id = apiStore.user_id;
            this.company_id = apiStore.company_id;
            this.api = apiStore.api;              
        },
        register(data) {
            if (this.api == null)
                this.initialise();
            data.company_id = this.company_id;
            this.api.post('/register', data)
            .then(res => console.log(res))
            .catch(error => console.log(error))
        },
    }
})