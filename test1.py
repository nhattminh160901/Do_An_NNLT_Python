class Course:
    def __init__(self, courseType:int):
        self.courseType = courseType
        self.courseYear = 0

    def getCourseName(self):
        if self.courseType == 1:
            self.courseName = "Engineer"
            return self.courseName
        if self.courseType == 2:
            self.courseName = "Bachelor"
            return self.courseName
    
    def getCourseYear(self):
        if self.getCourseName() == "Engineer":
            self.courseYear = 5
            return self.courseYear
        elif self.getCourseName == "Bachelor":
            self.courseYear = 4
            return self.courseYear
        else:
            self.courseYear = 'Wrong'
            return self.courseYear

class Specialization:
    course: Course
    def __init__(self, specializationName:str, course):
        self.specializationName = specializationName
        self.course = course

    def getClassType(self):
        return self.course.getCourseName()

    def getClassName(self):
        return self.specializationName

class Terms(Specialization):
    def __init__(self, specializationName, course, ternName:list, credits:list):
        Specialization.__init__(self, specializationName, course)
        self.ternName = ternName
        self.credits = credits
    
    def getTermsandCredits(self):
        TandC = {}
        dem = 0
        for i in self.ternName:
            TandC[i] = self.credits[dem]
            dem +=1
        return TandC

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

    def getFullName(self):
        return self.lastName, self.firstName

class Student(Person):
    term: Terms
    def __init__(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, studentNumber:str):
        Person.__init__(self, firstName, lastName, age, sex, phoneNumber, email)
        self.studentNumber = studentNumber

    def informationStudent(self):
        return  self.getInformation() + (self.studentNumber,)

    def informationStudentCourse(self, term):
        self.term = term
        return  self.getInformation() + (self.studentNumber, self.term.getClassType(), self.term.getClassName(), self.term.getTermsandCredits())

    def addListStudent(self, listStudent:list):
        self.listStudent = listStudent
        self.listStudent.append(self.informationStudentCourse(self.term))
        return self.listStudent

class Lecturer(Person):
    stu: Student
    def __init__(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, degreeType:str, major:str):
        Person.__init__(self, firstName, lastName, age, sex, phoneNumber, email)
        self.degreeType = degreeType
        self.major = major

    def getInformationLecturer(self):
        return self.getInformation() + (self.degreeType, self.major)

    def memberClass(self, className:str, listStudent):
        self.className = className
        self.listStudent = listStudent
        self.listClass = []
        for i in self.listStudent:
            for j in i:
                if j == self.className:
                    self.listClass.append((i[0], i[1]))
                    break
        return self.listClass

class YouthUnion:
    std: Student
    def __init__(self, YUM:bool, std):
        self.YUM = YUM
        self.std = std

    def checkYouthUnionMember(self):
        if self.YUM == True:
            return "X"
        else:
            return "O"

    def addYouthUnionMember(self):
        if self.checkYouthUnionMember() == "O":
            return "UM+"
        else:
            return "UM"

    def youthUnionMember(self):
        return self.std.informationStudent() + (self.addYouthUnionMember(),)

class StudyPoint:
    def __init__(self, processPoint:float=0.0, examPoint:float=0.0):
        self.processPoint = processPoint
        self.examPoint = examPoint

    def getGPA(self):
        return (self.processPoint+self.examPoint*2)/3

class TrainingPoint:
    def __init__(self, trainingPoint:int=0):
        self.trainingPoint = trainingPoint

    def getTP(self):
        return self.trainingPoint

class Rank:
    sp: StudyPoint
    tp: TrainingPoint
    def __init__(self, sp, tp):
        self.sp = sp
        self.tp = tp
    
    def getPoints(self):
        return self.sp.getGPA(), self.tp.getTP()
    
    def ranked(self):
        if self.sp.getGPA() > 8 and self.tp.getTP() > 80:
            return 'Very Good'
        elif self.sp.getGPA() > 6.5 and self.tp.getTP() > 65:
            return 'Good'
        elif self.sp.getGPA() > 5.5 and self.tp.getTP() > 55:
            return 'Average'
        elif self.sp.getGPA() > 4 and self.tp.getTP() > 40:
            return 'Weak'
        else:
            return 'Poor'
