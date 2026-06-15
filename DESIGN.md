# Design

## Theme

**Modo escuro** — paleta inspirada nas cores dos três países-sede da Copa do Mundo FIFA 2026: México, Canadá e Estados Unidos, com acento de campanha roxo. Fundo escuro como base, superfícies em cinza escuro, texto em cinza claro. As cores vibrantes vêm das bandeiras: verde México (vitórias/metricas), vermelho Canadá (derrotas/alertas), azul EUA (links/filtros), roxo campanha (categorias secundárias).

Mood: *"União das Américas — noite de abertura, refletores, placar eletrônico."*

## Palette

```css
--bg:             #0A0A0A    /* fundo escuro absoluto */
--surface:        #1A1A1A    /* cartões e tabelas */
--surface-hover:  #2A2A2A
--surface-raised: #333333
--border:         #333333    /* bordas sutis */
--ink:            #F4F5F7    /* texto principal */
--muted:          #888888    /* texto secundário */
--accent:         #002868    /* Azul EUA — links, filtros */
--accent-hover:   #003BA0
--win:            #006341    /* Verde México — vitórias */
--draw:           #5D2F91    /* Roxo Campanha — empates/secundário */
--loss:           #DA291C    /* Vermelho Canadá — derrotas/alertas */
```

## Typography

| Role | Face | Weight | Size |
|---|---|---|---|
| Display (h1) | Inter | 800 | clamp(1.75rem, 3vw, 2.5rem) |
| Heading (h2) | Inter | 700 | clamp(1.25rem, 2vw, 1.5rem) |
| Subheading (h3) | Inter | 600 | 1rem |
| Body | Inter | 400 | 0.9375rem |
| Small/label | Inter | 500 | 0.75rem |
| Score/mono | JetBrains Mono | 500 | 1rem |

Import: Google Fonts (Inter + JetBrains Mono).

## Icons

Lucide (`lucide-vue-next`): `CircleDot` (nav brand), `Trophy` (bracket).

## Components

### Nav
Altura fixa 56px, bg `--surface`, borda inferior `--border`. Brand à esquerda com `CircleDot` em `--accent`. Links com `--muted` / hover `--ink`, ativo `--surface-raised`. Seletor de idioma (`LocaleSwitcher`) alinhado à direita.

### Cards
Bg `--surface`, border-radius 6px (`rounded-md`), borda `1px solid --border`. Padding 20px. Hover: `--surface-hover`.

### Tables
Headers em `--muted` size 0.75rem, uppercase tracking 0.06em. Rows com borda `--border`. Última row sem borda.

### Tabela de classificação (grupos)
Destaque para as 2 primeiras posições (classificadas) com indicador verde `Q` e borda sutil `border-win/20`. Pontos em `--accent` (azul).

### Bracket
Match cards com bg `--surface`, vencedor em `--accent` (azul). Placar em JetBrains Mono. Grid CSS (9 colunas × 16 linhas). Final com borda `--accent/35`.

### Links / times
`--accent` (azul) para links de times.

### Botões / filtros
Selects com bg `--surface`, borda `--border`, texto `--ink`. Focus: `--accent` ring.

### Loading state
`--muted` centralizado.

## Motion

- Transitions: 0.15s ease-out para hovers e focus
- Page transitions: fade de 0.15s (classe `.page-*`)
- `@media (prefers-reduced-motion: reduce)` desliga tudo

## Responsivo

- Breakpoint único: 768px (md)
- Grid de grupos/dashboard vira 1 coluna em mobile
- Bracket vira scroll horizontal
- Nav mantém horizontal (poucos links)
