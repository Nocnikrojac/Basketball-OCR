# YOMZO apk assistant / sends live time to OBS using FOLDER SERVER apk
# for basketball scoreboard

         import tkinter as tk

         master = tk.Tk()
         tk.Label(master, 
                  text="URL:", width = "5").grid(row=0)
         tk.Label(master, 
                  text="CSV:", width = "5").grid(row=1)

         e1 = tk.Entry(master)
         e2 = tk.Entry(master)

         e1.grid(row=0, column=1)
         e2.grid(row=1, column=1)

         def show_entry_fields():

             file = open("IP-CSV.txt", "w")
             file.write ((e1.get() + e2.get()))
             file.close()
             print ("URL: %s\nCSV: %s" % (e1.get(), e2.get()))

         tk.Button(master, 
                   text='ENTRY', height = 2, width = 16, bg='yellow', command=show_entry_fields).grid(row=3, 
                                                                column=0, 
                                                                sticky=tk.W, 
                                                                pady=4)

         tk.Button(master, 
                   text='START', height = 2, width = 16, bg='green', command=master.destroy).grid(row=3, 
                                             column=1, 
                                             sticky=tk.W, 
                                             pady=4)


         tk.mainloop()

         while True:

             from urllib import request

             f = open("IP-CSV.txt", "r")

             url = (f.read())
             response = request.urlopen(url)
             line = response.read().decode('latin-1')


             outFileName="OBStime.txt"
             outFile=open(outFileName, "w")
             outFile.write(line[-7:]) # or -5[-7:]
             outFile.close()
