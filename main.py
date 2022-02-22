import datetime
import csv

# Date obtainer
now = datetime.datetime.now()
date_today = now.strftime("%D")

day_today = date_today[3:5]
month_number_today = date_today[:2]

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_days = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']

month_today = months[int(month_number_today) - 1]
year_today = '20' + date_today[6:]

month_display = month_today + " " + year_today

try:
    import Tkinter as tk
except:
    import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage, None)

    def switch_frame(self, frame_class, var1):
        new_frame = frame_class(self, var1)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

########################################################################################################################

class StartPage(tk.Frame):
    def __init__(self, master, var1):
        tk.Frame.__init__(self, master)

        master.title("My Calendar")

        # App Heading
        tk.Label(self, text="My Calendar!", font=('Helvetica', 16, "bold")).grid(row = 1, column = 2, pady = 35)
        # ADD "Created by Soham Sarbadhikary" SOMEWHERE IN THE START PAGE!!

        # Today's Calendar button
        btn_today = tk.Button(self, text="Today's Calendar", width = 20, height = 3, command=lambda: master.switch_frame(Calendar, month_display))
        btn_today.grid(row = 3, column = 2, pady = 40, padx = 60)

        # Entry Form
        entry_form = tk.Entry(self)
        entry_form.insert(0, 'Month, Year')
        entry_form.grid(row = 4, column = 2, pady = 0)

        # Specify Calendar button
        btn_specify = tk.Button(self, text="Specify month",width = 20, height = 3,command=lambda: self.enter_date(entry_form.get()))
        btn_specify.grid(row = 5, column = 2, pady = 10)

        # Quit button
        btn_quit = tk.Button(self, text="Quit App",width = 20, height = 3,command=master.destroy)
        btn_quit.grid(row = 6, column = 2, pady = 20)

    def enter_date(self, text):
        self.master.switch_frame(Calendar, text)
        
########################################################################################################################

class Calendar(tk.Frame):
    def __init__(self, master, var1):

        tk.Frame.__init__(self, master)
        master.title(var1)
        master.geometry("1080x640")

        lbl_display = tk.Label(self, text= var1)
        lbl_display.grid(row = 1, column = 4)

        date_splitter = var1.split(" ")
        
        month_var = date_splitter[0]
        days_index = months.index(month_var)

        year_var = var1[-4:]


        # Leap year identifier
        is_leap_year = False

        if int(year_var) % 4 == 0:
            is_leap_year = True
            if int(year_var) % 100 == 0:
                is_leap_year = False
                if int(year_var) % 400 == 0:
                    is_leap_year = True
        else:
            is_leap_year = False


        # Number of days identifier
        if month_var == "February":
            if is_leap_year == True:
                days_in_month = 29
            else:
                days_in_month = 28
        else:
            days_in_month = month_days[days_index]


        # Next and previous month variables assigned
        if month_var != 'December':
            month_next = months[days_index+1]
            year_next = year_var
        else:
            month_next = 'January'
            year_next = str(int(year_var) + 1)

        if month_var != 'January':
            month_previous = months[days_index-1]
            year_previous = year_var
        else:
            month_previous = 'December'
            year_previous = str(int(year_var) - 1)
            
        calendar_next = month_next + " " + year_next
        calendar_previous = month_previous + " " + year_previous


        # Creating date buttons
        counter = 0
        date_to_pass = var1

        for a in range (3, 8):
            for b in range(1, 8):
                row_counter = 7*counter
                date = row_counter + b
                
                if date > int(days_in_month):
                    date = date - int(days_in_month)
                    date_to_pass = calendar_next
                date_full = str(date) + " " + date_to_pass
                day_button = tk.Button(self, text = str(date),
                                       command=lambda date_full = date_full: master.switch_frame(DateActions, date_full))
                if b in [2, 3, 5, 6]:
                    day_button.grid(row = a, column = b, padx = 30, pady = 10)
                else:
                    day_button.grid(row = a, column = b, padx = 10, pady = 10)
            counter = counter + 1


        # Next and previous month buttons
        btn_previous = tk.Button(self, text="Previous Month",
                                 command=lambda: master.switch_frame(Calendar, calendar_previous))
        btn_previous.grid(row = 8, column = 1, padx = 10, pady = 10)

        
        btn_next = tk.Button(self, text="Next Month",
                             command=lambda: master.switch_frame(Calendar, calendar_next))
        btn_next.grid(row = 8, column = 4, padx = 10, pady = 10)

        
        btn_return = tk.Button(self, text="Return to Menu",command=lambda: master.switch_frame(StartPage, None))
        btn_return.grid(row = 8, column = 7, padx = 10, pady = 10)

