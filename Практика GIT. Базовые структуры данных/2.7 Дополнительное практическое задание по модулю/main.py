#Start value
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

_listOfStudents = list(students)
_listOfStudents.sort()
_sumOfGrades = 0
_newGrades = []

for i in range(0,(len(_listOfStudents))):
    _currentGrades = grades[i]
    for j in range(0, len(_currentGrades)):
        _sumOfGrades += _currentGrades[j]
    _newGrades.append(_sumOfGrades / (len(_currentGrades)))
    _sumOfGrades = 0

_finalDictionary = dict([])
for i in range(0, len(_listOfStudents)):
    _finalDictionary.update({_listOfStudents[i]:_newGrades[i]})

print(_finalDictionary)