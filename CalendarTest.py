import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

class Event:
    def __init__(self, date, description, image_path=None):
        self.date = date
        self.description = description
        self.image_path = image_path

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        
        self.events = []
        
        self.date_label = tk.Label(root, text="Date:")
        self.date_label.pack()
        
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()
        
        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack()
        
        self.description_entry = tk.Entry(root)
        self.description_entry.pack()
        
        self.image_label = tk.Label(root, text="Image Path:")
        self.image_label.pack()
        
        self.image_path_entry = tk.Entry(root)
        self.image_path_entry.pack()
        
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_image)
        self.browse_button.pack()
        
        self.add_event_button = tk.Button(root, text="Add Event", command=self.add_event)
        self.add_event_button.pack()
        
        self.event_listbox = tk.Listbox(root)
        self.event_listbox.pack()
        self.event_listbox.bind("<Enter>", self.show_image_popup)  # Bind hover event
        self.event_listbox.bind("<Leave>", self.hide_image_popup)  # Bind leave event
        
        self.image_popup = None
        
    def browse_image(self):
        file_path = filedialog.askopenfilename()
        self.image_path_entry.delete(0, tk.END)
        self.image_path_entry.insert(0, file_path)
        
    def add_event(self):
        date = self.date_entry.get()
        description = self.description_entry.get()
        image_path = self.image_path_entry.get()
        
        if date and description:
            event = Event(date, description, image_path)
            self.events.append(event)
            self.update_event_listbox()
            self.clear_inputs()
            messagebox.showinfo("Success", "Event added successfully!")
        else:
            messagebox.showerror("Error", "Date and description are required fields.")
        
    def clear_inputs(self):
        self.date_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.image_path_entry.delete(0, tk.END)
        
    def update_event_listbox(self):
        self.event_listbox.delete(0, tk.END)
        for event in self.events:
            self.event_listbox.insert(tk.END, f"{event.date}: {event.description}")
        
    def show_image_popup(self, event):
        selected_index = self.event_listbox.nearest(event.y)
        if selected_index >= 0 and selected_index < len(self.events):
            event_obj = self.events[selected_index]
            image_path = event_obj.image_path
            if image_path:
                self.display_image_popup(image_path)
        
    def hide_image_popup(self, event):
        if self.image_popup:
            self.image_popup.destroy()
            self.image_popup = None
        
    def display_image_popup(self, image_path):
        if self.image_popup:
            self.image_popup.destroy()
        self.image_popup = tk.Toplevel(self.root)
        self.image_popup.title("Image Popup")
        
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        
        img_label = tk.Label(self.image_popup, image=img)
        img_label.image = img
        img_label.pack()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
