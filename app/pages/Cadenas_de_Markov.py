import streamlit as st

st.title("Cadenas de Markov")

st.text('''Para analizar el comportamiento del mercado farmacéutico y conocer las 
probabilidades de que un producto sea desactivado o activado en Medicom, una de 
las unidades de negocios de distribución masiva del grupo PiSA, se hizo uso de 
las cadenas de Markov, modelos matemáticos que representan sistemas que cambian 
de estado de manera probabilística en intervalos discretos de tiempo, donde el 
estado futuro depende únicamente del estado presente, esto nos ayudará a predecir 
la compra o no compra de cada producto en cada perfil de venta (Hospitales, 
Farmacias y Distribuidores). Lo anterior se logró agrupando y filtrando la base 
de datos por cliente id y material id para realizar la matriz de transición con 
el objetivo de obtener las probabilidades estables. Los puntos a considerar en 
estas cadenas de Markov, es que se tienen dos estados planteados:''') 

st.latex(r'E = \{0, 1\}')

st.text('''donde 0 es que el producto fue comprado y 1 que el producto no fue comprado 
y los intervalos de tiempo se manejan en meses.''')

st.text('''Para lograr la convergencia de una probabilidad estable las cadenas de
Markov tienen que cumplir con las siguientes condiciones:''')

st.text('''1. Irreducibilidad: Desde cualquier estado es posible llegar a cualquier otro
estado en un n ́umero finito de pasos, es decir, que todos los estados sean
accesibles entre sí.''')

st.text('''2. Aperiodicidad: La cadena debe ser aperi ́odica, lo que asegura que no
est ́e atrapada en ciclos repetitivos y que con el tiempo cualquier estado
pueda ser alcanzado.''')

st.text('''3. ''')
