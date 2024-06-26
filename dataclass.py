class Course:
    def __init__(self, courseType:int) -> None:
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
    def __init__(self, specializationName:str, course) -> None:
        self.specializationName = specializationName
        self.course = course

    def getClassType(self) -> str:
        return self.course.getCourseName()

    def getSpecializationName(self) -> str:
        return self.specializationName

class Terms(Specialization):
    def __init__(self, specializationName, course, termName:list, credits:list) -> None:
        Specialization.__init__(self, specializationName, course)
        self.termName = termName
        self.credits = credits
    
    def getTermsandCredits(self) -> dict:
        TandC = {}
        dem = 0
        for i in self.termName:
            TandC[i] = self.credits[dem]
            dem +=1
        return TandC

class Person:
    def __init__(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.sex = sex
        self.phoneNumber = phoneNumber
        self.email = email

    def getInformation(self) -> tuple:
        return self.lastName, self.firstName, self.age, self.sex, self.phoneNumber, self.email

    def getFullName(self) -> tuple:
        return self.lastName, self.firstName

class Student(Person):
    term: Terms
    def __init__(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, studentNumber:str) -> None:
        Person.__init__(self, firstName, lastName, age, sex, phoneNumber, email)
        self.studentNumber = studentNumber

    def informationStudent(self) -> tuple:
        return  self.getInformation() + (self.studentNumber,)

    def informationStudentCourse(self, term) -> tuple:
        self.term = term
        return  self.getInformation() + (self.studentNumber, self.term.getClassType(), self.term.getSpecializationName(), self.term.getTermsandCredits())

    def addListStudent(self, listStudent:list) -> list:
        self.listStudent = listStudent
        self.listStudent.append(self.informationStudentCourse(self.term))
        return self.listStudent

class Lecturer(Person):
    stu: Student
    def __init__(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, degreeType:str, major:str, classTerm:str) -> None:
        Person.__init__(self, firstName, lastName, age, sex, phoneNumber, email)
        self.degreeType = degreeType
        self.major = major
        self.classTerm = classTerm

    def getInformationLecturer(self) -> tuple:
        return self.getInformation() + (self.degreeType, self.major, self.classTerm)

    def getClassName(self) -> str:
        return self.classTerm

    def memberClass(self, listStudent) -> list:
        self.listStudent = listStudent
        self.listClass = []
        for i in self.listStudent:
            termName = i[9]
            for j in termName:
                if self.classTerm == j:
                    self.listClass.append(i)
                    break
        return self.listClass

class YouthUnion:
    std: Student
    def __init__(self, YUM:bool, std) -> None:
        self.YUM = YUM
        self.std = std

    def checkYouthUnionMember(self) -> str:
        if self.YUM == True:
            return "X"
        else:
            return "O"

    def addYouthUnionMember(self) -> str:
        if self.checkYouthUnionMember() == "O":
            return "UM+"
        else:
            return "UM"

    def youthUnionMember(self) -> tuple:
        return self.std.informationStudent() + (self.addYouthUnionMember(),)

class StudyPoint:
    def __init__(self, processPoint:float=0.0, examPoint:float=0.0) -> None:
        self.processPoint = processPoint
        self.examPoint = examPoint

    def getGPA(self) -> float:
        return (self.processPoint+self.examPoint*2)/3

class TrainingPoint:
    def __init__(self, trainingPoint:int=0) -> None:
        self.trainingPoint = trainingPoint

    def getTP(self) -> int:
        return self.trainingPoint

class Rank:
    sp: StudyPoint
    tp: TrainingPoint
    def __init__(self, sp, tp) -> None:
        self.sp = sp
        self.tp = tp
    
    def getPoints(self) -> float:
        return self.sp.getGPA(), self.tp.getTP()
    
    def ranked(self) -> str:
        if self.sp.getGPA() > 8 and self.tp.getTP() > 80:
            return "Very Good"
        elif self.sp.getGPA() > 6.5 and self.tp.getTP() > 65:
            return "Good"
        elif self.sp.getGPA() > 5.5 and self.tp.getTP() > 55:
            return "Average"
        elif self.sp.getGPA() > 4 and self.tp.getTP() > 40:
            return "Weak"
        else:
            return "Poor"