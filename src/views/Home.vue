<template>
  <v-app>
    <v-content>
      <HelloWorld/>
      <v-container>
        <v-row class="text-center">
          <v-col class="mb-4">
            <v-flex my-5><v-btn >書籍一覧</v-btn></v-flex>
            <v-flex my-5><v-btn to="/search">本の登録</v-btn></v-flex>
          </v-col>
        </v-row>
      </v-container>
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
