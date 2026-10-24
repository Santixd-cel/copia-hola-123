COLOR_PRIMARIO = "#101827"         # Azul Python
COLOR_PRIMARIO_HOVER = "#101827"    # Azul oscuro
COLOR_FONDO_SECUNDARIO = "#f0f2f5"   # Fondo secundario
COLOR_SECUNDARIO = "#1B263B"     # Amarillo Python
COLOR_SECUNDARIO_HOVER = "#1B263B"  # Amarillo oscuro

COLOR_TEXTO_CLARO = "#FFFFFF"       # Blanco
COLOR_TEXTO_OBSCURO = "#101827"   # Azul oscuro

COLOR_VERDE = "#10B981"
COLOR_ROJO = "#fb1e6b"
COLOR_BLANCO = "#FFFFFF"
COLOR_FONDO = "#e3e5f3"
COLOR_FONDO_OBSCURO = "#101827"
COLOR_BORDE = "#e3e5f3"
COLOR_SOMBRA = "#dcdfef"

COLOR_ASENTO_1 = "#23cef9"  # Naranja Python
COLOR_ASENTO_2 = "#a87cff"  # Azul Python
COLOR_ASENTO_3 = "#e469e8"  # Verde Python

TRANSPARENTE = "transparent"
ALTURA_ESTANDAR_WIDGET = 35

TAMANO_LETRA_NORMAL = ALTURA_ESTANDAR_WIDGET*(2/5)
TAMANO_LETRA_TITULO = ALTURA_ESTANDAR_WIDGET*(3/5)

ESTILO_DE_LETRA_NORMAL = ("Montserrat", TAMANO_LETRA_NORMAL)
ESTILO_DE_LETRA_NORMAL_BOLD = ("Montserrat", TAMANO_LETRA_NORMAL,"bold")
ESTILO_DE_LETRA_GRANDE = ("Montserrat",TAMANO_LETRA_TITULO*1.5,"bold")
ESTILO_DE_LETRA_TITULO = ("Montserrat", TAMANO_LETRA_TITULO,"bold")


ESTILO_ENTRY = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 10,
    "border_width": 2,
    "border_color": COLOR_VERDE,
    "fg_color": COLOR_PRIMARIO,
    "text_color": COLOR_TEXTO_CLARO,
    "placeholder_text_color": COLOR_SOMBRA,
    "justify": "center",
    "font": ESTILO_DE_LETRA_NORMAL_BOLD,
    "state": "normal",
}


ESTILO_TEXTBOX = {
    "corner_radius": 0,
    "border_width": 0,
    "border_spacing": 3,
    "border_color": COLOR_BLANCO,
    "fg_color": COLOR_BLANCO,
    "text_color": COLOR_TEXTO_OBSCURO,
    "font": ESTILO_DE_LETRA_NORMAL,
    "scrollbar_button_color": COLOR_PRIMARIO,
    "scrollbar_button_hover_color": COLOR_SECUNDARIO,
    "activate_scrollbars": True,
    "wrap": "word",
}


ESTILO_CHECKBOX = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "checkbox_width": (ALTURA_ESTANDAR_WIDGET/2),
    "checkbox_height": (ALTURA_ESTANDAR_WIDGET/2),
    "corner_radius": 0,
    "border_width": 2,
    "fg_color": COLOR_SECUNDARIO,
    "border_color": COLOR_PRIMARIO,
    "hover_color": COLOR_PRIMARIO,
    "text_color": COLOR_TEXTO_OBSCURO,
    "text_color_disabled": COLOR_SOMBRA,
    "font": ESTILO_DE_LETRA_NORMAL,
    "onvalue": True,
    "offvalue": False,
    "hover": True,
    "state": "normal",
}


