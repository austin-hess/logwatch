import tkinter as tk

class UserList(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()

    def createWidgets(self):
        self.user_list_label = tk.Label(self,text="User Traces")
        self.user_list_scrollbar_vert = tk.Scrollbar(self,orient=tk.VERTICAL)
        self.user_list_scrollbar_hor = tk.Scrollbar(self,orient=tk.HORIZONTAL)
        self.user_list = tk.Listbox(self, width=200,height=10,yscrollcommand=self.user_list_scrollbar_vert.set,xscrollcommand=self.user_list_scrollbar_hor.set)

        self.user_list_label.grid(row=2,column=0,sticky=tk.W)
        self.user_list.grid(row=3,column=0,columnspan=self.master.grid_size()[0],sticky=tk.N+tk.S+tk.E+tk.W)
        self.user_list_scrollbar_vert.grid(row=3,column=self.grid_size()[0]+1,sticky=tk.N+tk.S)
        self.user_list_scrollbar_hor.grid(row=4,column=0,columnspan=self.grid_size()[0]-1,sticky=tk.E+tk.W)
        self.user_list_scrollbar_vert['command'] = self.user_list.yview
        self.user_list_scrollbar_hor['command'] = self.user_list.xview

        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=2)
