class Student:
    def __init__(self, lastName:str, firstName:str, sex:str, age:int, phoneNumber:int, email:str):
        self.lastName = lastName
        self.firstName = firstName
        self.sex = sex
        self.age = age
        self.phoneNumber = phoneNumber
        self.email = email

    def getinformation(self):
        return self.lastName, self.firstName, self.sex, self.age, self.phoneNumber, self.email

    def updateInformation(self, age, phoneNumber, email):
        self.age = age
        self.phoneNumber = phoneNumber
        self.email = email
        return self.lastName, self.firstName, self.sex, self.age, self.phoneNumber, self.email

class Course(Student):
    def __init__(self, lastName, firstName, sex, age, phoneNumber, email, courseYear:str, nameClass:str, studentNumber:str):
        Student.__init__(self, lastName, firstName, sex, age, phoneNumber, email)
        self.courseYear = courseYear
        self.nameClass = nameClass
        self.studentNumber = studentNumber

    def getCourse(self):
        return self.courseYear, self.nameClass, self.studentNumber

    def updateCourse(self, courseYear, nameClass, studentNumber):
        self.courseYear = courseYear
        self.nameClass = nameClass
        self.studentNumber = studentNumber

    
class StudyPoint:
    def __init__(self, processPoint=0.0, examPoint=0.0):
        self.processPoint = processPoint
        self.examPoint = examPoint

    def averagePoint(self):
        return (self.processPoint+self.examPoint*2)/3

class TrainingPoint:
    def __init__(self, selfAssessment=0, classAssessment=0):
        self.selfAssessment = selfAssessment
        self.classAssessment = classAssessment

    def getTP(self):
        return (self.selfAssessment+self.classAssessment)/2

class Rank:
    sp: StudyPoint
    tp: TrainingPoint
    def __init__(self, sp, tp):
        self.sp = sp.averagePoint()
        self.tp = tp.getTP()
    
    def ranked(self):
        return self.tp, self.sp
# a = Course('minh', 'le', 'male', 21, 8489898989, 'vippro', 1, "KHDL&TTNT", '20E1020074')
# print(a.getCourse())

a = StudyPoint()
b = TrainingPoint()
c = Rank(a, b)
print(c.ranked())