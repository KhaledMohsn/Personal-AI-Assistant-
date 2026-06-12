import customtkinter as ctk
from datetime import datetime
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

ICONS = {
    "search": "🔍",
    "open_app": "🖥",
    "create_file": "📄",
    "chat": "💬",
    "exit": "👋",
}

GREEN = "#4ade80"
RED = "#f87171"
SUBTEXT = "#9a9a9a"
TEXT = "#e0e0e0"


class AssistantUI:
    def __init__(self, user_name="Khaled", wake_word="vevo"):
        self.root = ctk.CTk()
        self.root.title("Vevo Assistant")
        self.root.geometry("220x335")
        self.root.resizable(False, False)

        # --- Outer rounded container ---
        self.container = ctk.CTkFrame(self.root, corner_radius=20)
        self.container.pack(fill="both", expand=True, padx=8, pady=8)

        # --- Header ---
        header = ctk.CTkFrame(self.container, fg_color="transparent")
        header.pack(fill="x", padx=12, pady=(10, 0))
        ctk.CTkLabel(header, text="🤖 Vevo", font=("Segoe UI", 13, "bold")).pack(side="left")

        # --- Avatar + status ---
        self.label = ctk.CTkLabel(self.container, text="🤖", font=("Arial", 48), text_color=TEXT)
        self.label.pack(pady=(8, 4))

        self.status = ctk.CTkLabel(
            self.container,
            text=f'Listening for "{wake_word}"',
            font=("Segoe UI", 11),
            text_color=GREEN,
        )
        self.status.pack(pady=(0, 10))

        # --- Command log ---
        ctk.CTkLabel(self.container, text="Command log", font=("Segoe UI", 10), text_color=SUBTEXT)\
            .pack(anchor="w", padx=14)

        self.log_frame = ctk.CTkScrollableFrame(
            self.container, height=140, corner_radius=12, fg_color="#2a2a2a"
        )
        self.log_frame.pack(fill="both", expand=True, padx=12, pady=(4, 10))

        # --- Settings row ---
        settings = ctk.CTkFrame(self.container, fg_color="transparent")
        settings.pack(fill="x", padx=12, pady=(0, 12))


    # --- State methods (thread-safe via root.after) ---
    def set_active(self):
        self.root.after(0, self._set_active)

    def _set_active(self):
        self.label.configure(text_color=RED)
        self.status.configure(text="Listening...", text_color=RED)

    def set_idle(self):
        self.root.after(0, self._set_idle)

    def _set_idle(self):
        self.label.configure(text_color=TEXT)
        self.status.configure(text="Idle", text_color=SUBTEXT)

    def log_command(self, action: str, text: str):
        self.root.after(0, self._add_log_entry, action, text)

    def _add_log_entry(self, action: str, text: str):
        icon = ICONS.get(action, "•")
        timestamp = datetime.now().strftime("%H:%M")

        entry = ctk.CTkLabel(
            self.log_frame,
            text=f"{icon}  {text}   ({timestamp})",
            font=("Segoe UI", 10),
            text_color=TEXT,
            anchor="w",
        )
        entry.pack(fill="x", padx=8, pady=2)

        children = self.log_frame.winfo_children()
        if len(children) > 20:
            children[0].destroy()
            children = self.log_frame.winfo_children()

        # Move the new entry to the top
        if len(children) > 1:
            entry.pack_configure(before=children[0])

    def start(self, background_task):
        threading.Thread(target=background_task, daemon=True).start()
        self.root.mainloop()

    def destroy(self):
        self.root.after(0, self.root.destroy)


if __name__ == "__main__":
    # Quick preview/test
    ui = AssistantUI()
    ui.log_command("search", "search for cristiano ronaldo")
    ui.log_command("open_app", "open chrome")
    ui.log_command("create_file", "create file kk.txt")
    ui.root.mainloop()

'''
 minimal( More simple and readable ) 

import tkinter as tk
import threading


class AssistantUI :
        
    def __init__(self):
           
        self.root = tk.Tk()
        self.root.title("AI Assistant")
        self.label = tk.Label(text="🤖" , font=("Arial",120,'bold'))
        self.label.pack()             
                 
    def set_active(self):
       self.label.config(fg="red")

    def set_idle(self):
         self.label.config(fg='black')    

    def start(self,background_task):
        threading.Thread(target=background_task, daemon=True).start()
        self.root.mainloop()

    def destroy(self):
        self.root.destroy()       
       

'''        