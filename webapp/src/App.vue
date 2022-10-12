<template>
  <div class="style-body">
    <NavBar/>
    <router-view />
    <FooterCommon />
  </div>
</template>

<script>
import FooterCommon from './components/static/FooterCommon.vue'
import NavBar from './components/static/NavBar.vue'
export default {
  name: 'App',
  components: {NavBar, FooterCommon},
}
</script>

<style>
  .style-body {
    background: #808080;
  }
</style>
