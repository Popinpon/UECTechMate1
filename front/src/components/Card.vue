<template>
  <div class="max-w-sm bg-white border-2 border-gray-300 p-6 rounded-md tracking-wide shadow-lg">
    <div id="header" class="flex items-center mb-4">
      <img class="w-20 rounded-full border-2 border-gray-300" alt="avatar" stc="https://picsum.photos/seed/picsum/200">
      <div id="header-text" class="leading-5 ml-6 sm">
        <h4 class="text-xl font-semibold">name</h4>
        <h5 class="font-semibold text-blue-600">Jobs</h5>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'Card',
})
</script>