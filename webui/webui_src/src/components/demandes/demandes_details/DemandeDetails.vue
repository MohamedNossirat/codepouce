<template>
  <v-row>
    <v-col class="d-flex flex-column">
      <v-card variant="elevated">
        <template #title>
          <div class="d-flex align-center">
            <v-avatar color="transparent">
              <v-img cover :src="demande.owner_info.photo"></v-img>
            </v-avatar>
            <h5 class="mx-4">{{ $filters.upperCaser(demande.title) }}</h5>
          </div>
        </template>
        <v-card-subtitle>{{ $filters.timeAgo(demande.created) }}</v-card-subtitle>
        <v-card-text class="text-justify">
          {{ demande.description }}
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>

export default {
  name: "DemandeDetails",
  props: {
    demandeProps: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      demande: null,
    }
  },
  created() {
    this.demande = this.demandeProps
  },
}
</script>

<style scoped>

</style>
