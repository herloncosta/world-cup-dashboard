export function formatDate(dateStr, locale = 'en-US', options = {}) {
  if (!dateStr) return ''
  const d = new Date(dateStr + 'T12:00:00')
  const fmt = {
    month: options.month || 'short',
    day: 'numeric',
    ...(options.year ? { year: options.year } : {}),
  }
  return d.toLocaleDateString(locale, fmt)
}
