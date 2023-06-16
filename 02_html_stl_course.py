####
## Status: revisado
## Fecha revisión: 20220608
####

##
# Comandos básicos de Streamlitli
##
from utils import *
# Título
header("9 casos de negocio con Streamlit")
st.subheader("2. Funciones Básicas de Streamlit")
st.subheader("Introducción")

st.markdown(""" 
    En esta segunda sesión conocerán alguna funciones básica de Streamlit que generar un 
    sitio web sencillo sin necesidad de usar CSS o HTML. *__!Pregunte por las restricciones!__*

    Revisaremos varios de los elementos comunes del lenguaje HTML, los cuales permiten 
    diseñar y dar funcionalidad a una página web.

    Sin embargo, es posible que en algunos momentos debamos usar código de CSS y de HTML.

    A continuación veremos como definir algunos de los elementos básicos de **HTML**.
""")


st.markdown("### a. Encabezado (*header*)")
# Header
st.write("Código")
code = '''
st.header("Esto es un encabezado") 
'''
st.code(code, language='python')
st.write("Resultado")
st.header("Esto es un encabezado")

# Separador
st.markdown('___')
# Subheader
st.markdown("### b. Subencabezado (*subheader*)")
st.write("Código")

code = '''
st.header("Esto es un subencabezado") 
'''
st.code(code, language='python')
st.write("Resultado")
st.subheader("Esto es un subencabezado")

# Separador
st.markdown('___')
# Text
st.markdown("### c. Texto (*text*)")
st.write("Código")

code = '''
st.text("¡Hola. geeks!") 
'''
st.code(code, language='python')
st.write("Resultado")
st.text("¡Hola, geeks!")

# Separador
st.markdown('___')

# Markdown
st.markdown("### d. Markdown")

st.write("Código")

code = '''
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.markdown("### This is a markdown")
'''
st.code(code, language='python')

st.write("Resultado")

st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.markdown("### This is a markdown")

# Separador
st.markdown('___')

# Mensajes
st.markdown("### e. Mensajes")
st.write("Código")

code = '''
st.success("Success")
st.write("Resultado")
st.info("Information")
st.warning("Warning")
st.error("Error")
'''
st.code(code, language='python')

st.write("Resultado")
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")

# Separador
st.markdown('___')

# Write text
st.markdown("### f. Write")
st.write("Código")
code = '''
st.write("Texto con write.")
'''
st.code(code, language='python')

st.write("Resultado")
st.write("Texto con write.")
 

# Separador
st.markdown('___')

# Display Images
# import Image from pillow to open images
st.markdown("### g. Imágenes")
st.write("Código")

code = '''
from PIL import Image
img = Image.open("images/streamlit.png")
st.image(img, width=200)
'''
st.code(code, language='python')

