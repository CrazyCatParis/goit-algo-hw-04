from pathlib import Path

def total_salary(path):
    total = 0
    count = 0

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            name, salary = line.strip().split(',')
            count += 1
            total += int(salary)
        average = int(total/count)
        return total, average
          
            


total, average = total_salary(Path('monthly_salaries_list.txt'))
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
# Result = Загальна сума заробітної плати: 10575, Середня заробітна плата: 1762




