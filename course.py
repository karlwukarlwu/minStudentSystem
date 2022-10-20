class Course:
    # 课程名称、课程分数
    def __init__(self,*set:set):
        self.dic = {}
        self.schedule = set



    def update_add_sche(self,new_course):
        if not new_course in self.schedule:
            self.schedule.add(new_course)
        else:
            return "AbadFlag"

    def update_del_sche(self,old_course):
        if old_course in self.schedule:
            self.schedule.remove(old_course)
        else:
            return "DbadFlag"

    def update_mod_sche(self,old_course,new_course):
        if (old_course not in self.schedule) or (new_course in self.schedule):
            return "MbadFlag"
        self.schedule.add(new_course)
        self.schedule.remove(old_course)



    # add一门分数为0的课程
    def add_course(self, name):
        if self.find_optional(name):
            print("adding failed")
            return
        if not(self.find_course(name)=="Flag"):
            print("already enrolled in this course")
            return
        self.dic[name] = 0
        print("adding succeed")


    # 直接删除这门课程
    def del_course(self, name):
        if self.find_course(name)=="Flag":
            print("deleting failed")
            return
        del self.dic[name]
        print("deleting succeed")

    # 给这个课程设置分数
    def set_score(self, name, score):
        #
        if self.find_course(name)=="Flag":
            print("name can not find")
            print("setting failed")
            return
        if not(self.test_score(score)):
            print("score illegal")
            print("setting failed")
            return
        self.dic[name] = score
        print("setting succeed")

    # 判断课程是否合法
    def find_optional(self,name):
        if name in self.schedule:
            return False
        else:
            print("The class you choose is not in this semester's the schedule")
            return True

    # 判断是否找到了名字，找到返回姓名，找不到返回false
    def find_course(self, name):
        return self.dic.get(name, "Flag")
    # 判断成绩是否合法
    def test_score(self, score):
        return score >= 0
