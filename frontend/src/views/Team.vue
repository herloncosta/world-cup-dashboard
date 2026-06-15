<template>
  <div v-if="!team" class="flex items-center justify-center py-20 text-muted">{{ $t('common.loading') }}</div>

  <div v-else>
    <div :style="headerGradient" class="px-4 md:px-6 py-6 md:py-8">
      <div class="max-w-[1200px] mx-auto">
        <div class="flex items-center gap-2 md:gap-3 mb-1">
          <img v-if="flagUrl(team.name)" :src="flagUrl(team.name)" :alt="$teamName(team.name)" class="w-6 h-[18px] md:w-8 md:h-6 rounded shadow-sm" />
          <h1 class="text-white mb-0 text-xl md:text-2xl">{{ $teamName(team.name) }}</h1>
        </div>
        <p class="text-blue-200/70 text-sm">
          {{ team.group_letter ? $t('common.group') + ' ' + team.group_letter : $t('common.knockout') }}
        </p>
      </div>
    </div>

    <div class="max-w-[1200px] mx-auto px-4 md:px-6 py-4 md:py-6 space-y-4 md:space-y-6">
      <div v-if="matches" class="bg-surface rounded-xl border border-border shadow-sm overflow-x-auto">
        <div class="px-4 md:px-5 py-3 md:py-4 border-b border-border">
          <h2 class="mb-0 text-sm md:text-base font-bold">{{ $t('team.matches') }}</h2>
        </div>
        <table class="w-full text-sm min-w-[500px]">
          <thead>
            <tr class="bg-bg/50 text-muted border-b border-border">
              <th class="px-4 py-3 text-left font-medium text-xs uppercase tracking-[0.06em]">{{ $t('common.date') }}</th>
              <th class="px-4 py-3 text-left font-medium text-xs uppercase tracking-[0.06em]">{{ $t('common.round') }}</th>
              <th class="px-4 py-3 text-left font-medium text-xs uppercase tracking-[0.06em]">{{ $t('common.opponent') }}</th>
              <th class="px-4 py-3 text-center font-medium text-xs uppercase tracking-[0.06em]">{{ $t('common.result') }}</th>
              <th class="px-4 py-3 text-left font-medium text-xs uppercase tracking-[0.06em]">{{ $t('common.stadium') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="m in matches" :key="m.id" class="border-b border-border/50 hover:bg-bg/30 transition-colors last:border-b-0">
              <td class="px-4 py-3 text-muted whitespace-nowrap">{{ formatDate(m.date, locale, { month: 'short' }) }}</td>
              <td class="px-4 py-3 text-muted text-xs">{{ m.round_name }}</td>
              <td class="px-4 py-3">
                <RouterLink :to="`/team/${opponent(m).id}`" class="flex items-center gap-2 text-accent font-medium underline underline-offset-2 decoration-accent/30 hover:decoration-accent"
                  v-if="opponent(m)">
                  <img v-if="flagUrl(opponent(m).name)" :src="flagUrl(opponent(m).name)" :alt="$teamName(opponent(m).name)" class="w-5 h-4 rounded-sm object-cover" />
                  {{ teamName(opponent(m).name) }}
                </RouterLink>
              </td>
              <td class="px-4 py-3 text-center">
                <template v-if="m.played">
                  <span class="font-mono font-semibold text-base px-3 py-0.5 bg-bg rounded-md inline-block"
                    :class="resultColor(m)">
                    {{ m.score_ft_home }} – {{ m.score_ft_away }}
                  </span>
                </template>
                <span v-else class="text-muted text-sm">{{ formatDate(m.date, locale, { month: 'short' }) }} {{ m.time }}</span>
              </td>
              <td class="px-4 py-3 text-muted text-xs">{{ m.stadium?.name || $t('common.tbd') }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-if="goals.length" class="bg-surface rounded-xl border border-border shadow-sm overflow-x-auto">
        <div class="px-4 md:px-5 py-3 md:py-4 border-b border-border">
          <h2 class="mb-0 text-sm md:text-base font-bold">{{ $t('team.goals') }}</h2>
        </div>
        <table class="w-full text-sm min-w-[400px]">
          <thead>
            <tr class="bg-bg/50 text-muted border-b border-border">
              <th class="px-4 py-3 text-left font-medium text-xs uppercase tracking-[0.06em]">{{ $t('common.player') }}</th>
              <th class="px-4 py-3 text-left font-medium text-xs uppercase tracking-[0.06em]">{{ $t('common.minute') }}</th>
              <th class="px-4 py-3 text-left font-medium text-xs uppercase tracking-[0.06em]">{{ $t('common.penalty') }}</th>
              <th class="px-4 py-3 text-left font-medium text-xs uppercase tracking-[0.06em]">{{ $t('common.ownGoal') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="g in goals" :key="g.id" class="border-b border-border/50 last:border-b-0">
              <td class="px-4 py-3 font-semibold">{{ g.scorer }}</td>
              <td class="px-4 py-3 font-mono text-sm">{{ g.minute }}<span class="text-muted">'</span></td>
              <td class="px-4 py-3 text-muted">{{ g.penalty ? $t('common.yes') : '' }}</td>
              <td class="px-4 py-3 text-muted">{{ g.own_goal ? $t('common.yes') : '' }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { flagUrl } from '../utils/flags.js'
import { flagColors } from '../utils/teamColors.js'
import { formatDate } from '../utils/date.js'

const { locale, t } = useI18n()
const route = useRoute()
const API = '/api'
const team = ref(null)
const matches = ref(null)

function opponent(m) {
  return m.team1?.id === team.value?.id ? m.team2 : m.team1
}

function teamName(name) {
  return t('teams.' + name) || name
}

function resultColor(m) {
  if (!m.played) return ''
  const tid = team.value?.id
  if (m.winner?.id === tid) return 'text-win'
  if (m.winner === null) return 'text-draw'
  return 'text-loss'
}

const goals = computed(() => {
  if (!matches.value || !team.value) return []
  return matches.value.flatMap(m =>
    (m.goals || []).filter(g => g.team_id === team.value.id)
  ).sort((a, b) => parseInt(a.minute) - parseInt(b.minute))
})

const headerGradient = computed(() => {
  const colors = flagColors(team.value?.name)
  const nonWhite = colors.filter(c => c !== '#FFFFFF')
  const from = nonWhite[0] || '#002868'
  const to = nonWhite[1] || nonWhite[0] || '#1E3A5F'
  return { backgroundImage: `linear-gradient(to right, ${from}, ${to})` }
})

onMounted(async () => {
  await loadTeam()
})

watch(() => route.params.id, async () => {
  await loadTeam()
})

async function loadTeam() {
  const res = await fetch(`${API}/teams/${route.params.id}`)
  team.value = await res.json()
  const all = await fetch(`${API}/matches?team=${team.value.name}`).then(r => r.json())
  matches.value = all
}
</script>
