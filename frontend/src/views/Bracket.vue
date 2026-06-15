<template>
  <div>
    <div class="bg-linear-to-r from-hero-start to-hero-end px-4 md:px-6 py-6 md:py-8">
      <div class="max-w-300 mx-auto">
        <div class="flex items-center gap-3 mb-1">
          <h1 class="text-white mb-0 text-xl md:text-2xl">{{ $t("bracket.title") }}</h1>
        </div>
        <p class="text-blue-200/70 text-sm">
          Knockout phase — 32 teams, single elimination
        </p>
      </div>
    </div>

    <div
      v-if="!rounds"
      class="flex items-center justify-center py-20 text-muted"
    >
      {{ $t("common.loading") }}
    </div>

    <div v-else class="max-w-300 mx-auto px-4 md:px-6 py-4 md:py-6 overflow-x-auto">
      <div
        class="grid grid-cols-[1fr_1fr_1fr_1fr_1.3fr_1fr_1fr_1fr_1fr] grid-rows-[repeat(16,1fr)] min-w-275 min-h-145 bg-surface rounded-xl border border-border shadow-sm p-3 md:p-4"
      >
        <!-- Left side -->
        <template v-for="(match, i) in leftMatches" :key="'l' + i">
          <div
            class="flex items-center justify-center p-0.75 relative"
            :style="{
              gridColumn: match.col,
              gridRow: `${match.rowStart} / ${match.rowEnd}`,
            }"
          >
            <div
              class="bg-white border border-border rounded-lg px-2.5 py-2 w-full max-w-46.25 shadow-sm hover:shadow-md transition-shadow"
            >
              <div
                class="flex justify-between items-center gap-1.5 text-xs"
                :class="{
                  'font-bold text-accent': match.winner === match.team1,
                }"
              >
                <div class="flex items-center gap-1.5 flex-1 min-w-0">
                  <img
                    v-if="flagUrl(match.team1)"
                    :src="flagUrl(match.team1)"
                    :alt="$teamName(match.team1)"
                    class="w-4 h-3 rounded-sm object-cover shrink-0"
                  />
                  <RouterLink
                    v-if="match.team1Id"
                    :to="`/team/${match.team1Id}`"
                    class="truncate hover:text-accent/80 transition-colors underline underline-offset-1 decoration-accent/20 hover:decoration-accent text-inherit"
                    >{{ $teamName(match.team1) }}</RouterLink
                  >
                  <span v-else class="truncate">{{
                    $teamName(match.team1) || "TBD"
                  }}</span>
                </div>
                <span class="font-mono font-semibold text-xs shrink-0">{{
                  match.score1
                }}</span>
              </div>
              <div
                class="flex justify-between items-center gap-1.5 text-xs mt-1"
                :class="{
                  'font-bold text-accent': match.winner === match.team2,
                }"
              >
                <div class="flex items-center gap-1.5 flex-1 min-w-0">
                  <img
                    v-if="flagUrl(match.team2)"
                    :src="flagUrl(match.team2)"
                    :alt="$teamName(match.team2)"
                    class="w-4 h-3 rounded-sm object-cover shrink-0"
                  />
                  <RouterLink
                    v-if="match.team2Id"
                    :to="`/team/${match.team2Id}`"
                    class="truncate hover:text-accent/80 transition-colors underline underline-offset-1 decoration-accent/20 hover:decoration-accent text-inherit"
                    >{{ $teamName(match.team2) }}</RouterLink
                  >
                  <span v-else class="truncate">{{
                    $teamName(match.team2) || "TBD"
                  }}</span>
                </div>
                <span class="font-mono font-semibold text-xs shrink-0">{{
                  match.score2
                }}</span>
              </div>
            </div>
          </div>
          <div
            v-if="match.conn"
            class="conn-line"
            :style="match.conn.style"
          ></div>
        </template>

        <!-- Right side -->
        <template v-for="(match, i) in rightMatches" :key="'r' + i">
          <div
            class="flex items-center justify-center p-0.75 relative"
            :style="{
              gridColumn: match.col,
              gridRow: `${match.rowStart} / ${match.rowEnd}`,
            }"
          >
            <div
              class="bg-white border border-border rounded-lg px-2.5 py-2 w-full max-w-46.25 shadow-sm hover:shadow-md transition-shadow"
            >
              <div
                class="flex justify-between items-center gap-1.5 text-xs"
                :class="{
                  'font-bold text-accent': match.winner === match.team1,
                }"
              >
                <div class="flex items-center gap-1.5 flex-1 min-w-0">
                  <img
                    v-if="flagUrl(match.team1)"
                    :src="flagUrl(match.team1)"
                    :alt="$teamName(match.team1)"
                    class="w-4 h-3 rounded-sm object-cover shrink-0"
                  />
                  <RouterLink
                    v-if="match.team1Id"
                    :to="`/team/${match.team1Id}`"
                    class="truncate hover:text-accent/80 transition-colors underline underline-offset-1 decoration-accent/20 hover:decoration-accent text-inherit"
                    >{{ $teamName(match.team1) }}</RouterLink
                  >
                  <span v-else class="truncate">{{
                    $teamName(match.team1) || "TBD"
                  }}</span>
                </div>
                <span class="font-mono font-semibold text-xs shrink-0">{{
                  match.score1
                }}</span>
              </div>
              <div
                class="flex justify-between items-center gap-1.5 text-xs mt-1"
                :class="{
                  'font-bold text-accent': match.winner === match.team2,
                }"
              >
                <div class="flex items-center gap-1.5 flex-1 min-w-0">
                  <img
                    v-if="flagUrl(match.team2)"
                    :src="flagUrl(match.team2)"
                    :alt="$teamName(match.team2)"
                    class="w-4 h-3 rounded-sm object-cover shrink-0"
                  />
                  <RouterLink
                    v-if="match.team2Id"
                    :to="`/team/${match.team2Id}`"
                    class="truncate hover:text-accent/80 transition-colors underline underline-offset-1 decoration-accent/20 hover:decoration-accent text-inherit"
                    >{{ $teamName(match.team2) }}</RouterLink
                  >
                  <span v-else class="truncate">{{
                    $teamName(match.team2) || "TBD"
                  }}</span>
                </div>
                <span class="font-mono font-semibold text-xs shrink-0">{{
                  match.score2
                }}</span>
              </div>
            </div>
          </div>
          <div
            v-if="match.conn"
            class="conn-line"
            :style="match.conn.style"
          ></div>
        </template>

        <!-- Trophy center -->
        <div
          class="flex flex-col items-center justify-center p-1 relative"
          :style="{ gridColumn: 5, gridRow: '3 / 6' }"
        >
          <div class="flex flex-col items-center gap-0.5 select-none">
            <img
              src="/taca-copa-do-mundo.webp"
              alt="Trophy"
              class="h-20 w-auto mx-auto drop-shadow-[0_0_20px_rgba(200,169,81,0.6)]"
            />
            <span
              class="text-[11px] font-bold text-[#C8A951] uppercase tracking-[0.15em]"
              >Champion</span
            >
          </div>
        </div>

        <!-- Final -->
        <div
          class="flex items-center justify-center p-0.75 relative"
          v-if="finalMatch"
          :style="{ gridColumn: 5, gridRow: '7 / 11' }"
        >
          <div
            class="bg-white border-2 border-[#C8A951]/40 rounded-lg px-3 py-3 w-full max-w-46.25 shadow-md"
          >
            <div
              class="text-[10px] font-bold text-[#C8A951] uppercase tracking-widest mb-1.5 text-center"
            >
              Final
            </div>
            <div
              class="flex justify-between items-center gap-1.5 text-xs"
              :class="{
                'font-bold text-accent': finalMatch.winner === finalMatch.team1,
              }"
            >
              <div class="flex items-center gap-1.5 flex-1 min-w-0">
                <img
                  v-if="flagUrl(finalMatch.team1)"
                  :src="flagUrl(finalMatch.team1)"
                  :alt="$teamName(finalMatch.team1)"
                  class="w-4 h-3 rounded-sm object-cover shrink-0"
                />
                <RouterLink
                  v-if="finalMatch.team1Id"
                  :to="`/team/${finalMatch.team1Id}`"
                  class="truncate hover:text-accent/80 transition-colors underline underline-offset-1 decoration-accent/20 hover:decoration-accent text-inherit"
                  >{{ $teamName(finalMatch.team1) }}</RouterLink
                >
                <span v-else class="truncate">{{
                  $teamName(finalMatch.team1) || "TBD"
                }}</span>
              </div>
              <span class="font-mono font-semibold text-xs shrink-0">{{
                finalMatch.score1
              }}</span>
            </div>
            <div
              class="flex justify-between items-center gap-1.5 text-xs mt-1"
              :class="{
                'font-bold text-accent': finalMatch.winner === finalMatch.team2,
              }"
            >
              <div class="flex items-center gap-1.5 flex-1 min-w-0">
                <img
                  v-if="flagUrl(finalMatch.team2)"
                  :src="flagUrl(finalMatch.team2)"
                  :alt="$teamName(finalMatch.team2)"
                  class="w-4 h-3 rounded-sm object-cover shrink-0"
                />
                <RouterLink
                  v-if="finalMatch.team2Id"
                  :to="`/team/${finalMatch.team2Id}`"
                  class="truncate hover:text-accent/80 transition-colors underline underline-offset-1 decoration-accent/20 hover:decoration-accent text-inherit"
                  >{{ $teamName(finalMatch.team2) }}</RouterLink
                >
                <span v-else class="truncate">{{
                  $teamName(finalMatch.team2) || "TBD"
                }}</span>
              </div>
              <span class="font-mono font-semibold text-xs shrink-0">{{
                finalMatch.score2
              }}</span>
            </div>
          </div>
        </div>

        <!-- Third place -->
        <div
          class="flex items-center justify-center p-0.75 relative"
          v-if="thirdMatch"
          :style="{ gridColumn: 5, gridRow: '13 / 16' }"
        >
          <div
            class="bg-white border border-border rounded-lg px-2.5 py-2 w-full max-w-46.25 shadow-sm"
          >
            <div
              class="text-[9px] font-semibold text-muted uppercase tracking-[0.06em] mb-1"
            >
              {{ $t("common.matchForThird") }}
            </div>
            <div
              class="flex justify-between items-center gap-1.5 text-xs"
              :class="{
                'font-bold text-accent': thirdMatch.winner === thirdMatch.team1,
              }"
            >
              <div class="flex items-center gap-1.5 flex-1 min-w-0">
                <img
                  v-if="flagUrl(thirdMatch.team1)"
                  :src="flagUrl(thirdMatch.team1)"
                  :alt="$teamName(thirdMatch.team1)"
                  class="w-4 h-3 rounded-sm object-cover shrink-0"
                />
                <RouterLink
                  v-if="thirdMatch.team1Id"
                  :to="`/team/${thirdMatch.team1Id}`"
                  class="truncate hover:text-accent/80 transition-colors underline underline-offset-1 decoration-accent/20 hover:decoration-accent text-inherit"
                  >{{ $teamName(thirdMatch.team1) }}</RouterLink
                >
                <span v-else class="truncate">{{
                  $teamName(thirdMatch.team1) || "TBD"
                }}</span>
              </div>
              <span class="font-mono font-semibold text-xs shrink-0">{{
                thirdMatch.score1
              }}</span>
            </div>
            <div
              class="flex justify-between items-center gap-1.5 text-xs mt-1"
              :class="{
                'font-bold text-accent': thirdMatch.winner === thirdMatch.team2,
              }"
            >
              <div class="flex items-center gap-1.5 flex-1 min-w-0">
                <img
                  v-if="flagUrl(thirdMatch.team2)"
                  :src="flagUrl(thirdMatch.team2)"
                  :alt="$teamName(thirdMatch.team2)"
                  class="w-4 h-3 rounded-sm object-cover shrink-0"
                />
                <RouterLink
                  v-if="thirdMatch.team2Id"
                  :to="`/team/${thirdMatch.team2Id}`"
                  class="truncate hover:text-accent/80 transition-colors underline underline-offset-1 decoration-accent/20 hover:decoration-accent text-inherit"
                  >{{ $teamName(thirdMatch.team2) }}</RouterLink
                >
                <span v-else class="truncate">{{
                  $teamName(thirdMatch.team2) || "TBD"
                }}</span>
              </div>
              <span class="font-mono font-semibold text-xs shrink-0">{{
                thirdMatch.score2
              }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useI18n } from "vue-i18n";
