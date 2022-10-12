<template>
    <div class="tab-to-show">
        <TaskList v-if="active_tab == 'my-tasks'"/>
        <MyInfo v-if="active_tab == 'my-info'"/>
        
    </div>
</template>

<script>

import TaskList from "../task_app/TaskList.vue";
import MyInfo from '../common/MyInfo.vue'



export default {
    name: "TabsToShowUser",
    components: {TaskList, MyInfo},
    props: ['active_tab'],
}
</script>

<style>
    .tab-to-show {
        width: 100%;
        display: flex;
        justify-content: center;
        align-content: center;
    }
</style>