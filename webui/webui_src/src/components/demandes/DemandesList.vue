<template>
  <v-sheet>
    <v-sheet class="feeder" :height="sheetHeight">
      <v-row>
        <v-col cols="8">
          <span v-for="(demande, index) in demandes"
                :key="demande.id">
            <DemandeDetails :demande-props="demande"/>
            <span
              v-if="demandes.indexOf(demandes.at(-1))===index"
              v-intersect="loadMore"></span>
          </span>

        </v-col>
      </v-row>
    </v-sheet>
  </v-sheet>
</template>

<script>
import moment from 'moment';
import DemandeDetails from "@/components/demandes/demandes_details/DemandeDetails";

export default {
  name: "DemandesList",
  components: {DemandeDetails},
  data() {
    return {
      loading: false,
    }
  },
  computed: {
    sheetHeight() {
      return (window.outerHeight * 70 / 100).toFixed().toString();
    },
    demandes() {
      return this.$store.state.demandes.demandes
    }
  },
  beforeMount() {
    this.$store.dispatch('demandes/getDemandes')
  },
  methods: {
    loadMore(isIntersecting, entries, observer) {
      if (isIntersecting && !isNaN(this.$store.state.demandes.params.next)) {
        this.$store.dispatch('demandes/getDemandes')
      }
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
.feeder {
  overflow-y: auto;
}

.feeder::-webkit-scrollbar {
  display: none;
}
</style>
