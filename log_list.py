import tkinter as tk

class LogList(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.createWidgets()

    def createWidgets(self):
        self.log_list_label = tk.Label(self,text="Logs")
        self.log_list_scrollbar_vert = tk.Scrollbar(self,orient=tk.VERTICAL)
        self.log_list_scrollbar_hor = tk.Scrollbar(self,orient=tk.HORIZONTAL)
        self.log_list = tk.Listbox(self,width=100,yscrollcommand=self.log_list_scrollbar_vert.set,xscrollcommand=self.log_list_scrollbar_hor.set)

        self.log_list_label.grid(row=5,column=0,sticky=tk.W)
        self.log_list.grid(row=6,column=0,columnspan=self.grid_size()[0],sticky=tk.N+tk.S+tk.E+tk.W)
        self.log_list_scrollbar_vert.grid(row=6,column=self.grid_size()[0]+1,sticky=tk.N+tk.S)
        self.log_list_scrollbar_hor.grid(row=7,column=0,columnspan=self.grid_size()[0]-1,sticky=tk.E+tk.W)
        self.log_list_scrollbar_vert['command'] = self.log_list.yview
        self.log_list_scrollbar_hor['command'] = self.log_list.xview

        self.columnconfigure(0,weight=1)
        self.rowconfigure(5,weight=0)
        self.rowconfigure(6,weight=1)