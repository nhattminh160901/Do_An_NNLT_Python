from dataclass import *

class ManagementAll:
    def inputStudent(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, studentNumber:str) -> Student:
        st = Student(firstName, lastName, age, sex, phoneNumber, email, studentNumber)
        return st

    def inputCourse(self, courseType:int, specializationName:str, termName:list, credits:list) -> Terms:
        course = Course(courseType)
        term = Terms(specializationName, course, termName, credits)
        return term
    
    def inputLecturer(self, firstName:str, lastName:str, age:int, sex:str, phoneNumber:str, email:str, degreeType:str, major:str, classTerm:str) -> Lecturer:
        lec = Lecturer(firstName, lastName, age, sex, phoneNumber, email, degreeType, major, classTerm)
        return lec

    def addStudenttoList(self, inputStudent, inputCourse, listStudent:list) -> list:
        listStudent.append(inputStudent.informationStudentCourse(inputCourse))
        return listStudent

    def addStudentToClass(self, inputLecturer, listStudent:list) -> list:
        return inputLecturer.memberClass(listStudent)

    def getGPA(self, processPoint:float=0.0, examPoint:float=0.0) -> float:
        sp = StudyPoint(processPoint, examPoint)
        return sp.getGPA()

    def getRank(self, processPoint:float=0.0, examPoint:float=0.0, trainingPoint:int=0) -> str:
        sp = StudyPoint(processPoint, examPoint)
        tp = TrainingPoint(trainingPoint)
        rank = Rank(sp, tp)
        return rank.ranked()

    def addYUMList(self, YUM:bool, inputStudent:list) -> tuple:
        yum = YouthUnion(YUM, inputStudent)
        yum.addYouthUnionMember()
        return yum.youthUnionMember()

    def findByFullName(self, firstName:str, lastName:str, listStudent:list) -> None:
        find = 0
        for i in listStudent:
            if lastName == i[0] and firstName == i[1]:
                print(i)
                find += 1
        if find == 0:
            print("Student Information is not found")

    def findBySex(self, listStudent:list, sex:str) -> None:
        find = 0
        for i in listStudent:
            if sex == i[3]:
                print(i)
                find += 1
        if find == 0:
            print("Student Information is not found")

    def findByRank(self, listStudent:list, rank:str) -> None:
        find = 0
        for i in listStudent:
            if i[12] == rank:
                print(i)
                find += 1
        if find == 0:
            print("Scores have not been entered for any students yet")

    def findByClass(self, listStudent:list, className:str) -> None:
        print(className+":")
        find = 0
        for i in listStudent:
            termName = i[9]
            for j in termName:
                if j == className:
                    print(i)
                    find += 1
        if find == 0:
            print("There are no students in the class")

    def sortList(self, sortList:list, choose:int, option:bool) -> list:
        sortedList = sorted(sortList, key=lambda tup:tup[choose], reverse=option)
        return sortedList