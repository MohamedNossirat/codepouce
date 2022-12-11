<template>
  <v-container>
    <DemandesList/>
  </v-container>
</template>

<script>
import MeComponent from "@/components/MeComponent";
import DemandesList from "@/components/demandes/DemandesList";

export default {
  name: "HomeView",
  components: {DemandesList, MeComponent},
}
</script>

