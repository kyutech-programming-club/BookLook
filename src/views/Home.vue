<template>
  <v-app>
    <v-content>
      <v-container>
        <v-layout wrap>
          <v-flex xs12 sm6 md4 text-center my-5><v-btn>書籍一覧</v-btn></v-flex>
          <v-flex xs12 sm6 md4 text-center my-5><v-btn>本の登録</v-btn></v-flex>
       </v-layout>
      </v-container>
      <HelloWorld msg="Welcome to Your Vue.js App"/>
    </v-content>
  </v-app>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
