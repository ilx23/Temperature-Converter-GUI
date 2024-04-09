from tkinter import *  # Let's import all the tkinter magic
from tkinter import messagebox  # For popping up helpful messages

def celsius_to_fahrenheit_setup():  # Setting up the Celsius to Fahrenheit conversion interface
    global celsius_entry, fahrenheit_result  # Making these variables accessible globally

    # Clearing the window of any existing widgets
    for widget in app.winfo_children():
        widget.destroy()

    # Title for our Celsius to Fahrenheit converter
    app_title = Label(app,text="Celsius To Fahrenheit", font=("nectar bold", 15))
    app_title.pack()

    # Labels and entry field for Celsius input
    celsius_label = Label(app, text="Celsius", font=("aria", 12))
    celsius_label.pack(pady=10)
    celsius_entry = Entry(app, borderwidth=2, relief=GROOVE, font='aria')
    celsius_entry.pack()

    # "To" label between Celsius and Fahrenheit
    to_label = Label(app, text="To", font=("nectar bold", 14, 'bold'))
    to_label.pack(pady=10)

    # Labels for Fahrenheit result
    fahrenheit_label = Label(app, text="Fahrenheit", font=("aria", 12))
    fahrenheit_label.pack(pady=10)
    fahrenheit_result = Label(app, text="", font=("aria", 11), fg="#212121")
    fahrenheit_result.pack(pady=10)

    # Button to initiate Celsius to Fahrenheit conversion
    c_calc_button = Button(app, text="Calculate", width=10, font=('aria', 13), borderwidth=2, relief=GROOVE,
                           command=celsius_to_fahrenheit_calculator)
    c_calc_button.pack(side=LEFT, pady=20, padx=60)

    # Button to switch to Fahrenheit to Celsius converter
    f_to_c_button = Button(app, text="°F To °C", font=('aria', 13), borderwidth=2, relief=GROOVE, command=fahrenheit_to_celsius_setup)
    f_to_c_button.pack(side=LEFT)


def celsius_to_fahrenheit_calculator():  # Function to convert Celsius to Fahrenheit
    celsius = celsius_entry.get()  # Getting the Celsius value from the entry field

    if celsius == "":  # Checking if the entry is empty
        messagebox.showerror("Error", "Please fill in your Celsius")  # Prompting user to fill in the field
    else:
        try:
            float_celsius = float(celsius)  # Converting input to float
            fahrenheit_calc = (float_celsius * 9 / 5) + 32  # Conversion formula
            fahrenheit_result.config(text=f"{float_celsius}°C is {round(fahrenheit_calc, 2)}°F")  # Displaying the result
        except ValueError:
            messagebox.showerror("Error", "Please enter a number instead of a string")  # Handling non-numeric input


def fahrenheit_to_celsius_setup():  # Setting up the Fahrenheit to Celsius converter interface
    global fahrenheit_entry, celsius_result  # Making these variables accessible globally

    # Clearing the window of any existing widgets
    for widget in app.winfo_children():
        widget.destroy()

    # Title for our Fahrenheit to Celsius converter
    app_title = Label(app,text="Fahrenheit To Celsius", font=("nectar bold", 15))
    app_title.pack()

    # Labels and entry field for Fahrenheit input
    fahrenheit_label = Label(app, text='Fahrenheit', font=('aria', 12))
    fahrenheit_label.pack(pady=10)
    fahrenheit_entry = Entry(app, borderwidth=2, relief=GROOVE, font='aria')
    fahrenheit_entry.pack()

    # "To" label between Fahrenheit and Celsius
    to_label = Label(app, text='To', font=("nectar bold", 14, 'bold'))
    to_label.pack(pady=10)

    # Labels for Celsius result
    celsius_label = Label(app, text='Celsius', font=("aria", 12))
    celsius_label.pack(pady=10)
    celsius_result = Label(app, font=("arial", 11), fg="#212121")
    celsius_result.pack(pady=10)

    # Button to initiate Fahrenheit to Celsius conversion
    f_calc_button = Button(app, text="Calculate", width=10, font=("aria", 13), borderwidth=2, relief=GROOVE, command=fahrenheit_to_celsius_calculator)
    f_calc_button.pack(side=LEFT, pady=20, padx=60)

    # Button to switch to Celsius to Fahrenheit converter
    c_to_f_button = Button(app, text="°C To °F", font=('aria', 13), borderwidth=2, relief=GROOVE, command=celsius_to_fahrenheit_setup)
    c_to_f_button.pack(side=LEFT)


def fahrenheit_to_celsius_calculator():  # Function to convert Fahrenheit to Celsius
    fahrenheit_value = fahrenheit_entry.get()  # Getting the Fahrenheit value from the entry field

    if fahrenheit_value == '':  # Checking if the entry is empty
        messagebox.showerror("Error", "Please fill in your Fahrenheit")  # Prompting user to fill in the field
    else:
        try:
            float_fahrenheit = float(fahrenheit_value)  # Converting input to float
            celsius_calc = (float_fahrenheit - 32) * 5 / 9  # Conversion formula
            celsius_result.config(text=f"{float_fahrenheit}°F is {round(celsius_calc, 2)}°C")  # Displaying the result
        except ValueError:
            messagebox.showerror("Error", "Please enter a number instead of a string")  # Handling non-numeric input


app = Tk()  # Creating the tkinter application window
app.title("Temperature Converter")  # Setting the title of our awesome app
app.geometry("400x350")  # Defining the dimensions of the window
app.config(pady=10, padx=10)  # Adding some padding for aesthetics

celsius_to_fahrenheit_setup()  # Starting with the Celsius to Fahrenheit converter interface

app.mainloop()  # Letting tkinter do its magic and run the app
