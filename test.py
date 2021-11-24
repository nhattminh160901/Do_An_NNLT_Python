class Person:
    def __init__(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.sex = sex
        self.phoneNumber = phoneNumber
        self.email = email

    def getInformation(self):
        return self.firstName, self.lastName, self.age, self.sex, self.phoneNumber, self.email

    def updateInformation(self):
        self.firstName = input("First Name: ")
        self.lastName = input("Last Name: ")
        self.age = int(input("Age: "))
        self.sex = input("Sex: ")
        self.phoneNumber = input("Phone Number: ")
        self.email = input("Email: ")
        return self.firstName, self.lastName, self.age, self.sex, self.phoneNumber, self.email

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
    
    def ranked(self):
        return self.tp, self.sp

class Course:
    std: Student
    def __init__(self, courseType:str, std):
        self.courseType = courseType
        self.std = std.getInformation(), std.getInformationStudent()
        self.courseYear = 0
    
    def getCourseYear(self):
        if self.courseType == "Engineer":
            self.courseYear = 5
            return self.courseYear
        if self.courseType == "Bachelor":
            self.courseYear = 4
            return self.courseYear
    
    def addStudent(self):
        return self.std, self.getCourseYear()

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

    def getClassName(self):
        return self.specializationName

    def addClass(self):
        return self.course.addStudent(), self.specializationName
        
class Lecturer(Person):
    spec: Specialization
    def __init__(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, degreeType:str, major:str, spec):
        Person.__init__(self, firstName, lastName, age, sex, phoneNumber, email)
        self.degreeType = degreeType
        self.major = major
        self.spec = spec

    def getInformationLecturer(self):
        return self.degreeType, self.major

    def updateInformationLecturer(self):
        self.degreeType = input("Degree Type: ")
        self.major = input("Major: ")
        return self.degreeType, self.major

    def addLecturerTeachStudent(self):
        return self.lastName, self.spec.getClassType(), self.spec.getClassName()

class Union:
    std: Student
    def __init__(self, unionMember:bool, std):
        self.unionMember = unionMember
        self.std = std.getInformation(), std.getInformationStudent()

    def checkUnionMember(self):
        if self.unionMember == True:
            return "X"
        else:
            return "O"

    def addUnionMember(self):
        if self.checkUnionMember() == "O":
            return "UM+"
        else:
            return "UM"

    def UnionMember(self):
        return self.std, self.addUnionMember()

class Club:
    std: Student
    def __init__(self, nameClub, std):
        self.nameClub = nameClub
        self.std = std.getInformation(), std.getInformationStudent()

    def addClub(self):
        return self.std, self.nameClub