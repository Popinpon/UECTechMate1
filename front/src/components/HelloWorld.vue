<template>
  <div>
    <div class="hello bg-black text-white">
      <h3>Responce</h3>
      <ul>
        <li>{{ testData }}</li>
      </ul>
    </div>
    <div class="bg-blue-900 text-white">
      <h3>Youtube Responce</h3>
      <ul>
        <li>{{ youtubeMSG }}</li>
      </ul>
    </div>
    <div class="bg-pink-900 text-white">
      <h3>Twtter Responce</h3>
      <ul>
        <li>{{ twitterMSG }}</li>
      </ul>
      <table class="twitter_table">
        <thead>
          <tr>
            <th>ID</th>
            <th>DATETIME</th>
            <th>TEXT</th>
          </tr>
        </thead>
        <transition-group tag="twitter_data">
          <tr v-for="post in twitterTextData" :key="post.id">
            <td>{{ post.id }}</td>
            <td>{{ post.created_at }}</td>
            <td>{{ post.text }}</td>
          </tr>
        </transition-group>
      </table>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import axios from "axios";

export default Vue.extend({
  name: "HelloWorld",
  props: {
    msg: String,
    twitterMSG: String,
    youtubeMSG: String,
  },
  data() {
    return {
      twitterTextData: [], // type:String,id:String?,created_at:String,text:String
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
      const list = this.twitterTextData;
      list.push(data);
    },
  },
});
</script>