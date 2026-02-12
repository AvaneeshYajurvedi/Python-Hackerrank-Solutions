# Read number of students
n = int(input())

# Store student data in a list
students = []
for _ in range(n):
    name = input().strip()
    grade = float(input())
    students.append([name, grade])

# Extract all grades
grades = [g for _, g in students]

# Find the second lowest grade
unique_grades = sorted(set(grades))
second_lowest = unique_grades[1]

# Collect names with the second lowest grade
result = [name for name, g in students if g == second_lowest]

# Sort alphabetically
result.sort()

# Print each name on a new line
for name in result:
    print(name)
