import argparse
import pandas as pd
def clean_csv(input_path: str, output_path: str):
	"""Parses, cleans, standardises and deduplicates a raw CSV file."""
	print(f"[*] Loading dataset from: {input_path}")

	try:
		df = pd.read_csv(input_path)
	except UnicodeDecodeError:
		df = pd.read_csv(input_path, encoding="latin-1")

	initial_rows = len(df)

	# 1.Standardize column names (snake_case, lowercase, strip whitespace)
	df.columns = (
		df.columns.astype(str)
		.str.strip()
		.str.lower()
		.str.replace(r"[^\w\s]","",regex=True)
		.str.replace(r"\s+","_",regex=True)
	)

	# 2. Strip leading/trailing whitespaces and handle null-like strings
	string_cols = df.select_dtypes(include=["object"]).columns 
	for col in string_cols:
		df[col] = df[col].astype(str).str.strip()
		df[col] = df[col].replace(
			["nan","NaN","null","NULL","None",""], pd.NA
		)

	# 3.Handle Dates: Robust parsing for mixed international formats
	date_cols = [col for col in df.columns if "date" in col or "time" in col]
	for col in date_cols:
		# Try parsing standard formats, coercing absolute junk to NaT
		parsed_dates = pd.to_datetime(df[col], errors="coerce", dayfirst=True)
		# If a date was valid, format it; otherwise keep the original raw text so data is not lost!
		df[col] = parsed_dates.dt.strftime("%Y-%m-%d %H:%M:%S").fillna(df[col])

	# 4. Remove exact duplicate records
	df = df.drop_duplicates()
	duplicates_removed = initial_rows - len(df)

	# 5. Export cleaned dataset
	df.to_csv(output_path, index=False)

	print(f"[+] Cleaning complete!")
	print(f"    -Original rows: {initial_rows}")
	print(f"    -Cleaned rows: {len(df)}")
	print(f"    -Duplicates removed: {duplicates_removed}")
	print(f"    -Output saved to: {output_path}\n")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description="CLI tool to clean messy CSV logs."
	)
	parser.add_argument(
		"--input","-i",required=True, help="Path to input raw CSV"
	)
	parser.add_argument(
	"--output",
	"-o",
	default="cleaned_output_csv",
	help="Path for cleaned CSV",
	)

	args = parser.parse_args()
	clean_csv(args.input, args.output)