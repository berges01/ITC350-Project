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
        <option value="javascript">JavaScript</option>
        <option value="php">PHP</option>
        <option value="java">Java</option>
        <option value="golang">Golang</option>
        <option value="python">Python</option>
        <option value="c#">C#</option>
        <option value="C++">C++</option>
        <option value="erlang">Erlang</option>
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
