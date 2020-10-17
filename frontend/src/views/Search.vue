<template>
  <div class="about">
    <v-form>
      <v-text-field
      v-model="isbn"
      label="ISBN番号を入力">
      </v-text-field>
    </v-form>
    <v-btn
      @click="fetchInfo"
    >検索
    </v-btn>
    <div>
      <v-img
        max-height="250"
        max-width="150"
        :src="bookUrl"
      ></v-img>
    </div>
    <h2>{{ bookTitle }}</h2>
    <v-btn
      @click="postApi"
    >書籍登録</v-btn>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data(){
    return{
      isbn: null,
      bookUrl: null,
      bookTitle: null
    }
  },
  methods: {
    async fetchInfo() {
      const url = "https://api.openbd.jp/v1/get?isbn=" + this.isbn;
      
      const res = await axios.get(url);
      const items = res.data;
      this.bookUrl = items[0].summary.cover;
      this.bookTitle = items[0].summary.title;
      // console.log(item)
      // var speechText = items.description.text.replace(/\r?\n/g, '');
      // speechText = speechText.replace(/</g, '');
      // speechText = speechText.replace(/>/g, '');
      
      // console.log("speechText: " + speechText);
    },
    async postApi() {
      const result = await this.$axios.post('/api/book_register',{
        title: this.bookTitle
      }
      );
      console.log(this.bookTitle)
    }
  }
}
</script>
