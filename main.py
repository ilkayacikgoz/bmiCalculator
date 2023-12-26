import tkinter
window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30,pady=30)
window.geometry("500x200")

def select_gender():
    global result_gender
    gender_selection = gender.get()
    if gender_selection == 1:
        result_gender = "Mr"
    else:
        result_gender = "Mrs"
    return result_gender

def calculate_bmi():
    height=height_input.get()
    weight=weight_input.get()
    select_gender()

    if weight=="" or height=="":
        result_label.config(text="Enter both weight and height!")

    else:
        try:
            height_float = float(height)
            weight_float = float(weight)
            bmi= weight_float / (height_float / 100) **2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number")


#ui
name_input_label = tkinter.Label(text="Enter your name: ")
name_input_label.grid(column=0,row=0,sticky=tkinter.W)


name_input = tkinter.Entry(width=10)
name_input.grid(column=1,columnspan=2,row=0,sticky=tkinter.W)


gender_input_label=tkinter.Label(text="Select your gender: ")
gender_input_label.grid(column=0,row=1,sticky=tkinter.W)
gender = tkinter.IntVar()
gender_male = tkinter.Radiobutton(text="Male",variable=gender, value= 1)
gender_male.grid(column=1,row=1)
gender_female = tkinter.Radiobutton(text="Female",variable=gender,value= 2)
gender_female.grid(column=2,row=1,sticky=tkinter.W)


weight_input_label = tkinter.Label(text="Enter your weight (kg)")
weight_input_label.grid(column=0,row=2,sticky=tkinter.W)

weight_input = tkinter.Entry(width=10)
weight_input.grid(column=1,columnspan=2,row=2,sticky=tkinter.W)

height_input_label = tkinter.Label(text="Enter your height (cm)")
height_input_label.grid(column=0,row=3,sticky=tkinter.W)

height_input = tkinter.Entry(width=10)
height_input.grid(column=1,columnspan=2,row=3,sticky=tkinter.W)


calculate_button = tkinter.Button(text="Calculate",command=calculate_bmi)
calculate_button.grid(column=0,row=4,sticky=tkinter.W)
result_label=tkinter.Label()
result_label.grid(columnspan=3,row=5,sticky=tkinter.W)




def write_result(bmi):
    global result_gender
    result_string= f"{result_gender} {name_input.get()} your BMI is: {round(bmi,2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif bmi > 16 and bmi <=17:
        result_string += "moderately thin!"
    elif bmi > 17 and bmi <= 18.5:
        result_string += "mild thinness!"
    elif bmi > 18.5 and bmi <= 25:
        result_string += "normal!"
    elif bmi > 25 and bmi <= 30:
        result_string += "overweight!!"
    elif bmi > 30 and bmi <= 35:
        result_string += "obese class 1 !!"
    elif bmi > 35 and bmi <= 40:
        result_string += "obese class 2 !!"
    else:
        result_string += "obese class 3 !!"
    return result_string


window.mainloop()