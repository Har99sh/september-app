import { defineStore } from 'pinia';
import axios from 'axios';
import router from '@/router/routes';
import jwtDecode from 'jwt-decode';

const baseUrl = 'http://127.0.0.1:5000/'

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        user: JSON.parse(localStorage.getItem('j4w_user')),
        returnUrl: null,
    }),
    actions: {
        login(user) {
            axios.post(baseUrl + 'login', user)
                .then((response) => {
                    let user = response.data;
                    let dashboard = "";
                    this.user = user;
                    localStorage.setItem('j4w_user', JSON.stringify(this.user));
                    let token_data = jwtDecode(this.user.token)
                    dashboard = token_data.isAdmin ? "/dashboard-admin" : "/dashboard-user"
                    //Go to url after login
                    router.push(this.returnUrl || {path: dashboard})               
                })
                .catch(err => console.log(err))
        },
        logout() {
            this.user = null;
            localStorage.removeItem('j4w_user');
        },
        isLoggedIn() {
            let loggedIn = localStorage.getItem('j4w_user')
            return loggedIn == this.user ? true : false
        }
    }
});