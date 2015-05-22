## Built by John W. Harms ##
## Verson 0.01 -- Initial Build ##

import math
import Tkinter
import tkMessageBox
from Tkinter import *

root = Tk()
root.wm_title("ECI to COE")
label1 = Label(root, text="I:")
label1.grid(row=0, column=2)
E1 = Entry(root, bd=5)
label2 = Label(root, text="J:")
label2.grid(row=0, column=3)
E2 = Entry(root, bd=5)
label3 = Label(root, text="K:")
label3.grid(row=0, column=4)
E3 = Entry(root, bd=5)
label4 = Label(root, text="I:")
label4.grid(row=0, column=2)
E4 = Entry(root, bd=5)
label5 = Label(root, text="R Position")
label5.grid(row=1, column=1)
E5 = Entry(root, bd=5)
label6 = Label(root, text="V Velocity")
label6.grid(row=2, column=1)
E6 = Entry(root, bd=5)
# label7.grid(row=1, column=0)
# label8.grid(row=2, column=0)

# top = Tkinter.Tk()
# def hello():
#   tkMessageBox.showinfo("Say Hello", "Hello World")

# B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
# B1.pack()

# top.mainloop()

# Constants
mu = 398600.000000000000000000000


def RV2COE():
    RV2COE.rI_Input = float(E1.get())  # KM
    RV2COE.rJ_Input = float(E2.get())  # KM
    RV2COE.rK_Input = float(E3.get())  # KM
    RV2COE.vI_Input = float(E4.get())  # KM/s
    RV2COE.vJ_Input = float(E5.get())  # KM/s
    RV2COE.vK_Input = float(E6.get())  # KM/s

    RV2COE.rI = RV2COE.rI_Input + 0.000000000000000000000
    RV2COE.rJ = RV2COE.rJ_Input + 0.000000000000000000000
    RV2COE.rK = RV2COE.rK_Input + 0.000000000000000000000
    RV2COE.vI = RV2COE.vI_Input + 0.000000000000000000000
    RV2COE.vJ = RV2COE.vJ_Input + 0.000000000000000000000
    RV2COE.vK = RV2COE.vK_Input + 0.000000000000000000000
    # Calculations
    RV2COE.rVector = math.sqrt((math.pow(RV2COE.rI, 2)) + (math.pow(RV2COE.rJ, 2)) + (math.pow(RV2COE.rK, 2)))
    RV2COE.vVector = math.sqrt((math.pow(RV2COE.vI, 2)) + (math.pow(RV2COE.vJ, 2)) + (math.pow(RV2COE.vK, 2)))
    math.sqrt((math.pow(RV2COE.rI, 2)) + (math.pow(RV2COE.rJ, 2)) + (math.pow(RV2COE.rK, 2)))

    RV2COE.crossI = (RV2COE.rJ * RV2COE.vK) - (RV2COE.vJ * RV2COE.rK)
    RV2COE.crossJ = (RV2COE.rI * RV2COE.vK) - (RV2COE.vI * RV2COE.rK)
    RV2COE.crossK = (RV2COE.rI * RV2COE.vJ) - (RV2COE.vI * RV2COE.rJ)
    RV2COE.crossVector = math.sqrt(
        (math.pow(RV2COE.crossI, 2)) + (math.pow(RV2COE.crossJ, 2)) + (math.pow(RV2COE.crossK, 2)))

    RV2COE.dotI = (RV2COE.rI * RV2COE.vI)
    RV2COE.dotJ = (RV2COE.rJ * RV2COE.vJ)
    RV2COE.dotK = (RV2COE.rK * RV2COE.vK)
    RV2COE.dotVector = (RV2COE.dotI + RV2COE.dotJ + RV2COE.dotK)

    RV2COE.nI = RV2COE.crossI
    RV2COE.nJ = RV2COE.crossJ
    RV2COE.nK = 0
    RV2COE.nVector = math.sqrt((math.pow(RV2COE.nI, 2)) + (math.pow(RV2COE.nJ, 2)) + (math.pow(RV2COE.nK, 2)))
    RV2COE.eI = ((1 / mu) * (((((math.pow(RV2COE.vVector, 2))) - (mu / RV2COE.rVector))) * RV2COE.rI) - (
        (1 / mu) * (RV2COE.dotVector * RV2COE.vI)))
    RV2COE.eJ = ((1 / mu) * (((((math.pow(RV2COE.vVector, 2))) - (mu / RV2COE.rVector))) * RV2COE.rJ) - (
        (1 / mu) * (RV2COE.dotVector * RV2COE.vJ)))
    RV2COE.eK = ((1 / mu) * (((((math.pow(RV2COE.vVector, 2))) - (mu / RV2COE.rVector))) * RV2COE.rK) - (
        (1 / mu) * (RV2COE.dotVector * RV2COE.vK)))
    RV2COE.eVector = math.sqrt((math.pow(RV2COE.eI, 2)) + (math.pow(RV2COE.eJ, 2)) + (math.pow(RV2COE.eK, 2)))

    RV2COE.angMom = RV2COE.crossVector
    RV2COE.spMechEn = (((math.pow(RV2COE.vVector, 2)) / 2) - (mu / RV2COE.rVector))

    # SemiMajor Axis
    RV2COE.semiMajorAxis = (-1) * (mu / (2 * RV2COE.spMechEn))
    # Eccentricity
    RV2COE.ecc = RV2COE.eVector
    # Inclination
    if (math.degrees(math.acos(RV2COE.crossK / RV2COE.crossVector))) < 180:
        RV2COE.incl = math.degrees(math.acos(RV2COE.crossK / RV2COE.crossVector))
    else:
        RV2COE.incl = 180 - math.degrees(math.acos(RV2COE.crossK / RV2COE.crossVector))
    # RAAN
    if RV2COE.nVector < 0:
        RV2COE.raan = math.degrees(math.acos(RV2COE.nJ / RV2COE.nVector))
    else:
        RV2COE.raan = 360 - (math.degrees(math.acos(RV2COE.nJ / RV2COE.nVector)))
    # Argument of Perigee
    if RV2COE.eK < 0:
        RV2COE.aPer = (math.degrees(math.acos(
            ((RV2COE.nJ * RV2COE.eI) + (RV2COE.nI * RV2COE.eJ) + (RV2COE.nK * RV2COE.eK)) / (
                RV2COE.nVector * RV2COE.ecc))))
    else:
        RV2COE.aPer = (360 - math.degrees(math.acos(
            ((RV2COE.nJ * RV2COE.eI) + (RV2COE.nI * RV2COE.eJ) + (RV2COE.nK * RV2COE.eK)) / (
                RV2COE.nVector * RV2COE.ecc))))
    # True Anomaly
    if RV2COE.dotVector > 0:
        RV2COE.trueAnom = math.degrees(math.acos((((RV2COE.eI * RV2COE.rI) + (RV2COE.eJ * RV2COE.rJ) + (
            RV2COE.eK * RV2COE.rK)) / (RV2COE.eVector * RV2COE.rVector))))
    else:
        RV2COE.trueAnom = 360 - math.degrees(math.acos((((RV2COE.eI * RV2COE.rI) + (RV2COE.eJ * RV2COE.rJ) + (
            RV2COE.eK * RV2COE.rK)) / (RV2COE.eVector * RV2COE.rVector))))

    RV2COE_output = (
        "Semi-Major Axis:", RV2COE.semiMajorAxis, "\nEccentricity:", RV2COE.ecc, "\nInclination:", RV2COE.incl,
        "\nRAAN:", RV2COE.raan, "\nArgument of Perigee:", RV2COE.aPer, "\nTrue Anomaly:", RV2COE.trueAnom)

    # RV2COE_output = (
    # "SemiMajor Axis",
    # RV2COE.semiMajorAxis)

    labelframe = LabelFrame(root, text="This is a LabelFrame")
    labelframe.grid(row=6, column=1)
    left = Label(root, text=RV2COE_output, justify=LEFT)
    left.grid(row=7, column=1)

    # tkMessageBox("Output", RV2COE_output)
    ##var = StringVar()
    # label = Label( root, textvariable=var, relief=RAISED )
    # var.set(RV2COE_output)
    # label.grid(row=5, column=1,)


    return (RV2COE)


def close_window():
    root.destroy()


E1.grid(row=1, column=2)
E2.grid(row=1, column=3)
E3.grid(row=1, column=4)
E4.grid(row=2, column=2)
E5.grid(row=2, column=3)
E6.grid(row=2, column=4)

button = Button(root)
button['text'] ="Quit"
button['command'] = close_window
button.grid(row=3, column=2)
submit = Button(root, text ="Submit", command = RV2COE)
submit.grid(row=3, column=1)

root.mainloop()
