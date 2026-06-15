<template>
  <div>
    <div class="bg-gradient-to-r from-[#002868] to-[#1E3A5F] px-4 md:px-6 py-6 md:py-8">
      <div class="max-w-[1200px] mx-auto">
        <h1 class="text-white mb-1 text-xl md:text-2xl">{{ $t('matches.title') }}</h1>
        <p class="text-blue-200/70 text-sm">104 matches — filter by round or group</p>
      </div>
    </div>

    <div class="max-w-[1200px] mx-auto px-4 md:px-6 py-4 md:py-6">
      <div class="flex flex-col sm:flex-row gap-2 md:gap-3 mb-4 md:mb-5">
        <select v-model="filterRound" @change="load"
          class="appearance-none w-full sm:w-auto px-3 md:px-3.5 py-2 rounded-lg border border-border bg-white text-ink text-sm font-sans cursor-pointer transition-colors hover:border-accent focus:border-accent focus:ring-[3px] focus:ring-accent/20 focus:outline-none"
          style="background-image: url(&quot;data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%236B7280' stroke-width='2'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E&quot;); background-repeat: no-repeat; background-position: right 12px center; background-size: 16px; padding-right: 36px;">
          <option value="">{{ $t('matches.allRounds') }}</option>
          <option v-for="r in rounds" :key="r" :value="r">{{ r }}</option>
        </select>
        <select v-model="filterGroup" @change="load"
          class="appearance-none w-full sm:w-auto px-3 md:px-3.5 py-2 rounded-lg border border-border bg-white text-ink text-sm font-sans cursor-pointer transition-colors hover:border-accent focus:border-accent focus:ring-[3px] focus:ring-accent/20 focus:outline-none"
          style="background-image: url(&quot;data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%236B7280' stroke-width='2'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E&quot;); background-repeat: no-repeat; background-position: right 12px center; background-size: 16px; padding-right: 36px;">
          <option value="">{{ $t('matches.allGroups') }}</option>
          <option v-for="l in groupLetters" :key="l" :value="l">{{ $t('common.group') }} {{ l }}</option>
        </select>
      </div>

      <div v-if="!matches" class="flex items-center justify-center py-20 text-muted">{{ $t('common.loading') }}</div>

      <div v-else class="bg-surface rounded-xl border border-border shadow-sm overflow-x-auto">
        <table class="w-full text-sm min-w-[420px] md:min-w-[600px]">
          <thead>
            <tr class="bg-bg/50 text-muted border-b border-border">
              <th class="px-2 md:px-4 py-3 text-left font-medium text-[10px] md:text-xs uppercase tracking-[0.06em]">{{ $t('common.date') }}</th>
              <th class="px-2 md:px-4 py-3 text-left font-medium text-[10px] md:text-xs uppercase tracking-[0.06em]">{{ $t('common.round') }}</th>
              <th class="px-2 md:px-4 py-3 text-right font-medium text-[10px] md:text-xs uppercase tracking-[0.06em]" colspan="2">{{ $t('common.team1') }}</th>
              <th class="px-2 md:px-4 py-3 text-center font-medium text-[10px] md:text-xs uppercase tracking-[0.06em] w-[60px] md:w-[100px]">{{ $t('common.score') }}</th>
              <th class="px-2 md:px-4 py-3 text-left font-medium text-[10px] md:text-xs uppercase tracking-[0.06em]" colspan="2">{{ $t('common.team2') }}</th>
              <th class="hidden md:table-cell px-4 py-3 text-left font-medium text-xs uppercase tracking-[0.06em]">{{ $t('common.stadium') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="m in matches" :key="m.id" class="border-b border-border/50 hover:bg-bg/30 transition-colors last:border-b-0">
              <td class="px-2 md:px-4 py-3 text-muted whitespace-nowrap text-xs md:text-sm">
                <span class="md:hidden">{{ m.date?.slice(5, 10).replace('-', '/') }}</span>
                <span class="hidden md:inline">{{ formatDate(m.date, locale, { month: 'short' }) }}</span>
              </td>
              <td class="px-2 md:px-4 py-3 text-muted text-[11px] md:text-xs">
                <span class="md:hidden">{{ m.round_name?.match(/\d+/)?.[0] }}</span>
                <span class="hidden md:inline">{{ m.round_name }}</span>
              </td>
              <td class="px-2 md:px-4 py-3 text-right">
                <div class="flex items-center justify-end gap-1 md:gap-2">
                  <RouterLink v-if="m.team1" :to="`/team/${m.team1.id}`" class="font-medium underline underline-offset-2 decoration-accent/30 hover:decoration-accent transition-colors hidden md:inline" :class="m.winner?.id === m.team1?.id ? 'text-win font-semibold' : 'text-ink'">{{ $teamName(m.team1?.name) }}</RouterLink>
                  <img v-if="flagUrl(m.team1?.name)" :src="flagUrl(m.team1?.name)" :alt="$teamName(m.team1?.name)" class="w-5 h-4 rounded-sm object-cover shrink-0" />
                </div>
              </td>
              <td class="px-2 md:px-4 py-3 text-center">
                <template v-if="m.played">
                  <span class="font-mono font-bold text-xs md:text-base px-1.5 md:px-3 py-0.5 bg-bg rounded-md whitespace-nowrap">{{ m.score_ft_home }}–{{ m.score_ft_away }}</span>
                </template>
                <span v-else class="text-muted text-[10px] md:text-xs">vs</span>
              </td>
              <td class="px-2 md:px-4 py-3 text-left">
                <div class="flex items-center gap-1 md:gap-2">
                  <img v-if="flagUrl(m.team2?.name)" :src="flagUrl(m.team2?.name)" :alt="$teamName(m.team2?.name)" class="w-5 h-4 rounded-sm object-cover shrink-0" />
                  <RouterLink v-if="m.team2" :to="`/team/${m.team2.id}`" class="font-medium underline underline-offset-2 decoration-accent/30 hover:decoration-accent transition-colors hidden md:inline" :class="m.winner?.id === m.team2?.id ? 'text-win font-semibold' : 'text-ink'">{{ $teamName(m.team2?.name) }}</RouterLink>
                </div>
              </td>
              <td class="hidden md:table-cell px-4 py-3 text-muted text-xs">{{ m.stadium?.name || $t('common.tbd') }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { flagUrl } from '../utils/flags.js'
import { formatDate } from '../utils/date.js'

const { locale } = useI18n()

const API = '/api'
const matches = ref(null)
const filterRound = ref('')
const filterGroup = ref('')
const rounds = ref([])
const groupLetters = 'ABCDEFGHIJKL'.split('')

async function load() {
  const params = new URLSearchParams()
  if (filterRound.value) params.set('round_name', filterRound.value)
  if (filterGroup.value) params.set('group', filterGroup.value)
  const qs = params.toString()
  matches.value = await fetch(`${API}/matches${qs ? '?'+qs : ''}`).then(r => r.json())
}

onMounted(async () => {
  await load()
  const all = await fetch(`${API}/matches`).then(r => r.json())
  const r = [...new Set(all.map(m => m.round_name))]
  r.sort()
  rounds.value = r
})
</script>
