import flet as ft


def main(page: ft.Page):
    page.title = "First App"
    basic_text = ft.Text(value='Hello World!!!', color='red', size=25)

    # page.add(basic_text) / page.controls.append(basic_text) + page.update()

    # page.controls.append(basic_text)
    # page.update()

    page.add(basic_text)


# ft.app(target=main)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
