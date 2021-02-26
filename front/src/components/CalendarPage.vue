<template>
  <div class="flex justify-center">
    <div class="bg-blue-100 w-1/12">
      <div v-for="i in 8" v-bind:key="i" class="border-b-2 border-blue-500">
        <div class="h-8"></div>
        <p class="text-2xl text-center">{{i + 10}}</p>
        <div class="h-8"></div>
      </div>
    </div>
    <div v-for="i in 3" v-bind:key="i" class="bg-blue-200 w-1/4">
      <p>For a guide and recipes on how to configure / customize this project</p>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Card from './Card.vue'

export default Vue.extend({
  name: 'CalendarPage',
  components: {
    Card,
  }
})
</script>