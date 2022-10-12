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
        is_admin: null,
        is_logged: null,
        log_in_error: null,
        error_reason: null,
    }),
    actions: {
        login(user) {
            axios.post(baseUrl + 'login', user)
                .then((response) => {
                    console.log(response)
                    let user = response.data;
                    this.user = user;
                    localStorage.setItem('j4w_user', JSON.stringify(this.user));
                    let token_data = jwtDecode(this.user.token)
                    this.is_logged = true;
                    if (token_data.isAdmin != 'False') {
                        this.is_admin = false;
                        router.push({path : '/dashboard-admin'})   
                    } else 
                        router.push({path : '/dashboard-user'})   
                })
                .catch((err)=> {
                    this.log_in_error = true;
                    this.error_reason= err.response.data
                    router.push({path : '/login'})
                })
        },
        logout() {
            this.user = null;
            localStorage.removeItem('j4w_user');
        },
        isLoggedIn() {
            let loggedIn = JSON.parse(localStorage.getItem('j4w_user'));
            if (loggedIn != null) {
                console.log(this.user.token)
                console.log(loggedIn.token)
                if (this.user.token == loggedIn.token && this.user != null) {
                    console.log(true)
                    return true
                }
            }
        }
    }
});