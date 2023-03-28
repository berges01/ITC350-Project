<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>To execute a custom query, use the bar below</p>
    <label for="Query">Query:</label>
    <input type="text" id="Query" name="Query" placeholder="SELECT * FROM movie.mash" size="100">
    <input type="submit" value="Execute">

    <p>To execute a pre-built query, use the bar below</p>
    <form action="#">
      <label for="lang">Query: </label>
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
    <!-- todo connect backend -->
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HelloWorld',
  props: {
    msg: String
  }
})
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
