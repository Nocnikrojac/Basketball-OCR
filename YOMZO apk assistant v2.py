from tkinter import*

def save_info():
    
    URL_info = URL.get()
    URL_info = str(URL_info)
    CSV_info = CSV.get()
    CSV_info = str(CSV_info)
    adress = (URL.get() + CSV.get())

    file = open("IP-CSV.txt", "w")
    file.write (URL_info + CSV_info)
    file.close()

    screen.mainloop()
    
    while True:

            from urllib import request

            f = open("IP-CSV.txt", "r")
            
            url = (f.read())
            response = request.urlopen(url)
            line = response.read().decode('latin-1')
          

            outFileName="OBStime.txt"
            outFile=open(outFileName, "w")
            outFile.write(line[-7:])
            outFile.close()

screen = Tk()
screen.geometry("220x330")
screen.title("Python Form")
heading = Label(text = "YOMZO assistant", bg = "black", fg = "white", width = "500", height = "3")
heading.pack()

URL_text = Label(text = "URL ADDRESS:",)
CSV_text = Label(text = "NAME OF CSV FILE:",)
URL_text.place(x = 15, y = 70)
CSV_text.place (x = 15, y = 140)

URL = StringVar()
CSV = StringVar()

URL_entry = Entry(textvariable = URL, width = "30")
CSV_entry = Entry(textvariable = CSV, width = "30")

URL_entry.place(x = 15, y = 100)
CSV_entry.place(x = 15, y = 175)

register = Button(screen, text = "1. REGISTER", width = "25", height = "2", command = save_info, bg = "yellow")
register.place(x = 15, y =220)

run = Button(screen, text = "2. RUN", width = "25", height = "2", command = screen.destroy, bg = "green")
run.place(x = 15, y =270)
