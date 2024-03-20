import flet as ft


def main(page: ft.Page):
    page.title = "Weather Application"
    page.theme_mode = "light"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input_city = ft.TextField(label="Enter a city name", width=400)
    weather_data = ft.Text('TEST DATA', size=20, color=ft.colors.RED_800)

    page.update()

    page.add(
        ft.Row([input_city], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER)

    )


ft.app(target=main)

API_KEY = "6b8713d5636f326cb5cacece67d52b0f"
request_data = 'https://api.openweathermap.org/data/2.5/weather?q={city name = input_city.value}&appid={API key}'
