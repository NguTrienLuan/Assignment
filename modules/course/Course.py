import os
class Course():
    def __init__(self, name):
        self.name = name
        self.course_name = self.name.strip().replace(" ", "_")
        self.data_file_name = f"../course_data/students_data/{self.course_name}.txt"
        self.lecture_file_name = f"../course_data/course_lecture/{self.course_name}.txt"
        self.quiz_file_name = f"../course_data/course_quizzes/{self.course_name}.txt"
        self.course_initialization()

    def course_initialization(self):
        self.lectures = []
        self.quizzes = []
        try:
            with open(self.lecture_file_name, "r", encoding="utf8") as lf:
                content = lf.read()
                self.lectures.append(content)
            with open(self.quiz_file_name,"r", encoding="utf8") as qf:
                content = qf.read()
                self.quiz.append(content)
        except FileExistsError:
            print(f"Error: The file {self.course_name}.txt does not exist. Please check the course name.")
        except UnicodeDecodeError:
            print(f"Error: UnicodeDecodeError")


    def add_a_student(self, student):
        try:
            if os.path.exists(self.data_file_name):
                with open(self.data_file_name, "a", encoding="utf8") as f: 
                    new_student_line = f"{student.uid},{student.first_name},{student.last_name},,\n"
                    f.write(new_student_line)
                return True
        except FileExistsError:
            print(f"Error: The file {self.course_name}.txt does not exist. Please check the course name.")
        except UnicodeDecodeError:
            print(f"Error: UnicodeDecodeError")

    def update_status(self, student_name, quiz_status=False, lecture_status=False):
        with open(self.data_file_name, "r", encoding="utf8") as f:
            lines = f.readlines()
        with open(self.data_file_name, "w", encoding="utf8") as f:
            try:
                for line in lines:
                    if line.startswith(student_name):
                        line_parts = line.strip().split(',')
                        if quiz_status is True:
                            line_parts[3] = "completed"
                        if lecture_status is True:
                            line_parts[4] = "completed"
                        updated_line = ','.join(line_parts) + "\n"
                        f.write(updated_line)
                    else:
                        f.write(line)
            except FileExistsError:
                print(f"Error: The file {self.course_name}.txt does not exist. Please check the course name.")
            except UnicodeDecodeError:
                print(f"Error: UnicodeDecodeError")

    def calculate_course_track(self, student_name):
        all_tasks_counter = len(self.quizzes) + len(self.lectures)
        result = 0
        try:
            with open(self.data_file_name, "r", encoding="utf8") as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith(student_name):
                        line_parts = line.strip().split(',')
                        for element in range(2,len(line_parts)):
                            if element =="complete":
                                result += 1
                        result = result/all_tasks_counter * 100
                        return result
        except FileNotFoundError:
            print(f"Error: The file {self.course_name}.txt does not exist. Please check the course name.")

    
    def watch_the_lecture(self):
        try:
            with open(self.lecture_file_name, "r", encoding="utf8") as f:
                content = f.read()
                return content 
        except FileNotFoundError:
            return f"Error: The file {self.lecture_file_name} does not exist. Please check the course name."
        except UnicodeDecodeError:
                print(f"Error: UnicodeDecodeError")


