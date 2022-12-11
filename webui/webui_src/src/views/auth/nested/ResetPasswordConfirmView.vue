<template>
  <v-container class="fill-height d-flex align-center">
    <v-row class="fill-height" justify="center" align="center">
      <v-col cols="4">
        <v-card>
          <v-card-title>Reset Password</v-card-title>
          <v-card-text>
            <v-form v-model="form" @submit.prevent="resetPassword">
              <v-text-field
                v-model="resetedPassword.new_password"
                label="Mot de passe"
                clearable
                variant="solo"
                :rules="[required]"
                type="password"></v-text-field>
              <v-text-field
                v-model="resetedPassword.re_new_password"
                label="Vérification du mot de passe"
                clearable
                variant="solo"
                :rules="[required]"
                type="password"></v-text-field>
              <v-btn type="submit" block color="success">{{$t('buttons.send')}}</v-btn>
            </v-form>

          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "ResetPasswordConfirmView",
  beforeMount() {
    this.resetedPassword.uid = this.$route.params.uid
    this.resetedPassword.token = this.$route.params.token
  },
  data() {
    return {
      form: false,
      resetedPassword: {
        new_password: '',
        re_new_password: '',
        uid: '',
        token: '',
      }
    }
  },
  methods: {
    ...mapActions({
      resetPasswordConfirm: 'user/resetPasswordConfirm',
    }),
    resetPassword() {
      if (!this.form) return
      this.resetPasswordConfirm(this.resetedPassword).then(() => {
        this.$router.push('/login')
      })
    },
    required(v) {
      return !!v || 'Field is required'
    },
  }
}
</script>

<style scoped>

</style>
