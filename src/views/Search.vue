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
      @click="sendApi"
    >書籍登録</v-btn>
    <h1>{{ text }}</h1>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data(){
    return{
      isbn: null,
      bookUrl: null,
      bookTitle: null,
      text: ""
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
    async sendApi() {
      const res = await this.$axios.post(
        '/api/test',
        { title: this.bookTitle, 
          cover: this.bookUrl}
        )
        this.text = res.data.body
      console.log(this.bookTitle)
    }
  }
}
</script>
