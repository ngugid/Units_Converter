import customtkinter
from tkinter import *
from tkinter import messagebox
from forex_python.converter import CurrencyRates




app = customtkinter.CTk()
app.title('Data Converter')
app.geometry('600x500')
app.config(bg='#16085c')

font1 = ('Arial',30,'bold')
font2 = ('Arial',25,'bold')
font3 = ('Arial',15,'bold')

unit_options = ['Length','Area','Volume','Mass','Temperature','Currency']
length_options = ['nanometer','micrometer','millimeter','centimeter','decimeter','meter','decameter','hectometer','kilometer','inch','foot','yard','mile','nautical_mile']              
area_options = ['square_inches','square_feet','acre','hectare','square_miles','square_millimeters','square_centimeters','square_decimeters','square_meters','square_decameters','square_hectometets','square_kilometers']
volume_options = ['cubic_millimeter','cubic_centimeter','cubic_decimeter','cubic_meter','cubic_decameter','cubic_hectometer','cubic_kilometer','cubic_inch','cubic_foot','cubic_yard','cubic_mile','milliliter','centiliter','deciliter','liter','dekaliter','hectoliter','kiloliter','US_liquid_gallon','US_liquid_quart','US_liquid_pint','US_legal_cup','fluid_ounce','US_tablespoon','US_teaspoon','Imperial_gallon','Imperial_quart','Imperial_pint','Imperial_cup','Imperial_fluid_ounce','Imperial_tablespoon','Imperial_teaspoon']
mass_options = ['microgram','milligram','gram','kilogram','ounce','pound','stone','US_ton','Imperial_ton','Tonne']
temperature_options = ['Celsius', 'Fahrenheit', 'Kelvin']

variable1 = StringVar()
variable2 = StringVar()
variable3 = StringVar()

length_factors = {'nanometer': 0.000000001, 'micrometer': 0.000001,'millimeter': 0.001, 'centimeter': 0.01, 'decimeter': 0.1, 'meter': 1, 'decameter': 10, 'hectometer': 100, 'kilometer': 1000, 'inch': 39.3701, 'foot': 3.28084, 'yard': 1.09361, 'mile': 0.000621371, 'nautical mile': 0.000539957}

area_factors = {'square_millimeters': 0.000001, 'square_centimeters': 0.0001, 'square_decimeters': 0.01, 'square_meters': 1, 'square_decameters': 100, 'square_hectometers': 10000, 'square_kilometers': 1000000, 'square_inches': 0.00064516, 'square_feet': 0.092903, 'acre': 4046.86, 'hectare': 10000, 'square_miles': 2590000 }

volume_factors = {'cubic_millimeter': 0.000000001, 'cubic_centimeter': 0.000001, 'cubic_decimeter': 0.001, 'cubic_meter': 1, 'cubic_decameter': 1000, 'cubic_hectometer': 1000000, 'cubic_kilometer': 1000000000, 'cubic_inch': 0.0000163871, 'cubic_foot': 0.0283168, 'cubic_yard': 0.764555, 'cubic_mile': 4168181825.4405795840000000000, 'milliliter': 0.000001, 'centiliter': 0.00001, 'deciliter': 0.0001, 'liter': 0.001, 'dekaliter': 0.01, 'hectoliter': 0.1, 'kiloliter': 1000, 'US_liquid_gallon': 0.00378541, 'US_liquid_quart': 0.000946353, 'US_liquid_pint': 0.000473176, 'US_legal_cup': 0.000240885, 'fluid_ounce': 0.0000295735, 'US_tablespoon': 0.0000147868, 'US_teaspoon': 0.00000492892, 'Imperial_gallon': 0.00454609, 'Imperial_quart': 0.00113652, 'Imperial_pint': 0.000568261, 'Imperial_cup': 0.000284131, 'Imperial_fluid_ounce': 0.0000284131, 'Imperial_tablespoon': 0.0000177582, 'Imperial_teaspoon': 0.00000591939 }
            
mass_factors = {'microgram': 0.000000001, 'milligram': 0.000001, 'gram': 0.001, 'kilogram': 1, 'ounce': 0.0283495, 'pound': 0.453592, 'stone': 6.35029, 'US_ton': 907.185, 'Imperial_ton': 1016.05, 'Tonne': 1000}

temperature_factors = {
    'Celsius': {'Celsius': 1, 'Fahrenheit': 33.8, 'Kelvin': 274.15},
    'Fahrenheit': {'Celsius': -17.2222, 'Fahrenheit': 1, 'Kelvin': 255.928},
    'Kelvin': {'Celsius': -272.15, 'Fahrenheit': -457.87, 'Kelvin': 1}
}

c = CurrencyRates()      
        
