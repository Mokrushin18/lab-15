import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO


def get_dog_image():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        if response.status_code == 200:
            data = response.json()
            img_url = data["message"]

            img_response = requests.get(img_url)
            img_data = Image.open(BytesIO(img_response.content))
            img_data = img_data.resize((400, 300))
            img = ImageTk.PhotoImage(img_data)

            dog_label.config(image=img)
            dog_label.image = img
        else:
            dog_label.config(text="Ошибка загрузки фото")
    except Exception as e:
        dog_label.config(text=f"Ошибка: {e}")


window = tk.Tk()
window.title("Генератор фото собак")
window.geometry("500x450")

btn = tk.Button(window, text="Показать собаку!", command=get_dog_image, font=("Arial", 14), bg="#4CAF50", fg="white")
btn.pack(pady=10)

dog_label = tk.Label(window, text="Нажми на кнопку", font=("Arial", 12))
dog_label.pack(pady=10)

window.mainloop()