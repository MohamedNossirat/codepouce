<template>
  <v-container class="fill-height" v-if="demande&&true">
    <v-row>
      <v-col>
        <v-card elevation="0">
          <v-card-title class="d-flex align-center">
            <div>
              <v-avatar>
                <v-img cover :src="demande.owner_info.photo"></v-img>
              </v-avatar>
              {{ demande.owner_info.first_name }} {{ demande.owner_info.last_name }}
            </div>
            <v-divider vertical inset class="mx-4"></v-divider>
            {{ demande.title }}
            <v-divider vertical inset class="mx-4"></v-divider>
            Le {{ demandeDate(demande.date_rdv) }}
          </v-card-title>
          <v-card-subtitle>
            <v-chip>{{ demande.owner_info.langues.maternelle.name }}</v-chip>
          </v-card-subtitle>
          <v-card-text>
            <v-row>
              <v-col>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import httpClient from "@/http/httpClient";
import {QuillEditor} from "@vueup/vue-quill";

export default {
  name: "DemandeView",
  components: {QuillEditor},
  props: {
    slug: {
      type: String,
      required: true
    },
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      demande: null,
    }
  },
  computed: {},
  created() {
    this.getDemande()
  },
  methods: {
    async getDemande() {
      let res = await httpClient.get('api/demandes/' + this.id);
      if (!res) return
      this.demande = res.data;
      document.title = 'CodePouce | ' + this.demande.title
    },
    demandeDate: (date) => {
      return formateTime(date)
    }
  }
}
</script>

<style scoped>

</style>
