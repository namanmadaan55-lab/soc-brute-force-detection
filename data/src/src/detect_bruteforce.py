import csv
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

# Project root is the parent of the src folder.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_FILE = PROJECT_ROOT / "data" / "sample_failed_logins.csv"

# Flag an IP when it has at least 5 failures within 5 minutes.
THRESHOLD = 5
WINDOW = timedelta(minutes=5)


def main():
    failures = defaultdict(list)
    total_events = 0

    with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_events += 1

            if row["status"].strip().upper() != "FAILED":
                continue

            timestamp = datetime.fromisoformat(
                row["timestamp"].replace("Z", "+00:00")
            )
            source_ip = row["source_ip"].strip()
            failures[source_ip].append(timestamp)

    print("SOC Brute-Force Detection")
    print("=" * 35)
    print(f"Total events analysed: {total_events}")
    print(f"Failed logins: {sum(len(times) for times in failures.values())}")
    print("\nDetection results:")

    alerts = 0

    for source_ip, timestamps in failures.items():
        timestamps.sort()

        # Check each rolling five-minute window.
        for start in timestamps:
            end = start + WINDOW
            count = sum(start <= time <= end for time in timestamps)

            if count >= THRESHOLD:
                print(
                    f"[ALERT] {source_ip}: "
                    f"{count} failed logins within 5 minutes"
                )
                alerts += 1
                break

    if alerts == 0:
        print("No suspicious bursts detected.")

    print("\nNote: Alerts require investigation; they do not prove an attack.")


if __name__ == "__main__":
    main()
