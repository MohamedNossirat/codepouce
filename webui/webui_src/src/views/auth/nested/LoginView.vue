<template>
  <v-container class="fill-height d-flex align-center">
    <v-row justify="center" align="center">
      <v-col cols="4">
        <v-card class="mx-auto pa-12 pb-8 logocard" elevation="8" max-width="448" rounded="lg">
          <v-form
            v-model="form"
            @submit.prevent="onSubmit"
          >
            <div class="text-subtitle-1 text-medium-emphasis">{{ $t('lables.email') }}</div>
            <v-text-field
              v-model="email"
              :readonly="loading"
              :rules="[required]"
              class="mb-2"
              clearable
              :label="$t('lables.email')"
              variant="outlined"
            ></v-text-field>

            <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
              {{ $t('lables.password') }}
              <router-link
                class="text-caption text-decoration-none text-blue"
                to="/auth/reset_password"
              >
                {{ $t('lables.forgotPassword') }}
              </router-link>
            </div>
            <v-text-field
              v-model="password"
              :readonly="loading"
              :rules="[required]"
              type="password"
              clearable
              :label="$t('lables.password')"
              variant="outlined"
            ></v-text-field>

            <br>

            <v-btn
              :disabled="!form"
              :loading="loading"
              block
              color="success"
              size="large"
              type="submit"
              variant="elevated"
            >
              {{ $t('buttons.login') }}
            </v-btn>
          </v-form>
          <v-card-text class="text-center">
            <v-divider class="mb-2"></v-divider>
            <router-link
              class="text-blue text-decoration-none"
              to="/auth/signup"
            >
              {{$t('buttons.signup')}}
              <v-icon icon="mdi-chevron-right"></v-icon>
            </router-link>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {mapActions} from 'vuex';

export default {
  name: "LoginView",
  data: () => ({
    form: false,
    email: null,
    password: null,
    loading: false,
  }),
  created() {
    document.title = "CodePouce | Login"
  },
  methods: {
    ...mapActions({
      doLogin: 'user/login',
    }),
    onSubmit() {
      if (!this.form) return
      this.loading = true;
      this.doLogin({email: this.email, password: this.password}).then(() => {
        this.$router.push('/')
        this.loading = false;
      })
    },
    required(v) {
      return !!v || 'Field is required'
    },
  },
}
</script>
<style scoped lang="css">
.fill-height::before{
  content: "";
  background-image: url("@/assets/logo.svg");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: right;
  top:-100px;
  right: 200px;
  left: 0;
  bottom: 0;
  position: absolute;
  opacity: 0.7;
  transform: rotate(23deg);
}
</style>

