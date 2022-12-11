<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="8">
        <v-card
          class="mx-auto"
          color="grey-lighten-3">
          <v-card-text>
            <v-text-field
              density="compact"
              variant="solo"
              label="Search"
              append-inner-icon="mdi-magnify"
              single-line
              hide-details
              rounded
            ></v-text-field>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-divider class="ma-11"></v-divider>
    <v-row justify="center">
      <v-col>
        <DemandesList/>
      </v-col>
    </v-row>
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

