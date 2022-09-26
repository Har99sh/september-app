import { createRouter, createWebHistory } from 'vue-router'

/*Static file without login */
import LandingPage from '../components/LandingPage.vue'

/*Forms */
import CompanyRegisterForm from '../components/forms/CompanyRegisterForm.vue';
import EmployeeRegisterForm from '../components/forms/EmployeeRegisterForm.vue';
import LoginUser from '../components/forms/LoginUser.vue'


const routes = [
    {
        path:'/',
        name:'LandingPage',
        component: LandingPage,
    },
    {
        path:'/register/company',
        name:'CompanyRegisterForm',
        component: CompanyRegisterForm,
    },
    {
        path:'/register/employee',
        name:'EmployeeRegisterForm',
        component: EmployeeRegisterForm
    },
    {
        path:'/login',
        name:'LoginUser',
        component: LoginUser,
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: routes
})

export default router;