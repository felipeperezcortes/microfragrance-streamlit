""" """ """  # --- Bienvenida ---
print("-----------------------------")
print("Bienvenidos a MicroFragrance!")
print("-----------------------------\n")

# --- Listado de perfumes y precios ---
precios = {
    "Gucci - Bloom": {2: 3990, 5: 7990, 10: 13990},
    "Valentino - B.I.R Gold": {2: 5990, 5: 9990, 10: 18990},
    "Hermes - Jardin Sur Le Nil": {2: 6990, 5: 11990, 10: 22990},
    "Jean Paul Gaultier - Garden Paradise": {2: 5990, 5: 9990, 10: 18990}

}

print("PERFUMES DISPONIBLES: \n")
for indice, perfume in enumerate(precios, start=1):
    print(f"{indice}. {perfume}\n")

# --- Bucle para elegir perfume ---
while True:
    numero = input(">> ELIGE EL NÚMERO DEL PERFUME: ").strip()
    if not numero.isdigit():  # si no es número
        print("Debes ingresar un número, no texto.\n")
        continue  # vuelve a pedirlo
    numero = int(numero)

    if numero == 1:
        perfume_elegido = "Gucci - Bloom"
        print("Elegiste: Gucci - Bloom")
        break
    elif numero == 2:
        perfume_elegido = "Valentino - B.I.R Gold"
        print("Elegiste: Valentino - B.I.R Gold")
        break
    elif numero == 3:
        perfume_elegido = "Hermes - Jardin Sur Le Nil"
        print("Elegiste: Hermes - Jardin Sur Le Nil")
        break
    elif numero == 4:
        perfume_elegido = "Jean Paul Gaultier - Garden Paradise"
        print("Elegiste: Jean Paul Gaultier - Garden Paradise")
        break
    else:
        print("Número inválido, intenta nuevamente")

# --- Mostrar tamaños para perfume elegido ---
print("--------------------------------------\n")
print("TAMAÑOS DISPONIBLES PARA TU ELECCIÓN\n")
print("2ml, 5ml y 10ml\n")

# --- Elegir tamaños ---
while True:
    tamaño_txt = input(">> Elige el tamaño de tu decant (2, 5 o 10): ").strip()
    if not tamaño_txt.isdigit():  # si no es número
        print("Debes ingresar un número válido (2, 5 o 10).\n")
        continue  # vuelve a pedirlo

    tamaño = int(tamaño_txt)
    if tamaño == 2:
        precios_unit = precios[perfume_elegido][2]
        break
    elif tamaño == 5:
        precios_unit = precios[perfume_elegido][5]
        break
    elif tamaño == 10:
        precios_unit = precios[perfume_elegido][10]
        break
    else:
        print("TAMAÑO NO VALIDO!!. Intenta nuevamente \n")

print(f"\nPRECIO UNITARIO: ${precios_unit}")
print("--------------------------------------\n")


# --- Ofrecer descuentos por cantidad ---
print("DESCUENTOS: \n")
print("- Si compras 2 decants tienes un 10% de dcto")
print("- Si compras 3 o más decants tienes un 20% de dcto\n")

while True:
    cantidad_txt = input(">> ¿Cuantos decants deseas?: \n ").strip()
    if not cantidad_txt.isdigit():  # si no es número
        print("Debes ingresar un número, no texto.\n")
        continue  # vuelve a pedirlo

    cantidad = int(cantidad_txt)
    if cantidad == 0:
        print("CANTIDAD INVALIDA!!, ingresa nuevamente\n")
    if cantidad == 2:
        descuento = 0.10
        etiqueta_dcto = "10% de descuento"
        break
    elif cantidad >= 3:
        descuento = 0.20
        etiqueta_dcto = "20% de descuento"
        break
    else:
        descuento = 0
        etiqueta_dcto = "Sin descuento"

# Resumen
print("\n--------------------------------------")
print("RESUMEN: \n")
print(f"Perfume elegido: {perfume_elegido}")
print(f"Precio Unitario: ${precios_unit:,}")
print(f"Cantidad: {cantidad}")
print(f"descuento aplicado: {etiqueta_dcto}")
subtotal = round(precios_unit * cantidad)
print(f"Precio original: ${subtotal:,}")
total = round(subtotal * (1 - descuento))
print(f"Total: ${total:,}") """


import streamlit as st

# Configuración de la página
st.set_page_config(page_title="MicroFragrance",
                   page_icon="🧴", layout="centered")

st.title("🧴 MicroFragrance – Simulador de Cotización")
st.caption(
    "Elige perfume, tamaño y cantidad. Calculamos subtotal y aplicamos descuentos.")

# Catálogo (mismo modelo que tu script de consola)
PRECIOS = {
    "Gucci - Bloom": {2: 3990, 5: 7990, 10: 13990},
    "Valentino - B.I.R Gold": {2: 5990, 5: 9990, 10: 18990},
    "Hermes - Jardin Sur Le Nil": {2: 6990, 5: 11990, 10: 22990},
    "Jean Paul Gaultier - Garden Paradise": {2: 5990, 5: 9990, 10: 18990}
}

# --- UI ---
perfume = st.selectbox("Perfume", list(PRECIOS.keys()))
tam = st.radio("Tamaño (ml)", [2, 5, 10], horizontal=True)
cantidad = st.number_input("Cantidad de decants", min_value=1, step=1, value=1)

# Precios y cálculo
precio_unit = PRECIOS[perfume][tam]
subtotal = precio_unit * cantidad

# Descuentos
if cantidad == 2:
    descuento = 0.10
    etiqueta_desc = "10% de descuento"
elif cantidad >= 3:
    descuento = 0.20
    etiqueta_desc = "20% de descuento"
else:
    descuento = 0.0
    etiqueta_desc = "Sin descuento"

total = round(subtotal * (1 - descuento))
ahorro = round(subtotal * descuento)

# --- Resumen ---
st.divider()
st.subheader("Resumen")
c1, c2 = st.columns(2)
with c1:
    st.write(f"**Perfume:** {perfume}")
    st.write(f"**Tamaño:** {tam} ml")
    st.write(f"**Cantidad:** {cantidad}")
with c2:
    st.write(f"**Precio unitario:** ${precio_unit:,}")
    st.write(f"**Subtotal:** ${subtotal:,}")
    st.write(f"**Descuento:** {etiqueta_desc}")

st.metric("Total a pagar", f"${total:,}", delta=(
    f"-${ahorro:,}" if ahorro else "0"))
st.caption("Descuentos: 2 unidades → 10%, 3 o más → 20%")
