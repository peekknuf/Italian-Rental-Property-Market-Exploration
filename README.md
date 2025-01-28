# Data Analysis: Italian Rental Property Market Exploration

## Data Quality & Anomalies
- **Price Outliers**:  
  - Detected extremely high prices (e.g., €8,000–€19,000/month) requiring investigation.  
  - Proposed hypothesis: Possible decimal misplacement (e.g., €8000 → €800). Preserved original column for traceability.  
  - Validated plausibility for luxury properties in Rome/Milan but noted suspicious activity (e.g., 29 November bulk listings).  

- **Geographic Consistency**:  
  - All listings originated from Italy. Country code deemed redundant but retained for completeness.  

- **Missing Data**:  
  - 5% missing city data deemed manageable.  
  - ~50% missing property size data flagged as critical issue.  

- **Unexpected Trends**:  
  - Rome's absence from Top 5 cities by listing count challenged assumptions about rental market dynamics.  

---

## Data Cleaning & Transformations
- **String Formatting**:  
  Stripped extraneous quotes from `yes`/`no` values and `total_size` column.  

- **Size Approximation**:  
  - Created adjusted size column assuming `Private Room` sizes reflect room (not property) dimensions.  
  - Removed nonsensical entries (e.g., -135 m²).  

- **COVID-19 Impact**:  
  - Observed price plummet during pandemic (2020–2021) correlating with travel restrictions.  

---

## Key Insights & Observations
### Cities of Interest
- **Milan**: Dominates listings as Italy’s economic hub. High prices reflect demand (e.g., studios at ~€1,000/month).  
- **Rome**: Surprisingly low listing volume; hypothesized dominance of short-term rentals.  

### Property Characteristics
- **Registration Status**:  
  - 25% missing registration data for apartments; hypothesized bias toward registered properties.  
- **Room Type Distribution**:  
  - Balanced ratios for apartments, studios, and private rooms. Low shared-room listings flagged as unusual.  

### Socio-Economic Trends
- **Affordability**:  
  - Studio apartments deemed affordable outside Milan; shared rooms in Milan reflect economic strain.  
- **Market Drivers**:  
  - Identified key variables: city, district centrality, size, and price. Registration status noted as critical for renters.  

---

## Methodological Notes
- **Assumptions & Limitations**:  
  - Size adjustments for `Private Room` category acknowledged as imperfect but exploratory.  
  - Spike in luxury listings on 29 November flagged for external validation (e.g., agency bulk uploads).  
- **Future Directions**:  
  - Suggested deeper analysis of amenities (terrace, TV) and district-level pricing trends.  

*"The analysis evolved into a socio-economic exploration of Italy’s rental market, revealing systemic pressures on housing affordability."*