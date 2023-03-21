<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      To execute a query, use the bar below
    </p>
    <label for="Query">Query:</label>
    <input type="text" id="Query" name="Query" placeholder="SELECT * FROM movie.mash" size="100">
    <input type="submit" value="Execute">
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
