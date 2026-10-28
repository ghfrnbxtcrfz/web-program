class Faculty:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Faculty: {self.__name}")


class Job:
    def __init__(self, title, company):
        self.__title = title
        self.__company = company

    @property
    def title(self):
        return self.__title

    @property
    def company(self):
        return self.__company

    def display_info(self):
        print(f"Job: {self.__title} at {self.__company}")


class Student:
    def __init__(self, name, faculty):
        self.__name = name
        self.__faculty = faculty

    @property
    def name(self):
        return self.__name

    @property
    def faculty(self):
        return self.__faculty

    def display_info(self):
        print(f"Student: {self.__name}")

    def study(self):
        print(f"{self.name} studies at {self.faculty.name}")


class Employee:                          # ← на уровне модуля, не внутри Student
    def __init__(self, name):
        self.__name = name
        self.__jobs = []

    @property
    def name(self):
        return self.__name

    @property
    def jobs(self):
        return self.__jobs

    def add_job(self, job):
        self.__jobs.append(job)

    def display_info(self):
        print(f"Name: {self.__name} ")

    def work(self):
        print(f"{self.name} works")

def main():
    fit = Faculty("ФМФ")

    student = Student("ПОпова А.Д.", fit)
    student.display_info()
    student.study()
    print(f"Факультет студента: {student.faculty.name}")

    employee = Employee("Петров С.С.")
    employee.add_job(Job("Python-разработчик", "ООО Цветочек"))
    employee.add_job(Job("Преподаватель", "Университет"))

    employee.display_info()
    employee.work()
    for job in employee.jobs:
        job.display_info()


if __name__ == "__main__":
    main()