########################################################################################################################

class DateActions(tk.Frame):
    def __init__(self, master, var1):
        
        tk.Frame.__init__(self, master)
        master.title(var1)

        date_splitter = var1.split(" ")
        day = date_splitter[0]
        month = date_splitter[1]
        year = date_splitter[2]
        month_year = month + " " + year

        lbl_display = tk.Label(self, text= var1)
        lbl_display.grid(row = 0, column = 2)


        # Code for the tasks listbox
        self.task_box = tk.Listbox(self)
        
        with open('data.csv') as file1:
            reader = csv.reader(file1)
            task_list = []
            for row in reader:
                if row == []:
                    pass
                else:
                    if row[0] == month and row[1] == year and row[2] == day:
                        if row[3] == 'taskinfo':
                            pass
                        else:
                            task_list.append(row[3])


        # Separating taskinfo into desired outcomes
        name_list = []
        color_list = []

        for element in task_list:
            index1 = element.index(';')
            just_task = element[index1+1:]
            index2 = just_task.index(';')

            # Variables holding the task name string and color string
            just_name = just_task[index2+1:]
            just_color = just_task[:index2]
            
            name_list.append(just_name)
            color_list.append(just_color)

            self.task_box.insert("end", just_name)
        

        # Coloring the tasks
        color_counter = 0
        for color in color_list:
            self.task_box.itemconfig(color_counter, bg = color)
            color_counter = color_counter + 1
        
        self.task_box.grid(row = 2, column = 3)

        btn_add = tk.Button(self, text="Add Task", command=lambda: master.switch_frame(TaskEditor, var1 + ";Add Task;"))
        btn_add.grid(row = 1, column = 1)

        btn_edit = tk.Button(self, text="Edit Task", command=lambda: self.edit_button(var1, self.task_box.curselection()))
        btn_edit.grid(row = 2, column = 1)

        btn_del = tk.Button(self, text="Delete Task", command = lambda: self.delete(self.task_box.curselection(), var1))
        btn_del.grid(row = 3, column = 1)

        is_leap_year = False
        if int(year) % 4 == 0:
            is_leap_year = True
            if int(year) % 100 == 0:
                is_leap_year = False
                if int(year) % 400 == 0:
                    is_leap_year = True
        else:
            is_leap_year = False

        month_index = months.index(month)
        no_of_days = month_days[month_index]

        if int(day) == 28 and month == "February" and is_leap_year == False:
            next_date = "1 March " + year
        if int(day) == 28 and month == "February" and is_leap_year == True:
            next_date = "29 February " + year
        elif int(day) == 29 and month == "February" and is_leap_year == True:
            next_date = "1 March " + year
        elif int(day) == 31 and month == "December":
            next_date = "1 January " + str(int(year)+1)
        elif int(day) == int(no_of_days):
            next_date = "1 " + months[month_index+1] + " " + year
        else:
            next_date = str(int(day) + 1) + " " + month + " " + year

        if int(day) == 1 and month == "January":
            prev_date = "31 December " + str(int(year)-1)
        elif int(day) == 1 and month == "March" and is_leap_year == True:
            prev_date = "29 February " + year
        elif int(day) == 1 and month == "March" and is_leap_year == False:
            prev_date = "28 February " + year
        elif int(day) == 1:
            prev_date = month_days[month_index-1] + " " + months[month_index-1] + " " + year
        else:
            prev_date = str(int(day) - 1) + " " + month + " " + year

        btn_prevday = tk.Button(self, text="Previous Day", command=lambda: master.switch_frame(DateActions, prev_date))
        btn_prevday.grid(row = 4, column = 1)

        btn_nextday = tk.Button(self, text="Next Day", command=lambda: master.switch_frame(DateActions, next_date))
        btn_nextday.grid(row = 4, column = 2)

        btn_back = tk.Button(self, text="Return to Calendar", command=lambda: master.switch_frame(Calendar, month_year))
        btn_back.grid(row = 4, column = 3)

    def edit_button(self, var1, index):
        task_name = self.task_box.get(index[0])
        task_color = self.task_box.itemcget(index[0], "background")
        task_info = task_name + ";" + task_color
        self.master.switch_frame(TaskEditor, var1 + ";Edit Task;" + task_info)

    def delete(self, index, date):
        task_name = self.task_box.get(index[0])
        task_color = self.task_box.itemcget(index[0], "background")
        full_task = date + ";" + task_color + ";" + task_name
        self.task_box.delete(index[0])

        all_tasks = []

        with open('data.csv', 'r') as file1:
            reader = csv.reader(file1)
            for csv_row in reader:
                if csv_row == []:
                    pass
                else:
                    if csv_row[3] != full_task:
                        all_tasks.append(csv_row)

        with open('data.csv', 'w') as file2:
            writer = csv.writer(file2)
            for row in all_tasks:
                writer.writerow(row)

