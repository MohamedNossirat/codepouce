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


app.mount('#app')
