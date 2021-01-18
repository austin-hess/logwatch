import tkinter as tk

class LoggingForm(tk.Frame):

    def __init__(self, master=None, on_add_trace=None):
        tk.Frame.__init__(self, master)
        self.createWidgets(on_add_trace)

    def createWidgets(self, on_add_trace):
        self.username_to_trace_label = tk.Label(self, text="Username to Trace")
        self.username_to_trace_entry = tk.Entry(self)

        self.hours_to_trace_label = tk.Label(self, text="Hours to Trace")
        self.hours_to_trace_entry = tk.Entry(self)

        self.add_trace_button = tk.Button(self, text="Add")
        self.add_trace_button.bind('<Button-1>', self.default_on_add_trace if on_add_trace is None else on_add_trace)

        self.username_to_trace_label.grid(row=0,column=13, padx=10)
        self.username_to_trace_entry.grid(row=1,column=13, padx=10)

        self.hours_to_trace_label.grid(row=0,column=15, padx=10)
        self.hours_to_trace_entry.grid(row=1,column=15, padx=10)

        self.add_trace_button.grid(row=1, column=17, padx=10)

    def default_on_add_trace(self):
        print(self.username_to_trace_entry.get())
        print(self.hours_to_trace_entry.get())