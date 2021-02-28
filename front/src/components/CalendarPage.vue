<template>
  <div class="bg-black">
    <p class="text-center font-sans text-7xl text-white mb-9">Time Schedule</p>
    <div>
      <nav class="flex flex-col sm:flex-row justify-center mb-4">
        <button
          class="text-gray-600 text-3xl py-4 px-6 block hover:text-blue-500 focus:outline-none"
          :class="{
            'text-blue-500 border-b-2 font-medium border-blue-500':
              dayNum === 1,
          }"
          @click="dayNum = 1"
          :disabled="dayNum === 1"
        >
          Day 1
        </button>
        <button
          class="text-gray-600 text-3xl py-4 px-6 block hover:text-blue-500 focus:outline-none"
          :class="{
            'text-blue-500 border-b-2 font-medium border-blue-500':
              dayNum === 2,
          }"
          @click="dayNum = 2"
          :disabled="dayNum === 2"
        >
          Day 2</button
        ><button
          class="text-gray-600 text-3xl py-4 px-6 block hover:text-blue-500 focus:outline-none"
          :class="{
            'text-blue-500 border-b-2 font-medium border-blue-500':
              dayNum === 3,
          }"
          @click="dayNum = 3"
          :disabled="dayNum === 3"
        >
          Day 3
        </button>
      </nav>
    </div>
    <div class="flex justify-center">
      <div id="times" class="bg-blue-100 w-1/12 rounded-tl-md">
        <div class="h-20 bg-blue-900 text-white rounded-tl-md"></div>
        <div
          v-for="i in 8"
          v-bind:key="i"
          class="h-40 border-b-2 border-blue-500"
        >
          <div class="h-16"></div>
          <p class="text-2xl text-center">{{ i + 10 }}</p>
          <div class="h-16"></div>
        </div>
      </div>
      <template v-show="!isLoading && schedule">
        <div id="mainCards" class="w-3/4 rounded-tr-md">
          <div id="cards" class="flex justify-center">
            <div class="h-20 w-1/3 bg-green-600 p-4">
              <p class="font-mono text-5xl text-white extrabold text-center">
                ホールA
              </p>
            </div>
            <div class="h-20 w-1/3 bg-pink-600 p-4">
              <p class="font-mono text-5xl text-white extrabold text-center">
                ホールB
              </p>
            </div>
            <div class="h-20 w-1/3 bg-purple-600 p-4 rounded-tr-md">
              <p class="font-mono text-5xl text-white extrabold text-center">
                ホールC
              </p>
            </div>
          </div>

          <template v-if="dayNum === 1">
            <div id="wideCard" class="w-full bg-white">
              <div v-for="data in schedule.first_day.all_holl" :key="data">
                <WideCard v-bind="data" />
              </div>
            </div>
            <div id="cards" class="flex justify-center">
              <div
                v-for="(holl, key) in schedule.first_day.separate_holl"
                :key="key"
                class="w-1/3"
                :class="{
                  'bg-green-200': key === 'A',
                  'bg-pink-200': key === 'B',
                  'bg-purple-200': key === 'C',
                }"
              >
                <div v-for="data in holl" :key="data" v-bind="data">
                  <Card v-bind="data" />
                  <div v-if="data.time_end !== '18:00'" class="h-7"></div>
                </div>
              </div>
            </div>
            <div id="wideCard" class="w-full bg-white">
              <div v-for="data in schedule.first_day.gathering" :key="data">
                <WideCard v-bind="data" />
              </div>
            </div>
          </template>

          <template v-else-if="dayNum === 2">
            <div id="wideCard" class="w-full bg-white">
              <div v-for="data in schedule.second_day.all_holl" :key="data">
                <WideCard v-bind="data" />
              </div>
            </div>
            <div id="cards" class="flex justify-center">
              <div
                v-for="(holl, key) in schedule.second_day.separate_holl"
                :key="key"
                class="w-1/3"
                :class="{
                  'bg-green-200': key === 'A',
                  'bg-pink-200': key === 'B',
                  'bg-purple-200': key === 'C',
                }"
              >
                <div v-for="data in holl" :key="data" v-bind="data">
                  <Card v-bind="data" />
                  <div v-if="data.time_end !== '18:00'" class="h-7"></div>
                </div>
              </div>
            </div>
            <div id="wideCard" class="w-full bg-white">
              <div v-for="data in schedule.second_day.gathering" :key="data">
                <WideCard v-bind="data" />
              </div>
            </div>
          </template>

          <template v-else>
            <div id="cards" class="flex justify-center">
              <div
                v-for="(holl, key) in schedule.third_day.separate_holl"
                :key="key"
                class="w-1/3"
                :class="{
                  'bg-green-200': key === 'A',
                  'bg-pink-200': key === 'B',
                  'bg-purple-200': key === 'C',
                }"
              >
                <div v-for="data in holl" :key="data" v-bind="data">
                  <Card v-if="data.time_start === '11:00'" v-bind="data" />
                  <div v-if="data.time_start === '11:00'" class="h-7"></div>
                </div>
              </div>
            </div>
            <div id="wideCard" class="w-full bg-white">
              <div v-for="data in schedule.third_day.all_holl" :key="data">
                <WideCard v-bind="data" />
              </div>
            </div>
            <div id="cards" class="flex justify-center">
              <div
                v-for="(holl, key) in schedule.third_day.separate_holl"
                :key="key"
                class="w-1/3"
                :class="{
                  'bg-green-200': key === 'A',
                  'bg-pink-200': key === 'B',
                  'bg-purple-200': key === 'C',
                }"
              >
                <div v-for="data in holl" :key="data" v-bind="data">
                  <Card v-if="data.time_start !== '11:00'" v-bind="data" />
                  <div
                    v-if="
                      data.time_start !== '11:00' && data.time_end !== '18:00'
                    "
                    class="h-7"
                  ></div>
                </div>
              </div>
            </div>
            <div id="wideCard" class="w-full bg-white">
              <div v-for="data in schedule.third_day.gathering" :key="data">
                <WideCard v-bind="data" />
              </div>
            </div>
          </template>
        </div>
      </template>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import axios from "axios";
import Card from "./Card.vue";
import WideCard from "./WideCard.vue";

export default Vue.extend({
  name: "CalendarPage",
  data() {
    return {
      testCardData: {
        name: "Massann",
        job: "UEC1721",
        text: "セブンの焼きサバ食べたい",
        image: "static/img/pro.jpg",
      },
      schedule: {
        first_day: {},
        second_day: {},
        third_day: {},
      },
      isLoading: true,
      dayNum: 1,
    };
  },
  components: {
    Card,
    WideCard,
  },
  created() {
    this.getSchedule();
    this.isLoading = false;
  },
  methods: {
    getSchedule() {
      {
        const path = "http://127.0.0.1:5000/get_schedule_json";
        const params = new URLSearchParams();

        axios
          .post(path, params)
          .then((res) => {
            this.schedule = res.data.json_data;
            console.log(this.schedule);
          })
          .catch((e) => {
            console.log(e);
          });
      }
    },
  },
});
</script>