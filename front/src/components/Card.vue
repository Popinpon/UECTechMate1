<template>
  <div class="max-w-sm bg-white border-2 border-gray-300 p-6 rounded-md tracking-wide shadow-lg">
    <div id="header" class="flex items-center mb-4">
      <img class="w-20 rounded-full border-2 border-gray-300" alt="image" :src="image">
      <div id="header-text" class="leading-5 ml-6 sm">
        <h4 class="text-xl font-semibold">{{name}}</h4>
        <h5 class="font-semibold text-blue-600">{{job}}</h5>
      </div>
    </div>
    <div>
      <q class="italic text-gray-600">{{text}}</q>
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
  },
})
</script>