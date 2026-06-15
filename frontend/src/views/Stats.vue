<template>
  <div>
    <div class="bg-gradient-to-r from-[#002868] to-[#1E3A5F] px-4 md:px-6 py-6 md:py-8">
      <div class="max-w-[1200px] mx-auto">
        <h1 class="text-white mb-1 text-xl md:text-2xl">{{ $t('stats.title') }}</h1>
        <p class="text-blue-200/70 text-sm">Top scorers and group performance</p>
      </div>
    </div>

    <div class="max-w-[1200px] mx-auto px-4 md:px-6 py-4 md:py-6 space-y-4 md:space-y-6">
      <!-- Top Scorers -->
      <div class="bg-surface rounded-xl border border-border shadow-sm" v-if="scorers">
        <div class="px-4 md:px-5 py-3 md:py-4 border-b border-border">
          <h2 class="mb-0 text-sm md:text-base font-bold">{{ $t('scorers.title') }}</h2>
        </div>
        <div class="p-4 md:p-5 overflow-x-auto">
          <table class="w-full text-sm min-w-[400px]">
            <thead>
              <tr class="text-muted border-b border-border">
                <th class="py-2.5 pr-2 text-left font-medium w-8">#</th>
                <th class="py-2.5 px-2 text-left font-medium">{{ $t('common.player') }}</th>
                <th class="py-2.5 px-2 text-left font-medium">{{ $t('common.team') }}</th>
                <th class="py-2.5 px-2 text-center font-medium w-20">{{ $t('common.goals') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(s, i) in scorers" :key="i"
                :class="[i === 0 ? 'bg-[#C8A951]/5' : i === 1 ? 'bg-gray-50' : i === 2 ? 'bg-amber-50' : '', 'border-b border-border/50 last:border-b-0']">
                <td class="py-2.5 pr-2">
                  <div class="w-7 h-7 rounded-full flex items-center justify-center text-xs font-bold"
                    :class="[i === 0 ? 'bg-[#C8A951]/20 text-[#C8A951]' : i === 1 ? 'bg-gray-200 text-gray-500' : i === 2 ? 'bg-amber-100 text-amber-700' : 'text-muted']">
                    {{ i + 1 }}
                  </div>
                </td>
                <td class="py-2.5 px-2 font-semibold" :class="i < 3 ? 'text-ink' : ''">{{ s.player }}</td>
                <td class="py-2.5 px-2">
                  <div class="flex items-center gap-2">
                    <img v-if="flagUrl(s.team?.name)" :src="flagUrl(s.team?.name)" :alt="$teamName(s.team?.name)" class="w-5 h-4 rounded-sm object-cover" />
                    <RouterLink v-if="s.team?.id" :to="`/team/${s.team.id}`" class="text-muted text-sm underline underline-offset-2 decoration-accent/30 hover:decoration-accent hover:text-accent transition-colors">{{ $teamName(s.team?.name) }}</RouterLink>
                  </div>
                </td>
                <td class="py-2.5 px-2 text-center font-bold text-accent font-mono"
                  :class="[i === 0 ? 'text-2xl' : i === 1 ? 'text-xl' : i === 2 ? 'text-lg' : 'text-base']">{{ s.goals }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Group Summary -->
      <div class="bg-surface rounded-xl border border-border shadow-sm" v-if="summary">
        <div class="px-4 md:px-5 py-3 md:py-4 border-b border-border">
          <h2 class="mb-0 text-sm md:text-base font-bold">{{ $t('stats.groupSummary') }}</h2>
        </div>
        <div class="p-4 md:p-5 overflow-x-auto">
          <table class="w-full text-sm min-w-[400px]">
            <thead>
              <tr class="text-muted border-b border-border">
                <th class="py-2.5 px-3 text-left font-medium">{{ $t('common.group') }}</th>
                <th class="py-2.5 px-3 text-center font-medium">{{ $t('stats.teams') }}</th>
                <th class="py-2.5 px-3 text-center font-medium">{{ $t('stats.matchesPlayed') }}</th>
                <th class="py-2.5 px-3 text-center font-medium">{{ $t('stats.totalGoals') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(val, key) in summary" :key="key" class="border-b border-border/50 last:border-b-0">
                <td class="py-2.5 px-3 font-bold text-accent">{{ key }}</td>
                <td class="py-2.5 px-3 text-center text-muted">{{ val.teams }}</td>
                <td class="py-2.5 px-3 text-center text-muted">{{ val.matches_played }}</td>
                <td class="py-2.5 px-3 text-center font-mono font-semibold text-ink">{{ val.total_goals }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { flagUrl } from '../utils/flags.js'

const scorers = ref(null)
const summary = ref(null)

onMounted(async () => {
  const [s, sm] = await Promise.all([
    fetch('/api/stats/top-scorers?limit=50').then(r => r.json()),
    fetch('/api/stats/standings-summary').then(r => r.json()),
  ])
  scorers.value = s
  summary.value = sm
})
</script>
