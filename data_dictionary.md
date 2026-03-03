# Data Dictionary — German Weather ML Pipeline

## Source Information
| Field | Value |
|-------|-------|
| **Provider** | Deutscher Wetterdienst (DWD) — German Weather Service |
| **Dataset** | Climate Data Center (CDC) — Historical Hourly Observations |
| **URL** | https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/ |
| **License** | Open Data — DWD Terms of Use (free for all purposes) |
| **Coverage** | 500+ weather stations across Germany |
| **Temporal Range** | 1893 to present (varies by station) |
| **Update Frequency** | Daily |

---

## Raw Features (from DWD)

| Feature | Original | Unit | Type | Range | Description |
|---------|----------|------|------|-------|-------------|
| `station_id` | STATIONS_ID | — | int | — | DWD station identifier (5-digit) |
| `datetime` | MESS_DATUM | UTC | timestamp | — | Observation timestamp |
| `temperature_c` | TT_TU | °C | float | [-50, 50] | Air temperature at 2m |
| `relative_humidity_pct` | RF_TU | % | float | [0, 100] | Relative humidity at 2m |
| `precipitation_mm` | R1 | mm | float | [0, 200] | Hourly precipitation amount |
| `precipitation_type` | WRTR | code | int | [0-9] | Type: 0=none, 1=rain, 7=snow, 8=sleet |
| `wind_speed_ms` | F | m/s | float | [0, 75] | Mean wind speed at 10m |
| `wind_direction_deg` | D | ° | float | [0, 360] | Mean wind direction (0=N, 90=E) |
| `station_pressure_hpa` | P0 | hPa | float | [870, 1084] | Pressure at station level |
| `sea_level_pressure_hpa` | P | hPa | float | [870, 1084] | Pressure reduced to sea level |
| `cloud_cover_oktas` | V_N | oktas | int | [0, 8] | Cloud cover (0=clear, 8=overcast) |
| `sunshine_duration_min` | SD_SO | min | float | [0, 60] | Sunshine in past hour |
| `vapor_pressure_hpa` | VP_STD | hPa | float | [0, 50] | Water vapor pressure |
| `dew_point_c` | TF_STD | °C | float | [-60, 40] | Dew point temperature |
| `visibility_m` | V_VV | m | float | [0, 100000] | Horizontal visibility |

---

## Engineered Features

| Feature | Type | Description | Purpose |
|---------|------|-------------|---------|
| `hour_of_day` | int | Hour (0-23) | Diurnal pattern |
| `day_of_week` | int | Day (0-6, Mon-Sun) | Weekly pattern |
| `month` | int | Month (1-12) | Seasonal pattern |
| `day_of_year` | int | Day (1-366) | Fine seasonal |
| `hour_sin` | float | sin(2π × hour/24) | Cyclical hour |
| `hour_cos` | float | cos(2π × hour/24) | Cyclical hour |
| `month_sin` | float | sin(2π × month/12) | Cyclical month |
| `month_cos` | float | cos(2π × month/12) | Cyclical month |
| `wind_direction_sin` | float | sin(direction × π/180) | Cyclical direction |
| `wind_direction_cos` | float | cos(direction × π/180) | Cyclical direction |
| `temp_dewpoint_diff` | float | temp - dewpoint (°C) | Saturation proximity |
| `pressure_tendency` | float | Pressure change (hPa) | Weather trend |
| `humidity_temp_interaction` | float | humidity × temp | Interaction term |
| `station_latitude` | float | Station lat (°) | Geographic feature |
| `station_longitude` | float | Station lon (°) | Geographic feature |
| `station_elevation` | float | Station elevation (m) | Geographic feature |

---

## Target Variable

| Field | Value |
|-------|-------|
| **Name** | `has_precipitation` |
| **Type** | Binary (0 or 1) |
| **Definition** | 1 if `precipitation_mm` > 0, else 0 |
| **Positive Class** | 1 (precipitation occurred) |
| **Negative Class** | 0 (no precipitation) |
| **Expected Imbalance** | ~70% class 0, ~30% class 1 |

---

## Missing Value Convention

| Code | Meaning |
|------|---------|
| `-999` | Missing numeric value (DWD standard) |
| `-999.0` | Missing float value |
| `""` (empty) | Missing string value |
| `eor` | End of record marker |

---

## Quality Flags (QN_* columns)

| Flag | Meaning |
|------|---------|
| 1 | Only formal control performed |
| 2 | Controlled, not all parameters corrected |
| 3 | Automatic correction performed |
| 5 | Historical data, subjective procedures |
| 7 | Second control, not corrected |
| 8 | Quality assured |
| 9 | Not all parameters quality controlled |
| 10 | Quality assured, all parameters controlled |

**Recommendation**: Use records with quality flag ≥ 7 for highest reliability.

---

## Feature Count Summary

| Category | Count |
|----------|-------|
| Raw features | 15 |
| Engineered features | 16 |
| **Total features** | **31** |
| Target variable | 1 |

✓ **Exceeds assignment requirement of >10 features**
