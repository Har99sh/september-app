import { defineStore } from "pinia";
import { useApiStore } from "./api.store";

export const useEmployeeStore = defineStore({
    id:"employeeStore",
    state: ()=> ({
        employee_id : null,
        company_id: null,
        api: null,
        employee_info: null,
    }),    
    actions: {
        initialise() {
            const store = useApiStore();
            store.createApiInstance();
            this.employee_id = store.user_id;
            this.api = store.api;
            this.company_id = store.company_id;       
        },
        getInfo() {
            if (this.api == null)
                this.initialise();
            this.api.get('users/'+this.employee_id)
            .then((res)=> {
                console.log(res);
                this.employee_info = res.data;
            })
            .catch((err)=> console.log(err))
        }
    }
})