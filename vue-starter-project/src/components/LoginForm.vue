<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="handleSubmit">
        <label>
          Username:
          <input type="text" v-model="username" required>
        </label>
        <br>
        <label>
          Password:
          <input type="password" v-model="password" required>
        </label>
        <br>
        <button type="submit">Login</button>
      </form>
      <p v-if="error" style="color: red">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import { mapActions } from 'vuex';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        error: '',
      };
    },
    methods: {
      ...mapActions('auth', ['login']),
      async handleSubmit() {
        try {
          await this.login({ username: this.username, password: this.password });
          this.$router.push('/')
        } catch (error) {
          this.error = error.message
        }
      },
    },
  };
  </script>
  