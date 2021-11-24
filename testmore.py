from allclass import Lecturer
from allclass import Student
from allclass import StudyPoint
from allclass import TrainingPoint
from allclass import Rank
from allclass import Course
from allclass import Specialization
from allclass import Union
from allclass import Club

student = Student('Le Quang Nhat', 'Minh', 21, 'male', '0898989898', 'minh@gmail.com', '20E1020074')
cs = Course('Engineer', student)
print(student.updateInformationStudent())
# sp = Specialization('KHDL&TTNT', cs)
# print(sp.addClass())

# lec = Lecturer('Vo Quang', 'Nha', 35, 'male', '0989898989', 'nha@gmail.com', 'TS', 'Electronic', sp)
# print(lec.addLecturerTeachStudent())

# union = Union(False, student)
# print(union.UnionMember())

# clb = Club(['robot', 'football'], student)
# print(clb.addClub())