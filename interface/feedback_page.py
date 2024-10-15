import tkinter as tk
import os
class FeedbackPage(tk.Frame):

    def __init__(self, master, adult_learner_menu, adult_learner_user):
        super().__init__(master)
        self.master = master
        self.adult_learner_menu = adult_learner_menu
        self.adult_learner_user = adult_learner_user

        self.page_title= tk.Label(master=self, \
                                    text=f"Hi, {adult_learner_user.first_name}, Please give us some feedback!", \
                                    font=("Arial Bold", 20))
        self.page_title.grid(row=1, columnspan=2, padx=10, pady=10)

        self.feedback_label = tk.Label(self, text="Feedback:")
        self.feedback_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.feedback_text = tk.Text(master=self, width=50, height=10)  # Width for columns, height for rows
        self.feedback_text.grid(row=2, column=1, padx=20, pady=20, sticky=tk.W)

        self.feedback_button = tk.Button(master=self, text="Submit", command=self.submit_feedback)
        self.feedback_button.grid(row=5, columnspan=2, padx=10, pady=10)
        
        self.return_label = tk.Button(self,text="return to course selection", command=self.return_to_course_selection)
        self.return_label.grid(row=6, columnspan=2, padx=10, pady=10)

    def return_to_course_selection(self):
        self.place_forget()
        self.adult_learner_menu.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def submit_feedback(self):
        try:
            file_name = "./course_data/feedback.txt"
            feedback = self.feedback_text.get("1.0", tk.END).strip()  # Get text from Text widget
            
            if os.path.exists(file_name):
                with open(file_name, "a", encoding="utf8") as f:
                    new_feedback = f"{self.adult_learner_user.first_name}: {feedback}\n"
                    f.write(new_feedback)
                    print("Feedback submitted successfully.")
                    self.feedback_text.delete("1.0", tk.END)  # Clear the text after submission
            else:
                print(f"Error: The file {file_name} does not exist. Please check the file path.")
        except FileNotFoundError:
            print(f"Error: The file {file_name} does not exist. Please check the file path.")
        except UnicodeDecodeError:
            print(f"Error: UnicodeDecodeError")