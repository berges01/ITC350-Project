/* eslint-disable */
<template>
  <div class="hello">
    <p>To execute a custom query, use the bar below</p>
      Query:<input type="text" v-model="inputText" style="width: 700px;">
      <button @click="submitInput">Execute</button>
      <p v-if="outputText">{{ outputText }}</p>
    <p>To execute a pre-built query, use the bar below</p>
    <form action="#">
      <label for="lang">Query:</label>
      <select name="queries" id="query" style="width: 700px;">
        <option value="FavoritedByMe">SELECT * FROM movie.mash WHERE FavoritedByMe = uid</option>
        <option value="SortByReleaseDate">SELECT * FROM movie.mash WHERE releasedate = date</option>
        <option value="SortByRuntime">SELECT * FROM movie.mash WHERE run</option>
        <option value="SelectGenre">SELECT * FROM movie.mash WHERE</option>
        <option value="SortMoviesByTitle">SELECT * FROM movie.mash WHERE</option>
        <option value="MoviesWithActor">SELECT * FROM movie.mash WHERE</option>
        <option value="MoviesWithAward">SELECT * FROM movie.mash WHERE</option>
        <option value="MoviesWithDirector">SELECT * FROM movie.mash WHERE</option>
        <option value="ActorsWithAward">SELECT * FROM movie.mash WHERE</option>
        <option value="AvgMovieRatingByActor">SELECT * FROM movie.mash WHERE</option>
        <option value="AvgMovieRatingByDirector">SELECT * FROM movie.mash WHERE</option>
        <option value="ActorsWithDirector">SELECT * FROM movie.mash WHERE</option>
        <option value="SelectSpecificMovie">SELECT * FROM movie.mash WHERE</option>
        <option value="SelectContentRating">SELECT * FROM movie.mash WHERE</option>
        <option value="MovieRuntimeUnder2hours">SELECT * FROM movie.mash WHERE</option>
        <option value="SelectMoviesReleasedBetween">SELECT * FROM movie.mash WHERE</option>
      </select>
      <input type="submit" value="Execute" />
</form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      query: '',
      results: []
    }
  },
  methods: {
    submitQuery () {
      axios.get('/api/query', {
        params: { query: this.query }
      }).then((response) => {
        this.results = response.data
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
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