import { flagUrl } from "../utils/flags.js";

const { t } = useI18n();
const rounds = ref(null);

function slot(matchIdx, depth, col) {
  const span = 2 ** depth;
  const rowStart = matchIdx * span * 2 + 1;
  const rowEnd = rowStart + span * 2;
  return { col: col.toString(), rowStart, rowEnd };
}

const STRUCTURE = {
  left: [
    { key: "Ro32", col: 1, depth: 0, count: 8 },
    { key: "Ro16", col: 2, depth: 1, count: 4 },
    { key: "QF", col: 3, depth: 2, count: 2 },
    { key: "SF", col: 4, depth: 3, count: 1 },
  ],
  right: [
    { key: "Ro32", col: 9, depth: 0, count: 8 },
    { key: "Ro16", col: 8, depth: 1, count: 4 },
    { key: "QF", col: 7, depth: 2, count: 2 },
    { key: "SF", col: 6, depth: 3, count: 1 },
  ],
};

function buildSide(side, matchMap) {
  const result = [];
  const rounds = STRUCTURE[side];
  for (const rd of rounds) {
    for (let i = 0; i < rd.count; i++) {
      const pos = slot(i, rd.depth, rd.col);
      const found = matchMap[rd.key]?.[i];
      result.push({
        ...pos,
        round: rd.key,
        team1: found?.team1 || null,
        team1Id: found?.team1Id || null,
        team2: found?.team2 || null,
        team2Id: found?.team2Id || null,
        score1: found?.score1 ?? "",
        score2: found?.score2 ?? "",
        winner: found?.winner || null,
        played: found?.played || false,
      });
    }
  }
  return result;
}

