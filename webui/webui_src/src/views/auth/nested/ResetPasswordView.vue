<template>
  <v-container class="fill-height d-flex align-center">
    <v-row class="fill-height" justify="center" align="center">
      <v-col cols="4">
        <v-card>
          <v-card-title>Réinitialiser le mot de passe</v-card-title>
          <v-card-text>
            <p class="text-justify mb-6">
              Vous avez perdu votre mot de passe ? Veuillez entrer votre adresse e-mail, vous recevrez un lien pour
              créer un nouveau mot de passe par e-mail.
            </p>
            <v-text-field v-model="email" label="Email" clearable variant="solo"
                          density="compact"></v-text-field>
            <v-btn block color="success" @click="sendResetEmail">{{ $t('buttons.send') }}</v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "ResetPasswordView",
  data() {
    return {
      email: ''
    }
  },
  methods: {
    ...mapActions({
      sendResetEmailRequest: 'user/sendResetPasswordRequest'
    }),
    sendResetEmail() {
      if (!this.email) return
      else this.sendResetEmailRequest(this.email).then(() => {
        this.$router.push('/login')
      })
    }
  }
}
</script>

<style scoped>

</style>
