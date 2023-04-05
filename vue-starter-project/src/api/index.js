import axios from 'axios'

const API_URL = 'http://localhost:5000' // replace with your backend URL

export function hello() {
  return axios.get(`${API_URL}/hello`)
    .then(response => response.data)
    .catch(error => console.log(error))
}

