/* eslint-disable */
<template>
  <div class="hello">
    <p class="h2">To execute a custom query, use the bar below</p>
      <span class="h5">Query:</span>
      <input type="text" v-model="inputText" style="width: 700px; margin-bottom: 180px; height: 37px;"  placeholder="SELECT * FROM Movies" class="form-row align-items-center h5">
      <button @click="CustomQueryInput" class="btn btn-success">Execute</button>
      <div v-for="(item, index) in returnedItems" :key="index">
      <pre>{{ JSON.stringify(item, null, 2) }}</pre>
      </div>
    <p class="h2">To execute a pre-built query, use the bar below</p>
    <form action="#" class="h5"> <div></div>Query:
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
export default {
  name: 'InputComponent',
  data () {
    return {
      inputText: '',
      returnedItems: ''
    }
  },
  methods: {
    makeApiCall () {
      axios.get('https://your-backend-url.com/api/data')
        .then(response => {
          console.log(response.data)
        // do something with the data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
label {
    font-size: 20px !important;
  }

.navbar-custom {
  height: 100px;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
