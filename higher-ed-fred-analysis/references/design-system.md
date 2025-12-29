# Design System for Higher Education Economic Dashboards

Sophisticated, professional design system optimized for data-heavy institutional communications.

## Color Palette

### Primary Colors
```css
--primary: #1a2332;     /* Deep navy - main backgrounds */
--secondary: #2c4564;   /* Lighter navy - cards, gradients */
--bg: #0f1419;          /* Darkest - page background */
--surface: #1a2332;     /* Card surfaces */
```

### Accent Colors
```css
--accent: #d4af37;      /* Rich gold - primary accent, headers, highlights */
--accent-dim: #8b7355;  /* Muted gold - hover states, secondary accents */
```

### Text Colors
```css
--text: #e8e6e3;        /* Primary text - high contrast */
--text-dim: #a8a5a1;    /* Secondary text - descriptions, metadata */
```

### Semantic Colors
```css
--success: #4ade80;     /* Green - positive indicators, degree holders */
--warning: #fb923c;     /* Orange - neutral/warning, high school data */
--danger: #f87171;      /* Red - negative indicators, no diploma data */
--border: rgba(212, 175, 55, 0.15);  /* Subtle gold borders */
```

### Usage Guidelines

**When to use accent gold**:
- All major headers (h1, h2)
- Metric values (not labels)
- Primary data lines in charts
- Important CTAs and links
- Top borders on hover states

