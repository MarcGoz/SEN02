import tkinter as tk
from gamemode import GamemodeScreen

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Solo Defeat")
        self.geometry("1440x1024")
        self.configure(bg="#000000")  # Dark mode black background color

        self.create_widgets()

    def create_widgets(self):
        # Text widget for "Solo Defeat"
        solo_defeat_label = tk.Label(self, text="Solo Defeat", font=("Inter", 65), fg="white", bg="#000000")
        solo_defeat_label.place(relx=0.5, rely=0.05, anchor="center")

        # Container for shape
        shape_container = tk.Canvas(self, width=271, height=268, bg="#D9D9D9", highlightthickness=0)
        shape_container.place(relx=0.5, rely=0.3, anchor="center")

        # Draw first shape
        shape_container.create_rectangle(0, 0, 271, 268, outline="white", width=1.17)

        # Draw second shape
        shape_container.create_polygon(0, 0, 379.8, 0, 269.12, 268, fill="", outline="white", width=1.17)

        # Text widget for paragraph
        paragraph_text = tk.Label(self, text='''Introducing "Solo Defeat: The App Where You're Always the Winner... of Losing!" - a fun and engaging app that challenges you to stare at yourself in the camera and see how long you can last. This app is perfect for anyone who loves a good challenge and wants to have a laugh while doing it.''', font=("Inter", 20), fg="white", bg="#000000", wraplength=600, justify="center")
        paragraph_text.place(relx=0.5, rely=0.7, anchor="center")

        # PLAY button
        play_button = tk.Button(self, text="PLAY", font=("Inter", 20, "bold"), fg="black", bg="#D9D9D9", width=20, command=self.open_gamemode_screen)
        play_button.place(relx=0.5, rely=0.9, anchor="center")

        # SETTINGS button
        settings_button = tk.Button(self, text="SETTINGS", font=("Inter", 20, "bold"), fg="black", bg="#D9D9D9", width=20)
        settings_button.place(relx=0.5, rely=0.95, anchor="center")

    def open_gamemode_screen(self):
        # Destroy the existing widgets
        for widget in self.winfo_children():
            widget.destroy()
        
        # Create and display the GamemodeScreen
        gamemode_screen = GamemodeScreen(self)
        gamemode_screen.pack(fill="both", expand=True)

if __name__ == "__main__":
    main_page = MainPage()
    main_page.mainloop()
