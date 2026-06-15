<template>
  <select class="appearance-none ml-auto px-3 py-1.5 rounded-lg border border-border bg-bg text-muted text-sm font-medium font-sans cursor-pointer transition-colors hover:border-accent hover:text-accent"
    style="background-image: url(&quot;data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%236B7280' stroke-width='2'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E&quot;); background-repeat: no-repeat; background-position: right 10px center; background-size: 14px; padding-right: 32px;" :value="locale" @change="switchLocale">
    <option value="en-US">EN</option>
    <option value="pt-BR">PT</option>
  </select>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

function switchLocale(e) {
  const val = e.target.value
  locale.value = val
  localStorage.setItem('locale', val)
}
</script>
