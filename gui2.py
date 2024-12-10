from tkinter import *
from tkinter import messagebox
import functions2
import csv


class GradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grading System")

        """
        Creates widgets
        """
        self.student_name_label = Label(root, text="Enter the student's name:")
        self.student_name_label.pack(padx=20, pady=20)

        self.student_name_entry = Entry(root)
        self.student_name_entry.pack(padx=20, pady=10)

        self.num_assignments_label = Label(root, text="Enter the number of attempts:")
        self.num_assignments_label.pack(padx=20, pady=10)

        self.num_assignments_entry = Entry(root)
        self.num_assignments_entry.pack(padx=20, pady=10)

        self.enter_scores_button = Button(root, text="Enter Scores", command=self.enter_scores)
        self.enter_scores_button.pack(padx=20, pady=20)


        self.score_entries_frame = Frame(root)
        self.score_entries_frame.pack(padx=20, pady=20)

        self.submit_button = None

    def enter_scores(self):
        """
        Get the student's name and the number of attempts
        """
        student_name = self.student_name_entry.get()
        try:
            num_attempts = int(self.num_assignments_entry.get())
            if num_attempts < 1 or num_attempts > 4:
                raise ValueError("Number of attempts must be between 1 and 4.")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid number of attempts: {e}")
            return

        if not student_name:
            messagebox.showerror("Input Error", "Please enter a student's name.")
            return

        for widget in self.score_entries_frame.winfo_children():
            widget.destroy()

        self.score_entries = []

        for i in range(num_attempts):
            Label(self.score_entries_frame, text=f"Enter score for attempt {i + 1}:").grid(row=i, column=0)
            score_entry = Entry(self.score_entries_frame)
            score_entry.grid(row=i, column=1)
            self.score_entries.append(score_entry)

        if self.submit_button:
            self.submit_button.destroy()

        self.submit_button = Button(self.root, text="Submit Scores", command=self.submit_scores)
        self.submit_button.pack(pady=20)

    def submit_scores(self):
        """
        Collect scores from the user input and calculate the final grade
        """
        student_name = self.student_name_entry.get()
        try:
            scores = []
            for entry in self.score_entries:
                score = int(entry.get())
                if score < 0 or score > 100:
                    raise ValueError("Scores must be between 0 and 100.")
                scores.append(score)

            if len(scores) != len(self.score_entries):
                raise ValueError("Number of scores does not match the number of attempts.")

            final_grade = functions2.calculate_final_grade(scores)
            lowest_score = min(scores)
            highest_score = max(scores)

            self.save_results(student_name, scores, final_grade, lowest_score, highest_score)

            self.submit_button.destroy()

        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid score input: {e}")

    def save_results(self, student_name, scores, average_grade, lowest_score, highest_score):
        """
        Saves the student's name, scores, final grade, lowest score, and highest score to a csv file
        """
        with open('grades.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f"Name: {student_name}, {scores}, Grade: {highest_score}, Lowest score: {lowest_score}, Average score: {average_grade}"])
        messagebox.showinfo("Success", "Scores and grades have been saved.")

        self.student_name_entry.delete(0, END)
        self.num_assignments_entry.delete(0, END)

        for widget in self.score_entries_frame.winfo_children():
            widget.destroy()
        self.score_entries = []


