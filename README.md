# Automated CSV Log & Data Sanitizer

A lightweight Python pipeline designed to parse, clean and standardize messy CSV files and log exports. 
Built to fix corrupted formatting, unaligned date fields, trailing whitespaces, and duplicate records.

## Features:
- **Column Standardization:** Converts all header names to standardized 'snake_case'.
- **String Sanitization:** Strips trailing spaces and normalizes 'NULL'/'NaN' strings.
- **Date Normalization:** Auto-detects and converts inconsistent date formats while preserving unparsable raw entries.
- **Deduplication:** Identifies and purges duplicate rows automatically.
