from datetime import datetime

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    #类属性
    count = 0

    #初始化学生对象
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

        Student.count += 1
        self.sut_id = f'{datetime.now().year}{Student.count:03d}'
        self.scores = {}

    #给当前学生添加成绩信息
    def add_score(self, subjet, score):
        self.scores[subjet] = score

    def cal_avg(self):
        if self.scores:
            return sum(self.scores.values()) / len(self.scores)
        else:
            return 0

    def __str__(self):
        return f'{self.name}-{self.age}-{self.gender}，成绩：{self.scores}，平均分：{self.cal_avg():.2f}'


class Manager:
    def __init__(self):
        self.stu_list = []

    def add_student(self):
        name = input('请输入学生姓名')
        age = int(input('请输入学生年龄'))
        gender = input('请输入学生性别')

        stu = Student(name, age, gender)
        self.stu_list.append(stu)
        print(f'添加学生信息成功！学号是：{stu.sut_id}')

    def del_student(self):
        stu_id_input = input('请输入删除学生的学号')

        for stu in self.stu_list:
            if stu.sut_id == stu_id_input:
                self.stu_list.remove(stu)
                print(f'成功删除了学号是{stu.sut_id}的学生信息！')
                return
        else:
            print(f"输入的{stu_id_input}学号信息有误，删除失败！")

    def show_all_students(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print('暂无学生信息输入')

    def set_score(self):
        stu_id_input = input('请输入学号')

        for stu in self.stu_list:
            if stu.sut_id == stu_id_input:
                score_str = input('请输入成绩（学科-分数，学科-分数）')
                score_list = score_str.replace('，', ',').split(',')

                for score in score_list:
                    subjet, score = score.split('-')
                    subjet = subjet.strip()
                    score = float(score)

                    stu.add_score(subjet, score)

                print('学生成绩添加成功！')
                return

        print('输入学号有误！')

    def run(self):
        while True:
            print('************学生管理************')
            print('1. 添加学生')
            print('2. 删除学生')
            print('3. 查看所有学生')
            print('4. 录入成绩')
            print('5. 退出')

            choice = input('请输入操作编号：')

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.del_student()
            elif choice == '3':
                self.show_all_students()
            elif choice == '4':
                self.set_score()
            elif choice == '5':
                print('系统退出。。。')
                break
            else:
                print('输入有误！')

m1 = Manager()
m1.run()