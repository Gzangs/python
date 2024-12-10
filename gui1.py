from tkinter import *
from tkinter import messagebox
import functions1
import csv

class VotingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voting System")
        """
        Initialize vote counts
        """
        self.p1votes = 0
        self.p2votes = 0
        self.voter_id = ""

        """
        Set up the main menu frame
        """
        self.main_menu_frame = Frame(self.root)
        self.main_menu_frame.pack(padx=20, pady=20)

        self.vote_button = Button(self.main_menu_frame, text="Vote", command=self.show_vote_menu)
        self.vote_button.grid(row=0, column=0, padx=10, pady=10)

        self.quit_button = Button(self.main_menu_frame, text="Quit", command=self.quit_application)
        self.quit_button.grid(row=1, column=0, padx=10, pady=10)

    def show_vote_menu(self):
        """
        Hide main menu and show the vote menu
        """
        self.main_menu_frame.pack_forget()

        self.vote_menu_frame = Frame(self.root)
        self.vote_menu_frame.pack(padx=20, pady=20)

        self.vote_for_label = Label(self.vote_menu_frame, text="Vote for Candidate:")
        self.vote_for_label.grid(row=0, column=1, padx=10, pady=10)

        self.id_label = Label(self.vote_menu_frame, text="Enter ID (5 digit number):")
        self.id_label.grid(row=1, column=1, padx=10, pady=10)

        validate_id = self.root.register(self.validate_id)
        self.id_entry = Entry(self.vote_menu_frame, validate="key", validatecommand=(validate_id, "%P"))
        self.id_entry.grid(row=2, column=1, padx=10, pady=10)

        self.john_button = Button(self.vote_menu_frame, text="John", command=self.vote_for_john)
        self.john_button.grid(row=3, column=0, padx=10, pady=10)

        self.jane_button = Button(self.vote_menu_frame, text="Jane", command=self.vote_for_jane)
        self.jane_button.grid(row=3, column=2, padx=10, pady=10)

        self.back_button = Button(self.vote_menu_frame, text="Back", command=self.back_to_main_menu)
        self.back_button.grid(row=4, column=1, padx=10, pady=10)

    def validate_id(self, new_value):
        """
        Validates the ID so it's numeric and 5 characters long
        """
        if len(new_value) == 0:
            return True
        if len(new_value) > 5:
            return False
        return new_value.isdigit()

    def vote_for_john(self):
        self.voter_id = self.id_entry.get()
        if len(self.voter_id) == 5:
            self.p1votes = functions1.add_vote(self.p1votes)
            messagebox.showinfo("Voted", f"Voted for John with ID: {self.voter_id}")
            with open('data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([f"{self.voter_id} voted for John"])
            self.back_to_main_menu()
        else:
            messagebox.showerror("Invalid ID", "Please enter a valid 5-digit numeric ID.")

    def vote_for_jane(self):
        self.voter_id = self.id_entry.get()
        if len(self.voter_id) == 5:
            self.p2votes = functions1.add_vote(self.p2votes)
            messagebox.showinfo("Voted", f"Voted for Jane with voter ID: {self.voter_id}")
            with open('data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([f"{self.voter_id} voted for Jane"])
            self.back_to_main_menu()
        else:
            messagebox.showerror("Invalid ID", "Please enter a valid 5-digit numeric ID.")

    def back_to_main_menu(self):
        """
        Hide vote menu and show main menu
        """
        self.vote_menu_frame.pack_forget()
        self.main_menu_frame.pack(padx=20, pady=20)

    def quit_application(self):
        """
        Show a confirmation dialog before quitting
        """
        if messagebox.askyesno("Quit", "Are you sure you want to end the vote and quit?"):
            with open('data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                total = functions1.total_votes(self.p1votes, self.p2votes)
                writer.writerow([f"John Votes: {self.p1votes}", f" Jane Votes: {self.p2votes}", f" Total Votes: {total}"])
                self.root.quit()
