import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { MotionPlugin } from 'motion-v'
import i18n from './i18n.js'
import './style.css'
import App from './App.vue'
import Dashboard from './views/Dashboard.vue'
import Groups from './views/Groups.vue'
import Matches from './views/Matches.vue'
import Team from './views/Team.vue'
import Stats from './views/Stats.vue'
import Bracket from './views/Bracket.vue'

const routes = [
  { path: '/', component: Dashboard },
  { path: '/groups', component: Groups },
  { path: '/matches', component: Matches },
  { path: '/team/:id', component: Team },
  { path: '/stats', component: Stats },
  { path: '/bracket', component: Bracket },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

const app = createApp(App)
app.use(i18n)
app.use(router)
app.use(MotionPlugin)
app.config.globalProperties.$teamName = (name) => {
  if (!name) return name
  return i18n.global.t('teams.' + name) || name
}
app.mount('#app')
