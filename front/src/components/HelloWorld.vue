<template>
  <div class="hello bg-black text-white">
    <h3>Responce</h3>
    <ul>
      <li>{{testData}}</li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios'

export default Vue.extend({
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      testData: String
    }
  },
  created : function() {
    this.getData()
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
      })    }
  },
})
</script>