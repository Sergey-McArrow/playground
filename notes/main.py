import customtkinter as CTk
from PIL import Image
import json
import os
from warningWindow import WarningWindow

class NotesApp(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("My Notes")
        self.notes = self.load_notes()
        self.selected_index = None
        self.note_widgets = []
        self.entry_note = CTk.CTkEntry(master=self, width=300)
        self.entry_note.pack(pady=(20, 10))
        self.entry_note.focus()
        self.btn_add = CTk.CTkButton(master=self, text="Add note", command=self.add_note)
        self.btn_add.pack(pady=(0, 20))
        self.scrollable_frame = CTk.CTkScrollableFrame(master=self)
        self.scrollable_frame.pack(expand=True, fill="both", padx=20)
        self.edit_icon = CTk.CTkImage(dark_image=Image.open("edit.png"), size=(30,30))
        self.delete_icon = CTk.CTkImage(dark_image=Image.open("delete.png"), size=(30,30))
        self.warning_window = None
        self.update_note_list()
        
    def save_notes(self):
        with open('notes.json', 'w') as file:
            json.dump(self.notes, file, indent=4)

    def load_notes(self):
        if os.path.exists('notes.json'):
            with open('notes.json', 'r') as file:
                return json.load(file)
        return []

    def add_note(self):
        note_text = self.entry_note.get()
        if note_text:
            self.notes.append(note_text)
            self.update_note_list()
            self.entry_note.delete(0, 'end')
            self.save_notes()
        else:
            self.open_warning()

    def update_note_list(self):
        for widget in self.note_widgets:
            widget.destroy()
        self.note_widgets.clear()
        for index, note in enumerate(self.notes):
            frame = CTk.CTkFrame(master=self.scrollable_frame)
            frame.pack(fill="x", padx=5, pady=5)
            text = CTk.CTkLabel(master=frame, text=note, anchor="w", width=50)
            text.pack(side="left", padx=(5, 10), expand=True)
            btn_edit = CTk.CTkButton(master=frame, image=self.edit_icon, text="", command=lambda idx=index: self.edit_note(idx))
            btn_edit.pack(side="left", padx=5)
            btn_delete = CTk.CTkButton(master=frame, image=self.delete_icon, text="", command=lambda idx=index: self.delete_note(idx))
            btn_delete.pack(side="left", padx=5)
            self.note_widgets.append(frame)

    def edit_note(self, index):
        current_note = self.notes[index]
        dialog = CTk.CTkInputDialog(text="Type in a number:", title="Edit")
        new_note = dialog.get_input()
        if new_note:
            self.notes[index] = new_note
            self.update_note_list()
            self.save_notes()

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]
            self.update_note_list()
            self.save_notes()

    def open_warning(self):
        if self.warning_window is None or not self.warning_window.winfo_exists():
            self.warning_window = WarningWindow(self)
        else:
            self.warning_window.focus()

if __name__ == "__main__":
    app = NotesApp()
    app.mainloop()
