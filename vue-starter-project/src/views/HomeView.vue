/* eslint-disable */
<template>
  <div class="hello">
    <img alt="Home Logo" src="../assets/film_icon.png" height="150">
    <HelloWorld msg="Welcome to Movie Mash!"/>
    <p class="h2">To execute a custom query, use the bar below</p>
      <span class="h5" style = "padding-right: 40px;">Query:</span>
      <input type="text" v-model="inputText" style="width: 700px; margin-bottom: 100px; height: 37px;"  placeholder="SELECT * FROM Movies" class="form-row align-items-center h5">
      <button @click="CustomQueryInput" class="btn btn-success">Execute</button>
    <p class="h2">To execute a pre-built query, use the bar below</p>
    <form action="#" class="h5"> <div></div>
      <span style = "padding-right: 40px;">Query:</span>
      <label for="lang" class="h5" ></label>
      <select name="queries" id="query" style="width: 700px; height: 37px;">
        <option value="FavoritedByMe">SELECT * FROM selectmovies</option>
        <option value="SortByReleaseDate">SELECT * FROM movie_mash.highlyratedmovies</option>
        <option value="SortByRuntime">SELECT * FROM movie_mash.moviesbyreleasedate</option>
        <option value="SelectGenre">SELECT * FROM movie_mash.moviesbyruntime</option>
        <option value="SortMoviesByTitle">SELECT * FROM movie_mash.moviesundertwohours</option>
        <option value="MoviesWithActor">SELECT * FROM movie_mash.moviesbydirectorname</option>
        <option value="MoviesWithAward">SELECT Title, IMDB_Rating FROM movie_mash.sortbyrating</option>
        <option value="MoviesWithDirector">SELECT Title, Genre FROM movie_mash.sortbygenre</option>
      </select>
      <input type="submit" value="Execute" class="btn btn-success"/>
    </form>
  </div>
</template>

<script lang="js">
import axios from 'axios'
import { defineComponent } from 'vue'
export default {
  name: 'InputComponent',
  data () {
    return {
      inputText: '',
      returnedItems: ''
    }
  },
  methods: {
    async CustomQueryInput () {
      const response = await axios.get('http://127.0.0.1:5000/customsql/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          sql: this.inputText
        }
      })
        .then(response => {
          this.returnedItems = response.data
          const jsonString = JSON.stringify(this.returnedItems, null, 2)
          const newTab = window.open('', '_blank')
          newTab.document.body.innerHTML = `<div v-for="(item, index) in returnedItems" :key="index"><pre>${jsonString}</pre></div>`
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
