from modules.user.User import User
import os
class TeacherUser(User):
    @staticmethod
    def authenticate(input_username, input_password):
        teacher_path = f"./user_data/teachers.txt"
        if os.path.exists(teacher_path):
            with open(teacher_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                uid, first_name, last_name, contact_num, teaching_courses, username, password = line.strip("\n").split(",")
                courses_list = teaching_courses.split("&")
                if input_username == username:
                    if input_password == password:
                        return TeacherUser(uid, first_name, last_name, contact_num, courses_list, input_username, input_password)
                    else:
                        return None
        else:
            print(f"Please check subdirectory and file {teacher_path} exists.")

    def __init__(self, uid, first_name, last_name, contact_num, teaching_courses, username, password):
        """
        Constructor for the TeacherUser class
        """
        super().__init__(uid, first_name, last_name, contact_num, username, password)
        self.teaching_courses = teaching_courses
