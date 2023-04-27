from tkinter import *
import customtkinter
import random
from tkinter import messagebox
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")

ewg = customtkinter.CTk()
ewg.title("English informatics word generator")
ewg.geometry("1920x1080+0+0")

img1 = Image.open("pictures/AIO.jpg")
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open("pictures/Socket.jpg")
img2 = ImageTk.PhotoImage(img2)

img3 = Image.open("pictures/heatsink.jpg")
img3 = ImageTk.PhotoImage(img3)

img4 = Image.open("pictures/pwm.jpg")
img4 = ImageTk.PhotoImage(img4)

img5 = Image.open("pictures/CAS.png")
img5 = ImageTk.PhotoImage(img5)

img6 = Image.open("pictures/TDP.jpg")
img6 = ImageTk.PhotoImage(img6)

bgimage = Image.open("pictures/background.png")
bgimage = ImageTk.PhotoImage(bgimage)

logo = Image.open("pictures/Screenshot_3.png")
logo = ImageTk.PhotoImage(logo)

bgframe = customtkinter.CTkCanvas(ewg, width=2000, height=1500, highlightbackground="black", background="black")
bgframe.create_image(100, 1000, image=bgimage)
bgframe.create_image(1800, 500, image=logo)
bgframe.place(x=0, y=0)

with open("worddatabase.txt", "r") as file:
    words = [line.rstrip() for line in file]


# main function
def generator(category):
    product = []
    if len(category) == 0:
        messagebox.showinfo(title="Program Complete", message="There are no more words to display.")
    if 15 > len(category) > 0:
        messagebox.showwarning(title="Numbers of words Limited",
                               message="Attention!!\n""Less than 10 words remain,\n" "Display might be limited")
        for selector in range(len(category)):
            selector = random.choice(category)
            product.append(selector)
            category.remove(selector)
            with open("historydatabase.txt", "w+") as hdb:
                for element in product:
                    hdb.write(element + "\n")
        result_display.delete(0, END)
        for item in product:
            result_display.insert(END, item)
        return result_display
    else:
        for selector in range(15):
            selector = random.choice(category)
            product.append(selector)
            category.remove(selector)
            with open("historydatabase.txt", "w+") as hdb:
                for element in product:
                    hdb.write(element + "\n")
        result_display.delete(0, END)
    with open("worddatabase.txt", "w+") as wdb:
        for element in category:
            wdb.write(element + "\n")
        for item in product:
            if item == "PWM(pulse width modulation) = Σύνδεση διαχείρισης παλμού*":
                det = "PWM:\n" \
                      "PWM ονομάζονται οι συνδέσεις των περιφερειακών ανεμιστήρων οι οποίες εφαρμόζουν στις υποδοχές " \
                      "ελέγχου της μητρικής κάρτας ή σε μια μονάδα μαζικού ελέγχου ομαδοποιημένων ανεμιστήρων" \
                      "(fan controller).\n \n "
                adinfo.insert(END, det)
            if item == "CAS(column address strobe/signal) = Σήμα διεύθυνσης στήλης*":
                det = "CAS:\n" \
                      "Το σήμα διεύθυνσης στήλης είναι ο αριθμός των κύκλων του ρολογιού που χρειάζεται η μνήμη " \
                      "τυχαίας προσπέλασης(RAM) για να αποκτήσει πρόσβαση στα σέτ δεδομένων που είναι αποθηκευμένα " \
                      "στις στήλες της. Το συναντάμε\nκυρίως σε ιστοσελίδες όπως το σκρούτζ στα χαρακτηριστικά των RΑΜ " \
                      "κατά την αναζήτηση αγοράς και είναι ένας απο τους ποιο σημαντικούς παράγοντες καθορισμού της " \
                      "ταχύτητας της συσκευής.\n \n"
                adinfo.insert(END, det)
            if item == "Heat-sink = παθητικός εναλλακτής θερμότητας*":
                det = "HEAT-SINK:\n" \
                      "Παρόλο πού από το δεύτερο συνθετικό της λέξης ο ακροατής παραπέμπεται στήν ελληνική λέξη\n" \
                      "νεροχύτης (sink = νεροχύτης) κάθε άλλο παρά σε νεροχύτη μοιάζει αυτο το εξάρτημα. " \
                      "Ο παθητικός εναλλακτής θερμότητας είναι ένα μεταλλικό μπλόκ με πολλαπλές εγκοπές στήν μια του " \
                      "πλευρά το οποίο \nμεταφέρει τη θερμότητα που παράγεται από μια ηλεκτρονική ή μια μηχανική συσκευή " \
                      "σε ένα ρευστό μέσο, συχνά αέρα ή υγρό ψυκτικό, όπου διαχέεται μακριά από τη συσκευή, " \
                      "επιτρέποντας έτσι τη ρύθμιση της θερμοκρασίας της συσκευής. \n \n"
                adinfo.insert(END, det)
            if item == "AIO(All-in-one) cooler = Ψήκτρα (Όλα σε ένα)*":
                det = "AIO:\n" \
                      "Η ψήκτρα ολα-σε-ενα έχει πάρα πολλές ομοιότητες με το σύστημα ψύξης το οποίο χρησιμοποίειτε " \
                      "στα αυτοκίνητα.\nΑπαρτίζεται απο 4 μερη: την αντλία, η οποία εφαρμόζει επάνω στον κεντρικό " \
                      "επεξεργαστή,\nδύο αγωγούς (συνήθως φτιαγμένοι απο σκληρό λάστιχο) απο τους οποίους διαχέεται " \
                      "το υγρό ψύξης \nαπό και πρός το ψυγείο, ανεμιστήρες(1 εως 3 ανάλογα με το μέγεθος της ψήκτρας) " \
                      "οι οποίοι βιδώνουν επάνω στο\nψυγείο για να ψύχουν με κρύο αέρα το υγρό και τέλος το ψυγείο " \
                      "ενα ορθογώνιο μεταλλικό κουτί με μεταλλικό πλέγμα στο κέντρο του που παγώνει από τον" \
                      "κρύο αέρα των ανεμηστήρων και αυτό με τη σειρά του παγώνει το υγρό.\nΚατά την αγορά τους μπορούμε " \
                      "να τις διακρίνουμε από το νούμερο στην ονομασία τους που υποδηλώνει\nκαι το μέγεθός τους, " \
                      "120: 1 ανεμιστήρας, 240: 2 ανεμιστήρες, 360: 3 ανεμιστήρες. \n \n"
                adinfo.insert(END, det)
            if item == "TDP(thermal design power = Σημείο Θερμικής σχεδίασης*":
                det = "TDP:\n" \
                      "Το σημείο θερμικής σχεδίασης σε Watt αναφέρεται στην μέγιστη κατανάλωση ενέργειας της συσκευής" \
                      "\nστο μέγιστο θεωρητικό φορτίο λειτουργίας. Καθώς το μέγιστο φορτίο λειτουργίας σπάνια " \
                      "επιτυγχάνεται σε \nπραγματικές συνθήκες συνιστάται κατά την αγορά να διαιρούμε αυτόν τον αριθμό " \
                      "διά 2. \n \n"
                adinfo.insert(END, det)
            if item == "Socket = Θύρα επεξεργαστή*":
                det = "SOCKET:\n" \
                      "Καθώς η ακριβής μετάφραση της λέξης είναι Θύρα/Υποδοχή στην πληροφορική η λεξη socket\n" \
                      "δεσμεύεται αποκλειστικά για την θύρα του κεντρικού επεξεργαστή με τις υπόλοιπες θύρες να " \
                      "παίρνουν\nτο όνομά τους είτε από το βύσμα τους είτε από τον τρόπο λειτουργίας τους. \n \n"
                adinfo.insert(END, det)
            result_display.insert(END, item)
        return result_display


