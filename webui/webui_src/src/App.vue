<template>
  <v-app id="inspire" class="myapp">
    <v-main>
      <RouterView/>
    </v-main>
  </v-app>
</template>

<script>
import httpClient from "@/http/httpClient";

export default {
  name: 'App',
  beforeCreate() {
    this.$store.dispatch('local/initializeLocal');
    if (localStorage.getItem('userLocal')) {
      this.$i18n.locale = localStorage.getItem('userLocal');
    } else {
      this.$i18n.locale = 'fr'

    }
    this.$store.dispatch('user/initializeStore');
    if (localStorage.getItem('token')) {
      httpClient.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem('token');
    } else {
      httpClient.defaults.headers.common['Authorization'] = '';

    }
  },
}
</script>
<style scoped lang="css">
@import url("https://fonts.googleapis.com/css2?family=Cairo:wght@600&display=swap");

.myapp {
  font-family: 'Cairo', serif;

}
</style>
