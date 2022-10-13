import { createRouter, createWebHistory } from 'vue-router'

import { useAuthStore } from '@/controller/store/auth.store';

/*Static file without login */
import LandingPage from '../components/LandingPage.vue'

/*Forms */
import CompanyRegisterForm from '../components/forms/CompanyRegisterForm.vue';
import EmployeeRegisterForm from '../components/forms/EmployeeRegisterForm.vue';
import LoginUser from '../components/forms/LoginUser.vue'


/*Task app */
import AdminTasksView from '../components/task_app/AdminTasksView.vue'

/*Dashboard user */
import UserDashboard from '../components/dashboard_user/UserDashboard.vue'
import AdminDashboard from '../components/dashboard_admin/AdminDashboard.vue'

const routes = [
    /**Static pages routes */
    {
        path:'/',
        name:'LandingPage',
        component: LandingPage,
    },
    /**User sign in/register routes */
    {
        path:'/register-company',
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
    {
        path: '/admin/tasks',
        name: 'AdminTasksView',
        component: AdminTasksView,
    },
    /**User dashboard */
    {
        path: '/dashboard-user',
        name: 'UserDashboard',
        component: UserDashboard,        
    },
    {
        path: '/dashboard-admin',
        name: 'AdminDashboard',
        component: AdminDashboard,
    },
]
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes: routes
})

router.beforeEach(async (to) => {
    // redirect to login page if not logged in and trying to access a restricted page
    const publicPages = ['/login', '/', '/register-company'];
    const authRequired = !publicPages.includes(to.path);
    const auth = useAuthStore();    
    if (authRequired && !auth.is_logged) {
        auth.returnUrl = to.fullPath;
        return '/login';
    } 
});

export default router;