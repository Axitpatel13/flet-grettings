import flet as ft

def main(page: ft.Page):
    page.title = "Simple Greetings App"
    page.theme_mode = "dark"     
    #users greetings
    greetings = ft.Column()
    #click event
    def button_click(e):
        greetings.controls.append(ft.Text(f"Hello {first_name.value} {last_name.value} !"))
        first_name.value = ""
        last_name.value = ""
        page.update()
    
    #user input
    first_name = ft.TextField(label="Enter First Name: ", autofocus=True)
    last_name = ft.TextField(label="Enter Last Name: ")
    
    #button
    hello = ft.ElevatedButton("Say Hello",on_click=button_click)
    
    page.add(
        first_name,
        last_name,
        hello,
        greetings
    )
    
ft.app(target=main)