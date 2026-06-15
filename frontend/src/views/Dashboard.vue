<template>
  <div>
    <!-- Hero -->
    <div class="relative bg-gradient-to-br from-[#002868] via-[#003A7A] to-[#1E3A5F] overflow-hidden px-4 md:px-6 py-8 md:py-10 lg:py-14">
      <div class="absolute inset-0 opacity-[0.06]" style="background-image: radial-gradient(circle at 25% 50%, white 1px, transparent 1px); background-size: 40px 40px;"></div>
      <div class="absolute inset-0 bg-gradient-to-t from-[#002868]/80 to-transparent"></div>
      <div class="relative z-10 max-w-[1200px] mx-auto">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div>
            <div class="flex items-center gap-2 md:gap-3 mb-2">
              <Trophy :size="22" class="text-[#C8A951] shrink-0" />
              <span class="text-[#C8A951] text-xs md:text-sm font-semibold uppercase tracking-[0.15em]">FIFA World Cup</span>
            </div>
            <h1 class="text-white text-2xl md:text-3xl lg:text-4xl font-extrabold tracking-[-0.03em]">Canada • Mexico • USA</h1>
            <p class="text-blue-200/80 text-xs md:text-sm lg:text-base mt-1.5 max-w-xl">June 11 – July 19, 2026 &nbsp;·&nbsp; 48 teams &nbsp;·&nbsp; 104 matches</p>
          </div>
          <div class="flex items-center gap-4 md:gap-6">
            <div class="text-center">
              <div class="text-2xl md:text-3xl lg:text-4xl font-bold text-white font-mono">{{ daysLeft }}</div>
              <div class="text-blue-200/70 text-[10px] md:text-xs uppercase tracking-[0.1em] mt-0.5">{{ daysLabel }}</div>
            </div>
            <div class="flex -space-x-2 md:-space-x-3">
              <img src="https://flagcdn.com/24x18/ca.png" alt="Canada" class="w-6 h-[18px] md:w-8 md:h-6 rounded shadow-sm" />
              <img src="https://flagcdn.com/24x18/mx.png" alt="Mexico" class="w-6 h-[18px] md:w-8 md:h-6 rounded shadow-sm" />
              <img src="https://flagcdn.com/24x18/us.png" alt="USA" class="w-6 h-[18px] md:w-8 md:h-6 rounded shadow-sm" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Stories bar -->
    <div class="bg-white border-b border-border overflow-hidden" v-if="allTeams.length">
      <div class="max-w-[1200px] mx-auto px-4 md:px-6 py-2 md:py-3">
        <div class="flex gap-3 md:gap-4 marquee-content min-w-max">
          <RouterLink v-for="t in allTeams" :key="t.id" :to="`/team/${t.id}`"
            class="flex flex-col items-center gap-1 group shrink-0">
            <div class="rounded-full p-[1.5px] md:p-[2px] bg-gradient-to-b from-[#C8A951] via-[#DA291C] to-[#006341]">
              <div class="rounded-full bg-white p-[1.5px] md:p-[2px]">
                <img v-if="flagUrl(t.name)" :src="flagUrl(t.name)" :alt="$teamName(t.name)"
                  class="w-8 h-8 md:w-10 md:h-10 rounded-full object-cover" />
                <div v-else
                  class="w-8 h-8 md:w-10 md:h-10 rounded-full bg-bg flex items-center justify-center text-[9px] md:text-[10px] font-bold text-muted">
                  {{ t.name?.charAt(0) }}
                </div>
              </div>
            </div>
            <span class="text-[9px] md:text-[10px] text-muted font-medium truncate max-w-[48px] md:max-w-[56px] text-center leading-tight group-hover:text-accent transition-colors">{{ $teamName(t.name) }}</span>
          </RouterLink>
          <RouterLink v-for="t in allTeams" :key="'dup-'+t.id" :to="`/team/${t.id}`"
            class="flex flex-col items-center gap-1 group shrink-0">
            <div class="rounded-full p-[1.5px] md:p-[2px] bg-gradient-to-b from-[#C8A951] via-[#DA291C] to-[#006341]">
              <div class="rounded-full bg-white p-[1.5px] md:p-[2px]">
                <img v-if="flagUrl(t.name)" :src="flagUrl(t.name)" :alt="$teamName(t.name)"
                  class="w-8 h-8 md:w-10 md:h-10 rounded-full object-cover" />
                <div v-else
                  class="w-8 h-8 md:w-10 md:h-10 rounded-full bg-bg flex items-center justify-center text-[9px] md:text-[10px] font-bold text-muted">
                  {{ t.name?.charAt(0) }}
                </div>
              </div>
            </div>
            <span class="text-[9px] md:text-[10px] text-muted font-medium truncate max-w-[48px] md:max-w-[56px] text-center leading-tight group-hover:text-accent transition-colors">{{ $teamName(t.name) }}</span>
          </RouterLink>
        </div>
      </div>
    </div>

    <!-- Content -->
    <div class="max-w-[1200px] mx-auto px-4 md:px-6 py-4 md:py-6 space-y-4 md:space-y-6">
      <!-- Recent matches (top) -->
      <div class="bg-surface rounded-xl border border-border shadow-sm" v-if="matches">
        <div class="flex items-center justify-between px-4 md:px-5 py-3 md:py-4 border-b border-border">
          <h2 class="mb-0 text-sm md:text-base font-bold">{{ $t('dashboard.recentMatches') }}</h2>
          <RouterLink to="/matches" class="text-xs text-accent font-medium hover:underline">{{ $t('dashboard.allMatches') }} →</RouterLink>
        </div>
        <div class="p-5">
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
            <div v-for="m in matches.slice(0, 4)" :key="m.id"
              class="flex flex-col gap-2 p-3 rounded-lg border border-border/60 bg-bg/50 hover:bg-surface-hover transition-colors cursor-pointer">
              <div class="flex items-center justify-between text-[10px] text-muted uppercase tracking-[0.06em]">
                <span>{{ m.round_name }}</span>
                <span>{{ formatDate(m.date, locale, { month: 'short' }) }}</span>
              </div>
              <div v-if="m.team1" class="flex items-center gap-2">
                <img v-if="flagUrl(m.team1.name)" :src="flagUrl(m.team1.name)" :alt="$teamName(m.team1.name)" class="w-5 h-4 rounded-sm object-cover" />
                <RouterLink :to="`/team/${m.team1.id}`" class="flex-1 text-sm font-medium truncate underline underline-offset-2 decoration-accent/30 hover:decoration-accent transition-colors" :class="m.winner?.id === m.team1?.id ? 'text-win font-semibold' : 'text-ink'">{{ $teamName(m.team1.name) }}</RouterLink>
                <span v-if="m.played" class="text-sm font-bold font-mono text-win">{{ m.score_ft_home }}</span>
              </div>
              <div v-if="m.team2" class="flex items-center gap-2">
                <img v-if="flagUrl(m.team2.name)" :src="flagUrl(m.team2.name)" :alt="$teamName(m.team2.name)" class="w-5 h-4 rounded-sm object-cover" />
                <RouterLink :to="`/team/${m.team2.id}`" class="flex-1 text-sm font-medium truncate underline underline-offset-2 decoration-accent/30 hover:decoration-accent transition-colors" :class="m.winner?.id === m.team2?.id ? 'text-win font-semibold' : 'text-ink'">{{ $teamName(m.team2.name) }}</RouterLink>
                <span v-if="m.played" class="text-sm font-bold font-mono text-win">{{ m.score_ft_away }}</span>
              </div>
              <div v-if="!m.played" class="flex items-center justify-center py-1 text-xs text-muted">{{ $t('common.vs') }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom row: Groups summary + Top scorers -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Group leaders -->
        <div class="lg:col-span-2 bg-surface rounded-xl border border-border shadow-sm">
          <div class="flex items-center justify-between px-4 md:px-5 py-3 md:py-4 border-b border-border">
            <h2 class="mb-0 text-sm md:text-base font-bold">{{ $t('dashboard.groupStandings') }}</h2>
            <RouterLink to="/groups" class="text-xs text-accent font-medium hover:underline">{{ $t('dashboard.allGroups') }} →</RouterLink>
          </div>
          <div class="p-5" v-if="standings">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div v-for="g in standings" :key="g.letter">
                <div class="text-[11px] font-semibold text-muted uppercase tracking-[0.1em] mb-2">Group {{ g.letter }}</div>
                <table class="w-full text-xs">
                  <thead>
                    <tr class="text-muted border-b border-border">
                      <th class="py-1.5 pr-2 text-left font-medium w-5">#</th>
                      <th class="py-1.5 px-2 text-left font-medium">Team</th>
                      <th class="py-1.5 px-2 text-center font-medium w-6">P</th>
                      <th class="py-1.5 px-2 text-center font-medium w-6">W</th>
                      <th class="py-1.5 px-2 text-center font-medium w-6">D</th>
                      <th class="py-1.5 px-2 text-center font-medium w-6">L</th>
                      <th class="py-1.5 px-2 text-center font-medium w-8">Pts</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="s in g.standings" :key="s.team.id"
                      :class="[s.position <= 2 ? '' : 'opacity-60', 'border-b border-border/50 last:border-b-0']">
                      <td class="py-1.5 pr-2 font-semibold" :class="s.position <= 2 ? 'text-win' : 'text-muted'">{{ s.position }}</td>
                      <td class="py-1.5 px-2">
                          <div class="flex items-center gap-1.5 flex-1 min-w-0">
                            <img v-if="flagUrl(s.team.name)" :src="flagUrl(s.team.name)" :alt="$teamName(s.team.name)" class="w-4 h-3 rounded-sm object-cover shrink-0" />
                            <RouterLink :to="`/team/${s.team.id}`" class="truncate font-medium underline underline-offset-2 decoration-accent/30 hover:decoration-accent transition-colors" :class="s.position <= 2 ? 'text-ink' : 'text-muted'">{{ $teamName(s.team.name) }}</RouterLink>
                        </div>
                      </td>
                      <td class="py-1.5 px-2 text-center text-muted">{{ s.played }}</td>
                      <td class="py-1.5 px-2 text-center text-muted">{{ s.won }}</td>
                      <td class="py-1.5 px-2 text-center text-muted">{{ s.drawn }}</td>
                      <td class="py-1.5 px-2 text-center text-muted">{{ s.lost }}</td>
                      <td class="py-1.5 px-2 text-center font-bold text-accent">{{ s.points }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>

        <!-- Right column: Today's matches + Top scorers -->
        <div class="flex flex-col gap-4 md:gap-6">
          <!-- Today's matches -->
          <div class="bg-surface rounded-xl border border-border shadow-sm" v-if="todayMatches.length">
            <div class="flex items-center justify-between px-4 md:px-5 py-3 md:py-4 border-b border-border">
              <h2 class="mb-0 text-sm md:text-base font-bold">{{ $t('dashboard.todayMatches') }}</h2>
              <RouterLink to="/matches" class="text-xs text-accent font-medium hover:underline">{{ $t('common.viewAll') }} →</RouterLink>
            </div>
            <div class="p-4 space-y-3">
              <div v-for="m in todayMatches" :key="m.id"
                class="flex items-center gap-3 p-2.5 rounded-lg bg-bg/50 hover:bg-surface-hover transition-colors">
                <div class="flex-1 min-w-0 text-right">
                  <div class="flex items-center justify-end gap-1.5">
                    <span class="text-sm font-medium truncate" :class="m.winner?.id === m.team1?.id ? 'text-win font-semibold' : 'text-ink'">{{ $teamName(m.team1?.name) }}</span>
                    <img v-if="flagUrl(m.team1?.name)" :src="flagUrl(m.team1?.name)" :alt="$teamName(m.team1?.name)" class="w-5 h-4 rounded-sm object-cover shrink-0" />
                  </div>
                </div>
                <div class="shrink-0 text-center min-w-[48px]">
                  <template v-if="m.played">
                    <span class="text-sm font-bold font-mono px-2 py-0.5 rounded bg-white border"
                      :class="m.score_ft_home > m.score_ft_away ? 'text-win border-win/20' : m.score_ft_home < m.score_ft_away ? 'text-loss border-loss/20' : 'text-draw border-draw/20'">{{ m.score_ft_home }}–{{ m.score_ft_away }}</span>
                  </template>
                  <span v-else class="text-[10px] text-muted font-medium">{{ m.time?.slice(0, 5) || 'TBD' }}</span>
                </div>
                <div class="flex-1 min-w-0 text-left">
                  <div class="flex items-center gap-1.5">
                    <img v-if="flagUrl(m.team2?.name)" :src="flagUrl(m.team2?.name)" :alt="$teamName(m.team2?.name)" class="w-5 h-4 rounded-sm object-cover shrink-0" />
                    <span class="text-sm font-medium truncate" :class="m.winner?.id === m.team2?.id ? 'text-win font-semibold' : 'text-ink'">{{ $teamName(m.team2?.name) }}</span>
                  </div>
                </div>
              </div>
              <div v-if="!todayMatches.length" class="text-center py-6 text-muted text-sm">{{ $t('dashboard.noMatches') }}</div>
            </div>
          </div>

          <!-- Top scorers -->
          <div class="bg-surface rounded-xl border border-border shadow-sm">
            <div class="flex items-center justify-between px-4 md:px-5 py-3 md:py-4 border-b border-border">
              <h2 class="mb-0 text-sm md:text-base font-bold">{{ $t('dashboard.topScorers') }}</h2>
              <RouterLink to="/stats" class="text-xs text-accent font-medium hover:underline">{{ $t('common.fullList') }} →</RouterLink>
            </div>
            <div class="p-5" v-if="scorers">
              <div v-for="(s, i) in scorers.slice(0, 10)" :key="i"
                class="flex items-center gap-3 py-2.5 border-b border-border/50 last:border-b-0">
                <div class="w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold shrink-0"
                  :class="[i === 0 ? 'bg-[#C8A951]/20 text-[#C8A951]' : i === 1 ? 'bg-gray-200 text-gray-500' : i === 2 ? 'bg-amber-100 text-amber-700' : 'bg-transparent text-muted']">
                  {{ i + 1 }}
                </div>
                <img v-if="flagUrl(s.team?.name)" :src="flagUrl(s.team.name)" :alt="$teamName(s.team.name)" class="w-5 h-4 rounded-sm object-cover shrink-0" />
                <div class="flex-1 min-w-0">
                  <div class="text-sm font-semibold truncate">{{ s.player }}</div>
                  <RouterLink v-if="s.team?.id" :to="`/team/${s.team.id}`" class="text-[11px] text-muted underline underline-offset-2 decoration-accent/30 hover:decoration-accent hover:text-accent transition-colors">{{ $teamName(s.team?.name) }}</RouterLink>
                </div>
                <div class="text-lg font-bold text-accent font-mono">{{ s.goals }}</div>
              </div>
              <div v-if="!scorers" class="text-center py-8 text-muted text-sm">Loading...</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { Trophy } from 'lucide-vue-next'
import { flagUrl } from '../utils/flags.js'
import { formatDate } from '../utils/date.js'

const { locale } = useI18n()

const API = '/api'
const standings = ref(null)
const scorers = ref(null)
const matches = ref(null)

const targetDate = new Date('2026-07-19T20:00:00')
const now = new Date()
const diff = targetDate - now
const daysLeft = Math.max(0, Math.ceil(diff / (1000 * 60 * 60 * 24)))

const startDate = new Date('2026-06-11T12:00:00')
const endDate = new Date('2026-07-19T23:00:00')
const daysLabel = computed(() => {
  if (now < startDate) return 'days to go'
  if (now > endDate) return 'tournament over'
  if (daysLeft === 0) return 'final day'
  return daysLeft === 1 ? 'day until final' : 'days until final'
})

const allTeams = computed(() => {
  if (!standings.value) return []
  return standings.value.flatMap(g => g.standings.map(s => s.team))
})

const todayStr = now.toISOString().slice(0, 10)
const todayMatches = computed(() => {
  if (!matches.value) return []
  return matches.value.filter(m => String(m.date).slice(0, 10) === todayStr)
})

onMounted(async () => {
  const [s, sc, m] = await Promise.all([
    fetch(`${API}/groups`).then(r => r.json()),
    fetch(`${API}/stats/top-scorers`).then(r => r.json()),
    fetch(`${API}/matches`).then(r => r.json()),
  ])
  standings.value = s
  scorers.value = sc
  matches.value = m
})
</script>
