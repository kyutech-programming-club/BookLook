<template>
  <v-card>
    <v-card-title>
      <h1 class="display-1">Login</h1>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field
          v-model="username"
          label="ユーザ名" />
        <v-text-field
          v-model="pass"
          label="パスワード" />
        <v-card-actions>
      <v-btn @click="sendRegister">登録</v-btn>
    </v-card-actions>
      </v-form>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'Register',
  data(){
    return {
      username: ""
    }
  },
  methods: {
    async sendRegister(){
      const res = await this.$axios.post(
        '/auth/register',
        {
          username : this.username,
        },
        this.test = res.data.body
      )
    }
  }
}
</script>