from tkinter import *
import requests
import json
# I used this below website to get API service
# https://docs.airnowapi.org/
# Below is the generated URL
# https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode=89129&date=2024-04-10T00-0000&distance=5&API_KEY=80599F15-A413-4492-9620-E4ED538110B3
root = Tk()
root.title('WeatherApp_Tkinter')
root.geometry("400x400")

api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode=89129&date=2024-04-10T00-0000&distance=5&API_KEY=80599F15-A413-4492-9620-E4ED538110B3")

root.mainloop()