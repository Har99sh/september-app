<template>
    <div class="main-body">
        <TheSideBar @change-tab="getActiveTab"/>
        <TabsToShowUser :active_tab="active_tab"/>
    </div>
</template>
<script>
import TheSideBar from '../static/TheSideBarUser.vue';
import TabsToShowUser from './TabsToShowUser.vue';

export default {
    name: "UserDashboard",
    components: {TheSideBar, TabsToShowUser},
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
    width: 100vw;
    max-height: 100vh;
}
</style>