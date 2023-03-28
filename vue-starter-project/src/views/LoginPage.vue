/* eslint-disable */
<template>
    <div>
      <h1>Login Page</h1>
      <LoginForm/>
      This is not working!
    </div>
  </template>
  <!-- todo get the login stuff working -->

<script lang="ts">
import { defineComponent } from 'vue'
import LoginForm from '@/components/LoginForm.vue'

export default defineComponent({
  name: 'LoginPage',
  components: {
    LoginForm
  }
})
</script>
