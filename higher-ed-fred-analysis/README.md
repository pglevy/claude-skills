# Higher Ed FRED Analysis Skill - Usage Guide

## What You Just Created

You now have a complete Claude Skill for creating sophisticated higher education economic analyses using FRED data. The skill includes:

### Main Components

1. **SKILL.md** - Core instructions that Claude will read when the skill triggers
2. **4 Reference Files** - Detailed guides Claude can consult as needed:
   - `fred-series-guide.md` - Catalog of all relevant FRED economic series
   - `design-system.md` - Complete visual design specifications
   - `narrative-templates.md` - Report writing structures and guidelines
   - `stakeholder-personas.md` - Audience-specific communication strategies

3. **Python Script** - `fetch_fred_data.py` for programmatic FRED data retrieval
4. **Dashboard Template** - Your complete POC dashboard as a reusable starting point

## How to Use This Skill

### Option 1: Install in Claude Desktop/Projects
1. Upload the `higher-ed-fred-analysis.skill` file to a Claude project
2. The skill will automatically trigger when you request higher ed economic analysis
3. Claude will read the SKILL.md and reference appropriate guides as needed

### Option 2: Use as a Reference
Even without formal installation, you can:
- Share specific reference files with Claude in conversations
- Copy sections into your project knowledge base
- Use the templates as starting points for custom work

## What the Skill Does

When triggered, Claude will:

1. **Identify the analysis type** you need (dashboard vs. report vs. combined)
2. **Select relevant FRED series** from the comprehensive catalog
3. **Apply consistent design system** matching your POC's sophisticated aesthetic
4. **Craft stakeholder-appropriate narratives** based on audience personas
5. **Follow evidence-based principles** ensuring balanced, actionable insights

## Example Triggers

The skill will activate when you say things like:
- "Create a dashboard showing student debt trends and employment outcomes"
- "Write a report on higher ed ROI for our board of trustees"
- "Build an interactive visualization of earnings by education level"
- "Analyze unemployment rates by degree attainment for our enrollment team"
- "Create a one-pager about college value for prospective students"

## Key Features

### Progressive Disclosure
- Main SKILL.md is concise (<500 lines)
- Detailed info lives in reference files
- Claude only loads what it needs for each task

### Audience-Aware
- 7 stakeholder personas with specific strategies
- Different communication approaches for each audience
- Ready-to-use messaging frameworks

### Design Consistency
- Your dark theme with gold accents codified
- Chart.js configurations documented
- Typography and layout patterns specified

### Evidence-Based Framework
- ROI analysis patterns
- Trend analysis guidelines
- Limitation acknowledgment templates

## Evolving the Skill

As you use this skill and learn what works, you can:

1. **Update reference files** with new FRED series or better messaging
2. **Add new templates** for specific use cases you encounter
3. **Refine stakeholder personas** based on real interactions
4. **Expand the design system** with new chart types or layouts

To update:
1. Unzip the `.skill` file
2. Edit the relevant markdown files
3. Re-package using the skill-creator script

## Quick Start Workflow

### For Your Next Dashboard:
```
"Using the higher-ed-fred-analysis skill, create an interactive dashboard 
comparing unemployment rates and earnings by education level. Use the 
last 10 years of data and target it for our enrollment management team."
```

Claude will:
- Read the main SKILL.md
- Consult `fred-series-guide.md` for the right series
- Apply design from `design-system.md`
- Check `stakeholder-personas.md` for enrollment messaging
- Copy and customize `dashboard-template.html`

### For Your Next Report:
```
"Create a 3-page analytical report on higher ed economic value for our 
board of trustees. Focus on ROI and employment protection."
```

Claude will:
- Use the Analytical Report template from `narrative-templates.md`
- Apply Board persona strategies from `stakeholder-personas.md`
- Include appropriate FRED series from the catalog
- Follow the evidence-based principles in SKILL.md

## What Makes This Different

Unlike ad-hoc requests where Claude might reinvent the wheel each time:

- **Consistency**: Same design language, same data sources, same quality standards
- **Efficiency**: No need to re-explain your institution's needs or preferred style
- **Scalability**: Other team members can get the same quality output
- **Iteration**: The skill gets better as you refine it based on real use

## File Structure

```
higher-ed-fred-analysis/
├── SKILL.md                              # Main instructions (always loaded)
├── scripts/
│   └── fetch_fred_data.py               # Reusable data fetching utility
├── references/                           # Loaded as needed
│   ├── fred-series-guide.md
│   ├── design-system.md
│   ├── narrative-templates.md
│   └── stakeholder-personas.md
└── assets/
    └── dashboard-template.html          # Your POC as a template
```

## Next Steps

1. **Test the skill** by uploading it to a Claude project and requesting an analysis
2. **Iterate based on results** - update reference files as you learn what works
3. **Share with colleagues** - packaged skills are easy to distribute
4. **Expand over time** - add more series, templates, or personas as needed

## Questions to Consider

As you use the skill, think about:
- Are there other FRED series relevant to your institution?
- Do you need additional stakeholder personas (e.g., alumni, donors)?
- Are there report types you create repeatedly that should be templated?
- What design variations might be useful (light theme, print-friendly)?

The beauty of skills is they evolve with your needs. Start with this foundation and refine as you go!
