import tkinter as tk
import pyotp

class MFAApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Multi-Factor Authentication")


        self.secret_key = pyotp.random_base32()

        self.totp = pyotp.TOTP(self.secret_key)
        self.current_otp = self.totp.now()

        self.label_instruction = tk.Label(master, text="Enter the OTP to access:")
        self.label_instruction.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

        self.label_otp = tk.Label(master, text="OTP:")
        self.label_otp.grid(row=1, column=0, padx=10, pady=5)

        self.entry_otp = tk.Entry(master, width=20, show="*")
        self.entry_otp.grid(row=1, column=1, padx=10, pady=5)

        self.label_generated_otp = tk.Label(master, text="Generated OTP:\n" + self.current_otp)
        self.label_generated_otp.grid(row=1, column=2, padx=10, pady=5)

        self.button_generate_otp = tk.Button(master, text="Generate OTP", command=self.generate_otp)
        self.button_generate_otp.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.button_submit = tk.Button(master, text="Submit", command=self.check_otp)
        self.button_submit.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def generate_otp(self):
        self.current_otp = self.totp.now()
        self.label_generated_otp.config(text="Generated OTP:\n" + self.current_otp)

    def check_otp(self):
        entered_otp = self.entry_otp.get()
        if entered_otp == self.current_otp:
            self.show_access_granted()
        else:
            self.show_access_denied()

    def show_access_granted(self):
        self.label_instruction.config(text="Access Granted", fg="green")
        self.entry_otp.config(state="disabled")
        self.button_submit.config(state="disabled")

    def show_access_denied(self):
        self.label_instruction.config(text="Access Denied", fg="red")
        self.entry_otp.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = MFAApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
