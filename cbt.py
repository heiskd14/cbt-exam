import random
import json
import time
import csv
from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox, simpledialog


def load_questions(filename):
    with open(filename, "r") as f:
        return json.load(f)


def save_result(name, subject, score, total):
    percent = (score / total) * 100
    try:
        with open("results.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, subject, score, total, f"{percent: 2f}%"])
    except Exception as e:
        print("Error saving results:", e)


class CBTExam:
    def __init__(self, master, student_name, subject_name, filename, num_questions=30, duration_minutes=60):
        self.master = master
        self.student_name = student_name
        self.subject_name = subject_name
        self.questions = load_questions(filename)
        self.num_questions = min(num_questions, len(self.questions))
        self.selected = random.sample(self.questions, self.num_questions)
        self.current_index = 0
        self.score = 0
        self.start_time = time.time()
        self.total_time = duration_minutes * 60
        self.create_ui()
        self.show_question()
        self.update_timer()

    def create_ui(self):
        self.master.title(
            f"{self.subject_name} CBT Exam - {self.student_name}")

        self.timer_label = tk.Label(
            self.master, text="", font=("Times New Roman", 14), fg="red")
        self.timer_label.pack(pady=5)

        self.question_label = tk.Label(
            self.master, text="", wraplength=480, justify="left", font=("Arial", 12))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            letter = chr(65 + i)  # 'A', 'B', 'C', 'D'
            btn = tk.Button(
                self.master,
                text="",
                font=("Arial", 12),
                width=50,
                anchor="w",
                command=lambda o=letter: self.check_answer(o),
            )
            btn.pack(pady=4, fill="x", padx=10)
            self.option_buttons.append(btn)

    def update_timer(self):
        elapsed = time.time() - self.start_time
        remaining = int(self.total_time - elapsed)

        if remaining <= 0:
            messagebox.showinfo("Time Up", "Time is Up!")
            self.finish_exam()
            return

        minutes = remaining // 60
        seconds = remaining % 60

        self.timer_label.config(text=f"Time Left: {minutes:02d}:{seconds:02d}")
        self.master.after(1000, self.update_timer)

    def show_question(self):
        if self.current_index >= self.num_questions:
            self.finish_exam()
            return

        q = self.selected[self.current_index]
        # q expected to be a dict with 'question', 'options' (list), and 'answer' (letter)
        self.question_label.config(
            text=f"Question {self.current_index + 1}: {q['question']}")

        for i, opt_text in enumerate(q.get('options', [])):
            if i < len(self.option_buttons):
                self.option_buttons[i].config(text=f"{chr(65+i)}. {opt_text}")

    def check_answer(self, choice):
        q = self.selected[self.current_index]
        correct = str(q.get('answer', '')).upper().strip()

        if choice == correct:
            self.score += 1

        self.current_index += 1
        self.show_question()

    def finish_exam(self):
        percent = (self.score / self.num_questions) * \
            100 if self.num_questions else 0
        save_result(self.student_name, self.subject_name,
                    self.score, self.num_questions)

        messagebox.showinfo(
            "Exam Finished",
            f"{self.subject_name} Exam Completed!\n"
            f"Student: {self.student_name}\n"
            f"Score: {self.score}/{self.num_questions}\n"
            f"Percentage: {percent:.2f}%"
        )
        self.master.destroy()


def main():
    def start_subject(subject, file):
        name = simpledialog.askstring("Student Name", "Enter your full name:")
        if not name:

            messagebox.showwarning(
                "Missing Name", "Please enter your name to continue.")
            return
    selector.destroy()
    root = tk.Tk
    CBTExam("root", "name", "subject", "file")
    root.mainloop()

    selector = tk.TK()
    selector.title("CBT EXAM")

    tk.Label(selector, text="Select a Subject",
             font=("Arial", 14, "bold")).pack(pady=10)
    tk.Button(selector, text="English", width=25, command=lambda: start_subject(
        "English", "english.json")).pack(pady=5)
    tk.Button(selector, text="Mathematics", width=25, command=lambda: start_subject(
        "Mathematics", "maths.json")).pack(pady=5)
    tk.Button(selector, text="General Paper", width=25, command=lambda: start_subject(
        "General Paper", "general.json")).pack(pady=5)
