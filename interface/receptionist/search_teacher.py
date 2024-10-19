"""
FIT1056 2024 Semester 2
Programming Concepts Task 4

This file contains the class definition for the SearchTeachers class.
"""

# Third party imports
import tkinter as tk

class SearchTeachers(tk.Frame):
    def __init__(self, master, receptionist_menu, receptionist_user):
        """
        Constructor for the SearchTeachers class.

        Parameters:
        - master: master widget of this widget instance
        - receptionist_menu: an instance of the ReceptionistMenu class
        """
        super().__init__(master)
        self.master = master
        self.receptionist_menu = receptionist_menu
        self.receptionist_user = receptionist_user

        self.page_title = tk.Label(master=self, \
                                    text="Search Teachers based on the course", \
                                    font=("Arial Bold", 20))
        self.page_title.grid(row=1, columnspan=2, padx=10, pady=10)

        self.username_label = tk.Label(master=self, text="Please enter the course:")
        self.username_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.instrument_var = tk.StringVar(master=self)
        self.instrument_entry = tk.Entry(master=self, textvariable=self.instrument_var)
        self.instrument_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.teacher_var = tk.StringVar(master=self)
        self.teacher_label = tk.Label(master=self, textvariable=self.teacher_var)
        self.teacher_label.grid(row=3, columnspan=2, padx=10, pady=10)

        self.search_button = tk.Button(master=self, text="search", command=self.search_teachers_by_courses)
        self.search_button.grid(row=4, columnspan=2, padx=10, pady=10)

        self.return_button = tk.Button(self, text="Return to menu", command=self.return_to_menu)
        self.return_button.grid(row=5, columnspan=2, padx=10, pady=10)


    def search_teachers_by_courses(self):
        """
        This method handles the GUI logic to search teachers by instrument, 
        and display the full names of the teachers that teach the searched 
        instrument name.
        
        Parameters:
        (None)

        Returns:
        (None)
        """
        teachers_list = self.receptionist_user.list_teachers_by_courses(self.instrument_var.get())

        if len(teachers_list) == 0:
            self.teacher_var.set("The search is not successful, please try again.")
        else:
            # Create headers with manual spacing
            teacher_detail = f"{'Teacher ID':<15}{'Teacher Name':<25}{'Contact No':<15}\n"
            teacher_detail += "-" * 55 + "\n"  # Separator line

            # Add each teacher's information
            for teacher in teachers_list:
                teacher_detail += f"{teacher.uid:<15}{teacher.first_name + ' ' + teacher.last_name.upper():<25}{teacher.contact_num:<15}\n"
            
            # Set the formatted teacher details in the StringVar
            self.teacher_var.set(teacher_detail)

        # Clear the instrument entry field after the search
        self.instrument_entry.delete(0, tk.END)


    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.receptionist_menu.place(relx=.5, rely=.5, anchor=tk.CENTER)

if __name__ == "__main__":
    # DO NOT MODIFY
    pass