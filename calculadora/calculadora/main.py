import flet as ft

def primer_numero(text_field, page):

    
    num1 = text_field.value
    dialog = ft.AlertDialog(
        title=ft.Text("calculadora"),
        actions=[
            ft.TextButton("salir", on_click=lambda e: close_dialog(page))
        ],
    )
    
def segundo_numero(text_field, page):
    
    
    num2 = text_field.value
    dialog = ft.AlertDialog(
        title=ft.Text("calculadora"),
        actions=[
            ft.TextButton("salir", on_click=lambda e: close_dialog(page))
        ],
    )
    
    page.dialog = dialog
    page.dialog.open = True
    page.update()
    
def close_dialog(page):
    page.dialog.open = False
    page.update()
    
def main(page: ft.Page):
    page.title=("calculadora")
    page.bgcolor="green"
    text_field = ft,Text_field(label="ingresa el primer numero")
    button = ft.ElevatedButton(
        text="suma",
        on_click=lambda e: primer_numero+segundo_numero(text_field, page)
    )
    page.add(
        ft.Row(controls=[
            text_field,
            text_field,
            button
        ])
    )
ft.app(target=main)
