from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
checkmarks = 0
timer = None
 
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global checkmarks
    global reps
    checkmarks = 0
    reps = 0
    timer_lb.config(text="Timer", fg=GREEN)
    canvas.itemconfig(count_lb, text="00:00")
    window.after_cancel(timer)
    checkmark_lb.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global checkmarks
    global reps
    if reps % 8 == 0 and reps != 0:
        timer_lb.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 != 0:
        timer_lb.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    elif reps % 2 == 0:
        timer_lb.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)
        checkmarks += 1
    else:
        print("Invalid Reps Parameter/Argument")
    reps+=1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    min = int(count / 60)
    sec = int(count % 60)
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = f"0{sec}"
    if count >= 0:
        canvas.itemconfig(count_lb, text=f"{min}:{sec}")
        timer = window.after(1000, count_down, count-1)
    else:
        checkmark_lb.config(text=f"{'✔'*checkmarks}")
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_lb = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "bold"))
timer_lb.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
count_lb = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", bg="white", fg="black", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

checkmark_lb = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark_lb.grid(column=1, row=2)

reset_btn = Button(text="Reset", bg="white", fg="black", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

window.mainloop()