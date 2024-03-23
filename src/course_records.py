class Course:
    def __init__(self, name: str, grade: int, credits: int) -> None:
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def grade(self):
        return self.__grade
    
    def credits(self):
        return self.__credits
    
    def update_grade(self, grade: int):
        if grade > self.__grade:
            self.__grade = grade

    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"
    
class CourseRecord:
    def __init__(self) -> None:
        self.__courses = {}

    def __update_course(self, name: str, grade: int):
        course = self.__courses[name]
        course.update_grade(grade)

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        else:
            self.__update_course(name, grade)

    def get_course_data(self, name: str):
        if name in self.__courses:
            course = self.__courses[name]
            return course
        else:
            return None

    def __print_grade_distribution(self):
        grade_dict = {}

        for course in self.__courses:
            if self.__courses[course].grade() in grade_dict:
                grade_dict[self.__courses[course].grade()] += 1
            else:
                grade_dict[self.__courses[course].grade()] = 1

        for i in range(5, 0, -1):
            print(f"{i}: {('x' * grade_dict[i]) if i in grade_dict else ''}")

    def print_stats(self):
        courses_len = len(self.__courses)
        total_credits = sum([self.__courses[course].credits() for course in self.__courses])
        total_grades = sum([self.__courses[course].grade() for course in self.__courses])
        mean = total_grades / courses_len

        print(f"{courses_len} completed courses, a total of {total_credits} credits")
        print(f"mean {round(mean, 1)}")
        print("grade distribution")
        self.__print_grade_distribution()

class CourseApplication:
    def __init__(self) -> None:
        self.__course_record = CourseRecord()

    def __help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def __add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))

        self.__course_record.add_course(name, grade, credits)

    def __get_course_data(self):
        name = input("course: ")
        course = self.__course_record.get_course_data(name)

        if course is None:
            print("no entry for this course")
        else:
            print(course)

    def execute(self):
        self.__help()

        while True:
            print()
            cmd = input("command: ")

            if cmd == "0":
                break
            elif cmd == "1":
                self.__add_course()
            elif cmd == "2":
                self.__get_course_data()
            elif cmd == "3":
                self.__course_record.print_stats()


course_application = CourseApplication()
course_application.execute()