<template>
  <div class="bg-black text-white">
    <p class="text-center font-sans text-7xl mb-9">Responce</p>
    <div class="flex justify-center">
      <div class="w-4/5 flex justify-center mb-6">
        <div class="w-1/3 h-20 bg-green-600 rounded-full m-1 p-4">
          <p class="font-mono text-5xl text-white extrabold text-center">
            ホールA
          </p>
        </div>
        <div class="w-1/3 h-20 bg-pink-600 rounded-full m-1 p-4">
          <p class="font-mono text-5xl text-white extrabold text-center">
            ホールB
          </p>
        </div>
        <div class="w-1/3 h-20 bg-purple-600 rounded-full m-1 p-4">
          <p class="font-mono text-5xl text-white extrabold text-center">
            ホールC
          </p>
        </div>
      </div>
    </div>
    <div class="flex justify-center mb-6">
      <div class="w-4/5 flex justify-center mb-6">
        <div
          class="w-1/3 bg-white border-2 rounded-md border-gray-300 m-1 bg-green-200"
        >
          <div v-for="roomA in roomAData" :key="roomA.id">
            <TwitterCard v-if="roomA.type == 'twitter'" v-bind="roomA" />
            <YoutubeCard v-else v-bind="roomA" />
          </div>
        </div>
        <div
          class="w-1/3 bg-white border-2 rounded-md border-gray-300 m-1 bg-pink-200"
        >
          <div v-for="roomB in roomBData" :key="roomB.id">
            <TwitterCard v-if="roomB.type == 'twitter'" v-bind="roomB" />
            <YoutubeCard v-else v-bind="roomB" />
          </div>
        </div>
        <div
          class="w-1/3 bg-white border-2 rounded-md border-gray-300 m-1 bg-purple-200"
        >
          <div v-for="roomC in roomCData" :key="roomC.id">
            <TwitterCard v-if="roomC.type == 'twitter'" v-bind="roomC" />
            <YoutubeCard v-else v-bind="roomC" />
          </div>
        </div>
      </div>
    </div>

    <!-- <p class="text-center font-sans text-7xl mb-9">Twtter Responce</p>
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
    <div class="flex justify-center mb-6">
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
    </div> -->

    <!-- 
    <p class="text-center font-sans text-7xl mb-9">Youtube Responce</p>
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
          <div v-for="commentA in youtubeRoomAData" :key="commentA.id">
            <YoutubeCard v-bind="commentA"/>
          </div>
        </div>
        <div class="w-1/3 bg-white border-2 rounded-md border-gray-300 m-1 bg-pink-200">
          <div v-for="commentB in youtubeRoomBData" :key="commentB.id">
            <YoutubeCard v-bind="commentB"/>
          </div>
        </div>
        <div class="w-1/3 bg-white border-2 rounded-md border-gray-300 m-1 bg-purple-200">
          <div v-for="commentC in youtubeRoomCData" :key="commentC.id">
            <YoutubeCard v-bind="commentC"/>
          </div>
        </div>
      </div>
    </div> -->
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Axios from "axios";
import TwitterCard from "./TwitterCard.vue";
import YoutubeCard from "./YoutubeCard.vue";

export default Vue.extend({
  name: "RoomInfoPage",
  props: {},
  data() {
    return {
      imageSrc: "/static/img/no_image.jpg",
      // youtubeRoomAData: [],
      // youtubeRoomBData: [],
      // youtubeRoomCData: [],
      // twitterRoomAData: [],
      // twitterRoomBData: [],
      // twitterRoomCData: [],
      roomAData: [],
      roomBData: [],
      roomCData: [],
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
  created: function () {
    this.initData();
  },
  methods: {
    addData(data) {
      // youtubeとtwitter仕分けしていろいろ
      if (data.room_type == "A") {
        const list = this.roomAData;
        list.push(data);
        if (list.length >= 10) list.shift();
      } else if (data.room_type == "B") {
        const list = this.roomBData;
        list.push(data);
        if (list.length >= 10) list.shift();
      } else {
        const list = this.roomCData;
        list.push(data);
        if (list.length >= 10) list.shift();
      }
    },
    initData() {
      var args = {
        data: "hoge",
      };
      Axios.post("http://localhost:5000/init_json", args)
        .then((response) => {
          const json_data = response.data;
          console.log(response);
          console.log(json_data);
          const listA = this.roomAData;
          const listB = this.roomBData;
          const listC = this.roomCData;

          json_data.roomA.forEach((element) => {
            listA.push(element);
          });
          json_data.roomB.forEach((element) => {
            listB.push(element);
          });
          json_data.roomC.forEach((element) => {
            listC.push(element);
          });
          // this.roomAData = json_data.roomA;
          // this.roomBData = json_data.roomB;
          // this.roomCData = json_data.roomC;
        })
        .catch(function (error) {
          console.log(error);
        })
        .then(function () {});
    },

    // if (data.type == "twitter") {
    //   if (data.room_type == "A") {
    //     const list = this.twitterRoomAData;
    //     list.push(data);
    //     if (list.length >= 10) list.shift();
    //   } else if (data.room_type == "B") {
    //     const list = this.twitterRoomBData;
    //     list.push(data);
    //     if (list.length >= 10) list.shift();
    //   } else {
    //     const list = this.twitterRoomCData;
    //     list.push(data);
    //     if (list.length >= 10) list.shift();
    //   }
    // } else {
    //   if (data.room_type == "A") {
    //     const list = this.youtubeRoomAData;
    //     list.push(data);
    //     if (list.length >= 10) list.shift();
    //   } else if (data.room_type == "B") {
    //     const list = this.youtubeRoomBData;
    //     list.push(data);
    //     if (list.length >= 10) list.shift();
    //   } else {
    //     const list = this.youtubeRoomCData;
    //     list.push(data);
    //     if (list.length >= 10) list.shift();
    //   }
    // }
  },
});
</script>
