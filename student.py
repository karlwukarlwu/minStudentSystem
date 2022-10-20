from course import Course


class Student:
    # 增删改
    def __init__(self, stuNum, *schedule:set):
        self.stuNum = stuNum
        self.course = Course(*schedule)


    def mod_stu_num(self,num):
        self.stuNum=num
        print(f"student's new Number is {num}\n")

    # 学生直接通过这个加课
    def add_course(self, name):
        print(f"adding by student{self.stuNum}")
        self.course.add_course(name)
        self.show_all()

    # 学生通过这个设置成绩
    def set_score(self, name, score):
        print(f"setting by student{self.stuNum}")
        self.course.set_score(name, score)
        self.show_all()

    # 删除学生的课程
    def delete_class(self, name):
        print(f"deleting by admin{self.stuNum}")
        self.course.del_course(name)
        self.show_all()

    # 展示学生所有的成绩
    def show_all(self):
        if self.course.dic == {}:
            print("enrol none")
            print("\n")
            return

        for k,v in self.course.dic.items():
            print(f"course name {k}, course score {v}")
        print("")

    def show_schedule(self):
        print(self.course.schedule)
        print("")


