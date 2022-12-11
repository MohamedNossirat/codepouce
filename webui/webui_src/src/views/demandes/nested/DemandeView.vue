<template>
  <pre>{{ demande }}</pre>
</template>

<script>
import httpClient from "@/http/httpClient";

export default {
  name: "DemandeView",
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
      demande: {}
    }
  },
  mounted() {
    this.getDemande()
  },
  methods: {
    async getDemande() {
      let res = await httpClient.get('api/demandes/' + this.id);
      if (!res) return
      this.demande = res.data;
      document.title = 'CodePouce | ' + this.demande.title
    }
  }
}
</script>

<style scoped>

</style>
