from customtkinter import *
from colores_estilos import *
import requests
import threading

def mostar_mensaje (mensaje, COLOR_FONDO):
    etiqueta_error.configure(text=mensaje, fg_color = COLOR_FONDO)
    etiqueta_error.after(
        2000, lambda: etiqueta_error.configure(text="---",
                                               fg_color = COLOR_SECUNDARIO)
    )


def click_boton_limpiar():
    entrada_quetzales.delete(0, "end")
    actualizar_resultados(0.00, 0.00, 0.00)
    
def actualizar_resultados(dolares, euros, libras):
    etiqueta_cantidad_dolares.configure(text=f"{dolares:,.2f}")
    etiqueta_cantidad_euros.configure(text=f"{euros:,.2f}")
    etiqueta_cantidad_libras.configure(text=f"{libras:,.2f}")


def obtener_tasa_cambio():
    try:
        respuesta = requests.get(API_EXCHANGE, timeout=10)
        respuesta.raise_for_status()
        if respuesta.status_code != 200:
            return {}
        return respuesta.json()

    except requests.exception:
        ventana.after(0, lambda: mostar_mensaje("ERROR CON LA API", COLOR_ROJO))

def convertir_quetzales():
    quetzales = entrada_quetzales.get()
    
    if not quetzales:
        ventana.after(0, lambda: mostar_mensaje("INGRESE UNA CANTIDAD VÁLIDA", COLOR_ROJO))
        return
    
    try:
        quetzales = float(quetzales)
        if quetzales <=0:
            ventana.after(0, lambda: mostar_mensaje("Ingrese una cantidad válida", COLOR_ROJO))
            return
        
        tasas_cambio = obtener_tasa_cambio()
        
        if not "rates" in tasas_cambio:
            ventana.after(0, lambda: mostar_mensaje ("NO RATES", COLOR_ROJO))
            return
        
        tasa_dolar = tasas_cambio.get("rates").get("USD", 0)
        tasa_euro = tasas_cambio.get("rates").get("EUR", 0)
        tasa_libra = tasas_cambio.get("rates").get("GBP", 0)
        
        
        dolares = quetzales * tasa_dolar
        euros = quetzales * tasa_euro
        libras = quetzales * tasa_libra
        ventana.after(0, lambda: actualizar_resultados(dolares, euros, libras))
        
    
    except:
        ventana.after(0, lambda: mostar_mensaje("ERROR AL CONVERTIR", COLOR_ROJO))
    
def click_boton_calcular():
    hilo = threading.Thread(target=convertir_quetzales, daemon=True)
    hilo.start()




API_EXCHANGE = "https://api.exchangerate.fun/latest?base=GTQ"

ventana = CTk()
ventana.title("EXCHANGE")
ventana.geometry("500x620")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

set_appearance_mode("Dark")

contenedor_principal = CTkFrame(
    master=ventana,
    corner_radius=0,
    fg_color=COLOR_FONDO_OBSCURO,
)

contenedor_principal.grid(
    row=0,
    column=0,
    sticky="nsew",
)

contenedor_principal.grid_columnconfigure(0, weight=1)
contenedor_principal.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)

contenedor_titulo = CTkFrame(
    master=contenedor_principal,
    border_width=0,
    corner_radius=20,
    fg_color=TRANSPARENTE,
)


contenedor_titulo.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=10,
)
contenedor_titulo.grid_columnconfigure(0, weight=1)
contenedor_titulo.grid_rowconfigure([0, 1], weight=1)

etiqueta_titulo = CTkLabel(
    master=contenedor_titulo,
    text="QUETZAL CONVERTER",
    **ESTILO_LABEL_TITULO_TRANSPARENTE,
)
etiqueta_titulo.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=20,
    pady=(10, 5),
)
etiqueta_subtitulo = CTkLabel(
    master=contenedor_titulo,
    text="Convierte tus quetzales a monedas internacionales",
    **ESTILO_LABEL_NORMAL_TRANSPARENTE,
)
etiqueta_subtitulo.grid(
    row=1,
    column=0,
    sticky="new",
    padx=20,
    pady=(0, 10),
)

contenedor_quetzales = CTkFrame(
    master=contenedor_principal,
    corner_radius=20,
    fg_color=COLOR_SECUNDARIO,
)

contenedor_quetzales.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=20,
    pady=10,
)
contenedor_quetzales.grid_columnconfigure(0, weight=1)
contenedor_quetzales.grid_rowconfigure([0, 1], weight=1)

etiqueta_quetzales = CTkLabel(
    master=contenedor_quetzales,
    text="Cantidad en Quetzales (GTQ)",
    **ESTILO_LABEL_NORMAL_TRANSPARENTE,
)
etiqueta_quetzales.grid(
    row=0,
    column=0,
    sticky="nsw",
    padx=20,
    pady=(10, 5),
)

entrada_quetzales = CTkEntry(
    master=contenedor_quetzales,
    placeholder_text="Ejemplo: 100",
    **(ESTILO_ENTRY | {"border_color": COLOR_ASENTO_1}),
)
entrada_quetzales.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=20,
    pady=(5, 10),
)
entrada_quetzales.bind ("<Return>", lambda event: click_boton_calcular())


contenedor_botones = CTkFrame(
    master=contenedor_principal,
    corner_radius=0,
    fg_color=TRANSPARENTE,
)

contenedor_botones.grid(
    row=2,
    column=0,
    sticky="nsew",
    padx=20,
    pady=20,
)
contenedor_botones.grid_columnconfigure(0, weight=1)
contenedor_botones.grid_rowconfigure([0, 1], weight=1)

