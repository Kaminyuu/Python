people = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

print(people['emp3'])
print(people['emp3']['salary'])
people['emp3']['salary'] = 8500
for i in people:
    print(i)
    for j in people[i]:
        print(j, ":", people[i][j])

