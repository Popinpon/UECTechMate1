<template>
  <a :href="'https://twitter.com/' + user_id" target="_blank">
    <div class="h-42 max-w-sm bg-white hover:bg-blue-200 border-2 border-gray-300 p-2 rounded-md tracking-wide shadow-lg relative">
      <img src="/static/img/twitter.png" class="w-5 h-5 absolute top-0 right-0 m-2">
      <div id="header" class="flex items-center mb-2">
        <img class="w-16 rounded-full border-2 border-gray-300" alt="image" :src="icon_url">
        <div id="header-text" class="leading-5 ml-6 sm">
          <div class="flex justify-start">
            <h4 class="text-lg text-gray-600 font-semibold">{{user}}</h4>
          </div>
          <h5 class="font-semibold text-base text-gray-400">{{created_at}}</h5>
        </div>
      </div>
      <div>
        <span class="text-sm text-gray-800 font-extrabold">{{text}}</span>
      </div>
    </div>
  </a>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'TwitterCard',
  props: {
    icon_url: String,
    user: String,
    text: String,
    created_at: String,
    user_id: String,
    id: String,
  },
})
</script>