ESTILO_RADIOBUTTON = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "radiobutton_width": (ALTURA_ESTANDAR_WIDGET/2),
    "radiobutton_height": (ALTURA_ESTANDAR_WIDGET/2),
    "corner_radius": 100,
    "border_width_unchecked": 2,
    "border_width_checked": 4,
    "fg_color": COLOR_SECUNDARIO,
    "border_color": COLOR_PRIMARIO,
    "hover_color": COLOR_SECUNDARIO,
    "text_color": COLOR_TEXTO_OBSCURO,
    "text_color_disabled": COLOR_SOMBRA,
    "font": ESTILO_DE_LETRA_NORMAL,
    "hover": True,
    "state": "normal",
}


ESTILO_SWITCH = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "switch_width": ALTURA_ESTANDAR_WIDGET,
    "switch_height": (ALTURA_ESTANDAR_WIDGET/2),
    "border_width": 0,
    "fg_color": COLOR_SOMBRA,
    "border_color": COLOR_PRIMARIO,
    "progress_color": COLOR_SECUNDARIO,
    "button_color": COLOR_PRIMARIO,
    "button_hover_color": COLOR_SECUNDARIO,
    "text_color": COLOR_TEXTO_OBSCURO,
    "font": ESTILO_DE_LETRA_NORMAL,
    "state": "normal",
    "onvalue": "on",
    "offvalue": "off",
}


ESTILO_BOTON = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 10,
    "border_width": 2,
    "border_spacing": 2,
    "fg_color": COLOR_PRIMARIO,
    "hover_color": COLOR_SECUNDARIO,
    "border_color": COLOR_SECUNDARIO,
    "text_color": COLOR_TEXTO_CLARO,
    "text_color_disabled": COLOR_SOMBRA,
    "font": ESTILO_DE_LETRA_NORMAL,
    "anchor": "center",
    "state": "normal",
}


ESTILO_SEGMENTED_BUTTON = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "fg_color": COLOR_BLANCO,
    "selected_color": COLOR_SECUNDARIO,
    "selected_hover_color": COLOR_FONDO,
    "unselected_color": COLOR_PRIMARIO,
    "unselected_hover_color": COLOR_SECUNDARIO,
    "text_color": COLOR_TEXTO_CLARO,
    "text_color_disabled": COLOR_SOMBRA,
    "corner_radius": 0,
    "border_width": 2,
    "font": ESTILO_DE_LETRA_NORMAL,
    "dynamic_resizing": False,
    "state": "normal",
}


ESTILO_OPTIONMENU = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "fg_color": COLOR_PRIMARIO,
    "corner_radius": 0,
    "button_color": COLOR_SECUNDARIO,
    "button_hover_color": COLOR_SOMBRA,
    "font": ESTILO_DE_LETRA_NORMAL,
    "anchor": "center",
    "text_color": COLOR_TEXTO_CLARO,
    "text_color_disabled": COLOR_SOMBRA,
    "dropdown_text_color": COLOR_TEXTO_CLARO,
    "dropdown_fg_color": COLOR_PRIMARIO,
    "dropdown_font": ESTILO_DE_LETRA_NORMAL,
    "dropdown_hover_color": COLOR_SECUNDARIO,
    "hover": True,
    "dynamic_resizing": False,
    "state": "normal",
}


ESTILO_COMBOBOX = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "border_width": 0,
    "fg_color": COLOR_PRIMARIO,
    "border_color": COLOR_SECUNDARIO,
    "button_color": COLOR_SECUNDARIO,
    "button_hover_color": COLOR_SOMBRA,
    "dropdown_fg_color": COLOR_PRIMARIO,
    "dropdown_hover_color": COLOR_SECUNDARIO,
    "dropdown_text_color": COLOR_TEXTO_CLARO,
    "text_color": COLOR_TEXTO_CLARO,
    "text_color_disabled": COLOR_SOMBRA,
    "font": ESTILO_DE_LETRA_NORMAL,
    "dropdown_font": ESTILO_DE_LETRA_NORMAL,
    "hover": True,
    "state": "normal",
    "justify": "center",
}


