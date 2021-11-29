class Person:
    def __init__(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.sex = sex
        self.phoneNumber = phoneNumber
        self.email = email

    def getInformation(self):
        return self.lastName, self.firstName, self.age, self.sex, self.phoneNumber, self.email

    def updateInformation(self):
        self.firstName = input("First Name: ")
        self.lastName = input("Last Name: ")
        self.age = int(input("Age: "))
        self.sex = input("Sex: ")
        self.phoneNumber = input("Phone Number: ")
        self.email = input("Email: ")
        return self.lastName, self.firstName, self.age, self.sex, self.phoneNumber, self.email

    def getFullName(self):
        return self.lastName, self.firstName

class Student(Person):
    def __init__(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, studentNumber:str):
        Person.__init__(self, firstName, lastName, age, sex, phoneNumber, email)
        self.studentNumber = studentNumber

    def getInformationStudent(self):
        return  self.getInformation() + (self.studentNumber,)

    def updateInformationStudent(self):
        self.studentNumber = input("Student Number: ")
        return  self.getInformation() + (self.studentNumber,)

class StudyPoint:
    def __init__(self, processPoint:float=0.0, examPoint:float=0.0):
        self.processPoint = processPoint
        self.examPoint = examPoint

    def averagePoint(self):
        return (self.processPoint+self.examPoint*2)/3

class TrainingPoint:
    def __init__(self, selfAssessment:int=0, classAssessment:int=0):
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
    
    def getPoints(self):
        return self.sp, self.tp
    
    def ranked(self):
        if self.sp > 8 and self.tp > 80:
            return 'Very Good'
        elif self.sp > 6.5 and self.tp > 65:
            return 'Good'
        elif self.sp > 5.5 and self.tp > 55:
            return 'Average'
        elif self.sp > 4 and self.tp > 40:
            return 'Weak'
        else:
            return 'Poor'

class Course:
    std: Student
    def __init__(self, courseType:str, std):
        self.courseType = courseType
        self.std = std.getInformationStudent()
        self.courseYear = 0
    
    def getCourseYear(self):
        if self.courseType == "Engineer":
            self.courseYear = 5
            return self.courseYear
        if self.courseType == "Bachelor":
            self.courseYear = 4
            return self.courseYear
        else:
            self.courseYear = 'Wrong'
            return self.courseYear
    
    def addStudent(self):
        return self.std + (self.getCourseYear(),)

class Specialization:
    course: Course
    def __init__(self, specializationName:str, course):
        self.specializationName = specializationName
        self.course = course

    def getClassType(self):
        if self.course.getCourseYear() == 5:
            self.classType = "Engineer"
            return self.classType
        if self.course.getCourseYear() == 4:
            self.classType = "Bachelor"
            return self.classType

    def className(self):
        return self.specializationName

    def addClass(self):
        return self.course.addStudent() + (self.specializationName,)
    
class Lecturer(Person):
    def __init__(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, degreeType:str, major:str):
        Person.__init__(self, firstName, lastName, age, sex, phoneNumber, email)
        self.degreeType = degreeType
        self.major = major

    def getInformationLecturer(self):
        return self.getInformation() + (self.degreeType, self.major)

    def updateInformationLecturer(self):
        self.degreeType = input("Degree Type: ")
        self.major = input("Major: ")
        return self.degreeType, self.major

class Terms:
    ltName: Lecturer
    spec: Specialization
    def __init__(self, ternName:list, credits:list, ltName, spec):
        self.ternName = ternName
        self. credits = credits
        self. ltName = ltName
        self. spec = spec

    def lecturerName(self):
        return self.ltName.getFullName()
    def className(self):
        return self.spec.className()

class YouthUnion:
    std: Student
    def __init__(self, YouthUnionMember:bool, std):
        self.YouthUnionMember = YouthUnionMember
        self.std = std

    def checkUnionMember(self):
        if self.YouthUnionMember == True:
            return "X"
        else:
            return "O"

    def addUnionMember(self):
        if self.checkUnionMember() == "O":
            return "UM+"
        else:
            return "UM"

    def UnionMember(self):
        return self.std.getFullName() + (self.addUnionMember(),)

class Club:
    std: Student
    def __init__(self, nameClubs:list, std):
        self.nameClubs = nameClubs
        self.std = std

    def addClub(self):
        return self.std.getFullName() + (self.nameClubs,)