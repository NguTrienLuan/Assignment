import os
from modules.user.User import User
from modules.user.AdultLearner import AdultLearner
from modules.user.TeacherUser import TeacherUser
class ReceptionistUser(User):

    @staticmethod
    def authenticate(input_username, input_password, path_to_root="."):
        """
        Method to authenticate a ReceptionistUser user.

        Parameter(s):
        - input_username: str
        - input_password: str

        Returns:
        - an instance of ReceptionistUser corresponding to the username if successful,
          None otherwise
        """
        recept_path = f"{path_to_root}/user_data/receptionists.txt"
        if os.path.exists(recept_path):
            with open(recept_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                # Sequence unpacking: 
                # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
                recept_id, first_name, last_name, contact_num, username, password = line.strip("\n").split(",")
                
                if input_username == username:
                    if input_password == password:
                        return ReceptionistUser(recept_id, first_name, last_name, contact_num, input_username, input_password, path_to_root)
                    else:
                        return None # or return, or break
        else:
            print(f"Please check subdirectory and file {recept_path} exists.")
        

    def __init__(self, uid, first_name, last_name, contact_num, username, password, path_to_root=".."):
        """
        Constructor method for the ReceptionistUser class
        """
        super().__init__(uid, first_name, last_name, contact_num,username,password)
        self.import_all_data(path_to_root)

    def import_all_data(self, path_to_root):
        """
        Method to read all data by calling methods to read teachers data and students data.

        Parameter(s):
        - path_to_root: str

        Returns:
        (None)
        """
        self.import_teachers_data(path_to_root)
        self.import_students_data(path_to_root)

    def import_teachers_data(self, path_to_root):
        """
        Method to read teachers data and store it into the receptionist's session.

        Parameter(s):
        path_to_root: str, default is the local of the main.py file

        Returns:
        (None)
        """
        self.teachers = []
        teachers_path = f"{path_to_root}/user_data/teachers.txt"
        if os.path.exists(teachers_path):
            with open(teachers_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                # Sequence unpacking
                # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
                uid, first_name, last_name, contact_num, courses_name, username, password = line.strip("\n").split(",")
                courses_list = courses_name.split("&")
                teacher_obj = TeacherUser(uid, first_name, last_name, contact_num, courses_list, username, password)
                self.teachers.append(teacher_obj)
        else:
            print(f"Please check the subdirectory and file exists for {teachers_path}.")

    def import_students_data(self, path_to_root):
        """
        Method to read students data and store it into the receptionist's session.

        Parameter(s):
        path_to_root: str, default is the local of the main.py file

        Returns:
        (None)
        """
        self.students = []
        students_path = f"{path_to_root}/user_data/adult_learners.txt"
        if os.path.exists(students_path):
            with open(students_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                student_id, first_name, last_name, contact_num, courses_name, username, password = line.strip("\n").split(",")
                enrolled_courses = courses_name.split("&")
                student_obj = AdultLearner(student_id, first_name, last_name, contact_num, enrolled_courses, username, password)
                self.students.append(student_obj)
        else:
            print(f"Please check the subdirectory and file exists for {students_path}.")


    def list_teachers_by_instrument(self, instrument):
        """
        This method retrieves Teachers that are qualified to teach the specified instrument

        Parameter(s):
        - instrument: str, the instrument to be searched
        
        Returns:
        - list: list of Teacher objects that match the criteria
        """
        results = []
        for teacher_obj in self.teachers:
            if instrument.title() in teacher_obj.instruments:
                results.append(teacher_obj)
                continue

        return results

    def store_student_data(self, first_name, last_name, date_of_birth, contact_name, contact_num, username, password, path_to_root=".."):
        """
        Method to register the student in the system 
        and write the data of the new student into the file.

        Parameter(s):
        - first_name: str, student's first name
        - last_name: str, student's last name
        - date_of_birth: str, student's date of birth
        - contact_name: str, name of student's contact person
        - contact_num: str, contact number of either student or contact person

        Returns:
        - bool: True if student data is stored from the system into the txt file, 
                False otherwise
        """

        # Create the Student object
        # Assume no skips in student ID
        student_id = "s" + str(len(self.students) + 1).zfill(4)
        student_obj = AdultLearner(student_id, first_name, last_name, date_of_birth, contact_name, contact_num,username,password)
        self.students.append(student_obj)

        # Write to data/pst5_students.txt in a comma-separated format
        filepath = f"{path_to_root}/user_data/students.txt"
        if os.path.exists(filepath):
            with open(filepath, "a", encoding="utf8") as f:
                new_student_line = f"{student_id},{first_name},{last_name},{date_of_birth},{contact_name},{contact_num}"
                f.write(new_student_line + "\n")
            return True
        else:
            print(f"Please check the subdirectory and file {filepath} exists!")
            return False

    def store_lesson_data(self, day_of_week, start_time, duration_minutes, instrument, teacher_id, capacity, path_to_root=".."):
        """
        This method creates a lesson that is held weekly.

        Parameters:
        - day_of_week: str, name of the day of the week (e.g. Monday, Tuesday, etc.)
        - start_time: str, in HH:mm format (e.g. 08:00)
        - duration_minutes: int, number of minutes
        - instrument: str, name of the instrument
        - teacher_id: str, id of the teacher 
        - capacity: int, maximum number of students that can be enrolled into this lesson

        Returns:
        - bool: True if lesson data is stored from the system into the txt file, 
                False otherwise
        """

        # Write to pst5_lessons.txt in a comma-separated format
        filepath = f"{path_to_root}/user_data/pst5_lessons.txt"
        if os.path.exists(filepath):
            with open(filepath, "a", encoding="utf8") as f:
                new_class_line = f"{day_of_week},{start_time},{duration_minutes},{instrument},{teacher_id},{capacity}"
                f.write(new_class_line + "\n")
            return True
        else:
            print(f"Please check the subdirectory and file {filepath} exists!")
            return False

if __name__ == "__main__":
    pass
