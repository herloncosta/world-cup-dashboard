import { createI18n } from 'vue-i18n'
import { enUS } from './locales/en-US.js'
import { ptBR } from './locales/pt-BR.js'

const i18n = createI18n({
  legacy: false,
  locale: navigator.language.startsWith('pt') ? 'pt-BR' : 'en-US',
  fallbackLocale: 'en-US',
  messages: {
    'en-US': enUS,
    'pt-BR': ptBR,
  },
})

export default i18n
