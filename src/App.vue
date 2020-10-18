<template>
  <v-app>
    <header>
      <v-app-bar
        app
        light
      >
        <v-toolbar-title>BookLook</v-toolbar-title>
      </v-app-bar>
    </header>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
// import Home from './views/Home';

export default {
  name: 'App',

  // components: {
  //   Home,
  // },

  data: () => ({
    //
  }),
};
</script>
