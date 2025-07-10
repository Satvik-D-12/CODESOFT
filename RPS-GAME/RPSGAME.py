import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import random

choices = ['Rock', 'Paper', 'Scissors']
win_threshold = {3: 2, 5: 3, 7: 4}

class RPSGame:
    def __init__(self, root, total_rounds):
        self.root = root
        self.total_rounds = total_rounds
        self.required_wins = win_threshold[total_rounds]
        self.user_score = 0
        self.comp_score = 0
        self.current_round = 1

        root.title("Rock-Paper-Scissors")
        root.geometry("1020x700")
        root.configure(bg="#F0F8FF")

        self.images = {
            "Rock": ImageTk.PhotoImage(Image.open("rock.jpg").resize((300, 300))),
            "Paper": ImageTk.PhotoImage(Image.open("paper.jpg").resize((300, 300))),
            "Scissors": ImageTk.PhotoImage(Image.open("scissors.jpg").resize((300, 300)))
        }

        self.setup_ui()

    def setup_ui(self):
        colors = {
            "Rock": {"bg": "#B0E0E6", "fg": "#000000"},
            "Paper": {"bg": "#FFDAB9", "fg": "#000000"},
            "Scissors": {"bg": "#E6E6FA", "fg": "#000000"}
        }

        self.buttons_frame = tk.Frame(self.root, bg="#F0F8FF")
        self.buttons_frame.pack(side="bottom", pady=40)

        for choice in choices:
            tk.Button(self.buttons_frame, text=choice, width=10, font=("Helvetica", 14, "bold"),
                      command=lambda c=choice: self.play(c),
                      bg=colors[choice]["bg"], fg=colors[choice]["fg"]
                      ).pack(side="left", padx=20)

        self.result = tk.Label(self.root, text="", font=("Helvetica", 30, "bold"), bg="#F0F8FF")
        self.result.pack(pady=10)

        self.user_score_label = tk.Label(self.root, text="You: 0", font=("Helvetica", 24, "bold"),
                                         bg="#F0F8FF", fg="#228B22")
        self.user_score_label.place(x=20, y=20)

        self.comp_score_label = tk.Label(self.root, text="Computer: 0", font=("Helvetica", 24, "bold"),bg="#F0F8FF", fg="#B22222")
        self.comp_score_label.place(x=820, y=20)

        style = ttk.Style()
        style.configure("GameHeading.TLabel", background="#37474F", foreground="white",
                        font=("Helvetica", 30, "bold"), padding=10)

        heading_frame = tk.Frame(self.root, bg="#37474F")
        heading_frame.pack(fill="x", pady=(60, 0))

        ttk.Label(heading_frame, text="Choose Rock, Paper, or Scissors",style="GameHeading.TLabel", anchor="center", justify="center").pack(fill="x")

        self.choices_frame = tk.Frame(self.root, bg="#F0F8FF")
        self.choices_frame.pack(pady=20, fill="both", expand=True)

        self.user_img_label = tk.Label(self.choices_frame, bg="#F0F8FF")
        self.user_img_label.pack(side="left", expand=True)

        self.round_image = self.create_vertical_label()
        self.round_label = tk.Label(self.choices_frame, image=self.round_image, bg="#F0F8FF")
        self.round_label.pack(side="left", padx=10)

        self.comp_img_label = tk.Label(self.choices_frame, bg="#F0F8FF")
        self.comp_img_label.pack(side="right", expand=True)

    def create_vertical_label(self):
        stacked = "\n".join(list("ROUND")) + "\n\n" + str(self.current_round)
        try:
            font = ImageFont.truetype("arialbd.ttf", 28)
        except:
            font = ImageFont.truetype("arial.ttf", 28)

        img = Image.new("RGB", (60, 360), color="#F0F8FF")
        draw = ImageDraw.Draw(img)
        draw.multiline_text((10, 40), stacked, font=font, fill="#003366", spacing=5)
        return ImageTk.PhotoImage(img)

    def play(self, user_choice):
        comp_choice = random.choice(choices)
        self.result.config(text="")
        flicker_count = 8
        delay = 80
        current = [0]

        def flicker():
            if current[0] < flicker_count:
                temp_user = random.choice(choices)
                temp_comp = random.choice(choices)
                self.user_img_label.config(image=self.images[temp_user])
                self.comp_img_label.config(image=self.images[temp_comp])
                current[0] += 1
                self.root.after(delay, flicker)
            else:
                self.user_img_label.config(image=self.images[user_choice])
                self.comp_img_label.config(image=self.images[comp_choice])
                self.process_result(user_choice, comp_choice)

        flicker()

    def process_result(self, user, comp):
        if user == comp:
            self.result.config(text="IT'S A TIE!", fg="gray")
            return

        if (user == 'Rock' and comp == 'Scissors') or \
           (user == 'Scissors' and comp == 'Paper') or \
           (user == 'Paper' and comp == 'Rock'):
            self.user_score += 1
            self.result.config(text="YOU WIN", fg="green")
        else:
            self.comp_score += 1
            self.result.config(text="YOU LOSE", fg="red")

        self.user_score_label.config(text=f"You: {self.user_score}")
        self.comp_score_label.config(text=f"Computer: {self.comp_score}")
        self.advance_round()

        if self.user_score == self.required_wins:
            self.root.destroy()
            self.show_result_screen("win")
        elif self.comp_score == self.required_wins:
            self.root.destroy()
            self.show_result_screen("lose")

    def advance_round(self):
        self.current_round += 1
        self.round_image = self.create_vertical_label()
        self.round_label.config(image=self.round_image)

    def show_result_screen(self, result):
        end = tk.Tk()
        end.title("Match Result")
        end.geometry("530x300")
        end.configure(bg="#F0F8FF")

        msg = "🎉 Congratulations! You Win! 🎉" if result == "win" else "😔 You Lose! 😔"
        btn_text = "Play Again" if result == "win" else "Try Again"

        tk.Label(end, text=msg, font=("Helvetica", 26, "bold"),
                 bg="#F0F8FF", fg="#003366").pack(pady=60)

        tk.Button(end, text=btn_text, font=("Helvetica", 14, "bold"),
                  command=lambda: self.restart_to_launcher(end),
                  bg="#4682B4", fg="white", width=15).pack(side="bottom", pady=30)

        end.mainloop()

    def restart_to_launcher(self, result_window):
        result_window.destroy()
        show_start_page()

def launch_game(rounds_selected):
    launcher.destroy()
    root = tk.Tk()
    RPSGame(root, total_rounds=rounds_selected)
    root.mainloop()

def show_start_page():
    global launcher
    launcher = tk.Tk()
    launcher.title("Rock-Paper-Scissors Launcher")
    launcher.geometry("500x300")
    launcher.configure(bg="#F0F8FF")

    tk.Label(launcher, text="Select Number of Rounds", font=("Helvetica", 20, "bold"),bg="#F0F8FF", fg="#003366").pack(pady=(40, 10))

    round_var = tk.StringVar(value="3")
    tk.Spinbox(launcher, values=(3, 5, 7), textvariable=round_var,font=("Helvetica", 16), width=5, justify="center").pack()

    tk.Button(launcher, text="Start Game", font=("Helvetica", 14, "bold"),bg="#32CD32", fg="white", padx=20, pady=10,              
              command=lambda: launch_game(int(round_var.get()))).pack(side="bottom", pady=40)

    launcher.mainloop()

show_start_page()