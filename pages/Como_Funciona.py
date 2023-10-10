import streamlit as st
import pandas as pd

st.title("Cadenas de Markov")

st.text('''Para analizar el comportamiento del mercado farmacéutico y conocer las proba-
bilidades de que un producto sea desactivado o activado en una de las unidades
de negocios de distribución masiva del grupo PiSA, Medicom, se hizo uso de las
cadenas de Markov. Estas cadenas son modelos matemáticos que representan
sistemas que cambian de estado de manera probabilística en intervalos discretos
de tiempo, donde el estado futuro depende ́unicamente del estado presente, es
decir, son una serie de eventos, en la cual la probabilidad de que ocurra un
evento depende ́unicamente del evento inmediato anterior. A esto se le conoce
como pérdida de memoria, donde solo recuerdan el ́ultimo evento y esto condi-
ciona las posibilidades de los eventos futuros. Esto será de mucha ayuda para
predecir la compra o no compra de cada producto en cada perfil de venta (Hos-
pitales, Farmacias y Distribuidores). Lo anterior se logró agrupando y filtrando
la base de datos por cliente_id y material_id para realizar la matriz de tran-
sición, con el objetivo de obtener las probabilidades para n pasos, donde n son
los meses. Los puntos a considerar en estas cadenas de Markov, es que se tienen
dos estados planteados:''')

st.latex(r'E = \{0, 1\}')

st.text('''donde 0 es que el producto fue comprado y 1 que el producto no fue comprado 
y los intervalos de tiempo se manejan en meses.''')

st.text('''El diagrama de estado es el siguiente: ''')

st.image("images/estados.png", caption = 'Figure 1: Diagrama de estados', width=650)

st.text('''Y la matriz de transición queda:''')

st.image("images/transition_matrix.jpeg")

st.text('''donde p00 es la probabilidad de pasar al estado 0 dado que un paso anterior
estaba en el estado 0, p01 es la probabilidad de pasar al estado 1 dado que un
paso anterior estaba en el estado 0, p10 es la probabilidad de pasar al estado
0 dado que un paso anterior estaba en el estado 1 y p11 es la probabilidad de
pasar al estado 1 dado que un paso anterior estaba en el estado 1. La suma de
cada fila de la matriz de transición son siempre 1 (por ejemplo p00 + p01 = 1 y
p10 + p11 = 1''')

st.text('''Una de las propiedades de las cadenas de Markov es que siempre convergen
a probabilidades estables, esto permite encontrar el promedio a la larga o las
probabilidades de estado estable para cada estado. Para lograr la convergencia
de una probabilidad estable las cadenas de Markov tienen que cumplir con las
siguientes condiciones:''')

st.text('''1. Irreducibilidad: Desde cualquier estado es posible llegar a cualquier otro
estado en un número finito de pasos, es decir, que todos los estados sean
accesibles entre sí.''')

st.text('''2. Aperiodicidad: La cadena debe ser aperiódica, lo que asegura que no
esté atrapada en ciclos repetitivos y que con el tiempo cualquier estado
pueda ser alcanzado.''')

st.text('''3. Recurrente: Un estado recurrente es aquel desde el cual, una vez alcan-
zado, es seguro que volverá a visitarse en algún momento futuro. Para
asegurar la convergencia, es importante que la cadena tenga al menos un
estado recurrente positivo.''')

st.text('''El cumplimiento de las condiciones anteriores da lugar a una cadena de
Markov ergódica, esto significa que a medida que pasa el tiempo, la cadena
convergerá hacia una distribución de probabilidad constante, independiente de
las condiciones iniciales. Una vez sabiendo que se tiene una cadena érgodica,
el siguiente paso es usar la descomposición espectral (la factorización de una
matriz en términos de sus eigenvalores y eigenvectores) que se denota por la
siguiente ecuación.''')

st.latex(r'A = Q\Lambda Q^{-1}')

st.text('''donde Λ es una matriz diagonal de (p × p) cuyos elementos en la diagonal son
los eigenvalores y Q es una matriz p×p cuya i- ́esima columna es el i- ésimo 
eigenvector v.''')

st.text('''Para conseguir la descomposición, primero se calculan los eigenvalores y
eigenvectores de la matriz haciendo uso de las siguientes fórmulas''')

st.latex(r'Eigenvalores: p(\lambda) = \det(P - \lambda I) = 0')

st.latex(r'Eigenvectores: (P - \lambda I)v_i = 0')

st.text('''Los eigenvalores se guardan en la variable Λ, y los eigenvectores se almace-
nan en la variable Q. Se calcula la matriz inversa Q−1, y se realiza la matriz P P
multiplicando las matrices Q, Λ y Q−1, teniendo la matriz P P , la matriz diag-
onal Λ se eleva a la potencia n pasos. Y finalmente se calcula la matriz Pn con
las probabilidades estables a n pasos, haciendo la multiplicaci ́on de Q, Λn y Q−1.
Con las probabilidades constantes que arroja la matriz Pn se predicen y se
realizan las recomendaciones de desactivar o activar los productos dependiendo
de los porcentajes que se arroja en la matriz de 2x2. Si la probabilidad de com-
pra es mayor al 70% se recomendará que se siga manteniendo la producción del
producto.''')

st.text('''Además de tener conocimiento si el producto se debe continuar produciendo
o no, se añadió la recurrencia media, que se refiere al tiempo esperado o prome-
dio que toma para que un proceso de Markov regrese a un estado particular
después de haber salido de ese estado. Es decir, el tiempo que tardará un
cliente en comprar (o no) un producto dado que ya lo había comprado (o no).''')

st.text('''Lo anterior se calcula con los valores estables de las probabilidades de la
cadena π = (π0, π1, . . .). La probabilidad de que de la cadena llegue por primera
vez al estado i partiendo del estado i, por ejemplo, que vuelva a comprar un
producto dado que ya lo compro, esta dada por la fórmula''')

st.latex(r'\mu_{ii} = \frac{1}{\pi_i}')

st.text('''Mientras que el tiempo medio de recurrencia de un estado recurrente j par-
tiendo de un estado i, por ejemplo, que compre un producto dado que no lo
había comprado est ́a dado la siguiente fórmula''')

st.latex(r'\mu_{ij} = 1 + \sum_{k \neq j} \pi_k \mu_{kj}')

st.text('''Realizando lo anterior, sabemos cuantos meses tiene que pasar para que se
den los siguientes casos:''')

st.text('''1. Que un cliente compre un producto dado que ya lo había comprado''')
st.text('''2. Que un cliente no compre un producto dado que no lo había comprado''')
st.text('''3. Que un cliente compre un producto dado que no lo había comprado''')
st.text('''4. Que un cliente no compre un producto dado que lo había comprado''')
st.text('''Esto puede ser de utilidad para saber y actuar sobre la capacidad de almace-
namiento o de producción de los productos dependiendo de las acciones pasadas
de los clientes.''')