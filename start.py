from admin import Admin
from course import Course
from student import Student
from machine import Machine

print("start\n")
str = ""
schedule = set()
while True:
    str = input("create a shcedule ,input course name, input break means finish \n").strip()
    if str == "break":
        break
    schedule.add(str)
print("schedule has done\n")
stuTeam =list()

while True:
    stuNum = int(input("input student number,number 100 means stop\n").strip())
    if stuNum == 100:
        break
    stu = Student(stuNum, *schedule)
    stuTeam.append(stu)

print("creat admin\n")
admNum = int(input("input admin number\n").strip())
adminA = Admin(admNum, *schedule)

optStu = ""
courseName = ""
courseScore = 0

while True:
    stuNum = int(input("chose a student by their number,100 means break\n").strip())
    FlagD = True
    if stuNum == 100:
        break
    for stuN in stuTeam:
        if stuN.stuNum == stuNum:
            stuR = stuN
            FlagD =False
            while True:
                optStu = input("add or set or del , break means finish\n").strip()
                if optStu == "break":
                    break
                match optStu:
                    case "add":
                        courseName = input("course name\n").strip()
                        stuR.add_course(courseName)
                    case "set":
                        courseName = input("course name\n").strip()
                        courseScore = int(input("course score\n").strip())
                        stuR.set_score(courseName, courseScore)
                    case "del":
                        courseName = input("course name\n").strip()
                        stuR.delete_class(courseName)
                    case _:
                        print("input wrong\n")

    if FlagD:
        print(f"student{stuNum} is not found")





optSCorSorC = ""
NstuR =Student(0,schedule)

while True:
    print(f"admin{adminA.stuNum} is operating\n")
    finish = input("input break to finish, press key 'enter' to continue\n")

    if finish == "break":
        break
    while True:
        optSCorSorC = input("Operations of student's course(sc) or course(c) or student(s), input end to finish \n").strip()
        if optSCorSorC =="end":
            break
        if optSCorSorC == "sc":
            while True:
                stuNum = int(input("SC: chose a student by their number, 100 means break\n").strip())
                FlagDD = True
                if stuNum == 100:
                    break
                for NstuN in stuTeam:
                    if NstuN.stuNum == stuNum:
                        NstuR = NstuN
                        FlagDD = False
                        break
                if FlagDD:
                    print("no such student\n")
                    continue

                optStu = input("add or set or del , break means finish\n").strip()
                match optStu:
                    case "add":
                        courseName = input("course name\n").strip()
                        adminA.add_course(NstuR, courseName)
                    case "set":
                        courseName = input("course name\n").strip()
                        courseScore = int(input("course score\n").strip())
                        adminA.set_score(NstuR, courseName, courseScore)
                    case "del":
                        courseName = input("course name\n").strip()
                        adminA.delete_class(NstuR, courseName)
                    case "break":
                        print(f"student{stuNum}'s change by admin{adminA.stuNum} has done\n")
                    case _:
                        print("input wrong\n")

        elif optSCorSorC == "s":
            while True:
                stuNum = int(input("S: input student's number, 100 means break\n").strip())
                FlagDDD = True
                if stuNum == 100:
                    break

                for stu in stuTeam:
                    if stuNum == stu.stuNum:
                        FlagDDD = False
                        rStudent = stu
                        break
                if FlagDDD:
                    rStudent = "notIn"
                ope = input("add or mod or del\n").strip()
                match ope:
                    case "add":
                        if not rStudent == "notIn":
                            print("already has this student\n")
                        else:
                            newSt = adminA.add_stu(stuNum, *schedule)
                            stuTeam.append(newSt)
                    case "del":
                        if rStudent == "notIn":
                            print("can't find this student\n")
                        else:
                            adminA.del_stu(rStudent)
                            stuTeam.remove(rStudent)
                    case "mod":
                        if rStudent == "notIn":
                            print("can't find this student\n")
                        else:
                            newNumber =int(input("new number\n").strip())
                            adminA.mod_stu_num(rStudent, newNumber)
                    case _:
                        print("input wrong\n")

        elif optSCorSorC == "c":
            while True:
                Cname = input("C: input course name. break means finish\n").strip()
                if Cname == "break":
                    break

                ope = input("add or del or mod\n").strip()

                match ope:
                    case "add":
                        adminA.update_add_sche(Cname)
                    case "del":
                        adminA.update_del_sche(Cname, *stuTeam)

                    case "mod":
                        toName = input(f"{Cname} to ?\n".strip())
                        adminA.update_mod_shce(Cname, toName, *stuTeam)

                    case _:
                        print("input wrong\n")

print("schedule finished")
input("Press <enter>")
