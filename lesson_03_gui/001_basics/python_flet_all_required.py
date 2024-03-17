import flet as ft


class InfoField(ft.TextField):

    def __init__(self):
        super().__init__(width=150, text_align=ft.TextAlign.CENTER, value="")

    def get_value(self):
        return self.value


def main(page: ft.Page):
    page.title = "Flet App"
    page.theme_mode = "light"
    info_label = ft.Text("Information")
    info_text_field = InfoField()
    label_to_update = ft.Text()
    checkbox = ft.Checkbox('Agree with Conditions', value=False)

    def update_label(event: ft.ControlEvent):
        label_to_update.value = info_text_field.get_value()
        print(checkbox.value)
        page.update()

    page.add(
        ft.Row([
            ft.IconButton(ft.icons.HOME),
            ft.Icon(ft.icons.BACK_HAND)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            info_label,
            info_text_field
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.ElevatedButton(text="UPDATE LABEL", on_click=update_label),
            checkbox
        ], alignment=ft.MainAxisAlignment.CENTER)
        ,
        ft.Row([
            label_to_update
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

    page.update()


ft.app(target=main)
