import {createI18n} from "vue-i18n";

import messages from "@/i18n/messages";
import store from "@/store";

export const i18n = createI18n({
  locale: store.state["locale/locale"],
  fallbackLocale: 'fr',
  messages
})
