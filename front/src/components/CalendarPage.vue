<template>
  <div class="flex justify-center">
    <div id="times" class="bg-blue-100 w-1/12">
      <div v-for="i in 8" v-bind:key="i" class="h-40 border-b-2 border-blue-500">
        <div class="h-16"></div>
        <p class="text-2xl text-center">{{i + 10}}</p>
        <div class="h-16"></div>
      </div>
    </div>
    <template v-show="!isLoading && schedule">
      <div id="mainCards" class="bg-blue-200 w-3/4">
        <div id="wideCard" class="w-full">
          <div v-for="data in schedule.first_day.all_holl" :key="data">
            <WideCard v-bind="data"/>
          </div>
        </div>
        <div id="cards" class="flex justify-center">
          <div v-for="holl in schedule.first_day.separate_holl" :key="holl" class="w-1/3">
            <Card v-for="data in holl" :key="data" v-bind="data"/>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
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
      },
      schedule: {
        "first_day": {},
        "second_day": {},
        "third_day": {},
      },
      isLoading: true,
    }
  },
  components: {
    Card,
    WideCard,
  },
  created() {
    this.getSchedule()
    this.isLoading = false
  },
  methods: {
    getSchedule () {
      {
        const path = 'http://127.0.0.1:5000/get_schedule_json'
        const params = new URLSearchParams()

        axios.post(path, params).then(res => {
          this.schedule = res.data.json_data
          console.log(this.schedule)
        }).catch(e => {
          console.log(e)
        })
      }
    },
  },
})
</script>