<template>
  <div>
    <div class="bg-blue-900 text-white">
      <h3>Youtube Responce</h3>
      <div v-for="post in youtubeTextData" :key="post.id">
        <YoutubeCard v-bind="post" />
      </div>
    </div>
    <div class="bg-pink-900 text-white">
      <h3>Twtter Responce</h3>
      <div v-for="post in twitterTextData" :key="post.id">
        <TwitterCard v-bind="post" />
      </div>
    </div>
    <div><img :src="imageSrc" /></div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

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
        if (data.room_type == "A") {
          const list = this.twitterRoomAData;
          list.push(data);
          if (list.length >= 10) list.shift();
        } else if (data.room_type == "B") {
          const list = this.twitterRoomBData;
          list.push(data);
          if (list.length >= 10) list.shift();
        } else {
          const list = this.twitterRoomCData;
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
