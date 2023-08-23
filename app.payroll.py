from tkinter import *

root = Tk()
root.title("Υπολογισμός Μισθοδοσίας    Προγραμματισμός-Αγούλας Νίκος")


def check_error():
    if int(yperergasia.get()) < 0 or int(yperergasia.get()) > 32:
        error_yperergasia.config(text="Επιτρέπονται τιμές απο 0 εώς 32.")
        result["text"] = "Invalid input! Please enter valid numbers."
        return -1


def check_yperwries():
    if int(yperwries.get()) < 0 or int(yperwries.get()) > 44:
        error_yperwries.config(text="Επιτρέπονται τιμές απο 0 εώς 44.")
        result["text"] = "Invalid input! Please enter valid numbers."
        return -1


def apwn_error():
    if int(apwn.get()) < 0 or int(apwn.get()) > 25:
        error_apwn.config(text="Επιτρέπονται τιμές απο 0 εώς 25.")
        result["text"] = "Invalid input! Please enter valid numbers."
        return -1


def check_tekna():
    if int(tekna.get()) < 0 or int(tekna.get()) > 20:
        error_tekna.config(text="Επιτρέπονται τιμές απο 0 εώς 20.")
        result["text"] = "Invalid input! Please enter valid numbers."
        return -1


def miktos():
    try:
        x = float(synolo_symfwnithentos_misthou.get())
    except ValueError:
        result.config(text="Invalid input! Please enter valid numbers.")
    return x


def wromisthi():
    y = miktos()
    wromisthio = (y / 25) * 6 / 40
    return wromisthio


def ypol_yperergasias():
    error_yperergasia["text"] = " "
    k = check_error()
    if k == -1:
        return
    else:
        y = wromisthi()
        x = int(yperergasia.get())
        x = (((y * 20) / 100) * x + (y * x))
    return x


def ypol_ypwrwries():
    error_yperwries["text"] = " "
    k = check_yperwries()
    if k == -1:
        return
    try:
        y = wromisthi()
        x = int(yperwries.get())
        if x > 120:
            x = (((y * 60) / 100) * x) + (y * x)
        if x <= 120:
            x = (((y * 40) / 100) * x) + (y * x)
    except ValueError:
        result["text"] = "Invalid input! Please enter valid number"
    return x


def ypol_apwn():
    error_apwn["text"] = " "
    k = apwn_error()
    if k == -1:
        return

    try:
        x = int(apwn.get())
    except ValueError:
        result["text"] = "Invalid input! Please enter valid number"
    return x


def ypol_tekna():
    error_tekna["text"] = " "
    k = check_tekna()
    if k == -1:
        return x

    try:
        x = int(tekna.get())
    except ValueError:
        result["text"] = "Invalid input! Please enter valid number"
    return x


def ypol_meiktwn():
    x = miktos()
    y = ypol_yperergasias()
    z = ypol_ypwrwries()
    a = ypol_apwn()
    meiwsi_apo_apousies = x / 25
    synolo_apodoxwn = x + y + z - (meiwsi_apo_apousies * a)
    return synolo_apodoxwn


def ypol_ika():
    x = ypol_meiktwn()
    ika = 18.32
    kratiseis_ika = ((x * ika) / 100)
    return kratiseis_ika


