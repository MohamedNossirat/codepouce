<template>
  <v-card class="mx-auto pa-8 pb-8" elevation="8">
    <v-card-text>
      <v-form>
        <v-text-field v-model="user.email" density="compact" variant="outlined" :label="$t('lables.email')"
                      prepend-inner-icon="mdi-at"></v-text-field>
        <v-text-field v-model="user.password" density="compact" variant="outlined" :label="$t('lables.password')"
                      type="password" prepend-inner-icon="mdi-form-textbox-password"></v-text-field>
        <v-file-input density="compact" variant="outlined" :label="$t('lables.picture')"
                      prepend-icon="" prepend-inner-icon="mdi-account-box" @change="setPhoto"></v-file-input>
        <v-row dense>
          <v-col>
            <v-text-field v-model="user.first_name" density="compact" variant="outlined" :label="$t('lables.firstName')"
                          prepend-inner-icon="mdi-account"></v-text-field>
          </v-col>
          <v-col>
            <v-text-field v-model="user.last_name" density="compact" variant="outlined" :label="$t('lables.lastName')"
                          prepend-inner-icon="mdi-account"></v-text-field>
          </v-col>
        </v-row>
        <v-row dense>
          <v-col>
            <v-text-field v-model="user.date_naissance" variant="outlined" density="compact"
                          :label="$t('lables.birthDate')"
                          prepend-inner-icon="mdi-cake"></v-text-field>
          </v-col>
        </v-row>
        <v-row dense>
          <v-col>
            <v-autocomplete v-model="user.langues.maternelle" :items="langues" item-title="name" return-object
                            variant="outlined" density="compact"
                            :label="$t('lables.nativeLanguage')"
                            prepend-inner-icon="mdi-account-voice"></v-autocomplete>
          </v-col>
          <v-col>
            <v-autocomplete v-model="user.langues.spoken" :items="langues" item-title="name" return-object multiple
                            variant="outlined" density="compact"
                            :label="$t('lables.spokenLanguage')"
                            prepend-inner-icon="mdi-account-voice"
                            :menu-props="{bottom:true,height:'150', width:'100'}"></v-autocomplete>
          </v-col>
        </v-row>
        <v-row dense>
          <v-col>
            <v-text-field v-model="user.ville" variant="outlined" density="compact" :label="$t('lables.city')"
                          prepend-inner-icon="mdi-map-marker"></v-text-field>
          </v-col>
          <v-col>
            <v-text-field v-model="user.telephone" variant="outlined" density="compact" :label="$t('lables.telephone')"
                          prepend-inner-icon="mdi-cellphone"></v-text-field>
          </v-col>
        </v-row>
        <v-btn
          type="submit"
          variant="elevated"
          block
          color="success"
          @click.prevent="doSignUp">
          {{ $t('buttons.send') }}
        </v-btn>
      </v-form>
    </v-card-text>
    <v-card-text class="text-center">
      <v-divider class="mb-2"></v-divider>
      <router-link
        class="text-blue text-decoration-none"
        to="/auth/login"
      >
        {{ $t('buttons.login') }}
        <v-icon icon="mdi-chevron-right"></v-icon>
      </router-link>
    </v-card-text>
  </v-card>
</template>

<script>
import langues from '@/assets/langues/langues.json';

export default {
  name: "SignUpForm",
  data() {
    return {
      langues: langues,
      user: {
        email: null,
        password: null,
        first_name: null,
        last_name: null,
        pic: null,
        date_naissance: null,
        langues: {
          maternelle: null,
          spoken: []
        },
        ville: null,
        telephone: null
      }
    }
  },
  methods: {
    setPhoto(e) {
      this.user.pic = e.target.files[0]
    },
    doSignUp() {
      this.$store.dispatch('user/signup', this.user).then(() => {
        this.$router.push('/auth/login');
      })
    }
  }
}
</script>

<style scoped>

</style>
