<template>
  <div id="app">
    <div class="flex justify-center">
      <img alt="Vue logo" src="static/img/logo.png">
    </div>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import HelloWorld from './components/HelloWorld.vue'

export default Vue.extend({
  name: 'App',
  components: {
    HelloWorld
  }
})
</script>