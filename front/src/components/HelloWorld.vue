<template>
  <div>
    <div class="bg-blue-900 text-white">
      <h3>Youtube Responce</h3>
      <div v-for="post in youtubeTextData" :key="post.id">
        <YoutubeCard v-bind="post"/>
      </div>
    </div>
    <div class="bg-pink-900 text-white">
      <h3>Twtter Responce</h3>
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
import YoutubeCard from "./YoutubeCard.vue"

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
