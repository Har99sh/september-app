import { defineStore } from 'pinia';
import axios from 'axios';
import jwtDecode from 'jwt-decode';

export const useApiStore = defineStore({
    id: "api",
    state : () => ({
        api : null,
        token: null,
        user_id: null,
        company_id: null,
    }),
    actions: {
        createApiInstance() {
            this.setUserInfo();
            const base_url = "http://127.0.0.1:5000/";
            this.api =  axios.create({
                baseURL: base_url,
                headers: {
                            "Authorization" : 'Bearer ' + this.token,
                            "Content-Type": "application/json",
                            "Access-Control-Allow-Methods" : "PUT, POST, GET, OPTIONS, DELETE"
                        }
              });
        },
        setUserInfo() {
            const j4w_user = JSON.parse(localStorage.getItem("j4w_user"));
            this.token = j4w_user.token;
            this.user_id = j4w_user.user_id;
            let token_data = jwtDecode(this.token);
            this.company_id = token_data.companyID; 
        }
    }
});