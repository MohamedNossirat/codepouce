<template>
  <v-dialog v-model="dialog" width="80%" persistent>
    <v-card>
      <v-card-title>Add new demande</v-card-title>
      <v-card-text>
        <quill-editor toolbar=""></quill-editor>
      </v-card-text>
      <v-card-actions>
        <v-btn variant="text" v-text="$t('buttons.send')" color="success" @click="agree"></v-btn>
        <v-btn variant="text" v-text="$t('buttons.cancel')" color="error" @click="cancel"></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>

import {QuillEditor} from "@vueup/vue-quill";

export default {
  name: "AddDemande",
  components: {QuillEditor},
  data: () => ({
    dialog: false,
    resolve: null,
    reject: null,
    demande: {
      title: null,
      date_rdv: null,
      description:null,
    }
  }),
  methods: {
    open() {
      this.dialog = true;
      new Promise((resolve, reject) => {
        this.resolve = resolve;
        this.reject = reject
      })
    },
    agree() {
      this.dialog = false;
      this.resolve(true)
    },
    cancel() {
      this.dialog = false;
      this.resolve(false)
    }
  }
}
</script>

<style scoped>

</style>
