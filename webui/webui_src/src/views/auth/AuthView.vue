<template>
  <v-app>
    <v-toolbar flat color="transparent" height="120">
      <div class="d-flex flex-column justify-center align-center ml-10">
        <img src="@/assets/logo.svg" height="80"/>
        <h3 class="text-center">CodePouce</h3>
      </div>
      <v-spacer></v-spacer>
      <v-toolbar-items class="d-flex align-center mr-16">
        <v-menu open-on-hover>
          <template v-slot:activator="{ props }">
            <v-icon v-bind="props">mdi-translate</v-icon>

          </template>
          <v-list>
            <v-list-item
              v-for="(item, index) in [
              {code:'fr',text:'Français'},
              {code:'en',text:'English'},
              {code:'ar',text:'العربية'}
              ]"
              :key="index"
              :value="item.code"
              @click="changeLanguage(item.code)"
            >
              <v-list-item-title>{{ item.text }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-toolbar-items>
    </v-toolbar>
    <v-main>
      <RouterView/>
    </v-main>
  </v-app>

</template>

<script>
export default {
  name: "AuthView",
  methods: {
    changeLanguage(code) {
      this.$i18n.locale = code;
      this.$store.commit('local/setLocal', code)
    }
  }
}
</script>

<style scoped>

</style>
