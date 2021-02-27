<template>
  <div id="app">
    <div class="relative bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <div class="flex justify-between items-center border-b-2 border-gray-100 py-2 md:justify-start md:space-x-10">
          <div class="flex justify-start lg:w-0 lg:flex-1">
            <a href="#">
              <img class="h-16 w-auto rounded-full" src="static/img/team_logo.png">
            </a>
          </div>
          <nav class="hidden md:flex space-x-10">
            <button @click="isCalendar = !isCalendar" class="text-base font-medium hover:text-gray-900" :class="{'text-gray-500' : isCalendar, 'text-gray-900' : !isCalendar}" :disabled="!isCalendar">
              RoomInfomation
            </button>
            <button @click="isCalendar = !isCalendar" class="text-base font-medium hover:text-gray-900" :class="{'text-gray-900' : isCalendar, 'text-gray-500' : !isCalendar}" :disabled="isCalendar">
              Calendar
            </button>
          </nav>
        </div>
      </div>
    </div>
    <div class="flex justify-center bg-black">
      <img alt="Vue logo" src="static/img/logo_geek.png">
    </div>
    <CalendarPage v-if="isCalendar"/>
    <RoomInfoPage v-else/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import RoomInfoPage from './components/RoomInfoPage.vue'
import CalendarPage from './components/CalendarPage.vue'

export default Vue.extend({
  name: 'App',
  data() {
    return {
      isCalendar: false,
    }
  },
  components: {
    RoomInfoPage,
    CalendarPage,
  },
  methods: {

},
})
</script>