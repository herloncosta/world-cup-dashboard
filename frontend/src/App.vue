<template>
  <div class="min-h-screen flex flex-col bg-bg">
    <nav class="flex items-center px-4 md:px-6 h-16 md:h-20 bg-white/90 backdrop-blur-md border-b border-border sticky top-0 z-50">
      <RouterLink to="/" class="flex items-center gap-2 md:gap-3 text-lg md:text-xl font-extrabold text-accent no-underline tracking-[-0.02em]">
        <img src="/logo-copa-do-mundo.webp" alt="World Cup 2026" class="h-9 md:h-11 w-auto" />
        <span class="bg-gradient-to-r from-[#DA291C] via-[#002868] to-[#006341] text-transparent bg-clip-text hidden sm:inline">World Cup 2026</span>
        <span class="bg-gradient-to-r from-[#DA291C] via-[#002868] to-[#006341] text-transparent bg-clip-text sm:hidden">2026</span>
      </RouterLink>

      <div class="hidden lg:flex gap-1 ml-6 md:ml-10">
        <RouterLink to="/" class="px-3 md:px-4 py-2 rounded-lg text-sm font-medium text-muted hover:text-ink hover:bg-surface-hover transition-colors" active-class="bg-accent/10 text-accent font-semibold">{{ $t('nav.dashboard') }}</RouterLink>
        <RouterLink to="/groups" class="px-3 md:px-4 py-2 rounded-lg text-sm font-medium text-muted hover:text-ink hover:bg-surface-hover transition-colors" active-class="bg-accent/10 text-accent font-semibold">{{ $t('nav.groups') }}</RouterLink>
        <RouterLink to="/matches" class="px-3 md:px-4 py-2 rounded-lg text-sm font-medium text-muted hover:text-ink hover:bg-surface-hover transition-colors" active-class="bg-accent/10 text-accent font-semibold">{{ $t('nav.matches') }}</RouterLink>
        <RouterLink to="/stats" class="px-3 md:px-4 py-2 rounded-lg text-sm font-medium text-muted hover:text-ink hover:bg-surface-hover transition-colors" active-class="bg-accent/10 text-accent font-semibold">{{ $t('nav.stats') }}</RouterLink>
        <RouterLink to="/bracket" class="px-3 md:px-4 py-2 rounded-lg text-sm font-medium text-muted hover:text-ink hover:bg-surface-hover transition-colors" active-class="bg-accent/10 text-accent font-semibold">{{ $t('nav.bracket') }}</RouterLink>
      </div>

      <div class="flex-1 lg:hidden"></div>

      <LocaleSwitcher class="hidden lg:block" />

      <button @click="menuOpen = true" class="lg:hidden ml-2 p-2 rounded-lg text-muted hover:text-ink hover:bg-surface-hover transition-colors" aria-label="Open menu">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
      </button>
    </nav>

    <AnimatePresence>
      <motion.div v-if="menuOpen"
        class="fixed inset-0 bg-black/30 z-40 lg:hidden"
        :initial="{ opacity: 0 }" :animate="{ opacity: 1 }" :exit="{ opacity: 0 }"
        :transition="{ duration: 0.2 }"
        @click="menuOpen = false"
      />
    </AnimatePresence>

    <AnimatePresence>
      <motion.div v-if="menuOpen"
        class="fixed top-0 right-0 w-4/5 h-screen bg-white z-50 lg:hidden shadow-2xl flex flex-col"
        :initial="{ x: '100%' }" :animate="{ x: 0 }" :exit="{ x: '100%' }"
        :transition="{ duration: 0.25, ease: 'easeOut' }"
      >
        <div class="flex items-center justify-between px-5 h-16 border-b border-border shrink-0">
          <span class="text-sm font-bold text-ink">Menu</span>
          <button @click="menuOpen = false" class="p-2 rounded-lg text-muted hover:text-ink hover:bg-surface-hover transition-colors" aria-label="Close menu">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
          </button>
        </div>
        <div class="flex-1 flex flex-col p-5 gap-1 overflow-y-auto">
          <RouterLink @click="menuOpen = false" to="/" class="flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-muted hover:text-ink hover:bg-surface-hover transition-colors" active-class="bg-accent/10 text-accent font-semibold">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            {{ $t('nav.dashboard') }}
          </RouterLink>
          <RouterLink @click="menuOpen = false" to="/groups" class="flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-muted hover:text-ink hover:bg-surface-hover transition-colors" active-class="bg-accent/10 text-accent font-semibold">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            {{ $t('nav.groups') }}
          </RouterLink>
          <RouterLink @click="menuOpen = false" to="/matches" class="flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-muted hover:text-ink hover:bg-surface-hover transition-colors" active-class="bg-accent/10 text-accent font-semibold">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
            {{ $t('nav.matches') }}
          </RouterLink>
          <RouterLink @click="menuOpen = false" to="/stats" class="flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-muted hover:text-ink hover:bg-surface-hover transition-colors" active-class="bg-accent/10 text-accent font-semibold">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
            {{ $t('nav.stats') }}
          </RouterLink>
          <RouterLink @click="menuOpen = false" to="/bracket" class="flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-muted hover:text-ink hover:bg-surface-hover transition-colors" active-class="bg-accent/10 text-accent font-semibold">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M22 5v14H2V5h20z"/><path d="M2 10h20"/><path d="M10 5v14"/><path d="M14 5v14"/></svg>
            {{ $t('nav.bracket') }}
          </RouterLink>
        </div>
        <div class="px-5 pb-6 shrink-0 border-t border-border pt-4">
          <LocaleSwitcher class="w-full" />
        </div>
      </motion.div>
    </AnimatePresence>

    <main class="flex-1 w-full">
      <RouterView v-slot="{ Component }">
        <AnimatePresence mode="wait">
          <motion.div
            :key="$route.fullPath"
            :initial="{ opacity: 0, y: 12 }"
            :animate="{ opacity: 1, y: 0 }"
            :exit="{ opacity: 0, y: -12 }"
            :transition="{ duration: 0.2, ease: 'easeOut' }"
          >
            <component :is="Component" />
          </motion.div>
        </AnimatePresence>
      </RouterView>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { motion, AnimatePresence } from 'motion-v'
import LocaleSwitcher from './components/LocaleSwitcher.vue'

const menuOpen = ref(false)
</script>
