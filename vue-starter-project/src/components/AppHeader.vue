/* eslint-disable */
<template>
    <header>
      <img alt="Vue logo" src="../assets/movie-mash.jpg" height="75">
      <p class="display-4">Movie Mash</p>
      <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/documentation">Documentation</router-link></li>
        <li><router-link to="/login">Login</router-link></li>
        <li><router-link to="/createUser">Sign Up</router-link></li>
      </ul>
    </nav>
    </header>
  </template>

<style lang="scss">
    header {
    display: flex;
    border-bottom: 1px solid #4e4c4c;
    padding: .5rem 1rem;

    p {
      margin-left: 1rem;
    }
  }

  nav {
    margin-left: auto;

    ul {
      list-style: none;
    }

    ul li {
      display: inline-flex;
      margin-left: 1rem;
    }
  }
</style>
