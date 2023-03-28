/* eslint-disable */
<template>
    <div>
      <h1>Create User Page</h1>
      <LoginForm/>
      <p>This is not working!</p>
    </div>
</template>

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
