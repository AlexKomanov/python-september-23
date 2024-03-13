import flet as ft


def main(page: ft.Page):
    page.title = "Handle Events"
    page.window_width = 500
    first_name_input = ft.TextField(label='First Name', width=300)
    last_name_input = ft.TextField(label='Last Name', width=300)
    blank_text_element = ft.Text()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def print_name(e: ft.ControlEvent):
        print(f"Event is -> {e.name}")
        say_hello_text = f"Hello {first_name_input.value} {last_name_input.value}!!!"
        blank_text_element.value = say_hello_text
        first_name_input.value = ""
        last_name_input.value = ""
        first_name_input.focus()
        page.update()

    page.add(first_name_input,
             last_name_input,
             ft.ElevatedButton(text="Print a name", on_click=print_name),
             blank_text_element)


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
