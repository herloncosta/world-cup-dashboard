<template>
  <div>
    <!-- Hero banner -->
    <div class="bg-gradient-to-r from-[#002868] to-[#1E3A5F] px-4 md:px-6 py-6 md:py-8">
      <div class="max-w-[1200px] mx-auto">
        <h1 class="text-white mb-1 text-xl md:text-2xl">{{ $t("standings.title") }}</h1>
        <p class="text-blue-200/70 text-sm">
          Follow every group — 48 teams, 12 groups, top 2 advance
        </p>
      </div>
    </div>

    <div
      v-if="!groups"
      class="flex items-center justify-center py-20 text-muted"
    >
      {{ $t("common.loading") }}
    </div>

    <div class="max-w-[1200px] mx-auto px-4 md:px-6 py-4 md:py-6" v-else>
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 md:gap-5">
        <div
          v-for="(g, gi) in groups"
          :key="g.letter"
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :animate="{ opacity: 1, y: 0 }"
          :transition="{ duration: 0.3, delay: 0.05 * gi }"
          class="bg-surface rounded-xl border border-border shadow-sm overflow-hidden"
        >
          <div
            class="px-5 py-3.5 border-b border-border bg-gradient-to-r from-accent/5 to-transparent"
          >
            <h2 class="mb-0 text-base font-bold flex items-center gap-2">
              {{ $t("common.group") }} {{ g.letter }}
              <span
                class="text-[10px] font-medium text-muted uppercase tracking-[0.08em]"
                >Group Stage</span
              >
            </h2>
          </div>
          <div class="p-4 overflow-x-auto">
            <table class="w-full text-sm min-w-[400px]">
              <thead>
                <tr class="text-muted border-b border-border">
                  <th class="py-2 pr-2 text-left font-medium w-5">#</th>
                  <th class="py-2 px-2 text-left font-medium">
                    {{ $t("common.team") }}
                  </th>
                  <th class="py-2 px-2 text-center font-medium w-6">
                    {{ $t("standings.p") }}
                  </th>
                  <th class="py-2 px-2 text-center font-medium w-6">
                    {{ $t("standings.w") }}
                  </th>
                  <th class="py-2 px-2 text-center font-medium w-6">
                    {{ $t("standings.d") }}
                  </th>
                  <th class="py-2 px-2 text-center font-medium w-6">
                    {{ $t("standings.l") }}
                  </th>
                  <th class="py-2 px-2 text-center font-medium w-6">
                    {{ $t("standings.gd") }}
                  </th>
                  <th class="py-2 px-2 text-center font-medium w-8">
                    {{ $t("standings.pts") }}
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="s in g.standings"
                  :key="s.team.id"
                  :class="[
                    s.position <= 2 ? 'bg-win/5' : '',
                    'border-b border-border/50 last:border-b-0',
                  ]"
                >
                  <td
                    class="py-2 pr-2 font-semibold"
                    :class="s.position <= 2 ? 'text-win' : 'text-muted'"
                  >
                    {{ s.position }}
                  </td>
                  <td class="py-2 px-2">
                    <div class="flex items-center gap-2">
                      <img
                        v-if="flagUrl(s.team.name)"
                        :src="flagUrl(s.team.name)"
                        :alt="$teamName(s.team.name)"
                        class="w-5 h-4 rounded-sm object-cover shrink-0"
                      />
                      <div class="flex items-center gap-1.5 min-w-0">
                        <RouterLink
                          :to="`/team/${s.team.id}`"
                          :title="s.team.name"
                          class="truncate max-w-[10ch] font-medium underline underline-offset-2 decoration-accent/30 hover:decoration-accent transition-colors"
                          :class="s.position <= 2 ? 'text-ink' : 'text-muted'"
                          >{{ $teamName(s.team.name) }}</RouterLink
                        >
                        <span
                          v-if="s.position <= 2"
                          class="shrink-0 inline-flex items-center justify-center w-4 h-4 rounded-full bg-win text-white text-[8px] font-extrabold"
                          :title="$t('standings.qualified')"
                          >Q</span
                        >
                      </div>
                    </div>
                  </td>
                  <td class="py-2 px-2 text-center text-muted">
                    {{ s.played }}
                  </td>
                  <td class="py-2 px-2 text-center text-muted">{{ s.won }}</td>
                  <td class="py-2 px-2 text-center text-muted">
                    {{ s.drawn }}
                  </td>
                  <td class="py-2 px-2 text-center text-muted">{{ s.lost }}</td>
                  <td
                    class="py-2 px-2 text-center font-medium tabular-nums"
                    :class="{
                      'text-win': s.goal_diff > 0,
                      'text-muted': s.goal_diff === 0,
                      'text-loss': s.goal_diff < 0,
                    }"
                  >
                    {{ s.goal_diff > 0 ? "+" : "" }}{{ s.goal_diff }}
                  </td>
                  <td
                    class="py-2 px-2 text-center font-bold text-accent text-base"
                  >
                    {{ s.points }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { flagUrl } from "../utils/flags.js";

const groups = ref(null);

onMounted(async () => {
  groups.value = await fetch("/api/groups").then((r) => r.json());
});
</script>
