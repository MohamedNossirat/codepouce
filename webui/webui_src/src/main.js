/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import {createApp} from 'vue'

// Plugins
import {registerPlugins} from '@/plugins'

const app = createApp(App)

registerPlugins(app)
//i18n
import {i18n} from "@/i18n";

app.use(i18n)

//store
import store from '@/store';

app.use(store)
//router
import codePouceRouter from "@/router";

app.use(codePouceRouter)

// Quil Editor
import {QuillEditor} from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';

// filters
import helpers from "@/helpers/helpers";

app.config.globalProperties.$filters = {
  ...helpers
}
app.component('QuillEditor', QuillEditor)

app.mount('#app')
