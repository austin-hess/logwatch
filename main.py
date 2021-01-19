#!/usr/bin/env python
from sf import SfConnection
import tkinter as tk
import json
from login_form import LoginForm
from logging_form import LoggingForm
from user_list import UserList
from log_list import LogList

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.makeResponsive()
        self.createWidgets()

    def createWidgets(self):
        self.login_form = LoginForm(self, self.on_login)
        self.log_form_frame = LoggingForm(self)
        self.user_list = UserList(self)
        self.log_list = LogList(self)

        self.login_form.grid(column=0,row=0,stick=tk.W+tk.N)
        self.log_form_frame.grid(column=12,row=0,stick=tk.E+tk.N)
        tk.Frame(width=10).grid(row=0,column=11,rowspan=2)
        self.user_list.grid(column=0,row=2,columnspan=self.grid_size()[0], sticky=tk.N+tk.S+tk.E+tk.W)
        self.log_list.grid(column=0,row=3,columnspan=self.grid_size()[0],sticky=tk.N+tk.S+tk.E+tk.W)

    def on_login(self, event):
        print(self.login_form.username_entry.get())
        print(self.login_form.password_entry.get())
        print(self.login_form.security_token_entry.get())
        print(self.login_form.is_test_var.get())

        
        self.connection = SfConnection(
            self.login_form.username_entry.get(),
            self.login_form.password_entry.get(),
            self.login_form.security_token_entry.get(),
            self.login_form.is_test_var.get()
        )

        self.login_form.setLoggedIn(True)


    def makeResponsive(self):
        top=self.winfo_toplevel()
        top.rowconfigure(0,weight=1)
        top.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=6)
        self.columnconfigure(1,weight=0)
        self.columnconfigure(3,weight=0)
        self.columnconfigure(5,weight=0)
        self.columnconfigure(7,weight=0)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=0)
        self.rowconfigure(2,weight=1)
        self.rowconfigure(3,weight=6)

app = Application()
app.master.title('Apex Monitor')
app.master.state('zoomed')
app.mainloop()

