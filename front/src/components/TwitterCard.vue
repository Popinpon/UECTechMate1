<template>
    <div class="bg-white w-full flex items-center p-2 rounded-xl shadow border">
      <div class="flex items-center space-x-4">
        <img :src="icon_url.replace( /_normal/g , '')" alt="icon" class="w-16 h-16 rounded-full">
      </div>
      <div class="flex-grow p-3">
        <div class="font-semibold text-gray-700">
          {{user}}
        </div>
        <div class="text-sm text-gray-500">
          {{text}}
        </div>
      </div>
    </div>
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
