import os
import sys
from datetime import datetime

def parse_log_line(line: str) -> dict:
    """Parse a log line and return a dictionary with parsed components."""
    components = line.strip().split(' ', 3)
    timestamp = datetime.strptime(components[0] + ' ' + components[1], '%Y-%m-%d %H:%M:%S')
    level = components[2]
    message = components[3]
    return {'timestamp': timestamp, 'level': level, 'message': message}


def load_logs(file_path: str) -> list:
    """Load logs from a file and parse each line."""
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            logs.append(parse_log_line(line))
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Filter logs by the specified log level."""
    return [log for log in logs if log['level'] == level]


def count_logs_by_level(logs: list) -> dict:
    """Count the number of logs for each log level."""
    counts = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0}
    for log in logs:
        counts[log['level']] += 1
    return counts


def display_log_counts(counts: dict, selected_level: str):
    """Display log counts, highlighting the selected level."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        if level == selected_level:
            print(f"\033[1;33m{level.ljust(16)} | {count}\033[0m")  # Highlight selected level in yellow
        else:
            print(f"{level.ljust(16)} | {count}")


def display_logs_with_level(logs: list, level: str):
    """Display logs with the specified log level."""
    print(f"Деталі логів для рівня '{level}':")
    for log in logs:
        if log["level"] == level:
            print(f"{log['timestamp']} - {log['message']}")


def main():

    # if len(sys.argv) < 3:
    #     print("Usage: python main.py logfile.log log_level")
    #     return

    # file_path = sys.argv[1]
    # log_level = sys.argv[2]

    # if not os.path.isfile(file_path):
    #     print(f"File '{file_path}' does not exist.")
    #     return

    # logs = load_logs(file_path)
    # counts = count_logs_by_level(logs)
    # display_log_counts(counts, log_level)

    # filtered_logs = filter_logs_by_level(logs, log_level)
    # display_logs_with_level(filtered_logs, log_level)


    if len(sys.argv) < 2:
        print("Usage: python main.py logfile.log")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    
    while True:
        selected_level = input("Enter the log level to filter (INFO, DEBUG, ERROR, WARNING) or 'exit' to quit: ").upper()
        if selected_level == 'EXIT':
            print("Goodbye!")
            break

        if selected_level not in ('INFO', 'DEBUG', 'ERROR', 'WARNING'):
            print("Invalid log level. Please enter INFO, DEBUG, ERROR, or WARNING.")
            continue

        filtered_logs = filter_logs_by_level(logs, selected_level)
        counts = count_logs_by_level(logs)
        display_log_counts(counts, selected_level)
        display_logs_with_level(filtered_logs, selected_level)

if __name__ == "__main__":
    main()



# *********************************************************************
# Завдання #3     Enter a command:
# python task3.py path/to/logfile.log              (варіант 1)
# python main.py path/to/logfile.log INFO           (варіант 2)
# python main.py path/to/logfile.log DEBUG          (варіант 2)
# python main.py path/to/logfile.log ERROR          (варіант 2)
# python main.py path/to/logfile.log WARNING        (варіант 2)
# *********************************************************************