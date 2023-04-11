/* eslint-disable */
<template>
  <div class="hello">
    <img alt="Home Logo" src="../assets/film_icon.png" height="150">
    <HelloWorld msg="Welcome to Movie Mash!"/>
    <p class="h2">To execute a custom query, use the bar below</p>
      <span class="h5" style = "padding-right: 20px;">Query:</span>
      <input type="text" v-model="inputText" style="width: 1000px; margin-bottom: 100px; height: 37px;"  placeholder="SELECT * FROM Movies" class="form-row align-items-center h5">
      <button @click="CustomQueryInput" class="btn btn-success">Execute</button>
    <p class="h2">Or try some of our pre-built queries below</p>
    <button @click="sortMoviesByTitle" class="btn btn-success">SortMoviesByTitle</button>
    <button @click="highlyRatedMovies" class="btn btn-success">HighlyRatedMovies</button>
    <button @click="moviesByReleaseDate" class="btn btn-success">SortByReleaseDate</button>
    <button @click="moviesByRunTime" class="btn btn-success">SortByRunTime</button>
    <button @click="moviesUnderTwoHours" class="btn btn-success">MoviesUnder2Hours</button>
    <button @click="moviesByDirectorName" class="btn btn-success">SortMoviesByDirectorName</button>
    <button @click="moviesByRating" class="btn btn-success">SortMoviesByRating</button>
    <button @click="moviesByGenre" class="btn btn-success">SortMoviesByGenre</button>
    <p class="h2">These pre-built queries require input</p>
    </div>
    <div>
    <p class="h5">Add movie to favorited list.</p>
    <input type="text" v-model="user_id_favorite"  placeholder="your email" class="query-boxes">
    <input type="text" v-model="movie_id_favorite"  placeholder="movie_id" class="query-boxes">
    <button @click="FavoriteAMovie" class="btn btn-success">Execute</button>
    <p class="h5">See your favorite movies</p>
    <input type="text" v-model="user_id"  placeholder="Email" class="query-boxes">
    <button @click="favoritedByMe" class="btn btn-success">Execute</button>
    <p class="h5">See movies given a genre</p>
    <input type="text" v-model="movie_genre"  placeholder="Movie Genre" class="query-boxes">
    <button @click="moviesWithGenre" class="btn btn-success">Execute</button>
    <p class="h5">Get Details on a Movie from its ID</p>
    <input type="text" v-model="movie_id" placeholder="Movie_ID" class="query-boxes">
    <button @click="specificMovie" class="btn btn-success">Execute</button>
    <p class="h5">See what actors have worked with directors</p>
    <input type="text" v-model="actor_name_director" placeholder="Actor_Name" class="query-boxes">
    <button @click="actorsWithDirector" class="btn btn-success">Execute</button>
    <p class="h5">See average rating fo a director's movies</p>
    <input type="text" v-model="director_rating" placeholder="Director_Name" class="query-boxes">
    <button @click="avgDirectorsMoviesRatings" class="btn btn-success">Execute</button>
    <p class="h5">See average rating of movies with given actor</p>
    <input type="text" v-model="actor_rating" placeholder="Actor_Name" class="query-boxes">
    <button @click="avgActorsMoviesRatings" class="btn btn-success">Execute</button>
    <p class="h5">See what awards an actor has won</p>
    <input type="text" v-model="actor_award" placeholder="Actor_Name" class="query-boxes">
    <button @click="actorsAwards" class="btn btn-success">Execute</button>
    <p class="h5">See Movies done by a director </p>
    <input type="text" v-model="director_movies" placeholder="Director_id" class="query-boxes">
    <button @click="directorsMovies" class="btn btn-success">Execute</button>
    <p class="h5">See Movies given a content Rating</p>
    <input type="text" v-model="content_rating" placeholder="Content Rating e.g G,PG..." class="query-boxes">
    <button @click="moviesOfContentRating" class="btn btn-success">Execute</button>
    <p class="h5">Find movies release between years</p>
    <input type="text" v-model="date1" placeholder="Start year" class="query-boxes">
    <input type="text" v-model="date2" placeholder="End year" class="query-boxes">
    <button @click="moviesReleasedBetween" class="btn btn-success">Execute</button>
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
    async sortMoviesByTitle () {
      const response = await axios.get('http://127.0.0.1:5000/sortmoviesbytitle/', {
        headers: {
          'Content-Type': 'application/json'
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
    },
    async highlyRatedMovies () {
      const response = await axios.get('http://127.0.0.1:5000/highlyratedmovies/', {
        headers: {
          'Content-Type': 'application/json'
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
    },
    async moviesByReleaseDate () {
      const response = await axios.get('http://127.0.0.1:5000/moviesbyreleasedate/', {
        headers: {
          'Content-Type': 'application/json'
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
    },
    async moviesByRunTime () {
      const response = await axios.get('http://127.0.0.1:5000/moviesbyruntime/', {
        headers: {
          'Content-Type': 'application/json'
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
    },
    async moviesUnderTwoHours () {
      const response = await axios.get('http://127.0.0.1:5000/moviesundertwohours/', {
        headers: {
          'Content-Type': 'application/json'
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
    },
    async moviesByDirectorName () {
      const response = await axios.get('http://127.0.0.1:5000/moviesbydirectorname/', {
        headers: {
          'Content-Type': 'application/json'
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
    },
    async moviesByRating () {
      const response = await axios.get('http://127.0.0.1:5000/moviesbyrating/', {
        headers: {
          'Content-Type': 'application/json'
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
    },
    async moviesByGenre () {
      const response = await axios.get('http://127.0.0.1:5000/moviesbygenre/', {
        headers: {
          'Content-Type': 'application/json'
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
    },
    // Here begin the user input queries
    async moviesWithGenre () {
      const response = await axios.get('http://127.0.0.1:5000/movieswithgenre/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          genre: this.movie_genre
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
    },
    async specificMovie () {
      const response = await axios.get('http://127.0.0.1:5000/specificmovie/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          movie_id: this.movie_id
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
    },
    async actorsWithDirector () {
      const response = await axios.get('http://127.0.0.1:5000/actorswithdirector/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          actor_name: this.actor_name_director
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
    },
    async avgDirectorsMoviesRatings () {
      const response = await axios.get('http://127.0.0.1:5000/avgdirectorsmoviesratings/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          director_name: this.director_rating
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
    },
    async avgActorsMoviesRatings () {
      const response = await axios.get('http://127.0.0.1:5000/avgactorsmoviesratings/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          actor_name: this.actor_rating
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
    },
    async actorsAwards () {
      const response = await axios.get('http://127.0.0.1:5000/actorsawards/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          actor_name: this.actor_award
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
    },
    async directorsMovies () {
      const response = await axios.get('http://127.0.0.1:5000/directorsmovies/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          director_id: this.director_movies
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
    },
    async moviesAwards () {
      const response = await axios.get('http://127.0.0.1:5000/moviesawards/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          movie_id: this.inputText
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
    },
    async moviesOfContentRating () {
      const response = await axios.get('http://127.0.0.1:5000/moviesofcontentrating/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          content_rating: this.content_rating
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
    },
    async moviesReleasedBetween () {
      const response = await axios.get('http://127.0.0.1:5000/moviesreleasedbetween/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          date1: this.date1,
          date2: this.date2
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
    },
    async favoritedByMe () {
      const response = await axios.get('http://127.0.0.1:5000/favoritedbyme/', {
        headers: {
          'Content-Type': 'application/json'
        },
        params: {
          user_id: this.user_id
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
    },
    async FavoriteAMovie () {
      const response = await axios.post('http://127.0.0.1:5000/addfavmovie/', {
        user_email: this.user_id_favorite,
        movie_id: this.movie_id_favorite
      }, {
        headers: {
          'Content-Type': 'application/json'
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
    },
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

<style scoped>
 .query-boxes{
  width: 250px;
  margin-bottom: 50px;
  height: 37px;
  text-align: left;
 }
</style>