data = None


# button and window functions
def datawindow(dwin):
    if dwin is None or not dwin.winfo.exists():
        dwin = customtkinter.CTkToplevel(ewg)
        dwin.geometry("800x800")
        dwin.title("Database")
        database_display = customtkinter.CTkTextbox(dwin, font=("Calibri", 20), bg_color="white", height=750, width=750)
        xi = open("worddatabase.txt", "r")
        for k in xi:
            database_display.insert(END, k)
        xi.close()
        database_display.place(x=10, y=10)
    else:
        dwin.focus()
    return dwin


pics = None


def openpicwin(picwindow):
    if picwindow is None or not picwindow.winfo_exists():
        picwindow = customtkinter.CTkToplevel(ewg)
        picwindow.geometry("1920x1080+0+0")
        picwindow.title("Pictures")
        picframe1 = customtkinter.CTkCanvas(picwindow, width=500, height=500)
        picframe1.create_image(250, 250, image=img1)
        picframe1.place(x=0, y=0)
        picframe2 = customtkinter.CTkCanvas(picwindow, width=250, height=250)
        picframe2.create_image(130, 130, image=img2)
        picframe2.place(x=5, y=550)
        picframe3 = customtkinter.CTkCanvas(picwindow, width=400, height=400)
        picframe3.create_image(250, 250, image=img3)
        picframe3.place(x=1200, y=50)
        picframe4 = customtkinter.CTkCanvas(picwindow, width=500, height=500)
        picframe4.create_image(270, 270, image=img4)
        picframe4.place(x=600, y=0)
        picframe5 = customtkinter.CTkCanvas(picwindow, width=420, height=350)
        picframe5.create_image(215, 200, image=img5)
        picframe5.place(x=600, y=550)
        picframe6 = customtkinter.CTkCanvas(picwindow, width=600, height=450)
        picframe6.create_image(300, 300, image=img6)
        picframe6.place(x=1200, y=500)
    else:
        picwindow.focus()
    return picwindow.focus()


guidetext = None


