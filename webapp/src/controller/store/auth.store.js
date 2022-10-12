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
        is_admin: null
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
                    this.is_admin = token_data.isAdmin;
                    console.log(this.is_admin)
                    if (token_data.isAdmin != 'False')
                        router.push({path : '/dashboard-admin'})   
                    else 
                        router.push({path : '/dashboard-user'})   
                            
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