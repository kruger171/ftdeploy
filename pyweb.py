import flet as ft

import time
from flask import Flask

pyweb = Flask(__name__)


def main(page):
    text = ft.Text("Krg Live Chat",
          color=ft.colors.WHITE,
          font_family="Verdana",
          selectable=False, size="20",
          italic=True
    )

    username = ft.TextField(
        border_color=ft.colors.BLACK,
        color=ft.colors.WHITE,
        bgcolor="#1B1C24",
        input_filter=ft.TextOnlyInputFilter()
    )

    h = time.time()

    def server_tunnel(i):

        chat.controls.append(ft.Text(i))
        page.update()

    page.pubsub.subscribe(server_tunnel)

    def send_msg(msg):

        if typemsg.value == "":
            page.remove(row)

        usermsg = f"[{time.ctime(h)}] - {username.value}: {typemsg.value}"
        typemsg.value = ""

        page.pubsub.send_all(usermsg)

        page.update()

    send_btn = ft.ElevatedButton(text="Send", icon="EXIT_TO_APP_ROUNDED", on_click=send_msg, bgcolor=ft.colors.BLACK,
                                 color=ft.colors.WHITE)

    typemsg = ft.TextField(label="Type a message", on_submit=send_msg, color=ft.colors.WHITE,
                           focused_border_color="BLACK")

    chat = ft.Column()

    def start_a_chat(e):

        if username.value == "":
            username.value = "Desconhecido"

            pass

        popup.open = False
        page.remove(btn)


        row = ft.Row([typemsg, send_btn])

        page.add(chat)
        page.add(row)
        user_join = f"{username.value} aterriçou no chat."
        page.pubsub.send_all(user_join)

        exitbtn = ft.ElevatedButton(text="Exit", bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)
        skipchatbtn = ft.OutlinedButton(text="Skip chat", disabled=True)

        row2 = ft.Row([exitbtn, skipchatbtn])

        page.add(row2)
        page.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Username", color=ft.colors.WHITE),
        content=username,
        actions=[
            ft.ElevatedButton("Ready", on_click=start_a_chat, bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)
        ]

    )

    def openpop(f):
        page.dialog = popup
        popup.open = True

        page.update()
        popup.bgcolor = "white"

    btn = ft.ElevatedButton("Join", on_click=openpop, bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)

    page.add(text)
    page.add(btn)




ft.app(main, view=ft.WEB_BROWSER)
