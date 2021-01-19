import tkinter as tk

class LoginForm(tk.Frame):

    def __init__(self, master=None, on_submit=None):
        tk.Frame.__init__(self, master)
        self.createWidgets(on_submit)
    
    def createWidgets(self, on_submit):
        self.username_label = tk.Label(self, text="Username")
        self.username_entry = tk.Entry(self)

        self.password_label = tk.Label(self, text="Password")
        self.password_entry = tk.Entry(self, show='*')

        self.security_token_label = tk.Label(self, text="Security Token")
        self.security_token_entry = tk.Entry(self)

        self.is_test_var = tk.IntVar()
        self.is_test_label = tk.Label(self, text="Sandbox?")
        self.is_test_checkbox = tk.Checkbutton(self, variable=self.is_test_var)

        self.login_button = tk.Button(self, text="Login")

        self.username_label.grid(row=0,column=1, padx=10,sticky=tk.N)
        self.username_entry.grid(row=1,column=1, padx=10,sticky=tk.N)

        self.password_label.grid(row=0,column=3, padx=10)
        self.password_entry.grid(row=1,column=3, padx=10)

        self.security_token_label.grid(row=0,column=5, padx=10)
        self.security_token_entry.grid(row=1,column=5, padx=10)

        self.is_test_label.grid(row=0,column=7, padx=10)
        self.is_test_checkbox.grid(row=1,column=7, padx=10)

        self.login_button.grid(row=1, column=9, padx=10)
        
        if on_submit is None:
            self.login_button.bind('<Button-1>', self.default_on_submit)
        else:
            self.login_button.bind('<Button-1>', on_submit)

    def setLoggedIn(self, isLoggedIn):
        if isLoggedIn:
            self.username_label.grid_remove()
            self.username_entry.grid_remove()
            self.password_label.grid_remove()
            self.password_entry.grid_remove()
            self.security_token_label.grid_remove()
            self.security_token_entry.grid_remove()
            self.is_test_label.grid_remove()
            self.is_test_checkbox.grid_remove()
            self.login_button.grid_remove()
            self.logout_button = tk.Button(self, text="Logout")
            self.logout_button.grid(row=0,column=1)
            self.logout_button.bind('<Button-1>', self.logout)
        else:
            self.logout_button.grid_remove()
            self.username_label.grid()
            self.username_entry.grid()
            self.password_label.grid()
            self.password_entry.grid()
            self.security_token_label.grid()
            self.security_token_entry.grid()
            self.is_test_label.grid()
            self.is_test_checkbox.grid()
            self.login_button.grid()
            
    def logout(self, event):
        self.setLoggedIn(False)
        self.username_entry.delete(0,tk.END)
        self.password_entry.delete(0,tk.END)
        self.security_token_entry.delete(0,END)
        self.is_test_var.set(0)

    def default_on_submit(self, event):
        print(self.username_entry.get())
        print(self.password_entry.get())
        print(self.security_token_entry.get())
        print(self.is_test_var.get())