class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, *scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    
    def calculate(self):
        per = sum(scores)/len(scores)
        if 90<=per<=100:
            return 'O'
        elif 80<=per<90:
            return 'E'
        elif 70<=per<80:
            return 'A'
        elif 55<=per<70:
            return 'P'
        elif 40<=per<55:
            return 'D'
        elif per<40:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())