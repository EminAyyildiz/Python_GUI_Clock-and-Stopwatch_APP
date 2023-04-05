import tkinter as tk
import time


class ClockStopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("***Clock and Stopwatch *** Written by Emin Ayyıldız")

        self.master.configure(bg="gray")

        self.clock_label = tk.Label(self.master, font=("times new roman", 24,"bold"),background='orange')
        self.clock_label.pack(pady=20)

        self.date_label = tk.Label(self.master, font=("times new roman", 18,"bold"))
        self.date_label.pack()

        self.button_frame = tk.Frame(self.master)
        self.start_button = tk.Button(self.button_frame, text="START", command=self.start_timer,font=("times new roman", 10,"bold"))
        self.stop_button = tk.Button(self.button_frame, text="STOP", command=self.stop_timer,font=("times new roman", 10,"bold"))
        self.reset_button = tk.Button(self.button_frame, text="RESET", command=self.reset_timer,font=("times new roman", 10,"bold"))
        self.start_button.pack(side="left", padx=4)
        self.stop_button.pack(side="left", padx=4)
        self.reset_button.pack(side="left", padx=4)
        self.button_frame.pack(pady=15)

        self.is_running = False
        self.timer_counter = 0
        self.timer_label = tk.Label(self.master, text="00:00:00", font=("times new roman", 20),background="orange")
        self.timer_label.pack()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        current_date = time.strftime("%d/%m/%Y %A")
        self.clock_label.config(text=current_time)
        self.date_label.config(text=current_date)

        self.master.after(1000, self.update_clock)

    def start_timer(self):
        self.is_running = True
        self.timer()

    def stop_timer(self):
        self.is_running = False

    def reset_timer(self):
        self.timer_counter = 0
        self.timer_label.config(text="00:00:00")

    def timer(self):
        if self.is_running:
            self.timer_counter += 1
            hours = int(self.timer_counter / 3600)
            minutes = int((self.timer_counter - hours * 3600) / 60)
            seconds = int(self.timer_counter - hours * 3600 - minutes * 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=time_str)
            self.master.after(1000, self.timer)
        else:
            self.update_clock()

    def run(self):
        self.update_clock()
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = ClockStopwatchApp(root)
    app.run()