########################################################################################################################

class TaskEditor(tk.Frame):
    def __init__(self, master, var1):
        
        tk.Frame.__init__(self, master)

        colon_index = var1.index(';')
        var1_rest = var1[colon_index+1:]

        second_index = var1_rest.index(';')
        task_action = var1_rest[:second_index]

        if task_action == "Edit Task":
            submit_text = "Submit Changes"
            task_details = var1_rest[second_index + 1:]
            task_divider = task_details.index(';')

            task_name = task_details[:task_divider]
            task_color = task_details[task_divider + 1:]
        else:
            submit_text = "Add Task"

        var1 = var1[:colon_index]
        
        master.title(var1)

        lbl_display = tk.Label(self, text= var1)
        lbl_display.grid(row = 0, column = 2)

        if task_action == "Edit Task":
            self.lbl_preview = tk.Label(self, text= task_name, bg = task_color)
        else:
            self.lbl_preview = tk.Label(self, text=" ")
        self.lbl_preview.grid(row = 1, column = 2)

        lbl_name = tk.Label(self, text= "Name:")
        lbl_name.grid(row = 2, column = 1)

        entry_name = tk.Entry(self)
        entry_name.grid(row = 2, column = 3)

        lbl_color = tk.Label(self, text= "Color:")
        lbl_color.grid(row = 3, column = 1)

        entry_color = tk.Entry(self)
        entry_color.grid(row = 3, column = 3)
        
        btn_preview = tk.Button(self, text="Preview", command = lambda: self.preview(entry_name.get(), entry_color.get()))
        btn_preview.grid(row = 4, column = 2)

        if submit_text == "Add Task":
            btn_submit = tk.Button(self, text=submit_text, command=lambda: self.add_task(var1, entry_name.get(), entry_color.get()))
        else:
            btn_submit = tk.Button(self, text=submit_text, command=lambda: self.edit_task(var1, task_name, task_color, entry_name.get(), entry_color.get()))
        btn_submit.grid(row = 5, column = 2)

        btn_back = tk.Button(self, text="Return to Actions", command=lambda: master.switch_frame(DateActions, var1))
        btn_back.grid(row = 6, column = 2)


    def preview(self, name, color):
        self.lbl_preview.destroy()
        self.lbl_preview = tk.Label(self, text = name, bg = color)
        self.lbl_preview.grid(row = 1, column = 2)


    def edit_task(self, date, old_name, old_color, new_name, new_color):
        old_task = date + ";" + old_color + ";" + old_name
        new_task = date + ";" + new_color + ";" + new_name

        date_splitter = date.split(" ")

        day = date_splitter[0]
        month = date_splitter[1]
        year = date_splitter[2]

        all_tasks = []

        with open('data.csv', 'r') as file3:
            reader = csv.reader(file3)
            for csv_row in reader:
                if csv_row == []:
                    pass
                else:
                    if csv_row[3] == old_task:
                        all_tasks.append([month, year, day, new_task])
                    else:
                        all_tasks.append(csv_row)

        with open('data.csv', 'w') as file4:
            writer = csv.writer(file4)
            for task_details in all_tasks:
                writer.writerow(task_details)

        self.master.switch_frame(DateActions, date)


    def add_task(self, date, name, color):
        task = date + ";" + color + ";" + name
        date_splitter = date.split(' ')
        day = date_splitter[0]
        month = date_splitter[1]
        year = date_splitter[2]
        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([month, year, day, task])
        self.master.switch_frame(DateActions, date)

########################################################################################################################

if __name__ == "__main__":
    app = SampleApp()
    app.title("My Calendar!")
    app.mainloop()
