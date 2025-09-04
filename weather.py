import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "b25df6b33e8f82b2c23693ea2a670d05"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return
    
    # Build the URL with city and API key
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Network error:\n{e}")
        return

    data = response.json()
    if data.get("cod") !=200:
        messagebox.showerror("Error", "City not found! Please try again.")
        return

    temp = data['main']['temp']
    humidity = data['main']['humidity']
    desc = data['weather'][0]['description'].title()
    wind = data['wind']['speed']

    result = (
        f"🏙️ City: {city.title()}\n"
        f"🌡️Temp: {temp} °C\n"
        f"💧 Humidity: {humidity}%\n"
        f"🌬 Wind: {wind} m/s\n"
        f"☁ Weather: {desc}"
    )
    result_label.config(text=result)
        
 # Tkinter Window
root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")
root.config(bg="#87CEEB")
        
title_label = tk.Label(root, text="🌦 Weather App", font=("Arial", 16, "bold"), bg="#87CEEB")
title_label.pack(pady=10)
        
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)
city_entry.focus()

search_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
search_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#87CEEB", justify="left")
result_label.pack(pady=20)

# Allow pressing Enter to trigger search
root.bind("<Return>", lambda e: get_weather())

root.mainloop()