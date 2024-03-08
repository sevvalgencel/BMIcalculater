import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=30,pady=30)

def calculate_bmi():
   height = height_input.get()
   weight = weight_input.get()

   if weight == "" or height == "":
       result_label.config(text="Lütfen kilo ve boyu giriniz!")
   else:
      try:
           bmi = float(weight) /(float(height)/ 100) ** 2
           result_string = write_result(bmi)
           result_label.config(text=result_string)
      except:
          result_label.config(text="Lütfen bir sayı giriniz!")


#ui
weight_input_label = tkinter.Label(text="Lütfen kilonuzu giriniz (kg)")
weight_input_label.pack()

weight_input = tkinter.Entry(width_=10)
weight_input.pack()

height_input_label = tkinter.Label(text = "Lütfen boyunuzu giriniz(cm)")
height_input_label.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()

calculate_button = tkinter.Button(text="Hesapla", command=calculate_bmi )
calculate_button.pack()

result_label = tkinter.Label()
result_label.pack()

def write_result(bmi):
    result_string = f"Vücut kitle indeksiniz: {bmi}. Siz"
    if bmi <= 16:
        result_string += " çok zayıfsınız!"
    elif 16 < bmi <= 17:
        result_string += " orta dercede zayıfsınız!"
    elif 17 < bmi <= 18.5:
        result_string += " hafif zayıfsınız!"
    elif 18.5 < bmi <= 25:
        result_string += " normalsiniz!"
    elif 25 < bmi <= 30:
        result_string += " şişmansınız!"
    elif 30 < bmi <= 35:
        result_string+= " obezsiniz!"
    elif 35 < bmi <= 40:
        result_string += " 2. sınıf obezsiniz!"
    else:
        result_string += " 3. sınıf obezsiniz!"
    return result_string


window.mainloop()