import tkinter as tk

class GamemodeScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg="#000000")  # Dark mode black background color
        self.create_widgets()

    def create_widgets(self):
        # Header
        header_label = tk.Label(self, text="GAMEMODE", font=("Inter", 44, "bold"), fg="white", bg="#000000")
        header_label.pack(pady=20)

        # Infinite gamemode container
        infinite_container = tk.Frame(self, bg="#000000", highlightbackground="white", highlightthickness=2)
        infinite_container.pack(pady=(100, 20))

        # Box for shape
        shape_box = tk.Canvas(infinite_container, width=100, height=100, bg="black", highlightthickness=0)
        shape_box.pack(side="left", padx=20)

        # Draw first shape
        shape_box.create_rectangle(0, 0, 100, 100, outline="white", width=2)

        # Infinite gamemode label
        infinite_label = tk.Label(infinite_container, text="Infinite", font=("Inter", 25, "italic"), fg="white", bg="#000000")
        infinite_label.pack(pady=10)

        # Infinite gamemode description
        infinite_description = tk.Label(infinite_container, text="A never-ending journey of challenges and achievements awaits. How far can you go?", font=("Inter", 12), fg="white", bg="#000000", wraplength=400, justify="center")
        infinite_description.pack()

        # Infinite gamemode play button
        play_button = tk.Button(infinite_container, text="PLAY", font=("Inter", 16, "bold"), fg="black", bg="#D9D9D9", width=10)
        play_button.pack(pady=10)

        # Challenge gamemode container
        challenge_container = tk.Frame(self, bg="#000000", highlightbackground="white", highlightthickness=2)
        challenge_container.pack(pady=20)

        # Box for shape
        shape_box = tk.Canvas(challenge_container, width=100, height=100, bg="black", highlightthickness=0)
        shape_box.pack(side="left", padx=20)

        # Draw first shape
        shape_box.create_rectangle(0, 0, 100, 100, outline="white", width=2)

        # Challenge gamemode label
        challenge_label = tk.Label(challenge_container, text="Challenge", font=("Inter", 25, "italic"), fg="white", bg="#000000")
        challenge_label.pack(pady=10)

        # Challenge gamemode description
        challenge_description = tk.Label(challenge_container, text="Prepare yourself for a series of exciting and challenging tasks. Will you emerge victorious?", font=("Inter", 12), fg="white", bg="#000000", wraplength=400, justify="center")
        challenge_description.pack()

        # Challenge gamemode play button
        play_button = tk.Button(challenge_container, text="PLAY", font=("Inter", 16, "bold"), fg="black", bg="#D9D9D9", width=10)
        play_button.pack(pady=10)
