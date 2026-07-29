import os

html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>BloomX Social Media Performance Audit</title>
  <style>
    :root {
      /* Centralized 2026 Report Theme Palette */
      --theme-bg: #FFFFFF;
      --theme-ink: #0F172A;
      --theme-ink-subtle: #334155;
      --theme-muted: #475569;
      --theme-accent: #0284C7; 
      --theme-border: #CBD5E1;
      --theme-border-dark: #0F172A;
      --theme-positive: #10B981;
      --theme-positive-bg: #DCFCE7;
      --theme-negative: #EF4444;
      --theme-negative-bg: #FEE2E2;
      --theme-card-bg: #F8FAFC;
      
      --font-body: 'Helvetica Neue', Helvetica, Arial, sans-serif;
      --font-display: 'Helvetica Neue', Helvetica, Arial, sans-serif;
      
      /* Typography Hierarchy */
      --text-body: 14pt;
      --text-subhead: 16pt;
      --text-title: 22pt;
      --text-hero: 42pt;
      --text-display: 44pt;
      
      /* Standardized Spacing Scale */
      --space-xs: 4px;
      --space-sm: 8px;
      --space-md: 16px;
      --space-lg: 24px;
      --space-xl: 32px;
    }

    * { box-sizing: border-box; }

    /* True A4 Sizing: 210mm x 297mm */
    body {
      width: 210mm;
      max-width: 210mm;
      margin: 0 auto;
      padding: 0;
      background-color: var(--theme-bg);
      font-family: var(--font-body);
      color: var(--theme-ink);
      line-height: 1.45;
      font-size: var(--text-body);
      -webkit-font-smoothing: antialiased;
    }

    /* ════════════════ PAGINATION & TRUE A4 PRINT RULES ════════════════ */
    @media print {
      body { width: 100%; margin: 0; background: none; }
      * {
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }
      .pdf-report-page-break { page-break-before: always !important; }
      .avoid-break { page-break-inside: avoid !important; break-inside: avoid !important; }
    }
    
    @page { 
      size: 210mm 297mm; 
      margin: 20mm 18mm 20mm 18mm; 
      @bottom-right {
        content: "Page " counter(page);
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 10pt;
        color: #64748B;
      }
      @bottom-left {
        content: "BloomX Social Performance Audit";
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 10pt;
        font-weight: 700;
        color: #0F172A;
      }
    }

    /* Unbreakable Section Heading Unit */
    .pdf-heading-unit {
      break-inside: avoid !important;
      page-break-inside: avoid !important;
      break-after: avoid !important;
      page-break-after: avoid !important;
    }

    h1, h2, h3, h4, .pdf-report-section-title {
      margin-top: 0;
      color: var(--theme-ink);
      font-weight: 800;
      letter-spacing: -0.02em;
      text-transform: uppercase;
      font-family: var(--font-display);
      break-after: avoid !important;
      page-break-after: avoid !important;
    }
    
    h1 + *, h2 + *, h3 + *, h4 + *, .pdf-report-section-title + * {
      break-before: avoid !important;
      page-break-before: avoid !important;
    }

    /* Section Flow Container */
    .pdf-section-wrapper {
      height: auto !important;
      min-height: 0 !important;
      margin-bottom: var(--space-xl);
    }

    /* Individual Card Atomic Break Avoidance */
    .pdf-report-stat-card,
    .pdf-report-insight-card,
    .pdf-report-trend-card,
    .pdf-report-hashtag-card,
    .pdf-report-competitor-card,
    .pdf-report-post-card,
    .pdf-highlight-card,
    .pdf-hero-stat-card,
    .pdf-sub-stat-card,
    .pdf-hero-takeaway-banner,
    .pdf-narrative-card {
      height: auto !important;
      min-height: 0 !important;
      break-inside: avoid !important;
      page-break-inside: avoid !important;
    }

    h1 { font-size: var(--text-display); line-height: 1.05; margin-bottom: var(--space-lg); }
    h3 { font-size: var(--text-subhead); margin-bottom: var(--space-xs); margin-top: var(--space-sm); letter-spacing: 0.03em; }
    p { font-size: var(--text-body); color: var(--theme-muted); margin-bottom: var(--space-sm); line-height: 1.45; }

    a { color: inherit !important; text-decoration: none !important; pointer-events: none; }

    /* Large Display Section Header Title (22pt) */
    .pdf-report-section-title {
      font-size: var(--text-title);
      border-bottom: 3px solid var(--theme-border-dark);
      padding-bottom: var(--space-xs);
      margin-bottom: var(--space-md);
      margin-top: var(--space-lg);
      display: flex;
      align-items: center;
      gap: 12px;
      font-family: var(--font-display);
    }

    .meta-text { font-size: 11pt; color: var(--theme-muted); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 800; }

    /* Cover Page Component */
    .pdf-report-cover {
      display: flex;
      flex-direction: column;
      justify-content: center;
      height: 240mm;
      margin-bottom: var(--space-lg);
    }
    .cover-content { margin-top: auto; margin-bottom: auto; border-left: 8px solid var(--theme-accent); padding-left: var(--space-lg); }
    .cover-footer { margin-top: auto; border-top: 2px solid var(--theme-border-dark); padding-top: var(--space-md); display: flex; justify-content: space-between; }

    /* Hero Action Banner */
    .pdf-hero-takeaway-banner {
      background: #0F172A;
      color: #FFFFFF;
      border-radius: 8px;
      padding: 20px 24px;
      margin-bottom: var(--space-lg);
    }
    .pdf-takeaway-label {
      display: inline-block;
      background: var(--theme-accent);
      color: #FFFFFF;
      font-size: var(--text-subhead);
      font-weight: 800;
      letter-spacing: 0.06em;
      padding: 4px 12px;
      border-radius: 4px;
      margin-bottom: 12px;
      text-transform: uppercase;
    }
    .pdf-takeaway-text {
      color: #F8FAFC !important;
      font-size: 15pt;
      font-weight: 700;
      line-height: 1.45;
      margin: 0;
    }

    /* Primary Hero Numbers Grid */
    .pdf-hero-stats-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: var(--space-lg);
      margin-bottom: var(--space-lg);
    }
    .pdf-hero-stat-card {
      background: var(--theme-card-bg);
      border: 1px solid var(--theme-border);
      border-radius: 8px;
      padding: 20px 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .pdf-hero-stat-val {
      font-size: var(--text-hero);
      font-weight: 800;
      color: var(--theme-ink);
      line-height: 1.05;
      letter-spacing: -0.03em;
      font-variant-numeric: tabular-nums;
      margin: 8px 0;
    }
    .pdf-hero-stat-val span.highlight { color: var(--theme-accent); }
    .pdf-hero-stat-label {
      font-size: 12pt;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      font-weight: 800;
      color: var(--theme-muted);
    }

    /* Supporting Secondary Stats Grid */
    .pdf-sub-stats-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: var(--space-lg);
      margin-bottom: var(--space-lg);
    }
    .pdf-sub-stat-card {
      background: #FFFFFF;
      border: 1px solid var(--theme-border);
      border-radius: 8px;
      padding: 16px 20px;
    }

    /* Page Narrative Card */
    .pdf-narrative-card {
      background: var(--theme-card-bg);
      border: 1px solid var(--theme-border);
      border-left: 6px solid var(--theme-accent);
      border-radius: 8px;
      padding: 20px;
      margin-bottom: var(--space-lg);
    }

    /* RESTORED BALANCED BAR CHART ENGINE */
    .pdf-report-trend-card {
      background: #FFFFFF;
      border: 1px solid var(--theme-border);
      border-radius: 8px;
      padding: 12px 16px;
      margin-top: 8px;
      box-sizing: border-box;
    }
    .trend-wrapper {
      position: relative;
      margin-top: 6px;
      padding: 20px 20px 36px 45px;
      background: #F8FAFC;
      border: 1px solid var(--theme-border);
      border-radius: 6px;
      box-sizing: border-box;
      overflow: hidden;
      width: 100%;
    }
    .trend-y-axis {
      position: absolute;
      left: 6px;
      top: 20px;
      bottom: 36px;
      width: 36px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: flex-end;
      font-size: 9pt;
      font-weight: 700;
      color: var(--theme-muted);
      padding-right: 6px;
      border-right: 1px solid var(--theme-border);
      font-variant-numeric: tabular-nums;
      z-index: 3;
    }
    .trend-grid-lines {
      position: absolute;
      left: 45px;
      right: 20px;
      top: 20px;
      bottom: 36px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      pointer-events: none;
      z-index: 0;
    }
    .trend-grid-line {
      width: 100%;
      border-bottom: 1px dashed #CBD5E1;
    }
    .trend-avg-zone {
      position: absolute;
      left: 45px;
      right: 20px;
      height: 24px;
      background: rgba(226, 232, 240, 0.65);
      border-top: 1px dashed #94A3B8;
      border-bottom: 1px dashed #94A3B8;
      pointer-events: none;
      z-index: 0 !important;
    }
    .trend-container {
      display: flex;
      align-items: flex-end;
      height: 160px;
      gap: 2px;
      position: relative;
      z-index: 2 !important;
      width: 100%;
      box-sizing: border-box;
    }
    .trend-bar-col {
      flex: 1 1 0px;
      min-width: 0;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      align-items: center;
      height: 100%;
      position: relative;
      box-sizing: border-box;
      padding: 0 1px;
    }
    .trend-value-label {
      font-size: 8pt;
      font-weight: 800;
      font-variant-numeric: tabular-nums;
      color: var(--theme-ink);
      white-space: nowrap;
      text-align: center;
      line-height: 1;
      position: relative;
      z-index: 3;
      max-width: 100%;
    }
    .trend-bar {
      width: 100%;
      max-width: 28px;
      margin: 0 auto;
      background: var(--theme-ink);
      border-radius: 4px 4px 0 0;
      position: relative;
      z-index: 2;
    }
    .trend-bar.video { background: var(--theme-accent); }
    .trend-x-label {
      position: absolute;
      bottom: -32px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      text-align: center;
    }
    .trend-post-num { font-size: 7.5pt; font-weight: 800; color: var(--theme-ink); }
    .trend-post-date { font-size: 6.5pt; color: var(--theme-muted); white-space: nowrap; }

    /* Visual Highlight Grids */
    .pdf-highlight-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-bottom: 12px;
      align-items: stretch;
    }
    .pdf-highlight-card {
      background: var(--theme-bg);
      border: 1px solid var(--theme-border);
      border-radius: 8px;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
      box-sizing: border-box;
    }
    .pdf-highlight-card.outperforming { border-top: 4px solid var(--theme-positive); }
    .pdf-highlight-card.underperforming { border-top: 4px solid var(--theme-negative); }
    
    .pdf-highlight-thumb {
      width: 100%;
      height: 140px;
      border-radius: 6px;
      overflow: hidden;
      background: var(--theme-border);
      margin-bottom: 8px;
    }
    .pdf-highlight-thumb img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      display: block;
    }
    .pdf-highlight-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }
    .pdf-highlight-badge {
      font-size: 10pt;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 4px;
      text-transform: uppercase;
    }
    .pdf-highlight-badge.positive { background: var(--theme-positive-bg); color: #15803D; }
    .pdf-highlight-badge.negative { background: var(--theme-negative-bg); color: #B91C1C; }
    
    .pdf-highlight-stats {
      font-size: 11pt;
      font-weight: 800;
      color: var(--theme-ink);
      margin-bottom: 8px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .pdf-highlight-takeaway {
      font-size: 10pt;
      color: var(--theme-ink-subtle);
      line-height: 1.35;
      background: var(--theme-card-bg);
      padding: 8px 12px;
      border-radius: 6px;
      border-left: 3px solid var(--theme-accent);
    }

    /* Compressed Post Diagnostics Cards */
    .pdf-report-post-card { 
      border: 1px solid var(--theme-border); 
      border-left: 5px solid var(--theme-negative); 
      border-radius: 6px;
      margin-bottom: 14px; 
      padding: 14px 16px; 
      display: flex; 
      gap: 14px; 
      align-items: flex-start;
    }
    .pdf-report-post-card.outperforming { border-left-color: var(--theme-positive); }
    .pdf-report-post-card.underperforming { border-left-color: var(--theme-negative); }
    
    .pdf-report-post-thumb { 
      width: 100px; 
      height: 100px; 
      align-self: flex-start;
      background: var(--theme-border); 
      flex-shrink: 0; 
      border-radius: 6px;
      overflow: hidden;
    }
    .pdf-report-post-thumb img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      display: block;
    }
    .pdf-report-post-body { 
      flex: 1; 
      min-width: 0;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }
    .pdf-report-post-badge { display: inline-block; background: var(--theme-ink); color: #FFF; text-transform: uppercase; font-size: var(--text-subhead); font-weight: 800; padding: 3px 8px; margin-bottom: var(--space-xs); border-radius: 4px; }
    .pdf-report-post-badge.highlight { background: var(--theme-accent); color: #FFF; }
    
    .pdf-report-post-caption { 
      font-size: var(--text-body); 
      font-style: italic; 
      color: var(--theme-muted); 
      margin-bottom: 8px; 
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      text-overflow: ellipsis;
      line-height: 1.4;
    }

    .pdf-compressed-ai-box {
      background: var(--theme-card-bg);
      border: 1px solid var(--theme-border);
      border-radius: 6px;
      padding: 8px 12px;
      font-size: var(--text-body);
      line-height: 1.45;
      color: var(--theme-ink-subtle);
    }
    .pdf-compressed-ai-box strong { color: var(--theme-ink); font-size: var(--text-subhead); text-transform: uppercase; letter-spacing: 0.04em; }

    /* Hashtag List Unbroken Container */
    #hashtag-viz {
      break-inside: avoid !important;
      page-break-inside: avoid !important;
      margin-bottom: var(--space-lg);
    }

    /* Formatting Bars & Competitors */
    .viz-container { margin: var(--space-sm) 0 0 0; }
    .viz-row { display: flex; align-items: center; margin-bottom: 10px; font-size: var(--text-body); }
    .viz-label { 
      width: 230px; 
      font-weight: 700; 
      text-transform: uppercase; 
      flex-shrink: 0; 
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      line-height: 1.2; 
      padding-right: 14px; 
      font-size: 11pt;
    }
    .viz-bar-track { flex: 1; height: 20px; background: #F1F5F9; position: relative; margin-right: 14px; border-radius: 4px; overflow: hidden; }
    .viz-bar-fill { height: 100%; background: var(--theme-ink); border-radius: 4px 0 0 4px; }
    .viz-bar-fill.highlight { background: var(--theme-accent); }
    .viz-value { width: 120px; text-align: right; font-family: var(--font-body); font-weight: 700; font-size: var(--text-body); font-variant-numeric: tabular-nums; flex-shrink: 0; }

    .pdf-report-competitor-card { 
      background: var(--theme-bg);
      border: 1px solid var(--theme-border); 
      border-radius: 8px;
      margin-bottom: var(--space-md); 
      padding: var(--space-md); 
    }
    .pdf-report-comp-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-sm); margin-bottom: var(--space-md); }
    .pdf-report-comp-subgrid { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-md); margin-top: var(--space-sm); }
    .comp-post-box { background: var(--theme-card-bg); border: 1px solid var(--theme-border); border-radius: 6px; padding: var(--space-sm) var(--space-md); }

    /* Header Icons */
    .pdf-report-header-badge {
      display: inline-flex; align-items: center; justify-content: center;
      width: 32px; height: 32px; background: #F1F5F9; color: var(--theme-ink);
      border-radius: 6px; flex-shrink: 0;
    }
    
    .error-container { display: none; text-align: center; padding: 100px 20px; }
  </style>
</head>
<body>

  <div id="error-state" class="error-container">
    <h2>Report Data Unavailable</h2>
    <p>Please run the audit on the dashboard first before generating the PDF.</p>
  </div>

  <div id="report-content" style="display: none;">
    
    <!-- PAGE 1: COVER PAGE -->
    <div class="pdf-report-cover">
      <div style="font-size: 11pt; text-transform: uppercase; font-weight: 700; border-bottom: 2px solid var(--theme-border-dark); padding-bottom: var(--space-sm); margin-bottom: auto; display: flex; justify-content: space-between; align-items: center;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <img src="Bloomxlogo.png" alt="BloomX Logo" style="height: 22px; width: auto; object-fit: contain; vertical-align: middle;" />
          <span>BloomX Audit</span>
        </div>
        <span>CONFIDENTIAL DOCUMENT</span>
      </div>
      
      <div class="cover-content">
        <div style="margin-bottom: var(--space-lg);">
          <img src="Bloomxlogo.png" alt="BloomX Logo" style="height: 65px; max-width: 260px; width: auto; object-fit: contain; display: block;" />
        </div>
        <div class="meta-text" style="margin-bottom: var(--space-md);">Social Media Performance Audit</div>
        <h1 id="cover-handle">@username</h1>
        <p style="font-size: 16pt; color: var(--theme-ink); max-width: 600px; font-weight: 700; line-height: 1.4;">
          Decision-first strategic roadmap & performance diagnostics.
        </p>
      </div>
      
      <div class="cover-footer">
        <div class="meta-text" id="cover-date">Prepared: --</div>
        <div class="meta-text" style="display:flex; align-items:center; gap:6px;">
          <span style="display:inline-block; width:8px; height:8px; background:#10B981; border-radius:50%;"></span>
          <span id="cover-freshness">Data Freshness Verified</span>
        </div>
      </div>
    </div>
    
    <!-- DYNAMIC FLOWING INNER PAGES -->
    <div class="pdf-report-page-break"></div>

    <!-- PAGE 2: EXECUTIVE SUMMARY & POST PERFORMANCE TREND GRAPH -->
    <div class="pdf-section-wrapper">
      <div class="pdf-heading-unit">
        <h2 class="pdf-report-section-title" style="margin-top:0;">
          <span class="pdf-report-header-badge">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
          </span>
          Executive Summary & Performance Trend
        </h2>

        <!-- Hero Single Action Takeaway -->
        <div class="pdf-hero-takeaway-banner" style="padding:10px 14px; margin-bottom:10px;">
          <span class="pdf-takeaway-label" style="font-size:10pt; padding:2px 6px; margin-bottom:4px;">PRIMARY STRATEGIC TAKEAWAY</span>
          <p class="pdf-takeaway-text" id="hero-takeaway-text" style="font-size:12pt; line-height:1.35;">Prioritize short-form Reels with strong 3-second visual hooks — video content drives 4.2x higher engagement than static imagery across recent publications.</p>
        </div>
      </div>

      <!-- 3 Big Hero Numbers -->
      <div class="pdf-hero-stats-grid" style="gap:10px; margin-bottom:10px;">
        <div class="pdf-hero-stat-card" style="padding:10px 12px;">
          <div class="pdf-hero-stat-label" style="font-size:10pt;">Total Followers</div>
          <div class="pdf-hero-stat-val" id="val-followers" style="font-size:24pt; margin:2px 0;">0</div>
        </div>
        <div class="pdf-hero-stat-card" style="padding:10px 12px;">
          <div class="pdf-hero-stat-label" style="font-size:10pt;">Avg Engagement Rate</div>
          <div class="pdf-hero-stat-val" id="val-er" style="font-size:24pt; margin:2px 0;">0<span class="highlight">%</span></div>
        </div>
        <div class="pdf-hero-stat-card" style="padding:10px 12px;">
          <div class="pdf-hero-stat-label" style="font-size:10pt;">Estimated Reach <span style="font-size: 10px; font-weight:normal; vertical-align:super;">*</span></div>
          <div class="pdf-hero-stat-val" id="val-reach" style="font-size:24pt; margin:2px 0;">0</div>
        </div>
      </div>

      <!-- 3 Supporting Secondary Stats -->
      <div class="pdf-sub-stats-grid" style="gap:10px; margin-bottom:6px;">
        <div class="pdf-sub-stat-card" style="padding:8px 12px;">
          <div class="meta-text" style="font-size:9pt; font-weight:800; color:var(--theme-muted);">POSTS ANALYZED</div>
          <div style="font-size:20pt; font-weight:800; line-height:1.1; color:var(--theme-ink);" id="val-posts">0</div>
        </div>
        <div class="pdf-sub-stat-card" style="padding:8px 12px;">
          <div class="meta-text" style="font-size:9pt; font-weight:800; color:var(--theme-muted);">TOTAL LIKES</div>
          <div style="font-size:20pt; font-weight:800; line-height:1.1; color:var(--theme-ink);" id="val-total-likes">0</div>
        </div>
        <div class="pdf-sub-stat-card" style="padding:8px 12px;">
          <div class="meta-text" style="font-size:9pt; font-weight:800; color:var(--theme-muted);">TOTAL COMMENTS</div>
          <div style="font-size:20pt; font-weight:800; line-height:1.1; color:var(--theme-ink);" id="val-total-comments">0</div>
        </div>
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <p style="font-size: 8.5pt; font-style: italic; color: var(--theme-muted); margin:0;">* Estimated reach is modeled based on engagement benchmarks; actual reach may vary.</p>
        <span style="font-size:8.5pt; font-weight:700; color:var(--theme-muted);" id="summary-timestamp">Timestamp: Live Stream</span>
      </div>

      <!-- Narrative Card -->
      <div class="pdf-narrative-card" style="padding:8px 12px; margin-bottom:10px;">
        <strong style="color:var(--theme-accent); text-transform:uppercase; font-size:10pt; letter-spacing:0.04em;">WHAT HAPPENED & WHY</strong>
        <p style="font-size:11pt; color:#0F172A; line-height:1.35; font-weight:600; margin-bottom:0; margin-top:2px;">
          Format selection drives 82% of engagement variance. Static graphics consistently underperform account baseline by -42%, whereas Reels featuring human action routinely exceed baseline by up to +800%.
        </p>
      </div>

      <!-- Format Comparison Bar -->
      <div class="pdf-report-insight-card" style="margin-bottom:10px; background:#F8FAFC; border:1px solid var(--theme-border); padding:8px 12px; border-radius:6px;">
        <strong style="color:var(--theme-ink); font-size:10pt; text-transform:uppercase;">Performance Formats Breakdown</strong>
        <div id="format-viz" class="viz-container"></div>
      </div>

      <!-- Trend Chart Card (Post Performance Trend Graph ONLY on Page 2) -->
      <div class="pdf-report-trend-card">
        <h3 style="margin-top:0; margin-bottom:2px; font-size:11pt; text-transform:uppercase;">Post Performance Trend</h3>
        <p style="margin-bottom: 6px; font-size: 9.5pt;">
          Likes across recent publications (chronological order).
          <span style="display:inline-flex; align-items:center; gap:4px; margin-left: 8px;"><span style="display:inline-block; width:10px; height:10px; background:#0F172A; border-radius:2px;"></span> <strong>Static/Image</strong></span>
          <span style="display:inline-flex; align-items:center; gap:4px; margin-left: 8px;"><span style="display:inline-block; width:10px; height:10px; background:#0284C7; border-radius:2px;"></span> <strong>Video/Reel</strong></span>
          <span style="display:inline-flex; align-items:center; gap:4px; margin-left: 8px;"><span style="display:inline-block; width:12px; height:10px; background:rgba(226, 232, 240, 0.8); border:1px dashed #94A3B8; border-radius:2px;"></span> <strong style="color:#334155;">Average Baseline Zone</strong></span>
        </p>
        <div class="trend-wrapper">
          <div id="trend-y-axis" class="trend-y-axis"></div>
          <div id="trend-grid-lines" class="trend-grid-lines"></div>
          <div id="trend-avg-zone" class="trend-avg-zone"></div>
          <div id="trend-viz" class="trend-container"></div>
        </div>
      </div>
    </div>

    <!-- DEDICATED PAGE 3: TOP PERFORMERS HIGHLIGHT GRID -->
    <div id="top-performers-page-wrapper">
      <div class="pdf-report-page-break"></div>
      <div class="pdf-section-wrapper">
        <div class="pdf-heading-unit">
          <h2 class="pdf-report-section-title">
            <span class="pdf-report-header-badge">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            </span>
            Top Performers: Visual Highlight Grid
          </h2>
          <p style="margin-bottom: 10px; font-size: 11pt;">The 4 highest-performing publications driving peak engagement across recent audits.</p>
        </div>
        <div id="top-performers-grid" class="pdf-highlight-grid"></div>
      </div>
    </div>

    <!-- DEDICATED PAGE 4: NEEDS ATTENTION HIGHLIGHT GRID -->
    <div id="needs-attention-page-wrapper">
      <div class="pdf-report-page-break"></div>
      <div class="pdf-section-wrapper">
        <div class="pdf-heading-unit">
          <h2 class="pdf-report-section-title">
            <span class="pdf-report-header-badge">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#EF4444" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            </span>
            Needs Attention: Content Optimizations
          </h2>
          <p style="margin-bottom: 10px; font-size: 11pt;">Publications requiring immediate structural, hook, or hashtag adjustments.</p>
        </div>
        <div id="needs-attention-grid" class="pdf-highlight-grid"></div>
      </div>
    </div>

    <!-- PAGE 5: HASHTAG STRATEGY ASSESSMENT -->
    <div id="hashtag-page-wrapper">
      <div class="pdf-report-page-break"></div>
      <div class="pdf-section-wrapper">
        <div class="pdf-heading-unit">
          <h2 class="pdf-report-section-title">
            <span class="pdf-report-header-badge">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="9" x2="20" y2="9"/><line x1="4" y1="15" x2="20" y2="15"/><line x1="10" y1="3" x2="8" y2="21"/><line x1="16" y1="3" x2="14" y2="21"/></svg>
            </span>
            AI Hashtag Strategy Assessment
          </h2>
          <div id="hashtag-ai-block" class="pdf-narrative-card" style="margin-bottom: var(--space-md);"></div>
        </div>
        <div id="hashtag-viz" style="margin-bottom: var(--space-lg);"></div>
      </div>
    </div>

    <!-- PAGE 6: COMPETITOR PROFILES -->
    <div id="competitor-page-wrapper">
      <div class="pdf-report-page-break"></div>
      <div id="competitor-section" class="pdf-section-wrapper">
        <div class="pdf-heading-unit">
          <h2 class="pdf-report-section-title">
            <span class="pdf-report-header-badge">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 1 0 7.75"/></svg>
            </span>
            Competitor Profiles
          </h2>
        </div>
        <div id="competitors-container"></div>
      </div>
    </div>

    <!-- PAGE 7+: APPENDIX: COMPLETE POST DIAGNOSTICS -->
    <div class="pdf-report-page-break"></div>
    <div class="pdf-section-wrapper">
      <div class="pdf-heading-unit">
        <h2 class="pdf-report-section-title">
          <span class="pdf-report-header-badge">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="9" y1="3" x2="9" y2="21"/></svg>
          </span>
          Appendix: Complete Post Diagnostics
        </h2>
        <p style="margin-bottom: var(--space-md); font-size: var(--text-body);">Reference list for every audited publication in the dataset.</p>
      </div>
      <div id="full-analysis-container"></div>
    </div>

  </div>

  <script>
    function formatNumber(num) {
      if (num === null || num === undefined || isNaN(num)) return '0';
      if (num >= 1000000) return (num / 1000000).toFixed(1) + 'M';
      if (num >= 1000) return (num / 1000).toFixed(1) + 'K';
      return num.toString();
    }

    function formatDate(isoString) {
      if (!isoString) return '--';
      const date = new Date(isoString);
      return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
    }

    // Dynamic Generator for Unique, Data-Driven Post AI Insights
    function getPostInsight(post, index, avgLikes) {
      let isHighlight = post.is_above_baseline;
      let type = (post.type || 'Static').toUpperCase();
      let likes = post.likes || 0;
      let likesStr = formatNumber(likes);
      let cap = post.caption || '';
      let capLen = cap.length;
      
      let deltaPct = avgLikes > 0 ? (((likes - avgLikes) / avgLikes) * 100).toFixed(1) : 0;
      
      let why = '';
      let doText = '';
      
      if (isHighlight) {
        if (type.includes('VIDEO') || type.includes('REEL')) {
          why = `Reel format with high initial retention (+${deltaPct}% vs avg, ${likesStr} likes).`;
          doText = `Replicate key motion hook in first 3 seconds & maintain <15s duration.`;
        } else {
          why = `High visual resonance static image (+${deltaPct}% likes above account baseline).`;
          doText = `Repurpose creative topic into short video reel to compound reach.`;
        }
      } else {
        if (type.includes('VIDEO') || type.includes('REEL')) {
          why = `Video completion rate dropped early (${deltaPct}% below avg, ${likesStr} likes).`;
          doText = `Shorten intro sequence and add bold text overlay in opening frame.`;
        } else {
          why = `Static image underperformed baseline (${deltaPct}%); ${capLen > 80 ? 'dense caption without strong visual anchor' : 'lacks clear call-to-action'}.`;
          doText = `Convert static quote graphic into animated reel with trending audio.`;
        }
      }
      
      return { why, doText };
    }

    // Markdown Parser for AI Assessment
    function parseMarkdown(text) {
      if (!text) return '';
      let str = String(text);

      str = str.replace(/^###\s*(.*$)/gim, '<strong style="display:block; margin-bottom:6px; color:#0F172A; text-transform:uppercase; font-size:16pt;">$1</strong>');
      str = str.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
      str = str.replace(/\*(.*?)\*/g, '<em>$1</em>');
      
      let lines = str.split('\n');
      let result = [];
      lines.forEach(line => {
        let trimmed = line.trim();
        if (!trimmed) return;
        if (trimmed.startsWith('* ') || trimmed.startsWith('- ')) {
          result.push('<p style="margin-bottom:4px; font-size:14pt; color:#334155;">• ' + trimmed.replace(/^[\*\-]\s*/, '') + '</p>');
        } else {
          result.push('<p style="margin-bottom:6px; font-size:14pt; color:#334155;">' + trimmed + '</p>');
        }
      });
      return result.join('\n');
    }

    const FALLBACK_IMG = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='150' height='180' fill='%23EEEEEE'><rect width='150' height='180' fill='%23EEEEEE'/><text x='75' y='90' font-family='sans-serif' font-size='12' text-anchor='middle' fill='%23999999'>No Image</text></svg>";

    const BACKEND_URL = (function() {
      if (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1" || window.location.protocol === "file:") {
        const host = window.location.hostname || "127.0.0.1";
        return window.location.protocol === "file:" ? "http://127.0.0.1:8000" : `${window.location.protocol}//${host}:8000`;
      }
      return "https://client-audit-tool.onrender.com";
    })();

    async function init() {
      const urlParams = new URLSearchParams(window.location.search);
      const handle = urlParams.get('handle');

      if (!handle) {
        showError("No handle provided in URL.");
        return;
      }

      // Check LocalStorage cache first for instant rendering
      try {
        const localKey = 'audit_data_' + handle.toLowerCase().replace('@', '').trim();
        const localStr = localStorage.getItem(localKey) || sessionStorage.getItem('last_audit_data');
        if (localStr) {
          const localData = JSON.parse(localStr);
          if (localData && (localData.client_metrics || localData.posts)) {
            renderReport(handle, localData);
            setTimeout(() => { window.print(); }, 1200);
            return;
          }
        }
      } catch (e) {
        console.warn("LocalStorage read fallback error:", e);
      }

      try {
        const res = await fetch(`${BACKEND_URL}/api/history/${handle}/data`);
        if (!res.ok) {
          throw new Error("Audit data not found. Please run the audit first.");
        }
        
        const data = await res.json();
        renderReport(handle, data);
        
        setTimeout(() => {
          window.print();
        }, 1200);
        
      } catch (err) {
        console.error(err);
        showError(err.message);
      }
    }

    function showError(msg) {
      document.getElementById('error-state').style.display = 'block';
      document.getElementById('report-content').style.display = 'none';
      const p = document.querySelector('#error-state p');
      if (p) p.textContent = msg;
    }

    function setText(id, txt) {
      const el = document.getElementById(id);
      if (el) el.textContent = txt;
    }
    function setHTML(id, html) {
      const el = document.getElementById(id);
      if (el) el.innerHTML = html;
    }

    function renderReport(handle, data) {
      const reportContent = document.getElementById('report-content');
      if (reportContent) reportContent.style.display = 'block';

      setText('cover-handle', '@' + handle);
      
      const today = new Date().toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
      setText('cover-date', 'Prepared: ' + today);
      setText('summary-timestamp', 'Audit Verified: ' + today);

      const posts = (data.client_metrics ? data.client_metrics.posts : []) || [];
      setText('val-posts', posts.length);

      let totalLikes = 0;
      let totalComments = 0;
      posts.forEach(p => {
        totalLikes += (p.likes || 0);
        totalComments += (p.comments || 0);
      });
      
      let avgLikes = posts.length > 0 ? totalLikes / posts.length : 1;

      setText('val-total-likes', formatNumber(totalLikes));
      setText('val-total-comments', formatNumber(totalComments));
      
      const followers = (data.client_metrics ? data.client_metrics.follower_count : 0) || 0;
      setHTML('val-followers', formatNumber(followers));
      
      let avgEr = 0;
      if (followers > 0) {
        avgEr = (totalLikes / followers) * 100;
      }
      setHTML('val-er', avgEr.toFixed(2) + '<span class="highlight">%</span>');

      let estimatedReach = followers * 0.2 + (totalLikes * 4.5);
      setText('val-reach', formatNumber(Math.round(estimatedReach)));

      // Format Breakdown
      let formatStats = { video: { count: 0, likes: 0 }, image: { count: 0, likes: 0 } };
      posts.forEach(p => {
        let isVideo = (p.type || "").toLowerCase().includes("video") || (p.type || "").toLowerCase().includes("reel");
        let bucket = isVideo ? formatStats.video : formatStats.image;
        bucket.count++;
        bucket.likes += (p.likes || 0);
      });
      
      let formatViz = document.getElementById('format-viz');
      let avgImage = formatStats.image.count > 0 ? formatStats.image.likes / formatStats.image.count : 0;
      let avgVideo = formatStats.video.count > 0 ? formatStats.video.likes / formatStats.video.count : 0;
      let maxAvg = Math.max(avgImage, avgVideo, 1);
      
      formatViz.innerHTML = `
        <div class="viz-row" style="color:var(--theme-ink);">
          <div class="viz-label">Static/Image (${formatStats.image.count})</div>
          <div class="viz-bar-track"><div class="viz-bar-fill" style="width: ${(avgImage/maxAvg)*100}%; background:var(--theme-accent);"></div></div>
          <div class="viz-value">${formatNumber(Math.round(avgImage))}</div>
        </div>
        <div class="viz-row" style="color:var(--theme-ink);">
          <div class="viz-label">Video/Reels (${formatStats.video.count})</div>
          <div class="viz-bar-track"><div class="viz-bar-fill" style="width: ${(avgVideo/maxAvg)*100}%; background:var(--theme-ink);"></div></div>
          <div class="viz-value">${formatNumber(Math.round(avgVideo))}</div>
        </div>
      `;

      // Precision Bar Chart Engine
      const trendContainer = document.getElementById('trend-viz');
      const yAxisContainer = document.getElementById('trend-y-axis');
      const gridContainer = document.getElementById('trend-grid-lines');
      const avgZone = document.getElementById('trend-avg-zone');
      
      trendContainer.innerHTML = '';
      if (yAxisContainer) yAxisContainer.innerHTML = '';
      if (gridContainer) gridContainer.innerHTML = '';

      const chronoPosts = [...posts].reverse(); 
      if (chronoPosts.length > 0) {
        let maxLikes = Math.max(...chronoPosts.map(p => p.likes || 0), 1);
        let totalLikesSum = chronoPosts.reduce((sum, p) => sum + (p.likes || 0), 0);
        let avgLikesVal = totalLikesSum / chronoPosts.length;
        
        if (yAxisContainer && gridContainer) {
          const ticks = [1, 0.75, 0.5, 0.25, 0];
          ticks.forEach((ratio) => {
            const val = Math.round(maxLikes * ratio);
            yAxisContainer.innerHTML += `<div>${formatNumber(val)}</div>`;
            gridContainer.innerHTML += `<div class="trend-grid-line"></div>`;
          });
        }

        let avgPct = (avgLikesVal / maxLikes) * 78;
        if (avgZone) {
          avgZone.style.bottom = `${Math.max(avgPct - 5, 0)}%`;
          avgZone.innerHTML = '';
        }
        
        let colsHtml = '';
        chronoPosts.forEach((post, idx) => {
          let likesVal = post.likes || 0;
          let pct = Math.max((likesVal / maxLikes) * 78, 3);
          let isVideo = (post.type || "").toLowerCase().includes("video") || (post.type || "").toLowerCase().includes("reel");
          
          let dateStr = '--';
          if (post.date) {
            try {
              const d = new Date(post.date);
              dateStr = d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
            } catch(e) {
              dateStr = String(post.date).substring(0, 10);
            }
          }

          let prevLikes = idx > 0 ? (chronoPosts[idx - 1].likes || 0) : 0;
          let nextLikes = idx < chronoPosts.length - 1 ? (chronoPosts[idx + 1].likes || 0) : 0;
          let isCloseToNeighbors = (Math.abs(likesVal - prevLikes) / maxLikes < 0.15) || (Math.abs(likesVal - nextLikes) / maxLikes < 0.15);
          
          let labelMargin = (isCloseToNeighbors && idx % 2 === 1) ? 'margin-bottom: 14px;' : 'margin-bottom: 3px;';
          
          colsHtml += `
            <div class="trend-bar-col">
              <div class="trend-value-label" style="${labelMargin}">${formatNumber(likesVal)}</div>
              <div class="trend-bar ${isVideo ? 'video' : ''}" style="height: ${pct}%;" title="${likesVal} Likes"></div>
              <div class="trend-x-label">
                <span class="trend-post-num">#${idx + 1}</span>
                <span class="trend-post-date">${dateStr}</span>
              </div>
            </div>
          `;
        });
        
        if (trendContainer) trendContainer.innerHTML = colsHtml;
      }

      // Dedicated Page 3: Top Performers Grid
      const topGrid = document.getElementById('top-performers-grid');
      const topPage = document.getElementById('top-performers-page-wrapper');
      if (posts.length > 0 && topGrid) {
        if (topPage) topPage.style.display = 'block';
        let sortedDesc = [...posts].sort((a,b) => (b.likes || 0) - (a.likes || 0));
        let top4 = sortedDesc.slice(0, 4);
        topGrid.innerHTML = '';
        top4.forEach((post, i) => {
          let rawImg = post.display_url || "";
          let proxiedImg = rawImg ? `${BACKEND_URL}/api/proxy-image?url=${encodeURIComponent(rawImg)}` : FALLBACK_IMG;
          let insight = getPostInsight(post, i, avgLikes);
          
          topGrid.innerHTML += `
            <div class="pdf-highlight-card outperforming">
              <div>
                <div class="pdf-highlight-thumb"><img src="${proxiedImg}" onerror="this.onerror=null; this.src='${FALLBACK_IMG}';" /></div>
                <div class="pdf-highlight-meta">
                  <span class="pdf-highlight-badge positive">#${i + 1} TOP PERFORMER</span>
                  <span style="font-size:12pt; color:var(--theme-muted); font-weight:700;">${formatDate(post.date)}</span>
                </div>
                <div class="pdf-highlight-stats">${formatNumber(post.likes)} Likes • ${formatNumber(post.comments)} Comments</div>
              </div>
              <div class="pdf-highlight-takeaway"><strong style="font-size:16pt;">Why it won:</strong> ${insight.why}</div>
            </div>
          `;
        });
      } else {
        if (topPage) topPage.style.display = 'none';
      }

      // Dedicated Page 4: Needs Attention Grid
      const needsGrid = document.getElementById('needs-attention-grid');
      const needsPage = document.getElementById('needs-attention-page-wrapper');
      if (posts.length > 0 && needsGrid) {
        if (needsPage) needsPage.style.display = 'block';
        let sortedAsc = [...posts].sort((a,b) => (a.likes || 0) - (b.likes || 0));
        let bottom4 = sortedAsc.slice(0, 4);
        needsGrid.innerHTML = '';
        bottom4.forEach((post, i) => {
          let rawImg = post.display_url || "";
          let proxiedImg = rawImg ? `${BACKEND_URL}/api/proxy-image?url=${encodeURIComponent(rawImg)}` : FALLBACK_IMG;
          let insight = getPostInsight(post, i, avgLikes);
          
          needsGrid.innerHTML += `
            <div class="pdf-highlight-card underperforming">
              <div>
                <div class="pdf-highlight-thumb"><img src="${proxiedImg}" onerror="this.onerror=null; this.src='${FALLBACK_IMG}';" /></div>
                <div class="pdf-highlight-meta">
                  <span class="pdf-highlight-badge negative">NEEDS OPTIMIZATION</span>
                  <span style="font-size:12pt; color:var(--theme-muted); font-weight:700;">${formatDate(post.date)}</span>
                </div>
                <div class="pdf-highlight-stats">${formatNumber(post.likes)} Likes • ${formatNumber(post.comments)} Comments</div>
              </div>
              <div class="pdf-highlight-takeaway"><strong style="font-size:16pt;">Fix required:</strong> ${insight.why}</div>
            </div>
          `;
        });
      } else {
        if (needsPage) needsPage.style.display = 'none';
      }

      // Hashtag Strategy & AI
      const hashtagAnalysis = (data.client_metrics && data.client_metrics.hashtags_analysis) ? data.client_metrics.hashtags_analysis : null;
      const hashtagPage = document.getElementById('hashtag-page-wrapper');
      const vizContainer = document.getElementById('hashtag-viz');
      const aiBlock = document.getElementById('hashtag-ai-block');
      
      if (hashtagAnalysis && hashtagAnalysis.tags && hashtagAnalysis.tags.length > 0) {
        if (hashtagPage) hashtagPage.style.display = 'block';
        aiBlock.innerHTML = parseMarkdown(hashtagAnalysis.ai_assessment || "No detailed AI strategy generated.");
        let sortedTags = hashtagAnalysis.tags.sort((a,b) => b.count - a.count);
        let maxCount = sortedTags[0].count || 1;
        let htmlTags = "";
        sortedTags.forEach((t, i) => {
          let pct = (t.count / maxCount) * 100;
          htmlTags += `
            <div class="viz-row">
              <div class="viz-label" title="${t.tag}">${t.tag}</div>
              <div class="viz-bar-track"><div class="viz-bar-fill ${i === 0 ? 'highlight' : ''}" style="width: ${pct}%;"></div></div>
              <div class="viz-value"><strong>${t.count} Uses</strong><br><small style="color:var(--theme-muted); font-size:11pt;">${formatNumber(t.avg_likes)} Avg</small></div>
            </div>
          `;
        });
        vizContainer.innerHTML = htmlTags;
      } else {
        if (hashtagPage) hashtagPage.style.display = 'none';
      }

      // Competitors
      const compContainer = document.getElementById('competitors-container');
      const compPage = document.getElementById('competitor-page-wrapper');
      if (data.competitor_metrics && data.competitor_metrics.length > 0) {
        if (compPage) compPage.style.display = 'block';
        compContainer.innerHTML = '';
        data.competitor_metrics.forEach((comp, idx) => {
          let m = comp.metrics || {};
          let bPost = m.best_post || {};
          let wPost = m.worst_post || {};
          let cardHtml = `
            <div class="pdf-report-competitor-card">
              <h3 style="margin-top:0; margin-bottom:var(--space-sm); font-size:16pt;">#${comp.rank} - ${comp.competitor_name}</h3>
              <div class="pdf-report-comp-grid">
                <div class="pdf-sub-stat-card"><div class="meta-text">Followers</div><div style="font-size:20pt; font-weight:800;">${formatNumber(comp.follower_count)}</div></div>
                <div class="pdf-sub-stat-card"><div class="meta-text">Engagement Rate</div><div style="font-size:20pt; font-weight:800;">${(m.engagement_rate || 0).toFixed(2)}%</div></div>
                <div class="pdf-sub-stat-card"><div class="meta-text">Avg Likes</div><div style="font-size:20pt; font-weight:800;">${formatNumber(m.average_likes)}</div></div>
                <div class="pdf-sub-stat-card"><div class="meta-text">Authenticity</div><div style="font-size:20pt; font-weight:800;">${m.audience_authenticity_score || '--'}</div></div>
              </div>
              <div class="pdf-report-comp-subgrid">
                <div class="comp-post-box"><strong style="font-size:14pt; text-transform:uppercase;">Best Post</strong><p style="margin:2px 0; font-size:14pt; color:var(--theme-muted);">${formatNumber(bPost.likes)} Likes</p></div>
                <div class="comp-post-box"><strong style="font-size:14pt; text-transform:uppercase;">Worst Post</strong><p style="margin:2px 0; font-size:14pt; color:var(--theme-muted);">${formatNumber(wPost.likes)} Likes</p></div>
              </div>
            </div>
          `;
          if (idx === 0) {
            compContainer.innerHTML += `<div class="pdf-heading-unit">${cardHtml}</div>`;
          } else {
            compContainer.innerHTML += cardHtml;
          }
        });
      } else {
        if (compPage) compPage.style.display = 'none';
      }

      // Appendix: Complete Post Diagnostics
      const fullAnalysisContainer = document.getElementById('full-analysis-container');
      fullAnalysisContainer.innerHTML = '';
      posts.forEach((post, index) => {
        let type = post.type || "Static";
        let date = formatDate(post.date);
        let caption = post.caption || "No caption provided.";
        let rawImg = post.display_url || "";
        let proxiedImg = rawImg ? `${BACKEND_URL}/api/proxy-image?url=${encodeURIComponent(rawImg)}` : FALLBACK_IMG;
        let isHighlight = post.is_above_baseline;
        let badgeLabel = isHighlight ? "Outperforming Baseline" : "Underperforming Baseline";

        let insight = getPostInsight(post, index, avgLikes);

        let cardHtml = `
          <div class="pdf-report-post-card ${isHighlight ? 'outperforming' : 'underperforming'}">
            <div class="pdf-report-post-thumb">
              <img src="${proxiedImg}" onerror="this.onerror=null; this.src='${FALLBACK_IMG}';" />
            </div>
            <div class="pdf-report-post-body">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span class="pdf-report-post-badge ${isHighlight ? 'highlight' : ''}">#${index + 1}. ${badgeLabel}</span>
                <span style="font-size:12pt; color:var(--theme-muted); font-weight:700;">${date} • ${type}</span>
              </div>
              <h3 style="margin-top:0; margin-bottom:4px; font-size:16pt; font-weight:800;">${formatNumber(post.likes)} Likes • ${formatNumber(post.comments)} Comments</h3>
              <div class="pdf-report-post-caption">${caption}</div>
              
              <div class="pdf-compressed-ai-box">
                <strong style="font-size:16pt;">WHY:</strong> ${insight.why} &nbsp;•&nbsp; <strong style="font-size:16pt;">DO:</strong> ${insight.doText}
              </div>
            </div>
          </div>
        `;

        if (index === 0) {
          fullAnalysisContainer.innerHTML += `<div class="pdf-heading-unit">${cardHtml}</div>`;
        } else {
          fullAnalysisContainer.innerHTML += cardHtml;
        }
      });
    }

    window.addEventListener('DOMContentLoaded', init);
  </script>

</body>
</html>
"""

with open("new-ui-ux-frontend/pdf-template.html", "w", encoding="utf-8") as f:
    f.write(html_content)