ESTILO_SLIDER = {
    "height": (ALTURA_ESTANDAR_WIDGET / 2),
    "fg_color": COLOR_SOMBRA,
    "progress_color": COLOR_PRIMARIO,
    "button_color": COLOR_SECUNDARIO,
    "button_hover_color": COLOR_SECUNDARIO_HOVER,
    "corner_radius": 0,
    "button_corner_radius": 10,
    "orientation": "horizontal",
    "hover": True,
    "state": "normal",
}


ESTILO_LABEL_NORMAL_SECUNDARIO = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "fg_color": COLOR_SECUNDARIO,
    "text_color": COLOR_TEXTO_CLARO,
    "font": ESTILO_DE_LETRA_NORMAL,
    "anchor": "center",
    "compound": "center",
    "justify": "center", 
    "padx": (ALTURA_ESTANDAR_WIDGET/3),     
}


ESTILO_LABEL_NORMAL_TRANSPARENTE = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "fg_color": TRANSPARENTE,
    "text_color": COLOR_TEXTO_CLARO,
    "font": ESTILO_DE_LETRA_NORMAL,
    "anchor": "center",
    "compound": "center",
    "justify": "center", 
    "padx": (ALTURA_ESTANDAR_WIDGET/3),     
}


ESTILO_LABEL_NORMAL_GRANDE_TRANSPARENTE = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "fg_color": TRANSPARENTE,
    "text_color": COLOR_TEXTO_CLARO,
    "font": ESTILO_DE_LETRA_GRANDE,
    "anchor": "center",
    "compound": "center",
    "justify": "center", 
    "padx": (ALTURA_ESTANDAR_WIDGET/3),     
}

ESTILO_LABEL_TITULO = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "fg_color": COLOR_PRIMARIO,
    "text_color": COLOR_TEXTO_CLARO,
    "font": ESTILO_DE_LETRA_TITULO,
    "anchor": "center",
    "compound": "center",
    "justify": "center", 
    "padx": (ALTURA_ESTANDAR_WIDGET/3), 
    "pady": (ALTURA_ESTANDAR_WIDGET/3),     
}

ESTILO_LABEL_TITULO_TRANSPARENTE = {
    "height": ALTURA_ESTANDAR_WIDGET,
    "corner_radius": 0,
    "fg_color": TRANSPARENTE,
    "text_color": COLOR_TEXTO_CLARO,
    "font": ESTILO_DE_LETRA_TITULO,
    "anchor": "center",
    "compound": "center",
    "justify": "center", 
    "padx": (ALTURA_ESTANDAR_WIDGET/3), 
    "pady": (ALTURA_ESTANDAR_WIDGET/3),     
}


ESTILO_IMAGELABEL = {
    "corner_radius": 0,
    "fg_color": TRANSPARENTE,
    "text_color": COLOR_TEXTO_OBSCURO,
    "font": ESTILO_DE_LETRA_NORMAL,
    "text": "",
    "compound": "center",
    "state": "normal",
    "anchor": "center",
    "justify": "center"
}


ESTILO_PROGRESSBAR = {
    "height": (ALTURA_ESTANDAR_WIDGET/3),
    "border_width": 0,
    "corner_radius": 0,
    "fg_color": COLOR_SOMBRA,
    "border_color":COLOR_SECUNDARIO,
    "progress_color": COLOR_PRIMARIO,
    "orientation": "horizontal",
    "mode": "determinate",
}

ESTILO_TABVIEW = {
    "corner_radius":0,	
    "border_width":0,	
    "fg_color":COLOR_FONDO,	
    "border_color":COLOR_FONDO,	
    "segmented_button_fg_color":COLOR_SECUNDARIO,	
    "segmented_button_selected_color":COLOR_SECUNDARIO,
    "segmented_button_selected_hover_color":COLOR_PRIMARIO,	
    "segmented_button_unselected_color":COLOR_PRIMARIO,
    "segmented_button_unselected_hover_color":COLOR_SECUNDARIO,
    "text_color":COLOR_BLANCO,	
    "text_color_disabled":COLOR_BLANCO,
    "anchor":"center",
}