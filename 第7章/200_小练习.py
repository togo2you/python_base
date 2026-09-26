class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

        Student.count += 1

        self.stu_id = f'2026{Student.count:03d}'
        self.score = dict()

    def score_add(self, subject, score):
        self.score[subject] = score

    def get_avg(self):
        if self.score:
            return sum(self.score.values()) / len(self.score)
        else:
            return 0

    def __str__(self):
        return f'{self.name}-{self.age}-{self.gender};成绩:{self.score};平均分:{self.get_avg():.2f}'

class Manager:
    def __init__(self):
        self.stu_list = []

    def add_stu(self):
        name = input('请输入学生姓名')
        age = int(input('请输入学生年龄'))
        gender = input('请输入学生性别')

        stu = Student(name, age, gender)
        self.stu_list.append(stu)

        print(f'成功添加学生信息，学生学号为{stu.stu_id}')

    def del_stu(self):
        stu_id_input = input('请输入待删除学生的学号：')

        for stu in self.stu_list:
            if stu.stu_id == stu_id_input:
                self.stu_list.remove(stu)
                print(f'学生{stu.name}信息已删除，学号{stu.stu_id}')
                return
        else:
            print(f"学号为{stu_id_input}的学生不存在，删除失败")

    def show_all_students(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print('暂无学生信息录入')

    def set_score(self):
        stu_id_input = input('请输入学号')

        for stu in self.stu_list:
            if stu.stu_id == stu_id_input:
                score_str_input = input('请输入成绩：学科-成绩，学科-成绩').replace('，', ',').split(',')
                print(score_str_input)

                for score_str in score_str_input:
                    subject_input, score_input = score_str.split('-')
                    #stu.score[subject_input] = float(score_input)
                    stu.score_add(subject_input, float(score_input))

                print("添加成功")
                return
        else:
            print('学号信息不存在，添加失败')

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
                self.add_stu()
            elif choice == '2':
                self.del_stu()
            elif choice == '3':
                self.show_all_students()
            elif choice == '4':
                self.set_score()
            elif choice == '5':
                print('系统退出。。。')
                return 0
            else:
                print('输入操作有误，请重输入')

manager1 = Manager()

manager1.run()





