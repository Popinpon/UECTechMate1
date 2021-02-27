<template>
  <div class="h-42 max-w-sm bg-white border-2 border-gray-300 p-2 rounded-md tracking-wide shadow-lg relative">
    <img src="/static/img/youtube_logo.png" class="h-3 absolute top-0 right-0 m-2">
    <div id="header" class="flex items-center mb-2">
      <img class="w-16 rounded-full border-2 border-gray-300" alt="image" :src="icon">
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
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'YoutubeCard',
  props: {
    icon: String,
    text: String,
    user: String,
    created_at: String,
  },
})
</script>