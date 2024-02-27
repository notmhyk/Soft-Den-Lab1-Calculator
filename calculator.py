import tkinter as tk

class MainPage(tk.Tk): 
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Calculator")
        self.configure(bg="white")
        
        self.text_doubleVar = tk.DoubleVar()
        self.text2_doubleVar =tk.DoubleVar()

        self.text_strVar = tk.StringVar()
        self.operator_var = tk.StringVar()

        self.textBox = tk.Entry(self, textvariable=self.text_strVar, font=("Arial", 50), justify='right', validate='key', bg="lightgrey")
        self.textBox.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        validation = self.register(self.validate_input)
        
        self.textBox.config(validatecommand=(validation, '%P'))
        self.text_strVar.set("")
        self.operator_var.set("")
        

        num_lb = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            "0", "00", ".",
        ]

        for idx, button_data in enumerate(num_lb):
            self.label_num = tk.Label(self, text=button_data, font=("Arial", 40), bg="#3A3B3C", fg="white", width=3, height=1, cursor='hand2')
            self.label_num.grid(row=idx // 3 + 3, column=idx % 3, padx=1, pady=2, ipadx=60,ipady=5)
            self.label_num.bind("<Button-1>", lambda event, num=button_data: self.update_entry(num))
            self.label_num.bind("<Enter>", self.change_color_enter)
            self.label_num.bind("<Leave>", self.change_color_leave)

        operators_lb = ["÷", "×", "−", "+", "="]
        self.operator = {
            "÷" : "/",
            "×" : "*",
            "−" : "-",
            "+" : "+",
            "=" : "="
        }

        for idx, operators in enumerate(operators_lb):
            self.label_operators = tk.Label(self, text=operators, font=("Arial", 40), bg="#3A3B3C", fg="white",width=2, cursor='hand2')
            self.label_operators.grid(row=idx + 2, column=3, padx=1, pady=5, ipadx=5, ipady=4)
            if operators == "=": 
                self.label_operators.bind("<Button-1>", lambda event, op=operators: self.calculate())
            else:
                self.label_operators.bind("<Button-1>", lambda event, op=operators: self.update_operators(op))
            self.label_operators.bind("<Enter>", self.change_color_enter)
            self.label_operators.bind("<Leave>", self.change_color_leave)

        clear_btns = ["On/Off", "C", "AC"]
        
        for idx, btns in enumerate(clear_btns):
            if btns == "On/Off":
                self.label_btns = tk.Label(self, text=btns, font=("Arial", 20), background="#50C878", foreground="black", cursor="hand2")
            else:
                    self.label_btns = tk.Label(self, text = btns, font=("Arial", 20),bg="#3A3B3C", fg="white",width=5, cursor='hand2') 
            self.label_btns.grid(row=2, column=idx, padx=1, pady=2, ipadx=67,ipady=17.5)
            if btns == "C":
                self.label_btns.bind("<Button-1>", lambda event: self.clear_entry())
            elif btns == "AC":
                self.label_btns.bind("<Button-1>", lambda event: self.all_clear())
            elif btns == "On/Off":
                self.label_btns.bind("<Button-1>", lambda event: (self.toggle_entry_state(), self.change_color_onOff_click(event)))
            self.label_btns.bind("<Enter>", self.change_color_enter)
            self.label_btns.bind("<Leave>", self.change_color_leave)

    def change_color_onOff_click(self, event):
        current_bg_color = event.widget.cget("bg")
        if current_bg_color == "#50C878":  
            event.widget.config(bg="#C70039", fg="white")
        else:  
            event.widget.config(bg="#50C878", fg="black")

    def change_color_enter(self, event):
        if event.widget.cget("text") != "On/Off":
            event.widget.config(bg="white", fg="black")

    def change_color_leave(self, event):
        if event.widget.cget("text") != "On/Off":
            if event.widget.cget("bg") == "#C70039":
                event.widget.config(bg="#C70039", fg="white")
            else:
                event.widget.config(bg="#3A3B3C", fg="white")
    
    def toggle_entry_state(self):
        current_state = self.textBox['state']
        if current_state == 'normal':
            self.all_clear()
            self.textBox.config(state='readonly')
            for label in self.grid_slaves():
                if label.cget("text") != "On/Off":
                    label.config(state='disabled')
                    label.unbind("<Button-1>")
        else:
            self.textBox.config(state='normal')
            for label in self.grid_slaves():
                label.config(state='normal')
                label.bind("<Button-1>", self.label_click_event)
                if label.cget("text") == "On/Off":
                    label.bind("<Button-1>", lambda event: (self.toggle_entry_state(), self.change_color_onOff_click(event)))
                
    def label_click_event(self, event):
        label_text = event.widget.cget("text")
        if label_text.isdigit() or label_text in [".", "00"]:
            self.update_entry(label_text)
        elif label_text in ["÷", "×", "−", "+"]:
            self.update_operators(label_text)
        elif label_text == "=":
            self.calculate()
        elif label_text == "C":
            self.clear_entry()
        elif label_text == "AC":
            self.all_clear()
        elif label_text == "On/Off":
            self.toggle_entry_state()
        
    def all_clear(self):
        self.text_strVar.set("")
        self.text_doubleVar.set(0.0)
        self.text2_doubleVar.set(0.0)
        self.operator_var.set("")

    def clear_entry(self):
        current_text = self.text_strVar.get()
        new_text = current_text[:-1] 
        self.text_strVar.set(new_text)

    def validate_input(self, new_text):
        if new_text.isdigit() or new_text == "":
            return True
        else:
            return False
    
    def update_entry(self, num):
        current_text = self.text_strVar.get()
        cursor_position = self.textBox.index(tk.INSERT)
        new_text = current_text[:cursor_position] + num + current_text[cursor_position:]
        self.text_strVar.set(new_text)
        self.textBox.icursor(cursor_position + len(num))
        if '.' not in new_text: 
            try:
                int_value = int(new_text)
                self.text_doubleVar.set(int_value)
            except ValueError:
                pass
        else:
            try:
                float_value = float(new_text)
                self.text_doubleVar.set(float_value)
            except ValueError:
                pass
    
    def update_operators(self, operator):
        current_text = self.text_strVar.get()
        if current_text == "":
            return
        elif current_text[-1] in self.operator.keys():
            return
        else:
            try:
                self.text2_doubleVar.set(float(current_text))
                print("First number:", self.text2_doubleVar.get())
            except ValueError:
                pass
            self.text_strVar.set("")
            
            if operator == "÷":
                self.operator_var.set("/")
            elif operator == "×":
                self.operator_var.set("*")
            elif operator == "−":
                self.operator_var.set("-")
            else:
                self.operator_var.set("+")

            print("Operator selected:", self.operator_var.get())

    def calculate(self):
        first_number = self.text2_doubleVar.get()
        operator = self.operator_var.get()
        second_number = self.text_doubleVar.get()
    
        if second_number.is_integer():
            second_number = int(second_number)
        
        if operator == "/" and second_number == 0:
            self.text_strVar.set("Error")

        else:
            operations = {
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
                "/": lambda x, y: x / y,
            }
            if operator in operations:
                result = operations[operator](first_number, second_number)
                if result.is_integer():
                    result = int(result)
                self.text_strVar.set(str(result))
                self.text2_doubleVar.set(str(result))
        self.textBox.icursor(tk.END)

root = MainPage()
root.resizable(width=False, height=False)
root.mainloop()