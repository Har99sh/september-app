import { createRouter, createWebHistory } from 'vue-router'

/*Static file without login */
import LandingPage from '../components/LandingPage.vue'

/*Forms */
import CompanyRegisterForm from '../components/forms/CompanyRegisterForm.vue';
import EmployeeRegisterForm from '../components/forms/EmployeeRegisterForm.vue';
import LoginUser from '../components/forms/LoginUser.vue'

/*Task app */
import TaskList from '../components/task_app/TaskList.vue'
import CreateTask from '../components/task_app/CreateTask.vue'

const routes = [
    /**Static pages routes */
    {
        path:'/',
        name:'LandingPage',
        component: LandingPage,
    },
    /**User sign in/register routes */
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
    },
    /**Task app routes*/
    {
        path:'/tasks',
        name:'TaskList',
        component: TaskList,
    },
    {
        path:'/tasks/create',
        name:'CreateTask',
        component: CreateTask,
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: routes
})

export default router;