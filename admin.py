
from student import Student

class Admin(Student):
    def __init__(self,admNum,*schedule):
        super().__init__(admNum,*schedule)
    # 针对学生选课的修改
    def add_course(self,student:Student,name):
        print(f"adding by admin{self.stuNum}")
        student.course.add_course(name)
        student.show_all()

    def delete_class(self, student:Student,name):
        print(f"deleting by admin{self.stuNum}")
        student.course.delete_class(name)
        student.show_all()

    def set_score(self, student:Student,name, score):
        print(f"setting by admin{self.stuNum}")
        student.course.set_score(name,score)
        student.show_all()

    # 针对学生的修改
    # 添加
    def add_stu(self,num,schedule:set):
        student = Student(num,schedule)
        print(f"student{num} has added by admin{self.stuNum}\n")
        return student

    def del_stu(self,student:Student):
        print(f"student{student.stuNum} has deleted by admin{self.stuNum}\n")
        del student

    def mod_stu_num(self,student:Student,num):
        oldnum = student.stuNum
        student.mod_stu_num(num)
        print(f"student{oldnum} has be modified to student{num} by admin{self.stuNum}\n")
        return student

    # 更新课程表
    def update_add_sche(self,new_course,*students:Student):
        for stu in students:
            flag=stu.course.update_add_sche(new_course)
            if flag == "AbadFlag":
                print(f"The schedule already have course {new_course}\n")
                break
        print(f"{new_course} has been added by admin{self.stuNum}\n")

    def update_del_sche(self,old_course,*students:Student):
        for stu in students:
            flag = stu.course.update_del_sche(old_course)
            if flag == "DbadFlag":
                print(f"The schedule do not have course {old_course}\n")
                break
        print(f"{old_course} has been deleted by admin{self.stuNum}\n")

    def update_mod_shce(self,old_course,new_course,*students:Student):
        for stu in students:
            flag = stu.course.update_mod_sche(old_course,new_course)
            if flag == "MbadFlag":
                print(f"Can't modify course {old_course} to course {new_course}\n")
                break
        print(f"The course {old_course} has been modified to course {new_course} by admin{self.stuNum}\n")







#   针对课程的修改






