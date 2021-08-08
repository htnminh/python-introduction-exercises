class Student():
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade
    def __str__(self):
        return 'Name: ' + self.name + '\n' + \
        'ID: ' + str(self.id) + '\n' + \
        'Grade: ' + str(self.grade)
    def __lt__(self, other):
        return self.grade < other.grade
    def __eq__(self, other):
        return self.id == other.id
    def GradeType(self):
        if self.grade >= 3.6:
            return 'Excellent'
        if self.grade >= 3.2:
            return 'Good'
        if self.grade >= 2.5:
            return 'Fair'    
        return 'Poor'
'''  
s1 = Student('Nguyen Van An', 20201000, 3.75)
s2 = Student('Le Van Toan', 20202345, 2.80)
s3 = Student('Tran Thi Dung', 20201000, 3.12)
print(s1)
'''