def kratiseis_fmy():
    x = ypol_meiktwn()
    y = ypol_ika()
    z = ypol_tekna()
    forologiteo = ((x - y) * 14)
    syntelestis_meiwsis = ((forologiteo - 12000) / 1000) * 20
    klimaka_paidiwn = 0
    foros = 0
    if z == 0 and forologiteo <= 12000:
        klimaka_paidiwn = 777
    elif z == 0 and forologiteo > 12000:
        klimaka_paidiwn = 777 - syntelestis_meiwsis
    elif z == 1 and forologiteo <= 12000:
        klimaka_paidiwn = 810
    elif z == 1 and forologiteo > 12000:
        klimaka_paidiwn = 810 - syntelestis_meiwsis
    elif z == 2 and forologiteo <= 12000:
        klimaka_paidiwn = 900
    elif z == 2 and forologiteo > 12000:
        klimaka_paidiwn = 900 - syntelestis_meiwsis
    elif z == 3 and forologiteo <= 12000:
        klimaka_paidiwn = 1120
    elif z == 3 and forologiteo > 12000:
        klimaka_paidiwn = 1120 - syntelestis_meiwsis
    elif z == 4 and forologiteo <= 12000:
        klimaka_paidiwn = 1340
    elif z == 4 and forologiteo > 12000:
        klimaka_paidiwn = 1340 - syntelestis_meiwsis
    elif z == 5 and forologiteo <= 12000:
        klimaka_paidiwn = 1560
    elif z == 5 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 6 and forologiteo <= 12000:
        klimaka_paidiwn = 1780
    elif z == 6 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 7 and forologiteo <= 12000:
        klimaka_paidiwn = 2000
    elif z == 7 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 8 and forologiteo <= 12000:
        klimaka_paidiwn = 2220
    elif z == 8 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 9 and forologiteo <= 12000:
        klimaka_paidiwn = 2440
    elif z == 9 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 10 and forologiteo <= 12000:
        klimaka_paidiwn = 2660
    elif z == 10 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 11 and forologiteo <= 12000:
        klimaka_paidiwn = 2880
    elif z == 11 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 12 and forologiteo <= 12000:
        klimaka_paidiwn = 3100
    elif z == 12 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 13 and forologiteo <= 12000:
        klimaka_paidiwn = 3320
    elif z == 13 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 14 and forologiteo <= 12000:
        klimaka_paidiwn = 3540
    elif z == 14 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 15 and forologiteo <= 12000:
        klimaka_paidiwn = 3760
    elif z == 15 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 16 and forologiteo <= 12000:
        klimaka_paidiwn = 3980
    elif z == 16 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 17 and forologiteo <= 12000:
        klimaka_paidiwn = 4200
    elif z == 17 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 18 and forologiteo <= 12000:
        klimaka_paidiwn = 4420
    elif z == 18 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 19 and forologiteo <= 12000:
        klimaka_paidiwn = 4640
    elif z == 19 and forologiteo > 12000:
        klimaka_paidiwn = 1340
    elif z == 20 and forologiteo <= 12000:
        klimaka_paidiwn = 4860
    elif z == 20 and forologiteo > 12000:
        klimaka_paidiwn = 1340

    if forologiteo <= 10000:
        foros = ((forologiteo * 9) / 100)

    if forologiteo > 10000 & (forologiteo <= 20000):
        foros = (10000 * 9) / 100 + ((forologiteo - 10000) * 22) / 100
    if 20000 < forologiteo <= 30000:
        foros = (10000 * 9) / 100 + (10000 * 22 / 100) + ((forologiteo - 20000) * 28) / 100
    if 30000 < forologiteo <= 40000:
        foros = (10000 * 9) / 100 + (10000 * 22 / 100) + (10000 * 28 / 100) + ((forologiteo - 30000) * 36) / 100
    if forologiteo > 40000:
        foros = (10000 * 9 / 100) + (10000 * 22 / 100) + (10000 * 28 / 100) + (10000 * 36 / 100) + (
                (forologiteo - 40000) * 44) / 100
    foros = (foros - klimaka_paidiwn) / 14
    if foros < 0:
        foros = 0
    return foros


def kathares_apodoxes():
    x = ypol_meiktwn()
    y = ypol_ika()
    z = kratiseis_fmy()
    plirwtees_apodoxes = x - y - z
    result["text"] = f"Ο καθαρός μισθός είναι : {plirwtees_apodoxes:.2f}"
    return plirwtees_apodoxes


root.geometry('{}x{}'.format(900, 600))

label1 = Label(root, text=" Μικτός μισθός")
label1.grid(row=20, column=50, padx=270, pady=(100, 10))

synolo_symfwnithentos_misthou = Entry(root)
synolo_symfwnithentos_misthou.grid(row=22, column=50)

label2 = Label(root, text=" Υπερεργασία")
label2.grid(row=28, column=5)

yperergasia = Spinbox(root, from_=0, to=32)
yperergasia.grid(row=30, column=5)

error_yperergasia = Label(root, text=" ")
error_yperergasia.grid(row=32, column=5)

label3 = Label(root, text=" Υπερωρίες")
label3.grid(row=28, column=1660)

yperwries = Spinbox(root, from_=0, to=44)
yperwries.grid(row=30, column=1660)

error_yperwries = Label(root, text=" ")
error_yperwries.grid(row=32, column=1660)

label5 = Label(root, text=" Απών")
label5.grid(row=36, column=1660)

apwn = Spinbox(root, from_=0, to=22)
apwn.grid(row=38, column=1660)

error_apwn = Label(root, text=" ")
error_apwn.grid(row=40, column=1660)

label6 = Label(root, text=" Εξαρτώμενα τέκνα")
label6.grid(row=36, column=5)

tekna = Spinbox(root, from_=0, to=20)
tekna.grid(row=38, column=5)

error_tekna = Label(root, text=" ")
error_tekna.grid(row=40, column=5)

btn1 = Button(root, text="Υπολογισμός μισθοδοσίας", bg="#BFEFFF", command=kathares_apodoxes)
btn1.grid(row=65, column=50)

result = Label(root, text=" ")
result.grid(row=70, column=50)

root.rowconfigure(100, weight=100)
root.columnconfigure(100, weight=100)
root.columnconfigure(30, weight=100)

root.mainloop()
