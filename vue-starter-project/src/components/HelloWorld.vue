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
        <option value="FavoritedByMe">JavaScript</option>
        <option value="SortByReleaseDate">PHP</option>
        <option value="SortByRuntime">Java</option>
        <option value="SelectGenre">Golang</option>
        <option value="SortMoviesByTitle">Python</option>
        <option value="MoviesWithActor">C#</option>
        <option value="MoviesWithAward">C++</option>
        <option value="MoviesWithDirector">Erlang</option>
        <option value="ActorsWithAward">Erlang</option>
        <option value="AvgMovieRatingByActor">Erlang</option>
        <option value="AvgMovieRatingByDirector">Erlang</option>
        <option value="ActorsWithDirector">Erlang</option>
        <option value="SelectSpecificMovie">Erlang</option>
        <option value="SelectContentRating">Erlang</option>
        <option value="MovieRuntimeUnder2hours">Erlang</option>
        <option value="SelectMoviesReleasedBetween">Erlang</option>
      </select>
      <input type="submit" value="Submit" />
</form>
    <!-- todo add drop down of available queries -->
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
