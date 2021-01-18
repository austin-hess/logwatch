#!/usr/bin/env python
from sf import SfConnection
import tkinter as tk

class Application(tk.Frame):
    _login_username=''
    _login_password=''
    _login_security_token=''
    _login_is_sandbox=False

    _user_to_log_username=''
    _hours_to_log=0

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()

    def createWidgets(self):
        top=self.winfo_toplevel()
        top.rowconfigure(0,weight=1)
        top.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        
        '''
        Set up login area
        '''
        user_form_frame = tk.Frame(self)

        username_label = tk.Label(user_form_frame, text="Username")
        username_entry = tk.Entry(user_form_frame)
        username_entry.bind('<Key>', self._username_entry_key)

        password_label = tk.Label(user_form_frame, text="Password")
        password_entry = tk.Entry(user_form_frame)

        security_token_label = tk.Label(user_form_frame, text="Security Token")
        security_token_entry = tk.Entry(user_form_frame)

        is_test_label = tk.Label(user_form_frame, text="Sandbox?")
        is_test_checkbox = tk.Checkbutton(user_form_frame)

        login_button = tk.Button(user_form_frame, text="Login")

        '''
        Set up loggin form area
        '''
        log_form_frame = tk.Frame(self)

        username_to_trace_label = tk.Label(log_form_frame, text="Username to Trace")
        username_to_trace_entry = tk.Entry(log_form_frame)

        hours_to_trace_label = tk.Label(log_form_frame, text="Hours to Trace")
        hours_to_trace_entry = tk.Entry(log_form_frame)

        add_trace_button = tk.Button(log_form_frame, text="Add")

        user_list_label = tk.Label(self,text="User Traces")
        user_list_scrollbar_vert = tk.Scrollbar(self,orient=tk.VERTICAL)
        user_list_scrollbar_hor = tk.Scrollbar(self,orient=tk.HORIZONTAL)
        user_list = tk.Listbox(self, width=100,height=10,yscrollcommand=user_list_scrollbar_vert.set,xscrollcommand=user_list_scrollbar_hor.set)

        log_list_label = tk.Label(self,text="Logs")
        log_list_scrollbar_vert = tk.Scrollbar(self,orient=tk.VERTICAL)
        log_list_scrollbar_hor = tk.Scrollbar(self,orient=tk.HORIZONTAL)
        log_list = tk.Listbox(self,width=100,yscrollcommand=log_list_scrollbar_vert.set,xscrollcommand=log_list_scrollbar_hor.set)
        
        user_form_frame.grid(column=0,row=0,stick=tk.W+tk.N)
        
        username_label.grid(row=0,column=1, padx=10)
        username_entry.grid(row=1,column=1, padx=10)

        password_label.grid(row=0,column=3, padx=10)
        password_entry.grid(row=1,column=3, padx=10)

        security_token_label.grid(row=0,column=5, padx=10)
        security_token_entry.grid(row=1,column=5, padx=10)

        is_test_label.grid(row=0,column=7, padx=10)
        is_test_checkbox.grid(row=1,column=7, padx=10)

        login_button.grid(row=1, column=9, padx=10)

        tk.Frame(width=10).grid(row=0,column=11,rowspan=2)

        log_form_frame.grid(column=12,row=0,stick=tk.E+tk.N)
        
        username_to_trace_label.grid(row=0,column=13, padx=10)
        username_to_trace_entry.grid(row=1,column=13, padx=10)

        hours_to_trace_label.grid(row=0,column=15, padx=10)
        hours_to_trace_entry.grid(row=1,column=15, padx=10)

        add_trace_button.grid(row=1, column=17, padx=10)

        user_list_label.grid(row=2,column=0,sticky=tk.W)
        user_list.grid(row=3,column=0,columnspan=self.grid_size()[0],sticky=tk.N+tk.S+tk.E+tk.W)
        user_list_scrollbar_vert.grid(row=3,column=self.grid_size()[0]+1,sticky=tk.N+tk.S)
        user_list_scrollbar_hor.grid(row=4,column=0,columnspan=self.grid_size()[0]-1,sticky=tk.E+tk.W)
        user_list_scrollbar_vert['command'] = user_list.yview
        user_list_scrollbar_hor['command'] = user_list.xview

        log_list_label.grid(row=5,column=0,sticky=tk.W)
        log_list.grid(row=6,column=0,columnspan=self.grid_size()[0],sticky=tk.N+tk.S+tk.E+tk.W)
        log_list_scrollbar_vert.grid(row=6,column=self.grid_size()[0]+1,sticky=tk.N+tk.S)
        log_list_scrollbar_hor.grid(row=7,column=0,columnspan=self.grid_size()[0]-1,sticky=tk.E+tk.W)
        log_list_scrollbar_vert['command'] = log_list.yview
        log_list_scrollbar_hor['command'] = log_list.xview

        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=0)
        self.columnconfigure(3,weight=0)
        self.columnconfigure(5,weight=0)
        self.columnconfigure(7,weight=0)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=0)
        self.rowconfigure(2,weight=0)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=0)
        self.rowconfigure(5,weight=0)
        self.rowconfigure(6,weight=3)
        self.rowconfigure(7,weight=0)


        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()

    def _username_entry_key(self, event):
        self._login_username += event.char
        print(self._login_username)

app = Application()
app.master.title('Apex Monitor')
app.master.state('zoomed')
app.mainloop()
app.focus()


salesforce = SfConnection(
    "ahess@nnb.com.custondev", 
    "SoCasual#1", 
    "agrzEf7V1xHNm3LLCyre4Gqp6", 
    True
)

result = salesforce.query("SELECT Id, LastModifiedDate FROM ApexLog ORDER BY LastModifiedDate DESC LIMIT 5")
print(result)

