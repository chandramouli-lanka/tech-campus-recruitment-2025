import sys
import os

# Define paths
LOG_FILE_PATH = "data/logs_2024.log"  # Update with the actual file name inside data/
OUTPUT_DIR = "output"

def extract_logs(date):
    """Extract logs for a specific date from a large log file."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)  # Create output directory if it doesn't exist

    output_file = f"{OUTPUT_DIR}/output_{date}.txt"

    with open(LOG_FILE_PATH, "r", encoding="utf-8") as log_file, open(output_file, "w", encoding="utf-8") as output:
        for line in log_file:
            if line.startswith(date):
                output.write(line)  # Write matching logs to the output file

    print(f"Logs for {date} saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date = sys.argv[1]
    extract_logs(date)
