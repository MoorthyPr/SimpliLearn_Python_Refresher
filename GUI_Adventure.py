import tkinter as tk
from tkinter import messagebox


class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Land of Mysteries")
        self.root.geometry("800x600")

        self.title_label = tk.Label(
            root,
            text="🏆 Land of Mysteries 🏆",
            font=("Arial", 22, "bold")
        )
        self.title_label.pack(pady=20)

        self.story_label = tk.Label(
            root,
            text="Enter your name to begin the journey!",
            font=("Arial", 14),
            wraplength=700,
            justify="center"
        )
        self.story_label.pack(pady=20)

        self.name_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.name_entry.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)

        tk.Button(
            self.button_frame,
            text="Start Adventure",
            command=self.start_game,
            font=("Arial", 12)
        ).pack()

    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def start_game(self):
        self.player_name = self.name_entry.get().strip()

        if not self.player_name:
            messagebox.showwarning(
                "Missing Name",
                "Please enter your name."
            )
            return

        self.name_entry.pack_forget()

        self.story_label.config(
            text=f"Welcome, {self.player_name}, to the Land of Mysteries!\n\nChoose your path."
        )

        self.clear_buttons()

        tk.Button(
            self.button_frame,
            text="🌲 Dark Forest",
            width=25,
            command=self.forest_start
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="🪨 Hidden Cave",
            width=25,
            command=self.cave_start
        ).pack(pady=5)

    def reset_game(self):
        self.clear_buttons()

        self.story_label.config(
            text="Enter your name to begin the journey!"
        )

        self.name_entry.pack()
        self.name_entry.delete(0, tk.END)

        tk.Button(
            self.button_frame,
            text="Start Adventure",
            command=self.start_game
        ).pack()

    def game_over(self, message):
        self.story_label.config(text=message)

        self.clear_buttons()

        tk.Button(
            self.button_frame,
            text="Play Again",
            width=20,
            command=self.reset_game
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Exit",
            width=20,
            command=self.root.destroy
        ).pack(pady=5)

    # ========================
    # CAVE ADVENTURE
    # ========================

    def cave_start(self):
        self.clear_buttons()

        self.story_label.config(
            text="🪨 Hidden Cave\n\nWhat will you do next?"
        )

        tk.Button(
            self.button_frame,
            text="Move Forward",
            width=25,
            command=self.cave_move_forward
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Light a Torch",
            width=25,
            command=self.cave_light_torch
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Turn Back",
            width=25,
            command=lambda: self.game_over(
                "You decide to leave the cave safely."
            )
        ).pack(pady=5)

    def cave_move_forward(self):
        self.clear_buttons()

        self.story_label.config(
            text="You fell into a pit and got injured!\n\nChoose your next action."
        )

        tk.Button(
            self.button_frame,
            text="Climb Out Using Rope",
            width=25,
            command=self.cave_doors
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Dig Tunnel",
            width=25,
            command=lambda: self.game_over(
                "🐍 You encountered a snake!\n\nGame Over!"
            )
        ).pack(pady=5)

    def cave_light_torch(self):
        self.clear_buttons()

        self.story_label.config(
            text="The torch reveals a pit and a mysterious button."
        )

        tk.Button(
            self.button_frame,
            text="Use Rope",
            width=25,
            command=self.cave_doors
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Press Button",
            width=25,
            command=lambda: self.game_over(
                "💥 The floor collapsed!\n\nGame Over!"
            )
        ).pack(pady=5)

    def cave_doors(self):
        self.clear_buttons()

        self.story_label.config(
            text="You see three doors.\n\nChoose wisely!"
        )

        tk.Button(
            self.button_frame,
            text="Door 1",
            width=20,
            command=lambda: self.game_over(
                f"🏆 Congratulations {self.player_name}!\n\nYou found the treasure and won!"
            )
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Door 2",
            width=20,
            command=lambda: self.game_over(
                "⚠️ Trap Found!\n\nGame Over!"
            )
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Door 3",
            width=20,
            command=lambda: self.game_over(
                "👹 A Monster Appears!\n\nGame Over!"
            )
        ).pack(pady=5)

    # ========================
    # FOREST ADVENTURE
    # ========================

    def forest_start(self):
        self.clear_buttons()

        self.story_label.config(
            text="🌲 Dark Forest\n\nWhat will you do next?"
        )

        tk.Button(
            self.button_frame,
            text="Take Boat",
            width=25,
            command=self.forest_boat
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Climb Tree",
            width=25,
            command=self.forest_tree
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Turn Back",
            width=25,
            command=lambda: self.game_over(
                "You decide to leave the forest safely."
            )
        ).pack(pady=5)

    def forest_boat(self):
        self.clear_buttons()

        self.story_label.config(
            text="🚣 Your boat hits a rock and starts sinking!"
        )

        tk.Button(
            self.button_frame,
            text="Row Fast",
            width=25,
            command=self.forest_paths
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Swim to Shore",
            width=25,
            command=lambda: self.game_over(
                "🐊 A crocodile attacks!\n\nGame Over!"
            )
        ).pack(pady=5)

    def forest_tree(self):
        self.clear_buttons()

        self.story_label.config(
            text="🌳 You find a rope and a treasure box."
        )

        tk.Button(
            self.button_frame,
            text="Use Rope",
            width=25,
            command=self.forest_paths
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Touch Treasure Box",
            width=25,
            command=lambda: self.game_over(
                "⚡ Lightning strikes!\n\nGame Over!"
            )
        ).pack(pady=5)

    def forest_paths(self):
        self.clear_buttons()

        self.story_label.config(
            text="Three paths lie ahead.\n\nChoose wisely!"
        )

        tk.Button(
            self.button_frame,
            text="Left Path",
            width=20,
            command=lambda: self.game_over(
                "🦁 A Lion attacks!\n\nGame Over!"
            )
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Middle Path",
            width=20,
            command=lambda: self.game_over(
                "🐯 A Tiger attacks!\n\nGame Over!"
            )
        ).pack(pady=5)

        tk.Button(
            self.button_frame,
            text="Right Path",
            width=20,
            command=lambda: self.game_over(
                f"🏆 Congratulations {self.player_name}!\n\nYou found the treasure and won!"
            )
        ).pack(pady=5)


root = tk.Tk()
game = AdventureGame(root)
root.mainloop()