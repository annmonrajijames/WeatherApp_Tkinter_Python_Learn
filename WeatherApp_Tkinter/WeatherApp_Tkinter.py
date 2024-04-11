from tkinter import *
import requests
import json
# I used this below website to get API service
# https://docs.airnowapi.org/
# Below is the generated URL
# https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode=83814&date=2024-04-10T00-0000&distance=5&API_KEY=80599F15-A413-4492-9620-E4ED538110B3
root = Tk()
root.title('WeatherApp_Tkinter')
root.geometry("600x40")
def zipLookup():
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode="+ zip.get() +"&date=2024-04-10T00-0000&distance=5&API_KEY=80599F15-A413-4492-9620-E4ED538110B3")
        api = json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']
        if category == "Good":
            weather_color="green"
        elif category == "Moderate":
            weather_color="#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color="ff9900"
        elif category == "Unhealthy":
            weather_color="FF0000"
        elif category == "Very Healthy":
            weather_color="#990066"
        elif category == "Hazardous":
            weather_color="#660000"
        
        root.configure(background='green')
        myLabel = Label(root, text=city + " Air quality "+str(quality)+" "+ category, font=("Helvetica, 20"), background=weather_color)
        myLabel.grid(row=1,column=0,columnspan=2)
    except Exception as e:
        api = "Error..."
zip=Entry(root)
zip.grid(row=0, column=0)
zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1)
root.mainloop()