import argparse
from datetime import datetime
import pytz
import sys

def convert_meeting_time(date_time_str, original_zone_str):
    """
    Converts a meeting time from an original time zone to EST, IST, and UTC.
    """
    formats = [
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M"
    ]
    
    local_dt = None
    for fmt in formats:
        try:
            local_dt = datetime.strptime(date_time_str, fmt)
            break
        except ValueError:
            continue
            
    if local_dt is None:
        print(f"Error: Invalid date/time format: '{date_time_str}'.")
        print("Supported formats: YYYY-MM-DD HH:MM[:SS] or ISO format.")
        sys.exit(1)

    try:
        # Get the timezone object
        original_tz = pytz.timezone(original_zone_str)
    except pytz.UnknownTimeZoneError:
        print(f"Error: Unknown time zone '{original_zone_str}'.")
        sys.exit(1)

    # Localize the datetime object to the original timezone
    original_dt = original_tz.localize(local_dt)

    print(f"Original Time: {original_dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
    print("-" * 40)

    # Target time zones
    target_zones = {
        "EST": "US/Eastern",
        "IST": "Asia/Kolkata",
        "UTC": "UTC"
    }

    for code, zone in target_zones.items():
        try:
            tz = pytz.timezone(zone)
            converted_dt = original_dt.astimezone(tz)
            print(f"{code:<5}: {converted_dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
        except pytz.UnknownTimeZoneError:
            print(f"Error: Could not find time zone for {code} ({zone})")

def main():
    parser = argparse.ArgumentParser(description="Convert meeting time to EST, IST, and UTC.")
    parser.add_argument("args", nargs="+", help="Date, Time, and Timezone (e.g., '2023-12-25 10:00 CET')")

    args = parser.parse_args()
    
    if len(args.args) < 2:
        print("Error: Insufficient arguments. Please provide Date, Time, and Timezone.")
        sys.exit(1)

    # The last argument is the timezone
    timezone = args.args[-1]
    # Everything before the last argument is the date and time
    date_time_str = " ".join(args.args[:-1])

    convert_meeting_time(date_time_str, timezone)

if __name__ == "__main__":
    main()
