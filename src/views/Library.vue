<template>
  <div>
    <h2>書籍一覧</h2>
    <ul id="example-1">
      <li v-for="item in books" :key="item.title">
        {{ item.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios"
export default {
  data(){
    return{
      books: null
    }
  },
  created(){
    this.getBooks()
  },
  methods:{
    getBooks() {
      const res = this.$axios.get(
        '/api/test'
      )
      this.books = res.data
      console.log(this.books)
    }
  }
}

</script>