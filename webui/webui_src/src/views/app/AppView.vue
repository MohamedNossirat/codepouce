<template>
  <v-app>
    <v-app-bar flat app height="120">
      <div class="d-flex flex-column justify-center align-center ml-10">
        <h1 class="text-center">CodePouce</h1>
      </div>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-bell-badge-outline</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-email</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-account</v-icon>
      </v-btn>
      <v-menu open-on-hover>
        <template v-slot:activator="{ props }">
          <v-icon v-bind="props">mdi-translate</v-icon>
        </template>
        <v-list>
          <v-list-item
            v-model="$store.state.locale.locale"
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
      <v-btn
        prepend-icon="mdi-exit-to-app"
        color="error"
        @click="doLogout().then($router.push('/auth/login'))"
      >{{ $t('buttons.logout') }}
      </v-btn>
    </v-app-bar>
    <TheSideMenu/>
    <v-main>
      <RouterView></RouterView>
    </v-main>
  </v-app>
</template>
<script>
import TheSideMenu from "@/components/navigations/TheSideMenu";
import {mapActions} from "vuex";
import moment from "moment";

export default {
  name: "AppView",
  components: {TheSideMenu},
  created() {
    document.title = "CodePouce"
  },
  methods: {
    ...mapActions({
      doLogout: 'user/logout'
    }),
    changeLanguage(code) {
      this.$i18n.locale = code;
      this.$store.commit('local/setLocal', code)
    },
    printlocals() {
      console.log(moment.locales())
    }
  }
}
</script>

