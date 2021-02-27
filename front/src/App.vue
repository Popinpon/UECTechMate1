<template>
  <div id="app">
    <div class="flex justify-center">
      <img alt="Vue logo" src="static/img/logo.png">
    </div>
    <CalendarPage/>
    <!-- <Hallo/> -->
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import CalendarPage from './components/CalendarPage.vue'
// import Hallo from './components/HelloWorld'

export default Vue.extend({
  name: 'App',
  components: {
    CalendarPage,
  }
})
</script>