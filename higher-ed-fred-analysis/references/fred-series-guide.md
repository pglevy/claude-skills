# FRED Series Guide for Higher Education Analysis

Comprehensive catalog of Federal Reserve Economic Data series relevant to higher education economic analysis.

## Student Loan Debt

### SLOAS - Student Loans Owned and Securitized, Outstanding
**Frequency**: Quarterly
**Units**: Millions of Dollars
**Seasonal Adjustment**: Not Seasonally Adjusted
**Description**: Total outstanding student loan debt in the United States. Includes federal and private loans, both federally-held and securitized.
**Use**: Primary indicator for discussing student debt burden, trends over time, and context for ROI discussions.
**Note**: Divide by 1,000 to convert to billions, 1,000,000 to convert to trillions.

### Related Series
- **FGCCSAQ027S**: Federal Government: Student Loans (more specific to federal loans)
- **CMDEBT**: Consumer Debt Service Payments as a Percent of Disposable Personal Income

## Unemployment Rates by Educational Attainment

### LNS14027662 - Unemployment Rate: Bachelor's Degree and Higher, 25 years and over
**Frequency**: Monthly
**Units**: Percent
**Seasonal Adjustment**: Seasonally Adjusted
**Description**: Unemployment rate for individuals 25+ with bachelor's degree or higher education.
**Use**: Demonstrates labor market advantage of degree attainment.

### LNS14027660 - Unemployment Rate: High School Graduates, No College, 25 years and over
**Frequency**: Monthly
**Units**: Percent
**Seasonal Adjustment**: Seasonally Adjusted
**Description**: Unemployment rate for individuals 25+ with high school diploma, no college.
**Use**: Comparison baseline for demonstrating degree advantage.

### LNS14027659 - Unemployment Rate: Less than a High School Diploma, 25 years and over
**Frequency**: Monthly
**Units**: Percent
**Seasonal Adjustment**: Seasonally Adjusted
**Description**: Unemployment rate for individuals 25+ without high school completion.
**Use**: Shows full educational attainment spectrum.

### LNS14027689 - Unemployment Rate: Some College or Associate Degree, 25 years and over
**Frequency**: Monthly
**Units**: Percent
**Seasonal Adjustment**: Seasonally Adjusted
**Description**: Unemployment for those with some college but no bachelor's.
**Use**: Nuanced analysis of partial attainment effects.

## Earnings by Educational Attainment

### LEU0252918500A - Median Weekly Earnings: Bachelor's Degree and Higher, 25 years and over
**Frequency**: Annual
**Units**: Dollars
**Seasonal Adjustment**: Not Seasonally Adjusted
**Description**: Median usual weekly earnings for full-time wage and salary workers 25+ with bachelor's or higher.
**Use**: Primary earnings advantage metric for ROI analysis.

### LEU0252917300A - Median Weekly Earnings: High School Graduates, No College, 25 years and over
**Frequency**: Annual
**Units**: Dollars
**Seasonal Adjustment**: Not Seasonally Adjusted
**Description**: Median usual weekly earnings for full-time wage and salary workers 25+ with high school only.
**Use**: Comparison baseline for earnings premium calculations.

### LEU0252917500A - Median Weekly Earnings: Some College or Associate Degree, 25 years and over
**Frequency**: Annual
**Units**: Dollars
**Seasonal Adjustment**: Not Seasonally Adjusted
**Description**: Median earnings for those with some college.
**Use**: Demonstrates incremental benefit of partial college completion.

### LEU0252916500A - Median Weekly Earnings: Less than a High School Diploma, 25 years and over
**Frequency**: Annual
**Units**: Dollars
**Seasonal Adjustment**: Not Seasonally Adjusted
**Description**: Median earnings for those without high school diploma.
**Use**: Full earnings spectrum context.

## Labor Force Participation

### LNU01327662 - Labor Force Participation Rate: Bachelor's Degree and Higher, 25 years and over
**Frequency**: Monthly
**Units**: Percent
**Seasonal Adjustment**: Seasonally Adjusted
**Description**: Percentage of civilian noninstitutional population 25+ with bachelor's+ who are in labor force.
**Use**: Context for employment discussions - shows degree holders more likely to be employed or seeking employment.

### LNU01327660 - Labor Force Participation Rate: High School Graduates, No College, 25 years and over
**Frequency**: Monthly
**Units**: Percent
**Seasonal Adjustment**: Seasonally Adjusted
**Description**: Labor force participation for high school graduates.
**Use**: Comparison for understanding workforce engagement differentials.

## Economic Context Series

### UNRATE - Unemployment Rate
**Frequency**: Monthly
**Units**: Percent
**Seasonal Adjustment**: Seasonally Adjusted
**Description**: Overall civilian unemployment rate.
**Use**: Context for education-specific rates, understanding macro trends.

### CPIAUCSL - Consumer Price Index for All Urban Consumers: All Items
**Frequency**: Monthly
**Units**: Index 1982-1984=100
**Seasonal Adjustment**: Seasonally Adjusted
**Description**: CPI measure for inflation adjustments.
**Use**: Essential for real dollar comparisons across time periods.

### MEHOINUSA672N - Real Median Household Income in the United States
**Frequency**: Annual
**Units**: 2022 Dollars
**Seasonal Adjustment**: Not Seasonally Adjusted
**Description**: Inflation-adjusted median household income.
**Use**: Context for earnings discussions, broader economic trends.

## Query Patterns

### Basic Series Query
```
https://api.stlouisfed.org/fred/series/observations
?series_id=SLOAS
&api_key=YOUR_KEY
&file_type=json
&sort_order=desc
&limit=100
```

### Multiple Series (requires separate calls)
Fetch each series independently and join by date on client/script side.

### Common Transformations
- **YoY Change**: `&units=pc1` (percent change from year ago)
- **Compounded Annual Rate**: `&units=pca` 
- **Annual aggregation**: `&frequency=a&aggregation_method=avg`

### Handling Missing Data
FRED uses "." for missing observations. Always check value !== "." before parsing.

## Data Quality Notes

**BLS Revisions**: Unemployment and earnings data are subject to periodic revisions. Most recent 2-3 months may be preliminary.

**Sample Sizes**: Education-specific series have smaller sample sizes than aggregate measures. Monthly variation may reflect sampling rather than true trend.

**Definition Changes**: Educational attainment categories have remained stable, but survey methodologies evolve. Be cautious with very long time series (20+ years).

**Coverage**: All series cover civilian noninstitutional population. Does not include military, institutionalized populations, or those under 16 (or 25 for education series).

## Recommended Series Combinations

**ROI Package**: SLOAS + LNS14027662 + LNS14027660 + LEU0252918500A + LEU0252917300A

**Employment Stability**: LNS14027662 + LNS14027660 + UNRATE (with recession shading)

**Full Education Spectrum**: All four LNS1402766X unemployment series + corresponding earnings series

**Trend Analysis**: 10-year windows of SLOAS and earnings differentials to show consistent patterns
