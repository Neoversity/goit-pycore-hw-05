

import sys
from task1 import caching_fibonacci
from task2 import generator_numbers, sum_profit
from task4 import main as bot_main
from task3 import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts, display_logs_with_level

def main():
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

        
bot_main()
if __name__ == "__main__":
    main()


#  python main.py         завдання #4

#  python main.py path/to/logfile.log          завдання #3

#  python main.py path/to/logfile.log DEBUG    завдання #3










# *********************************************************************
# Завдання #3     Enter a command:
# python main.py path/to/logfile.log              (варіант 1)
# python main.py path/to/logfile.log INFO           (варіант 2)
# python main.py path/to/logfile.log DEBUG          (варіант 2)
# python main.py path/to/logfile.log ERROR          (варіант 2)
# python main.py path/to/logfile.log WARNING        (варіант 2)
# *********************************************************************






# *********************************************************************
# Завдання #1 Отримуємо функцію fibonacci
# fib = caching_fibonacci()

# *********************************************************************



# *********************************************************************
# Завдання #2
# text = "Загальний дохід працівника складається з декількох 
#частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")
# *********************************************************************



# *********************************************************************
# Завдання #4
# Enter a command: add
# Enter the argument for the command
# Enter a command: add Bob
# Enter the argument for the command
# Enter a command: add Jime 0501234356
# Contact added.
# Enter a command: phone
# Enter the argument for the command
# Enter a command: all
# Jime: 0501234356 
# Enter a command:
# *********************************************************************