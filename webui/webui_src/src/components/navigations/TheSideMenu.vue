<template>
  <v-navigation-drawer app floating>
    <MeComponent/>
  </v-navigation-drawer>
</template>

<script>
import MeComponent from "@/components/MeComponent";

export default {
  name: "TheSideMenu",
  components: {MeComponent}
}
</script>


