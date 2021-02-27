<template>
  <div class="h-40 max-w-sm bg-white border-2 border-gray-300 p-4 rounded-md tracking-wide shadow-lg">
    <div id="header" class="flex items-center mb-2">
      <img v-if="image" class="w-20 rounded-full border-2 border-gray-300" alt="image" :src="image">
      <img v-else class="w-20 rounded-full border-2 border-gray-300" alt="image" src="/static/img/no_image.jpg">
      <div id="header-text" class="leading-5 ml-6 sm">
        <div class="flex justify-start">
          <h4 class="text-xl font-semibold">{{name}}</h4>
          <a v-if="twitter" class="p-1" :href="twitter"><img class="w-5" src="/static/img/twitter.png"></a>
        </div>
        <h5 class="font-semibold  text-blue-600">{{job}}</h5>
      </div>
    </div>
    <div>
      <span class="italic text-xs text-gray-800">{{text}}</span>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'Card',
  props: {
    name: String,
    job: String,
    text: String,
    image: String,
    twitter: String,
  },
})
</script>