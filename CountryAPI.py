# API KEY - https://restcountries.com/v3.1/capital/

from tkinter import *
import requests
import json

root = Tk()
root.geometry("500x700")
root.title("Country API")
root.configure(bg = "lightpink")

city_name_label = Label(root, text = "Capital City Name", font = ("Times", 20, "bold"), bg = "lightpink")
city_name_label.place(relx = 0.3, rely = 0.1, anchor = CENTER)

city_entry = Entry(root)
city_entry.place(relx = 0.2, rely = 0.2, anchor = CENTER)

country_name = Label(root, text = "Country : ", font = ("Arial", 15), bg = "lightblue")
country_name.place(relx = 0.17, rely = 0.3, anchor = CENTER)

region = Label(root, text = "Region : ", font = ("Arial", 15), bg = "lightblue")
region.place(relx = 0.16,rely = 0.35,anchor = CENTER)

languages = Label(root, text = "Language : ", font = ("Arial", 15), bg = "lightblue")
languages.place(relx = 0.18 ,rely = 0.4, anchor = CENTER)

population = Label(root, text = "Population : ", font = ("Arial", 15), bg = "lightblue")
population.place(relx = 0.19, rely = 0.45, anchor = CENTER)

area = Label(root, text = "Area : ", font = ("Arial", 15), bg = "lightblue")
area.place(relx = 0.15 ,rely = 0.5, anchor = CENTER)

def city_details():
    api_request = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    api_output_json = json.loads(api_request.content)
    country = api_output_json[0]['name']
    reg = api_output_json[0]['region']
    lang = api_output_json[0]['demonym']
    popn = api_output_json[0]['population']
    country_area = api_output_json[0]['area']
    country_name["text"] = "Country : " + country
    region['text'] = "Region : " + reg
    languages['text'] = "Language : " + lang
    population['text'] = "Population : " + str(popn)
    area['text'] = "Area : " + str(country_area)
    
call_function = Button(root, text  = " City Details", command = city_details)
call_function.place(relx = 0.15, rely = 0.25, anchor = CENTER)
    
    

root.mainloop()