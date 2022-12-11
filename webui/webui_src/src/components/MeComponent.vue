<template>
  <v-sheet
    v-if="user"
    class="d-flex flex-column align-center pa-4 logoporter">
    <v-avatar size="64" class="mb-4">
      <v-img :src="user.photo"></v-img>
    </v-avatar>
    <h5>{{ user.first_name }} {{ user.last_name }}</h5>
  </v-sheet>
  <v-divider></v-divider>
  <v-list>
    <v-list-item link>
      <template v-slot:prepend>
        <v-icon>mdi-account</v-icon>
      </template>
      <v-list-item-title>Profile</v-list-item-title>
      <template v-slot:append>
        <v-icon>mdi-arrow-right</v-icon>
      </template>
    </v-list-item>
    <v-list-item link>
      <template v-slot:prepend>
        <v-icon>mdi-email-fast</v-icon>
      </template>
      <v-list-item-title>Messages</v-list-item-title>
      <template v-slot:append>
        <v-icon>mdi-arrow-right</v-icon>
      </template>
    </v-list-item>
    <v-list-item link>
      <template v-slot:prepend>
        <v-icon>mdi-bullhorn</v-icon>
      </template>
      <v-list-item-title>Demandes</v-list-item-title>
      <template v-slot:append>
        <v-icon>mdi-arrow-right</v-icon>
      </template>
    </v-list-item>
    <v-list-item link>
      <template v-slot:prepend>
        <v-icon>mdi-cogs</v-icon>
      </template>
      <v-list-item-title>Paramètres</v-list-item-title>
      <template v-slot:append>
        <v-icon>mdi-arrow-right</v-icon>
      </template>
    </v-list-item>
  </v-list>
</template>

<script>
import {mapActions, mapState} from "vuex";

export default {
  name: "MeComponent",
  data() {
    return {}
  },
  beforeMount() {
    this.getUserMe();
  },
  computed: {
    ...mapState({
      user: state => state.user.authUser,
    })
  },
  methods: {
    ...mapActions({
      getUserMe: 'user/getUserMe'
    })
  }
}
</script>

<style scoped lang="css">
.logoporter::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("@/assets/logo.svg");
  opacity: 0.1;
}

</style>