st.write("Resultado")
from PIL import Image
img = Image.open("images/streamlit.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)

# Separador
st.markdown('___')

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
st.markdown("### g. Checkbox")

st.write("Código")

code = '''
if st.checkbox("Mostrar/Ocultar"):
   
  # display the text if the checkbox returns True value
  st.text("Mostrando el elemento.")
'''
st.code(code, language='python')

st.write("Resultado")
if st.checkbox("Mostrar/Ocultar"):
   
  # display the text if the checkbox returns True value
  st.text("Mostrando el elemento.")


# Separador
st.markdown('___')

st.markdown("### h. Radio Button")

st.write("Código")

code = '''
# radio button
# El primer argumento es el título del botón de opción. 
# el segundo argumentos son las opciones del botón
status = st.radio("Seleccione el género: ", ('Mujer', 'Hombre'))
 
# Sentencia condicional a imprimir
# Se muestra el resultado usando la función de éxito (success)
if (status == 'Mujer'):
    st.success("Mujer")
else:
    st.success("Hombre")
'''

st.code(code, language='python')

st.write("Resultado")

# radio button
# El primer argumento es el título del botón de opción. 
# el segundo argumentos son las opciones del botón
status = st.radio("Seleccione el género: ", ('Mujer', 'Hombre'))
 
# Sentencia condicional a imprimir
# Se muestra el resultado usando la función de éxito (succes)
if (status == 'Mujer'):
    st.success("Mujer")
else:
    st.success("Hombre")

# Separador
st.markdown('___')

st.markdown("### i. Casilla de selección")

st.write("Código")
    
code = '''
# El primer argumento es es título de la casilla
# El segundo argumento contiene las opciones
hobby = st.selectbox("Pasatiempos: ",
    ['Baile', 'Lectura', 'Deportes'])

# Imprimimos el pasatiempo seleccionado
st.write("Tu pasatiempo es: ", hobby)
'''


st.code(code, language='python')
# Selection box
 
# first argument takes the titleof the selectionbox
# second argument takes options
# El primer argumento es es título de la casilla
# El segundo argumento contiene las opciones

st.write("Resultado")

hobby = st.selectbox("Pasatiempos: ",
    ['Baile', 'Lectura', 'Deportes'])

# Imprimimos el pasatiempo seleccionado

st.write("Tu pasatiempo es: ", hobby)

# Separador
st.markdown('___')

st.markdown("### j. Casilla de selección múltiple")

st.write("Código")
    
code = '''
# El primer argumento es es título de la casilla
# El segundo argumento contiene las opciones
hobbies = st.multiselect("Pasatiempos: ",
                         ['Baile', 'Lectura', 'Deportes'])
 
# Muestra la cantidad de pasatiempos seleccionados
st.write("Usted seleccionó", len(hobbies), 'pasatiempos')

# y los lista.
if hobbies:
    df = pd.DataFrame (hobbies, columns = ['Pasatiempos'])
    st.write('Hobbies seleccionados:')
    st.dataframe(df)
'''
st.code(code, language='python')

st.write("Resultado")

# El primer argumento es es título de la casilla
# El segundo argumento contiene las opciones
hobbies = st.multiselect("Pasatiempos: ",
                         ['Baile', 'Lectura', 'Deportes'])
 
# Muestra la cantidad de pasatiempos seleccionados
st.write("Usted seleccionó", len(hobbies), 'pasatiempos')

# y los lista.
if hobbies:
    df = pd.DataFrame (hobbies, columns = ['Pasatiempos'])
    st.write('Hobbies seleccionados:')
    st.dataframe(df)

# Separador
st.markdown('___')

st.markdown("### k. Campo de captura")

st.write("Código")
    
code = '''
# Campo de captura
 
# Guardamos el texto capturado en la variable 'name'
# El primer argumento es es título de la casilla
# El segundo argumento despliega un texto por omisión en el campo de captura
name = st.text_input("Escribe tu nombre", "Escribe aquí...")
 
# Se despliega el nombre al dar click en el botón de enviar
# .title() se usa para obtener la cadena capturada
if(st.button('Enviar')):
    result = name.title()
    st.success(result)
'''
st.code(code, language='python')

st.write("Resultado")

# Campo de captura
 
# Guardamos el texto capturado en la variable 'name'
# El primer argumento es es título de la casilla
# El segundo argumento despliega un texto por omisión en el campo de captura
name = st.text_input("Escribe tu nombre", "Escribe aquí...")
 
# Se despliega el nombre al dar click en el botón de enviar
# .title() se usa para obtener la cadena capturada
if(st.button('Enviar')):
    result = name.title()
    st.success(result)

# Separador
st.markdown('___')

st.markdown("### l. Control deslizante")

st.write("Código")
    
code = '''
# slider
 
# El primer argumento es es título del control
# el segundo argumento define el inicio del control
# el último define el rango superior
level = st.slider("Seleccione el nivel", 1, 5)
 
# Imprimimos el nivel
# se usa format() para el despliegue adecuado
# de la variable en una posición específica
st.text('Selección: {}'.format(level))
'''
st.code(code, language='python')

st.write("Resultado")

# slider
 
# El primer argumento es es título del control
# el segundo argumento define el inicio del control
# el último define el rango superior
level = st.slider("Seleccione el nivel", 1, 5)
 
# Imprimimos el nivel
# se usa format() para el despliegue adecuado
# de la variable en una posición específica
st.text('Selección: {}'.format(level))

"""
___
"""

#footer("Copyrigth © 2023, RAF")
