import tkinter

window = tkinter.Tk()
window.title("BIM  INDEX CALCULATOR")
window.minsize(height=450,width=520)

def calculateBIM():
    Weight = (my_enteryWeight.get())
    height = (my_entery2_Hight.get())



    def calculatorBIM(result):
        calculator1 = f"Your BMI is {round(result, 2)}. You are "
        if result < 18.4:
            calculator1 += "a thin person"
        elif 18.4 < result < 22.4:
            calculator1 += "a normal person"
        elif 22.4 < result < 29.9:
            calculator1 += "a fat person"
        else:
            calculator1 += "a obes person"
        return calculator1
    if Weight == "" or height == "":
        my_Last_Label.config(text="Enter both weight and height!")
    else:
        try:
            Weight = float(my_enteryWeight.get())
            height = float(my_entery2_Hight.get())

            BIM = Weight / (height * height)
            BIM2 = round(BIM, 2)
            calculator2 = calculatorBIM(BIM2)
            my_Last_Label.config(text = calculator2)
        except ValueError:
            my_Last_Label.config(text="Enter a valid number!")






my_label1 = tkinter.Label(text="Enter your weight(kg)")
my_label1.place(x=200, y=50)

my_enteryWeight = tkinter.Entry()
my_enteryWeight.place(x=199, y=70)

my_label2 = tkinter.Label(text="Enter your height (m)")
my_label2.place(x=200, y=100)

my_entery2_Hight = tkinter.Entry()
my_entery2_Hight.place(x=199, y=130)


my_button = tkinter.Button(text="Calculate", command= calculateBIM)
my_button.place(x=230, y=160)
my_Last_Label = tkinter.Label(font=("Helvetica", "12"))
my_Last_Label.place(x=165, y=250)
my_Last_Label.config(fg="red")






tkinter.mainloop()





