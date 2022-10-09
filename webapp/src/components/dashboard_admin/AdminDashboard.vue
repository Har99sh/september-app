<template>
    <div class="main-body">    
        <TheSideBar @change-tab="getActiveTab"/>
        <TabsToShow :active_tab="active_tab"/>
    </div>
</template>

<script>

import TheSideBar from '../static/TheSideBar.vue';
import TabsToShow from './TabsToShow.vue';

export default {
    name: "AdminDashboard",
    components: {TheSideBar, TabsToShow},
    data() {
        return {
            active_tab: "my-info",
        }
    },
    methods: {
        getActiveTab(tab) {
            this.active_tab = tab;
        }
    },
}
</script>

<style>
    .main-body {
        display: flex;
        flex-direction: row;
    }
</style>