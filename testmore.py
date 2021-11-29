from test import *

student = Student('Minh', 'Le Quang Nhat', 21, 'male', '0898989898', 'minh@gmail.com', '20E1020074')
cs = Course('Engineer', student)
sp = Specialization('KTD&TDH', cs)
print(sp.addClass())

lec = Lecturer('Nha', 'Vo Quang', 35, 'male', '0989898989', 'nha@gmail.com', 'TS', 'Electronic')

term = Terms(['KTD&TDH'],[4], lec, sp)
print(term.lecturerName())
print(term.className())

union = YouthUnion(True, student)
print(union.UnionMember())

clb = Club(['robot', 'football'], student)
print(clb.addClub())