<template>
  <div class="home">
    <img alt="Home Logo" src="../assets/film_icon.png" height="50">
    <HelloWorld msg="Welcome to Movie Mash!"/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import HelloWorld from '@/components/HelloWorld.vue' // @ is an alias to /src

export default defineComponent({
  name: 'HomeView',
  components: {
    HelloWorld
  }
})
</script>