boton_calcular = CTkButton(
    master=contenedor_botones,
    text="CALCULAR CONVERSIÓN",
    **(ESTILO_BOTON | {"hover_color": COLOR_ASENTO_1}),
    command = click_boton_calcular,
)
boton_calcular.grid(
    row=0,
    column=0,
    sticky="nsew",
    pady=(10, 5),
)

boton_limpiar = CTkButton(
    master=contenedor_botones,
    text="LIMPIAR",
    **ESTILO_BOTON,
    command=click_boton_limpiar,

    
)
boton_limpiar.grid(
    row=1,
    column=0,
    sticky="nsew",
    pady=(5, 10),
)


contenedor_cambio = CTkFrame(
    master=contenedor_principal,
    corner_radius=20,
    fg_color=TRANSPARENTE,
)

contenedor_cambio.grid(
    row=3,
    column=0,
    sticky="nsew",
    padx=20,
    pady=20,
)

contenedor_cambio.grid_columnconfigure([0, 1, 2], weight=1)
contenedor_cambio.grid_rowconfigure(0, weight=1)
contenedor_cambio.grid_propagate(False)

contenedor_dolares = CTkFrame(
    master=contenedor_cambio,
    corner_radius=20,
    fg_color=COLOR_SECUNDARIO,
)

contenedor_dolares.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=10,
    pady=10,
)

contenedor_dolares.grid_columnconfigure(0, weight=1)
contenedor_dolares.grid_rowconfigure([0, 1, 2, 3], weight=1)
contenedor_dolares.grid_propagate(False)

etiqueta_simbolo_dolares = CTkLabel(
    master=contenedor_dolares,
    text="$",
    **(ESTILO_LABEL_TITULO_TRANSPARENTE | {"text_color": COLOR_ASENTO_1}),
)
etiqueta_simbolo_dolares.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=20,
    pady=(10, 5),
)

etiqueta_dolares = CTkLabel(
    master=contenedor_dolares,
    text="DÓLARES",
    **ESTILO_LABEL_NORMAL_TRANSPARENTE,
)
etiqueta_dolares.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=20,
    pady=(5, 10),
)

etiqueta_cantidad_dolares = CTkLabel(
    master=contenedor_dolares,
    text="0.00",
    **(ESTILO_LABEL_TITULO_TRANSPARENTE | {"text_color": COLOR_ASENTO_1}),
)
etiqueta_cantidad_dolares.grid(
    row=2,
    column=0,
    sticky="nsew",
    padx=20,
    pady=(5, 10),
)


contenedor_euros = CTkFrame(
    master=contenedor_cambio,
    corner_radius=20,
    fg_color=COLOR_SECUNDARIO,
)

contenedor_euros.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=10,
    pady=10,
)

contenedor_euros.grid_columnconfigure(0, weight=1)
contenedor_euros.grid_rowconfigure([0, 1, 2, 3], weight=1)
contenedor_euros.grid_propagate(False)

etiqueta_simbolo_euros = CTkLabel(
    master=contenedor_euros,
    text="€",
    **(ESTILO_LABEL_TITULO_TRANSPARENTE | {"text_color": COLOR_ASENTO_2}),
)
etiqueta_simbolo_euros.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=20,
    pady=(10, 5),
)
etiqueta_euros = CTkLabel(
    master=contenedor_euros,
    text="EUROS",
    **ESTILO_LABEL_NORMAL_TRANSPARENTE,
)
etiqueta_euros.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=20,
    pady=(5, 10),
)
etiqueta_cantidad_euros = CTkLabel(
    master=contenedor_euros,
    text="0.00",
    **(ESTILO_LABEL_TITULO_TRANSPARENTE | {"text_color": COLOR_ASENTO_2}),
)
etiqueta_cantidad_euros.grid(
    row=2,
    column=0,
    sticky="nsew",
    padx=20,
    pady=(5, 10),
)

contenedor_libras = CTkFrame(
    master=contenedor_cambio,
    corner_radius=20,
    fg_color=COLOR_SECUNDARIO,
)

contenedor_libras.grid(
    row=0,
    column=2,
    sticky="nsew",
    padx=10,
    pady=10,
)

contenedor_libras.grid_columnconfigure(0, weight=1)
contenedor_libras.grid_rowconfigure([0, 1, 2, 3], weight=1)
contenedor_libras.grid_propagate(False)

etiqueta_simbolo_libras = CTkLabel(
    master=contenedor_libras,
    text="£",
    **(ESTILO_LABEL_TITULO_TRANSPARENTE | {"text_color": COLOR_ASENTO_3}),
)
etiqueta_simbolo_libras.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=20,
    pady=(10, 5),
)
etiqueta_libras = CTkLabel(
    master=contenedor_libras,
    text="LIBRAS",
    **ESTILO_LABEL_NORMAL_TRANSPARENTE,
)
etiqueta_libras.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=20,
    pady=(5, 10),
)
etiqueta_cantidad_libras = CTkLabel(
    master=contenedor_libras,
    text="0.00",
    **(ESTILO_LABEL_TITULO_TRANSPARENTE | {"text_color": COLOR_ASENTO_3}),
)
etiqueta_cantidad_libras.grid(
    row=2,
    column=0,
    sticky="nsew",
    padx=20,
    pady=(5, 10),
)

etiqueta_error = CTkLabel(
    master=contenedor_principal,
    text="---",
    **(
        ESTILO_LABEL_NORMAL_TRANSPARENTE
        | {
            "text_color": COLOR_TEXTO_CLARO,
            "fg_color": COLOR_SECUNDARIO,
            "height": 30,
        }
    ),
)
etiqueta_error.grid(
    row=4,
    column=0,
    sticky="ews",
)

ventana.mainloop()
