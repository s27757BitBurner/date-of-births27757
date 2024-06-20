import json
import argparse
from collections import Counter

def load_data(file):
    with open(file, 'r') as f:
        data = [json.loads(line) for line in f]
    return data

def analyze_names(data):
    names = [entry['name'] for entry in data]
    return Counter(names)

def analyze_days(data):
    days = [entry['day_of_week'] for entry in data]
    return Counter(days)

def main():
    parser = argparse.ArgumentParser(description="Analyze name and day of the week frequency from a JSON file.")
    parser.add_argument('-f', '--file', required=True, help="Specify the JSON file for analysis.")
    parser.add_argument('-n', '--name', action='store_true', help="Analyze the frequency of names.")
    parser.add_argument('-d', '--day', action='store_true', help="Analyze the frequency of days of the week.")
    
    args = parser.parse_args()
    data = load_data(args.file)
    
    if args.name:
        name_counts = analyze_names(data)
        print("Name Frequency:")
        for name, count in name_counts.items():
            print(f"{name}: {count}")
    
    if args.day:
        day_counts = analyze_days(data)
        print("Day of the Week Frequency:")
        for day, count in day_counts.items():
            print(f"{day}: {count}")

if __name__ == '__main__':
    main()
