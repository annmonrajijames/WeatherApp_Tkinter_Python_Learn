from tkinter import *
import requests
import json
# I used this below website to get API service
# https://docs.airnowapi.org/
# Below is the generated URL
# https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode=89129&date=2024-04-10T00-0000&distance=5&API_KEY=80599F15-A413-4492-9620-E4ED538110B3
root = Tk()
root.title('WeatherApp_Tkinter')
root.geometry("400x40")
root.configure(background='green')
try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode=89129&date=2024-04-10T00-0000&distance=5&API_KEY=80599F15-A413-4492-9620-E4ED538110B3")
    api = json.loads(api_request.content)
    city=api[0]['ReportingArea']
    quality=api[0]['AQI']
    category=api[0]['Category']['Name']
except Exception as e:
    api = "Error..."

myLabel = Label(root, text=city + " Air quality "+str(quality)+" "+ category, font=("Helvetica, 20"), background="green").pack()
root.mainloop()