import tkinter as tk
from threading import Timer

class MysteryApp:
    def __init__(self, root):
        """Initialize the MysteryApp with the main window and set up the GUI components."""
        self.root = root
        self.root.title("Mystery App")

        self.value = 0
        self.auto_increment_amount = 1
        self.auto_increment_rate = 5.0

        # Label to display the current value
        self.label = tk.Label(root, text=f"Value: {self.value}")
        self.label.pack()

        # Buttons for manual increments
        self.increment_1_button = tk.Button(root, text="1", command=lambda: self.manual(1))
        self.increment_1_button.pack()

        self.increment_10_button = tk.Button(root, text="10", command=lambda: self.manual(10))
        self.increment_10_button.pack()

        self.increment_100_button = tk.Button(root, text="100", command=lambda: self.manual(100))
        self.increment_100_button.pack()

        self.increment_1000_button = tk.Button(root, text="1000", command=lambda: self.manual(1000))
        self.increment_1000_button.pack()

        # Label and button to display and increase the auto increment amount
        self.auto_increment_amount_label = tk.Label(root, text=f"Auto Increment Amount: {self.auto_increment_amount}")
        self.auto_increment_amount_label.pack()

        self.increase_auto_increment_amount_button = tk.Button(root, text="Automatic Process Amount++ (Cost 50)", command=self.auto_amount_increase)
        self.increase_auto_increment_amount_button.pack()

        # Label and button to display and increase the auto increment rate
        self.auto_increment_rate_label = tk.Label(root, text=f"Auto Increment Rate: {self.auto_increment_rate}")
        self.auto_increment_rate_label.pack()

        self.increase_auto_increment_rate_button = tk.Button(root, text="Automatic Process Rate++ (Cost 100)", command=self.auto_rate_increase)
        self.increase_auto_increment_rate_button.pack()

        # Start the automatic increment and value watcher
        self.auto()
        self.watch_value()

    def manual(self, amount):
        """Manually increment the value by the specified amount."""
        print(f"Manual increment: {amount}")
        self.value += amount
        print(f"New value: {self.value}")
        self.label.config(text=f"Value: {self.value}")

    def auto(self):
        """Automatically increment the value by the auto increment amount at the auto increment rate."""
        self.manual(self.auto_increment_amount)
        self.timer = Timer(self.auto_increment_rate, self.auto)
        self.timer.start()

    def auto_amount_increase(self):
        """Increase the auto increment amount by 1 if the value is greater than 50."""
        if self.value > 50:
            self.value -= 50
            self.auto_increment_amount += 1
            self.auto_increment_amount_label.config(text=f"Auto Increment Amount: {self.auto_increment_amount}")

    def auto_rate_increase(self):
        """Halve the auto increment rate if the value is greater than 100."""
        if self.value > 100:
            self.value -= 100
            self.auto_increment_rate *= 0.5
            self.auto_increment_rate_label.config(text=f"Auto Increment Rate: {self.auto_increment_rate}")
            self.timer.cancel()
            self.timer = Timer(self.auto_increment_rate, self.auto)
            self.timer.start()

    def watch_value(self):
        """Monitor the value and close the application if the value exceeds 100,000,000."""
        if self.value > 100000000:
            self.on_closing()
        else:
            self.root.after(1000, self.watch_value)

    def on_closing(self):
        """Clean up the timer and close the application."""
        if hasattr(self, 'timer') and self.timer.is_alive():
            self.timer.cancel()
        print(f"Final value: {self.value}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MysteryApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()