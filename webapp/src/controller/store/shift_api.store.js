import { defineStore } from "pinia";
import { useApiStore } from "./api.store";

export const shiftStore = defineStore({
    id:"shiftStore",
    state: ()=> ({
        employee_id : null,
        api: null,
    }),
    
    actions: {
        initialise() {
            const store = useApiStore();
            store.createApiInstance();
            this.employee_id = store.user_id;
            this.api = store.api;
                        
        },
        startShift() {
            if (this.api == null)
            this.initialise();
            this.api.post('time_tracker/start/'+this.employee_id)
        },
        endShift() {
            if (this.api == null) {
                this.initialise();
            }
            this.api.post('time_tracker/end/'+this.employee_id)
            .then(res => console.log(res))
            .catch(err => console.log(err))
            .finally(()=> console.log("ended or not ended"))
        }

    }

})