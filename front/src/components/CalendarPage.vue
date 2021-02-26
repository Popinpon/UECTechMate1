<template>
  <div class="flex justify-center">
    <div id="times" class="bg-blue-100 w-1/12">
      <div v-for="i in 8" v-bind:key="i" class="h-40 border-b-2 border-blue-500">
        <div class="h-16"></div>
        <p class="text-2xl text-center">{{i + 10}}</p>
        <div class="h-16"></div>
      </div>
    </div>
    <div id="mainCards" class="bg-blue-200 w-3/4">
      <div id="wideCard" class="w-full">
        <WideCard v-bind="testCardData"/>
      </div>
      <div id="cards" class="flex justify-center">
        <div v-for="i in 3" v-bind:key="i" class="w-1/3">
          <Card v-bind="testCardData"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Card from './Card.vue'
import WideCard from './WideCard.vue'

export default Vue.extend({
  name: 'CalendarPage',
  data() {
    return {
      testCardData: {
        name: "Massann",
        job: "UEC1721",
        text: "セブンの焼きサバ食べたい",
        image: "static/img/pro.jpg"
      }
    }
  },
  components: {
    Card,
    WideCard,
  }
})
</script>