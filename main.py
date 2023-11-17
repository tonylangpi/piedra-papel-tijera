import flet as ft
import random
def main(page: ft.Page):
    page.title = "Juego de Piedra, papel o tijera"
    page.scroll = "adaptive"
    dlg = ft.AlertDialog()
    def eleccion(opc):
        if(int(opc) == 1):
            return "tijera"
        elif(int(opc) == 2):
            return "papel"
        elif(int(opc) == 3):
            return "piedra"
        else:
            return "No elegiste una opcion aceptable xd"


    def btn_click(e):
        if not txt_opc.value:
            txt_opc.error_text = "Por favor elige tu opcion para jugar"
            page.update()
        else:
            result = ""
            opcion = int(txt_opc.value)
            numero_ramdom_pc = random.randint(1,3)
            
            if(opcion == numero_ramdom_pc):
                result="Empate"
            elif (opcion == 1 and numero_ramdom_pc == 2 or opcion == 3 and numero_ramdom_pc == 1 or opcion == 2 and numero_ramdom_pc == 3):
                result="Haz ganado perro"
            elif(opcion not in range(1,3)):
                result="Perdiste"
            else:
                result="Looser!!!"
            page.dialog = dlg
            dlg.open = True
            dlg.title = ft.Text(f"{result}", size=30, color="pink600", italic=True)
            dlg.content = ft.Text(f"tu elegiste {eleccion(opcion)} y la maquina eligio: {eleccion(numero_ramdom_pc)}")
            page.update()
           



    txt_opc = ft.TextField(label="Tu opcion", autofocus=True)

    page.add(ft.Text("Bienvenido al juego de piedra papel o tijera", size=30, color="pink600", italic=True),
    ft.Text("presione 1 elige tijera, presione 2 elije papel, presione 3 elige piedra", size=20, color="BLUE"), txt_opc, ft.ElevatedButton("Jugar", on_click=btn_click))


#ft.app(target=main)
ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=4000) #esto para levantar aplicaciones web con flet