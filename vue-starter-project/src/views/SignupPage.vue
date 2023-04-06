/* eslint-disable */
<template>
  <h1>Sign-Up Page</h1>
<form>
  <!-- Email input -->
  <div class="form-outline mb-4">
    <label class="form-label" for="form2Example1" style = "padding-right: 20px; padding-top: 20px;">Username</label>
    <input type="text" name="username" v-model="input.username" placeholder="Username"  />
  </div>

  <!-- Password input -->
  <div class="form-outline mb-4">
    <label class="form-label" for="form2Example2" style = "padding-right: 20px;">Password</label>
    <input type="password" name="password" v-model="input.password" placeholder="Password" />
  </div>

  <!-- 2 column grid layout for inline styling -->
  <div class="row mb-4">
    <div class="col d-flex justify-content-center">
      <!-- Checkbox -->
    </div>
  </div>

  <!-- Submit button -->
  <button type="button" class="btn btn-primary btn-block mb-4 btn-success">Sign up</button>
</form>
</template>

<script>
export default {
  name: 'SignupPage',
  data () {
    return {
      input: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    login () {
      if (this.input.username !== '' && this.input.password !== '') {
        if (this.input.username === this.$parent.mockAccount.username && this.input.password === this.$parent.mockAccount.password) {
          this.$emit('authenticated', true)
          this.$router.replace({ name: 'secure' })
        } else {
          console.log('The username and / or password is incorrect')
        }
      } else {
        console.log('A username and password must be present')
      }
    }
  }
}
</script>

<style scoped>
    #login {
        width: 500px;
        border: 1px solid #CCCCCC;
        background-color: #FFFFFF;
        margin: auto;
        margin-top: 200px;
        padding: 20px;
    }
</style>
