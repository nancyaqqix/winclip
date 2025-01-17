import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip

class WinClip:
    def __init__(self, root):
        self.root = root
        self.root.title("WinClip")
        self.root.geometry("400x300")
        
        self.clips = []
        
        self.setup_ui()
        
    def setup_ui(self):
        self.clip_listbox = tk.Listbox(self.root, height=15, width=50)
        self.clip_listbox.pack(pady=10)
        
        self.add_clip_button = ttk.Button(self.root, text="Add Clip", command=self.add_clip)
        self.add_clip_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.remove_clip_button = ttk.Button(self.root, text="Remove Clip", command=self.remove_clip)
        self.remove_clip_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.copy_clip_button = ttk.Button(self.root, text="Copy Selected Clip", command=self.copy_clip)
        self.copy_clip_button.pack(side=tk.LEFT, padx=5, pady=5)
        
    def add_clip(self):
        clip_text = pyperclip.paste()
        if clip_text:
            self.clips.append(clip_text)
            self.clip_listbox.insert(tk.END, clip_text)
        else:
            messagebox.showwarning("Warning", "Clipboard is empty!")

    def remove_clip(self):
        selected_clip_index = self.clip_listbox.curselection()
        if selected_clip_index:
            self.clips.pop(selected_clip_index[0])
            self.clip_listbox.delete(selected_clip_index)
        else:
            messagebox.showwarning("Warning", "No clip selected!")

    def copy_clip(self):
        selected_clip_index = self.clip_listbox.curselection()
        if selected_clip_index:
            pyperclip.copy(self.clips[selected_clip_index[0]])
            messagebox.showinfo("Info", "Clip copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No clip selected!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WinClip(root)
    root.mainloop()