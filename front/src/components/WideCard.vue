<template>
  <div class="h-40 bg-white border-2 border-gray-300 p-4 rounded-md tracking-wide shadow-lg">
    <div id="header" class="flex items-center mb-4 mt-4">
      <div id="header-text" class="leading-5 ml-6 sm">
        <h4 class="text-4xl font-semibold">{{title}}</h4>
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
  name: 'WideCard',
  props: {
    title: String,
    text: String,
  },
})
</script>