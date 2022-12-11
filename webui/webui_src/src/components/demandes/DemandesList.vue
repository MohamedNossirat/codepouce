<template>
  <v-sheet class="list-group-wrapper">
    <v-sheet class="list-group" id="infinite-list" :height="sheetHeight">
      <v-list-item
        v-for="item in $store.state.demandes.demandes"
        :key="item.id">
        <template #title>
          <div class="d-flex align-center">
            <h4>{{ item.title }}</h4>
            <v-spacer></v-spacer>
            <v-chip>{{ formateDateRdv(item.date_rdv) }}</v-chip>
          </div>
        </template>
        <template #subtitle>
          <div class="d-flex align-center">
            <v-chip color="purple">{{ item.owner_info.langues.maternelle.name }}</v-chip>
            <v-divider vertical inset class="mx-3"></v-divider>
            <v-chip
              v-for="(langue, index) in item.owner_info.langues.spoken"
              :key="index"
              class="mx-1"
              color="primary">
              {{ langue.name }}
            </v-chip>
          </div>
        </template>
        <template #prepend>
          <v-avatar>
            <v-img :src="item.owner_info.photo" cover></v-img>
          </v-avatar>
        </template>
        <template #append>
          <v-btn icon variant="flat" @click="goToDemande(item)">
            <v-icon>mdi-arrow-right</v-icon>
          </v-btn>
        </template>
        <div class="my-2">
          <v-divider></v-divider>
        </div>
      </v-list-item>
    </v-sheet>
  </v-sheet>
</template>

<script>
import moment from 'moment';

export default {
  name: "DemandesList",
  data() {
    return {
      loading: false,
    }
  },
  computed: {
    sheetHeight() {
      return window.outerHeight * 50 / 100;
    },
  },
  beforeMount() {
    this.$store.dispatch('demandes/getDemandes')
  },
  mounted() {
    const scroller = document.querySelector('#infinite-list');
    scroller.addEventListener("scroll", e => {
      if (scroller.scrollTop + scroller.clientHeight >= scroller.scrollHeight) {
        this.loadMore()
      }
    });
  },
  methods: {
    loadMore() {
      this.$store.dispatch('demandes/getDemandes')
    },
    formateDateRdv(date) {
      return moment(date).format('DD/MM/YYYY à HH:MM')
    },
    goToDemande(item) {
      this.$router.push({
        name: 'DemandeView', params: {
          id: item.id,
          slug: item.slug,
        }
      })
    }
  }
}
</script>
<style scoped lang="css">
.list-group {
  overflow: auto;
  height: 20vh;
}
</style>
