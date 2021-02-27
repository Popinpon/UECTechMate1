<template>
  <div class="bg-black text-white">
    <p class="text-center font-sans text-7xl mb-9">Twtter Responce</p>
    <div class="flex justify-center">
      <div class="w-4/5 flex justify-center mb-6">
        <div class="w-1/3 h-20 bg-green-600 rounded-full m-1 p-4">
          <p class="font-mono text-5xl text-white extrabold text-center">ホールA</p>
        </div>
        <div class="w-1/3 h-20 bg-pink-600 rounded-full m-1 p-4">
          <p class="font-mono text-5xl text-white extrabold text-center">ホールB</p>
        </div>
        <div class="w-1/3 h-20 bg-purple-600 rounded-full m-1 p-4">
          <p class="font-mono text-5xl text-white extrabold text-center">ホールC</p>
        </div>
      </div>
    </div>
    <div class="flex justify-center">
      <div class="w-4/5 flex justify-center mb-6">
        <div v-for="i in 3" :key="i" class="w-1/3 bg-white border-2 rounded-md border-gray-300 m-1" :class="{'bg-green-200': i === 1, 'bg-pink-200': i === 2, 'bg-purple-200': i === 3}">
          <div v-for="post in twitterTextData" :key="post.id">
            <TwitterCard v-bind="post"/>
          </div>
        </div>
      </div>
    </div>
    <div class="bg-blue-900 text-white">
      <h3>Youtube Responce</h3>
      <div v-for="post in youtubeTextData" :key="post.id">
        <YoutubeCard v-bind="post"/>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import YoutubeCard from "./YoutubeCard.vue"
import TwitterCard from "./TwitterCard.vue"

export default Vue.extend({
  name: "HelloWorld",
  props: {},
  data() {
    return {
      youtubeTextData: [],
      twitterTextData: [], // type:String,id:String?,created_at:String,text:String
    };
  },
  components: {
    YoutubeCard,
    TwitterCard,
  },
  mounted() {
    const socket = new WebSocket("ws://localhost:5001");
    socket.onmessage = (event) => {
      console.log(event.data);
      const obj = JSON.parse(event.data);
      this.addData(obj);
    };
  },
  created: function () {},
  methods: {
    addData(data) {
      // youtubeとtwitter仕分けしていろいろ
      if (data.type == "twitter") {
        const list = this.twitterTextData;
        list.push(data);
        if (list.length >= 10) list.shift();
      } else {
        const list = this.youtubeTextData;
        list.push(data);
        if (list.length >= 10) list.shift();
      }
    },
  },
});
</script>
