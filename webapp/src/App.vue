<template>
  <div>
    <NavBar />
    <router-view />
    <FooterCommon />
  </div>
</template>

<script>
import FooterCommon from './components/static/FooterCommon.vue'
import NavBar from './components/static/NavBar.vue'
export default {
  name: 'App',
  components: { FooterCommon, NavBar },
}
</script>

<style>
</style>
