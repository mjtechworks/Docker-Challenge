<template>
  <body class="bg-gradient-to-r from-cyan-500 to-blue-500">
    
  <div >
    <div class="flex item-center justify-center mt-6"> 
      <span class="text-2xl text-white" >I want to work with you Please check this Challenge</span>
    </div>
    <div class="mt-10  flex item-center justify-center mt-6">
      <input type="text" class="border rounded-lg px-3 py-2 w-4/5"  placeholder="Name" ref="textbox">
    </div>
    <div class="flex item-center justify-center mt-6"> 
      <button @click="getData" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ">Click me</button>
    </div>

    <div class="flex item-center justify-center mt-6"> 
      <span class="text-2xl text-white">The reversed string is ok</span>
    </div>

    <div class="flex item-center justify-center mt-6"> 
      <span class="text-2xl text-white">{{result}}</span>
    </div>

    
  </div>
  </body>
</template>

<script>
import axios from 'axios';


export default {
  data() {
    return {
      result: '',
    };
  },
  methods: {
    
    getData() {
      const value = this.$refs.textbox.value; // Get the value of the textbox
      axios.get(`http://127.0.0.1:8000/api/test_users/${value}`)
        .then(response => {
          console.log(response)
          this.result = response.data.name
        })
        .catch(error => {
          // handle the error
        });
    }
  }
}
</script> 