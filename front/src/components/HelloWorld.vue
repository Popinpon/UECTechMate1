<template>
  <div>
    <div class="hello bg-black text-white">
      <h3>Responce</h3>
      <ul>
        <li>{{testData}}</li>
      </ul>
    </div>
    <div class="bg-blue-900 text-white">
      <h3>Youtube Responce</h3>
      <ul>
        <li>{{youtubeMSG}}</li>
      </ul>
    </div>
    <div class="bg-pink-900 text-white">
      <h3>Twtter Responce</h3>
      <ul>
        <li>{{twitterMSG}}</li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios'

export default Vue.extend({
  name: 'HelloWorld',
  props: {
    msg: String,
    twitterMSG: String,
    youtubeMSG: String,
  },
  data() {
    return {
      testData: String
    }
  },
  created : function() {
    this.getData()
    this.getYoutube()
    this.getTwitter()
  },
  methods: {
    getData(){
      const path = 'http://127.0.0.1:5000/get_test_data'
      const params = new URLSearchParams()
      params.append('test_post_data', "postでーた")
      axios.post(path, params).then(res => {
        this.testData = res.data.test_index_data
      }).catch(e => {
        console.log(e)
      })
    },
    getYoutube(){
      const path = 'http://127.0.0.1:5000/youtube_data'
      const params = new URLSearchParams()
      params.append('test_post_data', "youtube add data")
      axios.post(path, params).then(res => {
        this.youtubeMSG = res.data.youtube_data
      }).catch(e => {
        console.log(e)
      })
    },
    getTwitter(){
      const path = 'http://127.0.0.1:5000/twitter_data'
      const params = new URLSearchParams()
      params.append('test_post_data', "twitter add data")
      axios.post(path, params).then(res => {
        this.twitterMSG = res.data.twitter_data
      }).catch(e => {
        console.log(e)
      })
    }
  },
})
</script>