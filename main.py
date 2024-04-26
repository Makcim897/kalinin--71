import flet as ft
from flet import (
    ElevatedButton,
    FilePicker,
    Row,
    Text,
    icons,
)
def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txtnum = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def reset_click(e):
        txtnum.value = 0
        page.update()

    def minus_click(e):
        txtnum.value = str(int(txtnum.value) - 1)
        page.update()

    def plus_click(e):
        txtnum.value = str(int(txtnum.value) + 1)
        page.update()

    def save_file_result(e):
        save_file_path.value = e.path if e.path else "Cancelled!"
        save_file_path.update()

    save_file_dialog = FilePicker(txtnum)
    save_file_path = Text(txtnum)

    page.overlay.extend([save_file_dialog, save_file_path])

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txtnum,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],alignment=ft.MainAxisAlignment.CENTER,))

    page.add(
        ft.Row([ft.TextButton(text="reset", on_click=reset_click)],alignment=ft.MainAxisAlignment.CENTER,))

    page.add(
        Row(
        [
            ElevatedButton(
                "Save file",
                icon=icons.SAVE,
                on_click=lambda _: save_file_dialog.save_file(txtnum)
            ),
            save_file_path,
        ]
    ))


ft.app(main)