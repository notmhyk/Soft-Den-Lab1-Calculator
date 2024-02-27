import tkinter as tk

class MainPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Calculator")
        self.configure(bg="white")

        self.first_num = tk.DoubleVar()
        self.second_num = tk.DoubleVar()

        self.text = tk.StringVar()
        self.operator = tk.StringVar()

        self.entry_obj()
        self.num_lb_obj()
        self.operator_lb_obj()
        self.other_lb_obj()
        
    def entry_obj(self):
        self.entry = tk.Entry(self, textvariable=self.text, font=("Arial", 50), justify='right', validate='key', bg='lightgrey')
        self.entry.grid(row=0, column=0, columnspan=4 ,padx=5, pady=5)
        self.text.set("")
        self.operator.set("")

    def num_lb_obj(self):
        num = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            "0", "00", "=",
        ]
        for idx, num_data in enumerate(num):
            lb_num = tk.Label(self, text=num_data, font=("Arial", 40), bg="#3A3B3C", fg="white", width=3, height=1, cursor='hand2')
            lb_num.grid(row=idx // 3 + 3, column= idx % 3, padx=1, pady=2, ipadx=60,ipady=5)

    def operator_lb_obj(self):
        operator = ["÷", "×", "−", "+", "."]

        for idx, operator_data in enumerate(operator):
            lb_operator = tk.Label(self, text=operator_data,font=("Arial", 40), bg="#3A3B3C", fg="white", width=2, cursor='hand2')
            lb_operator.grid(row=idx + 2, column=3, padx=1, pady=5, ipadx=5, ipady=4)

    def other_lb_obj(self):
        other_btns = ["On/Off", "C", "AC"]
        for idx, other_btn in enumerate(other_btns):
            if other_btn == "On/Off":
                lb_other_btns = tk.Label(self, text=other_btn, font=("Arial", 20), background="#50C878", foreground="black", cursor="hand2")
            else: 
                lb_other_btns = tk.Label(self, text = other_btn, font=("Arial", 20),bg="#3A3B3C", fg="white",width=5, cursor='hand2')
            lb_other_btns.grid(row=2, column=idx, padx=1, pady=2, ipadx=67,ipady=17.5)
root = MainPage()
root.mainloop()