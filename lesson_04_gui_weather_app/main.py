import flet as ft
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def main(page: ft.Page):
    page.title = 'Weather App'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input_city = ft.TextField(label='Enter a city name', width=400)
    weather_data = ft.Text('', size=25, color='red')

    def get_info(e):
        if len(input_city.value) < 3:
            return

        api_key = os.getenv("API_KEY")
        request = f"https://api.openweathermap.org/data/2.5/weather?q={input_city.value}&appid={api_key}&units=metric"
        data_response = requests.get(request).json()
        print(data_response)
        temp = data_response['main']['temp']
        city = data_response['name']
        weather_data.value = f"{city}: {temp}°C"
        page.update()  # try without update()

    def change_theme(e: ft.ControlEvent):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        print(e.name)
        change_theme_icon.icon = get_theme_icon()
        print(e.control)
        page.update()

    def get_theme_icon():
        return ft.icons.SUNNY if page.theme_mode == 'dark' else ft.icons.DARK_MODE

    change_theme_icon = ft.IconButton(get_theme_icon(), on_click=change_theme)

    page.add(
        ft.Row([
            change_theme_icon,
            ft.Text('Weather App')
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([input_city], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton('Get Info', on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