def programinfo(info):
    if info is None or not info.winfo.exists():
        infotoplevel = customtkinter.CTkToplevel(ewg)
        infotoplevel.geometry("800x1000+0+0")
        infotoplevel.title("Program Information")
        infolabel = customtkinter.CTkLabel(infotoplevel, font=("Calibri", 20), text_color="white",
                                           text="This program was made by a first year informatics student of the 2nd vocational\n"
                                                "night school of Kavala, Greece. Although it has been optimized for\n"
                                                "third party usage, it's main purpose was to further increase my\n"
                                                "understanding of coding and its applications on real-life problems.\n"
                                                "That being said, i really hope you will find it to be somewhat usefull\n"
                                                "at assisting you in your daily workload and also i would like to\n"
                                                "express my gratitude to you for choosing to use this software.\n"
                                                "Thank you!!!!\n"
                                                "Sincerely,\n"
                                                "Angis Panagiotis.(informatics B class).")
        infolabel.place(x=0, y=0)
        infolabel2 = customtkinter.CTkLabel(infotoplevel, font=("Calibri", 20), text_color="white",
                                            text="English Word generator(EWG) is a digital dictionary for the English\n"
                                                 "informatics class of my school. By clicking the 'Generate words'\n"
                                                 "button 15 random words from a 150+ words database will be displayed\n"
                                                 "on the window labeled 'Words' above.\n"
                                                 "The sum of words has been selected from the book given to the students\n"
                                                 "for the class, from other classes related to the field of informatics\n"
                                                 "and from my personal experience building and maintaining computers\n"

                                                 "for more than 10 years as a hobby.\n"
                                                 "Words marked by an asterisk(*), will have additional explanation\n"
                                                 "displayed on the window labeled 'additional information' and also\n"
                                                 "have photographs displaying either the device that is described or\n"
                                                 "real-life encounters of the terminology.\n"
                                                 "Warning messages will be shown when there are 15 or less words\n"
                                                 "remaining and/or when the database has been emptied.")
        infolabel2.place(x=0, y=400)
        infolabel3 = customtkinter.CTkLabel(infotoplevel, font=("Calibri", 20),
                                            text="Feel free to contact me at: Namkorr@gmail.com for more\n"
                                                 "information.")
        infolabel3.place(x=0, y=800)
    return info


histdat = None


def historywindow(hwin):
    if hwin is None or not hwin.winfo.exists():
        hwin = customtkinter.CTkToplevel(ewg)
        hwin.geometry("800x800+0+0")
        hwin.title("Database")
        hisdatabase_display = customtkinter.CTkTextbox(hwin, font=("Calibri", 20), bg_color="white", height=750, width=750)
        xi = open("historydatabase.txt", "r")
        for k in xi:
            hisdatabase_display.insert(END, k)
        xi.close()
        hisdatabase_display.place(x=0, y=200)
        historyinfo_label = customtkinter.CTkLabel(hwin, font=("Calibri", 20), text="Notice:\n"
                                                                                    "History Usage will only display\n"
                                                                                    "the latest word generation you created\n"
                                                                                    "Please be aware that multiple word generation\n"
                                                                                    "will not be displayed to its fullest.")
        historyinfo_label.place(x=0, y=0)
    else:
        hwin.focus()
    return hwin


# words list box display
result_label = customtkinter.CTkLabel(ewg, font=("Calibri", 30), text="Words")
result_label.place(x=700, y=10)

result_display = Listbox(ewg, selectmode=EXTENDED, font=("Calibri", 16), height=13, width=90)
result_display.place(x=700, y=50)

# additional info box display
adinfo_label = customtkinter.CTkLabel(ewg, font=("Calibri", 30), text="Additional information")
adinfo_label.place(x=700, y=450)

adinfo = customtkinter.CTkTextbox(ewg, font=("Calibri", 20), text_color="black", fg_color="white", height=400,
                                  width=1000)
adinfo.place(x=700, y=500)

# Interaction buttons
gen_button = customtkinter.CTkButton(ewg, width=100, fg_color="purple", font=("Calibri", 20), text="Generate words",
                                     command=lambda: generator(words))
gen_button.place(x=1400, y=450)

database_button = customtkinter.CTkButton(ewg, width=100, fg_color="purple", font=("Calibri", 20), text="Database",
                                          command=lambda: datawindow(data))
database_button.place(x=40, y=900)

pics_button = customtkinter.CTkButton(ewg, width=100, fg_color="purple", font=("Calibri", 20), text="Pictures",
                                      command=lambda: openpicwin(pics))
pics_button.place(x=160, y=900)

pinfo_button = customtkinter.CTkButton(ewg, width=100, fg_color="purple", text="Program Info", font=("Calibri", 20),
                                       command=lambda: programinfo(guidetext))
pinfo_button.place(x=350, y=900)

historyusage_button = customtkinter.CTkButton(ewg, width=100, fg_color="purple", text="Usage history", font=("Calibri", 20),
                                              command=lambda: historywindow(histdat))
historyusage_button.place(x=540, y=900)
ewg.mainloop()
