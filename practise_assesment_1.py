from tkinter import *

main_window =Tk()

def quit():
    main_window.destroy()
    
def print_camp_details ():
    global j_names, total_entries, name_count
    name_count = 0
    Label(main_window, text="Row", font='bold') .grid(column=0, row=7)
    Label(main_window, text="Group Leader", font='bold') .grid(column=1, row=7)
    Label(main_window, text="Number of Campers", font='bold') .grid(column=2, row=7)
    Label(main_window, text="Location", font='bold') .grid(column=3, row=7)
    Label(main_window, text="Weather", font='bold') .grid(column=4, row=7)

    while name_count < total_entries :
         Label(main_window, text=name_count) .grid(column=0, row=name_count+8)
         Label(main_window, text=(camp_details[name_count][0])) .grid(column=1, row=name_count+8)
         Label(main_window, text=(camp_details[name_count][1])) .grid(column=2, row=name_count+8)
         Label(main_window, text=(camp_details[name_count][2])) .grid(column=3, row=name_count+8)
         Label(main_window, text=(camp_details[name_count][3])) .grid(column=4, row=name_count+8)
         name_count += 1
                             
def append_name ():
    global camp_details, entry_leader, entry_location, entry_campers, entry_weather, entry_row, total_entries
    if len(entry_leader.get()) != 0 :
        camp_details.append([entry_leader.get(), entry_location.get(), entry_campers.get(), entry_weather.get(), entry_row.get()]) 
        entry_leader.delete(0,'end')
        entry_location.delete(0,'end')
        entry_campers.delete(0,'end')
        entry_weather.delete(0,'end')
        entry_row.delete(0,'end')

        
def setup_buttons ():
    Button(main_window, text="Update", bg="Blue") .grid(column=0, row=1)
    Button(main_window, text="Print Camp Details",command=print_camp_details) .grid(column=2, row=6)
    Button(main_window, text="Delete Row", bg="Red") .grid(column=3, row=6)
    Button(main_window, text="Quit",command=quit, bg="Red") .grid(column=4, row=1)
    Button(main_window, text="Append Details", command=append_name) .grid(column=1, row=1)
    Label(main_window, text="Sunshine Adventure Camp") .grid(column=1, row=0)
    Label(main_window, text="Row") .grid(column=0, row=6)
    entry_row = Entry(main_window) .grid(column=1, row=6)
    Label(main_window, text="Group Leader") .grid(column=0, row=2)
    entry_leader = Entry(main_window) .grid(column=1, row=2)
    Label(main_window, text="Number of Campers") .grid(column=0, row=3)
    entry_campers = Entry(main_window) .grid(column=1, row=3)
    Label(main_window, text="Location") .grid(column=0, row=4)
    entry_location = Entry(main_window) .grid(column=1, row=4)
    Label(main_window, text="Weather") .grid(column=0, row=5)
    entry_weather = Entry(main_window) .grid(column=1, row=5)


def main ():
    global main_window
    global camp_details, entry_name, entry_age, entry_gender, total_entries
    camp_details = []
    total_entries = 0
    setup_buttons()
    main_window.mainloop()

main()


    







