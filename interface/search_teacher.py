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
        - receptionist_user: an instance of the ReceptionistUser class
        """
        super().__init__(master)
        self.master = master
        self.receptionist_menu = receptionist_menu
        self.receptionist_user = receptionist_user

        self.page_title = tk.Label(master=self, \
                                    text="Search Teachers based on the instrument", \
                                    font=("Arial Bold", 20))
        self.page_title.grid(row=1, columnspan=2, padx=10, pady=10)

        self.username_label = tk.Label(master=self, text="Please enter the instrument:")
        self.username_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.instrument_var = tk.StringVar(master=self)
        self.instrument_entry = tk.Entry(master=self, textvariable=self.instrument_var)
        self.instrument_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.teacher_var = tk.StringVar(master=self)
        self.teacher_label = tk.Label(master=self, textvariable=self.teacher_var)
        self.teacher_label.grid(row=3, columnspan=2, padx=10, pady=10)

        self.search_button = tk.Button(master=self, text="search", command=self.search_teachers_by_instrument)
        self.search_button.grid(row=4, columnspan=2, padx=10, pady=10)

        self.return_button = tk.Button(self, text="Return to menu", command=self.return_to_menu)
        self.return_button.grid(row=5, columnspan=2, padx=10, pady=10)


    def search_teachers_by_instrument(self):
        """
        This method handles the GUI logic to search teachers by instrument, 
        and display the full names of the teachers that teach the searched 
        instrument name.
        
        Parameters:
        (None)

        Returns:
        (None)
        """
        teacher_detail = ""
        teachers_list = self.receptionist_user.list_teachers_by_instrument(self.instrument_var.get())
        for teacher in teachers_list:
            teacher_detail += ("Teacher ID: "+teacher.uid + ", " + "Teacher Name: " + teacher.first_name + " " +
                               teacher.last_name + ", " + "Contact Number: " + teacher.contact_num + "\n")
        if len(teachers_list) == 0:
            self.teacher_var.set(f"The search is not successful, please try again")
        else:
            self.teacher_var.set(teacher_detail)
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