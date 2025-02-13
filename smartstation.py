import os
import tkinter as tk
from tkinter import simpledialog, messagebox
import json

class SmartStation:
    def __init__(self, master):
        self.master = master
        self.master.title("SmartStation")
        self.notes = {}
        self.load_notes()
        self.create_widgets()

    def create_widgets(self):
        self.create_note_button = tk.Button(self.master, text="Create Note", command=self.create_note)
        self.create_note_button.pack(pady=10)

        self.notes_frame = tk.Frame(self.master)
        self.notes_frame.pack(fill=tk.BOTH, expand=True)
        self.display_notes()

    def create_note(self):
        note_title = simpledialog.askstring("Input", "Enter note title:")

        if note_title:
            note_content = simpledialog.askstring("Input", "Enter note content:")
            if note_content is not None:
                self.notes[note_title] = note_content
                self.save_notes()
                self.display_notes()

    def display_notes(self):
        for widget in self.notes_frame.winfo_children():
            widget.destroy()

        for title, content in self.notes.items():
            note_frame = tk.Frame(self.notes_frame, pady=5, padx=5, relief=tk.RAISED, bd=1)
            note_frame.pack(fill=tk.X, padx=10, pady=5)

            title_label = tk.Label(note_frame, text=title, font=('Arial', 12, 'bold'))
            title_label.pack(anchor='w')

            content_label = tk.Label(note_frame, text=content, justify='left')
            content_label.pack(anchor='w')

            delete_button = tk.Button(note_frame, text="Delete", command=lambda t=title: self.delete_note(t))
            delete_button.pack(anchor='e')

    def delete_note(self, title):
        if messagebox.askyesno("Delete Note", f"Are you sure you want to delete the note titled '{title}'?"):
            del self.notes[title]
            self.save_notes()
            self.display_notes()

    def save_notes(self):
        with open('notes.json', 'w') as f:
            json.dump(self.notes, f)

    def load_notes(self):
        if os.path.exists('notes.json'):
            with open('notes.json', 'r') as f:
                self.notes = json.load(f)

def main():
    root = tk.Tk()
    root.geometry("400x500")
    app = SmartStation(master=root)
    root.mainloop()

if __name__ == "__main__":
    main()