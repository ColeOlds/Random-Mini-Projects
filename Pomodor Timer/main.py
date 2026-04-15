import tkinter as tk
import time
# from playsound import playsound

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")
        master.geometry("400x300")
        
        self.work_time = 25 * 60  # 25 minutes
        self.break_time = 5 * 60  # 5 minutes
        self.timer_running = False
        self.is_work_session = True
        self.current_time = self.work_time
        
        # UI Elements
        self.session_label = tk.Label(master, text="Work Session", font=("Arial", 20))
        self.session_label.pack(pady=10)

        self.time_label = tk.Label(master, text=self.format_time(self.current_time), font=("Arial", 48))
        self.time_label.pack(pady=20)
        
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)
        
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.pause_button = tk.Button(self.button_frame, text="Pause", command=self.pause_timer)
        self.pause_button.grid(row=0, column=1, padx=5)
        
        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=5)
        
    def format_time(self, seconds):
        """Formats seconds into a MM:SS string."""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
        
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.tick()
    
    def pause_timer(self):
        self.timer_running = False
        
    def reset_timer(self):
        self.pause_timer()
        self.is_work_session = True
        self.current_time = self.work_time
        self.session_label.config(text="Work Session")
        self.time_label.config(text=self.format_time(self.current_time))

    def tick(self):
        if not self.timer_running:
            return
            
        self.current_time -= 1
        self.time_label.config(text=self.format_time(self.current_time))
        
        if self.current_time <= 0:
            self.end_session()
        
        self.master.after(1000, self.tick) # Call tick again after 1 second

    def end_session(self):
        self.timer_running = False
        
        if self.is_work_session:
            self.is_work_session = False
            self.current_time = self.break_time
            self.session_label.config(text="Break Time")
        else:
            self.is_work_session = True
            self.current_time = self.work_time
            self.session_label.config(text="Work Session")

        self.time_label.config(text=self.format_time(self.current_time))
        self.start_timer() # Automatically start the next session/break

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
