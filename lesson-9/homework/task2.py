import csv

def read_grades(file_name):
    grades = []
    with open(file_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])  # Convert grade to integer
            grades.append(row)
    return grades

def calculate_average(grades):
    subject_totals = {}
    subject_counts = {}
    
    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']
        
        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0
        
        subject_totals[subject] += grade
        subject_counts[subject] += 1
    
    averages = {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}
    return averages

def write_averages(file_name, averages):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 2)])
grades_data = [['Name', 'Subject', 'Grade'],
               ['Alice', 'Math', '85'],
               ['Bob', 'Science', '78'],
               ['Carol', 'Math', '92'],
               ['Dave', 'History', '74']]

with open('grades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(grades_data)
grades = read_grades('grades.csv')
averages = calculate_average(grades)
write_averages('average_grades.csv', averages)

print("Average grades have been calculated and written to average_grades.csv.")
