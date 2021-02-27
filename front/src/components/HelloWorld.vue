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
        <div class="w-1/3 bg-white border-2 rounded-md border-gray-300 m-1 bg-green-200">
          <div v-for="tweetA in twitterRoomAData" :key="tweetA.id">
            <TwitterCard v-bind="tweetA"/>
          </div>
        </div>
        <div class="w-1/3 bg-white border-2 rounded-md border-gray-300 m-1 bg-pink-200">
          <div v-for="tweetB in twitterRoomBData" :key="tweetB.id">
            <TwitterCard v-bind="tweetB"/>
          </div>
        </div>
        <div class="w-1/3 bg-white border-2 rounded-md border-gray-300 m-1 bg-purple-200">
          <div v-for="tweetC in twitterRoomCData" :key="tweetC.id">
            <TwitterCard v-bind="tweetC"/>
          </div>
        </div>
      </div>
    </div>
    <div class="bg-blue-900 text-white">
      <h3>Youtube Responce</h3>
      <div v-for="post in youtubeRoomCData" :key="post.id">
        <YoutubeCard v-bind="post"/>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import TwitterCard from "./TwitterCard.vue"
import YoutubeCard from "./YoutubeCard.vue"

export default Vue.extend({
  name: "HelloWorld",
  props: {},
  data() {
    return {
      imageSrc: "/static/img/no_image.jpg",
      youtubeRoomAData: [],
      youtubeRoomBData: [],
      youtubeRoomCData: [],
      twitterRoomAData: [],
      twitterRoomBData: [],
      twitterRoomCData: [],
    };
  },
  components: {
    YoutubeCard,
    TwitterCard,
  },
  mounted() {
    const socket = new WebSocket("ws://localhost:5001");
    socket.onmessage = (event) => {
      // console.log(event.data);
      const obj = JSON.parse(event.data);
      this.addData(obj);
    };
  },
  created: function () {},
  methods: {
    addData(data) {
      // youtubeとtwitter仕分けしていろいろ
      if (data.type == "twitter") {
        if (data.room_type == "A") {
          const list = this.twitterRoomAData;
          console.log("A done")
          list.push(data);
          if (list.length >= 10) list.shift();
        } else if (data.room_type == "B") {
          const list = this.twitterRoomBData;
          console.log("B done")
          list.push(data);
          if (list.length >= 10) list.shift();
        } else {
          const list = this.twitterRoomCData;
          console.log("C done")
          list.push(data);
          if (list.length >= 10) list.shift();
        }
      } else {
        if (data.room_type == "A") {
          const list = this.youtubeRoomAData;
          list.push(data);
          if (list.length >= 10) list.shift();
        } else if (data.room_type == "B") {
          const list = this.youtubeRoomBData;
          list.push(data);
          if (list.length >= 10) list.shift();
        } else {
          const list = this.youtubeRoomCData;
          list.push(data);
          if (list.length >= 10) list.shift();
        }
      }
    },
  },
});
</script>