def convert():
    try:
        input_value = float(value_entry.get())
        converted_value = 0
        
        if variable1.get() == 'Length':
            meters = input_value * length_factors[variable2.get()]
            converted_value = meters / length_factors[variable3.get()]

        elif variable1.get() == 'Area':
            square_meters = input_value * area_factors[variable2.get()]
            converted_value = square_meters / area_factors[variable3.get()]

        elif variable1.get() == 'Volume':
            cubic_meters = input_value * volume_factors[variable2.get()]
            converted_value = cubic_meters / volume_factors[variable3.get()]

        elif variable1.get() == 'Mass':
            kilograms = input_value * mass_factors[variable2.get()]
            converted_value = kilograms / mass_factors[variable3.get()]

        elif variable1.get() == 'Temperature': 
            source_temp_unit = variable2.get()
            target_temp_unit = variable3.get()
            converted_value = (input_value - temperature_factors[source_temp_unit][target_temp_unit]) / temperature_factors[target_temp_unit][source_temp_unit]

        elif variable1.get() == 'Currency':  
            source_currency = variable2.get()
            target_currency = variable3.get()
            converted_value = c.convert(source_currency, target_currency, input_value)

        result_label.configure(text=f'{input_value} {variable2.get()} = {converted_value:.3f} {variable3.get()}')

    except ValueError:
        messagebox.showerror('Error', 'Please Enter a Valid Number!')





title_label = customtkinter.CTkLabel(app,font=font1,text='Data Converter',text_color='#fff',bg_color='#020a24')
title_label.place(x=150,y=20)

unit_label = customtkinter.CTkLabel(app,font=font2,text='Unit',text_color='#fff',bg_color='#020a24')
unit_label.place(x=180,y=100)

unit_option = customtkinter.CTkComboBox(app,font=font3,text_color='#000',dropdown_hover_color='#06911f',values=unit_options,variable=variable1,width=120)
unit_option.place(x=120,y=130)


from_label = customtkinter.CTkLabel(app,font=font2,text='From',text_color='#fff',bg_color='#020a24')
from_label.place(x=20,y=180)

from_option = customtkinter.CTkComboBox(app,font=font3,text_color='#000',dropdown_hover_color='#06911f',values=unit_options,variable=variable2,width=120)
from_option.place(x=20,y=210)

to_label = customtkinter.CTkLabel(app,font=font2,text='To',text_color='#fff',bg_color='#020a24')
to_label.place(x=180,y=180)

to_option = customtkinter.CTkComboBox(app,font=font3,text_color='#000',dropdown_hover_color='#06911f',values=unit_options,variable=variable3,width=120)
to_option.place(x=180,y=210)

value_label = customtkinter.CTkLabel(app,font=font1,text='Value',text_color='#fff',bg_color='#020a24')
value_label.place(x=150,y=280)

value_entry = customtkinter.CTkEntry(app,font=font3,text_color='#000',fg_color='#fff',border_color='#fff', width=150)
value_entry.place(x=340,y=210)

convert_button = customtkinter.CTkButton(app,command=convert,font=font2,text_color='#fff',text='Convert',fg_color='#eb05ae',hover_color='#a8057d',bg_color='#020a24',cursor='hand2',corner_radius=20,width=200)
convert_button.place(x=150,y=280)

result_label = customtkinter.CTkLabel(app,text='',font=font2,text_color='#fff',bg_color='#020a24')
result_label.place(x=70,y=350),


def update_options(*args):
    if variable1.get() == 'Length':
        from_option.configure(values=length_options)
        to_option.configure(values=length_options)
        from_option.set('meter')
        to_option.set('centimeter')
        
    elif variable1.get() == 'Area':
        from_option.configure(values=area_options)
        to_option.configure(values=area_options)
        from_option.set('square_meters')
        to_option.set('square_centimeters')
        
    elif variable1.get() == 'Volume':
        from_option.configure(values=volume_options)
        to_option.configure(values=volume_options)
        from_option.set('cubic_meter')
        to_option.set('cubic_centimeter')
        
    elif variable1.get() == 'Mass':
        from_option.configure(values=mass_options)
        to_option.configure(values=mass_options)
        from_option.set('kilogram')
        to_option.set('gram')
        
    elif variable1.get() == 'Temperature':
        from_option.configure(values=temperature_options)
        to_option.configure(values=temperature_options)
        from_option.set('Kelvin')
        to_option.set('Celsius')

    elif variable1.get() == 'Currency':  
        from_option.configure(values=c.get_rates('USD').keys())
        to_option.configure(values=c.get_rates('USD').keys())
        from_option.set('USD')
        to_option.set('EUR')
     


variable1.trace("w",update_options)

app.mainloop() 