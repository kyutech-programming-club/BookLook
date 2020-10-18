<template>
  <div class="about">
    <h1>This is an about page</h1>
    <v-form>
      <v-text-field
      v-model="text"
      label="名前">
      </v-text-field>
    </v-form>
    <v-btn
    @click="sendApi">
      送信
    </v-btn>
    <h1>{{ text }}</h1>
  </div>
</template>

<script>
  // import axios from 'axios';
  export default {
    name: 'About',
    data() {
      return {
        text: "",
      }
    },
    methods: {
      async sendApi() {
        const res = await this.$axios.post(
          '/api/test',
          { title: "test1",
            cover: "test1.png" }
          )
        this.text = res.data.body
      }
    }
  }

</script>