const leftMatches = computed(() => {
  if (!rounds.value) return [];
  return buildSide("left", rounds.value);
});

const rightMatches = computed(() => {
  if (!rounds.value) return [];
  return buildSide("right", rounds.value);
});

const finalMatch = computed(() => {
  if (!rounds.value) return null;
  return rounds.value.Final?.[0] || null;
});

const thirdMatch = computed(() => {
  if (!rounds.value) return null;
  return rounds.value["3rd"]?.[0] || null;
});

onMounted(async () => {
  const all = await fetch("/api/matches").then((r) => r.json());
  const ko = all.filter((m) => m.knockout || !m.group_name);

  const ROUND_NAMES = {
    "Matchday 16": "Ro32",
    "Matchday 17": "Ro32",
    "Round of 32": "Ro32",
    "Round of 16": "Ro16",
    "Quarter-final": "QF",
    "Semi-final": "SF",
    "Match for third place": "3rd",
    Final: "Final",
  };

  const map = { Ro32: [], Ro16: [], QF: [], SF: [], "3rd": [], Final: [] };

  for (const m of ko) {
    const key = ROUND_NAMES[m.round_name];
    if (!key) continue;
    const winner = m.winner_id
      ? m.winner_id === m.team1?.id
        ? m.team1?.name
        : m.team2?.name
      : null;
    map[key].push({
      team1: m.team1?.name || null,
      team1Id: m.team1?.id || null,
      team2: m.team2?.name || null,
      team2Id: m.team2?.id || null,
      score1: m.played ? m.score_ft_home : "",
      score2: m.played ? m.score_ft_away : "",
      winner,
      played: m.played,
    });
  }

  rounds.value = map;
});
</script>
