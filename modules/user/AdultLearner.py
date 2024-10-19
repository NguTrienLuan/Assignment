from modules.user.User import User
import os
class AdultLearner(User):
    
    @staticmethod
    def authenticate(input_username, input_password):
        teacher_path = f"./user_data/adult_learners.txt"
        if os.path.exists(teacher_path):
            with open(teacher_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                uid, first_name, last_name, dob, contact_num, enrolled_courses, username, password = line.strip("\n").split(",")
                courses_list = enrolled_courses.split("&")
                if input_username == username:
                    if input_password == password:
                        return AdultLearner(uid, first_name, last_name,dob, contact_num, courses_list, input_username, input_password)
                    else:
                        return None
        else:
            print(f"Please check subdirectory and file {teacher_path} exists.")

    def __init__(self, uid, first_name, last_name, dob, contact_num, enrolled_courses, username, password,):
        """
        Constructor for the StudentUser class
        """
        super().__init__(uid, first_name, last_name, contact_num, username, password)
        self.enrolled_courses = enrolled_courses
        
        self.dob = dob
        

if __name__ == "__main__":
    pass