**When to use semantic colors**:
- Bachelor's degree data: success green (#4ade80)
- High school data: warning orange (#fb923c)
- No diploma data: danger red (#f87171)
- Maintain these consistently across all charts for immediate recognition

## Typography

### Font Families
```css
--serif: 'Playfair Display', serif;
--mono: 'IBM Plex Mono', monospace;
--sans: 'Inter', sans-serif;
```

### Type Scale
```css
/* Headers - Use Playfair Display */
h1: 3.5rem, weight 900, letter-spacing -0.02em
h2: 2.5rem, weight 900
h3: 1.75rem, weight 700
h4: 1.3rem, weight 700

/* Data/Metrics - Use Playfair Display */
.metric-value: 2.5rem, weight 700
.chart-title: 1.75rem

/* UI Elements - Use IBM Plex Mono */
.subtitle: 0.9rem, uppercase, letter-spacing 0.05em
.metric-label: 0.75rem, uppercase, letter-spacing 0.1em
.btn: 0.85rem, uppercase, letter-spacing 0.05em, weight 500

/* Body Text - Use Inter */
body: 1rem, weight 400, line-height 1.6
.report-section p: 1rem, line-height 1.8
```

### Typography Rules
- **All headers use Playfair Display**: Establishes premium, institutional feel
- **All data/metrics use Playfair Display**: Creates visual hierarchy
- **All UI labels use IBM Plex Mono**: Technical precision for data context
- **All body text uses Inter**: Readable, professional for long-form content
- **Uppercase + letter-spacing for labels**: Reduces visual noise, improves scannability

## Layout Grid

### Metrics Grid
```css
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}
```

### Responsive Breakpoints
- **Desktop**: 1400px max-width, 2rem side padding
- **Tablet**: Full fluid width, 1.5rem padding
- **Mobile**: Full width, 1rem padding, single column metrics

## Component Patterns

### Metric Card
```html
<div class="metric-card">
  <div class="metric-label">Total Student Debt</div>
  <div class="metric-value">$1.77T</div>
  <div class="metric-change">+3.2% from last year</div>
</div>
```

**Styling**:
- Background: surface color
- Border: subtle gold (--border)
- Padding: 2rem
- Hover: Lift (translateY(-4px)), brighten border to --accent
- Top accent bar on hover: 3px gold gradient

### Chart Container
```html
<div class="chart-container">
  <h2 class="chart-title">Student Loan Debt Trajectory</h2>
  <p class="chart-description">
    Context and interpretation of the visualization...
  </p>
  <canvas></canvas>
</div>
```

**Styling**:
- Background: surface
- Padding: 2.5rem
- Border: subtle gold
- Title: accent gold, Playfair Display
- Description: text-dim, smaller than body

### Insight Box
```html
<div class="insight-box">
  <h3>Key Insight</h3>
  <p>Interpretation and strategic implications...</p>
</div>
```

**Styling**:
- Background: gradient gold overlay (5% → 2% opacity)
- Border-left: 4px solid accent
- Padding: 2rem
- Rounded corners (right side only): 8px

## Chart.js Configurations

### Line Chart (Time Series)
```javascript
{
  type: 'line',
  data: {
    labels: dates,
    datasets: [{
      data: values,
      borderColor: '#d4af37',        // Accent gold for primary series
      backgroundColor: 'rgba(212, 175, 55, 0.1)',
      borderWidth: 3,
      tension: 0.4,                   // Smooth curves
      fill: true,
      pointRadius: 0,                 // Hide points for cleaner look
      pointHoverRadius: 6             // Show on hover
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: { display: false },    // For single series
      tooltip: {
        backgroundColor: '#1a2332',
        titleColor: '#d4af37',
        bodyColor: '#e8e6e3',
        borderColor: '#d4af37',
        borderWidth: 1,
        padding: 12,
        displayColors: false
      }
    },
    scales: {
      x: {
        grid: { color: 'rgba(212, 175, 55, 0.05)' },
        ticks: { 
          color: '#a8a5a1',
          maxTicksLimit: 8 
        }
      },
      y: {
        grid: { color: 'rgba(212, 175, 55, 0.05)' },
        ticks: { 
          color: '#a8a5a1',
          callback: (value) => `$${value}B`  // Format as needed
        }
      }
    }
  }
}
```

### Multi-Series Line Chart (Comparisons)
```javascript
datasets: [
  {
    label: "Bachelor's Degree+",
    data: bachelorData,
    borderColor: '#4ade80',          // Success green
    backgroundColor: 'rgba(74, 222, 128, 0.1)',
    borderWidth: 3,
    tension: 0.4,
    pointRadius: 0
  },
  {
    label: 'High School Only',
    data: hsData,
    borderColor: '#fb923c',          // Warning orange
    backgroundColor: 'rgba(251, 146, 60, 0.1)',
    borderWidth: 3,
    tension: 0.4,
    pointRadius: 0
  },
  {
    label: 'No High School',
    data: noDiplomaData,
    borderColor: '#f87171',          // Danger red
    backgroundColor: 'rgba(248, 113, 113, 0.1)',
    borderWidth: 3,
    tension: 0.4,
    pointRadius: 0
  }
]
```

**Legend configuration for multi-series**:
```javascript
legend: {
  display: true,
  position: 'top',
  labels: {
    color: '#e8e6e3',
    font: { size: 12, family: 'IBM Plex Mono' },
    padding: 15,
    usePointStyle: true
  }
}
```

### Bar Chart (Annual Comparisons)
```javascript
{
  type: 'bar',
  data: {
    labels: years,
    datasets: [
      {
        label: "Bachelor's Degree+",
        data: bachelorEarnings,
        backgroundColor: 'rgba(74, 222, 128, 0.8)',
        borderColor: '#4ade80',
        borderWidth: 2
      },
      {
        label: 'High School Only',
        data: hsEarnings,
        backgroundColor: 'rgba(251, 146, 60, 0.8)',
        borderColor: '#fb923c',
        borderWidth: 2
      }
    ]
  }
}
```

## Animation Guidelines

### Fade-in on Load
```css
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.dashboard { animation: fadeIn 0.8s ease-out; }
```

### Slide-up Sections
```css
@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.metrics-grid { animation: slideUp 0.8s ease-out 0.2s both; }
.chart-container { animation: slideUp 0.8s ease-out 0.4s both; }
```

**Stagger delays**: 0.2s increments for sequential reveal effect

### Hover Transitions
```css
.metric-card {
  transition: all 0.3s;
}

.metric-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
}
```

## Accessibility Considerations

**Color Contrast**: All text meets WCAG AA standards
- Primary text (#e8e6e3) on dark backgrounds: >7:1 ratio
- Accent gold (#d4af37) reserved for large text (headers, metrics)

**Chart Accessibility**:
- Use patterns in addition to colors for print-friendly output
- Ensure semantic color meanings are reinforced with labels
- Provide ARIA labels for interactive elements

**Responsive Typography**: Font sizes scale down appropriately on mobile without losing legibility

## Dark Theme Rationale

**Why dark theme for institutional dashboards?**
1. **Reduces eye strain** during extended analysis sessions
2. **Highlights data** - gold accents pop against dark background
3. **Premium feel** - sophisticated, modern aesthetic appropriate for C-suite presentations
4. **Screen versatility** - looks professional in both bright offices and dim conference rooms

## Design Philosophy

**"Data First, Chrome Second"**: Every design element should enhance data comprehension, never compete with it. Gold accents draw eyes to insights. Typography hierarchy guides reading flow. Dark backgrounds recede, letting charts shine.

**Institutional Gravitas**: Playfair Display serif conveys established authority. IBM Plex Mono adds technical precision. Together they balance tradition with innovation - perfect for higher education contexts.

**Progressive Disclosure**: Animations reveal content in logical sequence. Hover states invite exploration. Design guides stakeholders through complex economic narratives without overwhelming.
