<template>
  <v-container class="fill-height d-flex align-center">
    <v-row class="fill-height" align="center" justify="center">
      <v-col cols="6">
        <SignUpForm/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import SignUpForm from "@/components/auth/signup/SignUpForm";

export default {
  name: "SignupView",
  components: {SignUpForm},
  mounted() {
    document.title = 'CodePouce | Signup'
  }
}
</script>

<style scoped>

</style>
