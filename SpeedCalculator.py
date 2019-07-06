from tkinter import *

root = Tk()
root.title('Speed Calculator')
root.geometry("250x400")


frequencyLabel = Label(root, text="Frequency: ")
frequencyBox = Entry(root, bd=5)

targetsLabel = Label(root, text="Targets: ")
targetsBox = Entry(root, bd=5)

diameterLabel = Label(root, text="Diameter Of Wheel: ")
diameterBox = Entry(root, bd=5)

secsPerHour = 3600
pi = 3.14159
inchesPerMile = 1 * 12 * 5280


def getSpeed():
    (float(frequencyBox.get()) / (float(targetsBox.get())) * float(secsPerHour)) * (pi * float(diameterBox.get()) / float(inchesPerMile))


def calculateSpeed():
    speed = (float(frequencyBox.get()) / (float(targetsBox.get())) * float(secsPerHour)) * (pi * float(diameterBox.get()) / float(inchesPerMile))
    speedBox.insert(0, speed)


speedLabel = Label(root, text="Speed: ")
speedBox = Entry(root, bd=9, width=10)

CalculateSpeed = Button(root, text="Calculate", command=getSpeed)

submitButton = Button(root, text="Submit", command=calculateSpeed)

quitButton = Button(root, text="Quit", command=root.quit)


frequencyLabel.pack()
frequencyBox.pack()

targetsLabel.pack()
targetsBox.pack()

diameterLabel.pack()
diameterBox.pack()

speedLabel.pack()
speedBox.pack()

submitButton.pack()
quitButton.pack()

root.mainloop()
