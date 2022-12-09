# Trabajo 02 Riesgo de Credito

## Introduccion
Para este trabajo crearemos una aplicacion que permita a un usuario en base , a su informacion financiera le permita predecir como sera su scorecard , ademas mostrará si es mayor o menor que la población.

Para esto tomamos un dataset que esta disponible en kaggle , este contiene información corceniente a datos de los prestamos de clientes recopilados por la compañia Lending Club, una compañia de prestamo P2P (Peer-to-Peer), la informacion contiene alrededor de 450000 registros de prestamos de clientes entre el año 2007 a 2014, con alrededor de 75 variables que nos indican informacion sobre los clientes y el prestamo.

## Eliminacion de variables

Primero para garantizar mas exactitud en el modelo , eliminamos variables que cuenten con un gran porcentaje de nulos, precisamente , eliminamos variables que posean 80% de datos nulos.

Imagen 01

Lo siguiente sera eliminar variables con informacion que no es relevante para el modelo.

Imagen 02

## Identificacion de la variable objetivo

Primero encontramos la variable que nos interesa predecir , la cual es loan status , primero visualizamos como esta distribuidan sus diferentes valores unicos, una vez visualizados , necesitamos transformar la variable de forma que nos interese predecir, primero separamos los valores de loan status que tienden a mostrar que una persona es una buena o mala opcion para darle un prestamo, y luego eliminamos la columna de loan status original

Las variables que deciden si una persona no es buena opcion para un prestamo son (Charged Off', 'Default', 'Late (31-120 days)','Does not meet the credit policy. Status:Charged Off'), a estas personas se les asignara un 0 , y al resto de la poblacion se le asignara un 1. Convirtiendo asi la variable objetivo en un 0 siendo mala opcion y un 1 una buena opcion.

Imagen 03

## Dividir el dataset
Dividimos el dataset en entrenamiento y validacion , con una relacion de 80 y 20 rspectivamente del dataset original.

Imagen 04

## Manejo de datos
Ahora manejamos variables con informacion que en la manera que esta , no se puede digitar en un modelo, primero transformamos la variables emp_length ( el cual es años trabajando) , eliminamos toda cadena de texto , y en caso de ser especificamente trabajando menos de un año se vuelve 0 , ya despues de eso tenemos unicamente, datos numericos , en formato cadena , asi que transformamos en formato numerico los numeros.

Asi para otras variables que necesiten algun manejo de datos se aplicara una funcion que las modifique.

Imagen 05

## Seleccion de variables
Usando el metodo de chi cuadrado encontramos posibles variables para el modelo

Imagen 06

Usando el analisis de varianza usando el estadistico F, encontramos las siguientes variables para el modelo.

Imagen 07

## Mapa de coorelacion

Usando las 20 primeras variables, grraficamos el mapa de coorrelacion para poder obtener como se relacionan entre si.

Imagen 08

siendo que out_prncp_inv y total_pymnt_inv tienen una alta coorelacion se eliminan.

## WOE
Luego de haber seleccionado las variables , y haberles aplicado metodo de one hot encoding para que sean aptas para el modelo, se comienza la parte de la ingenieria de caracteristicas

Para esto calculamos el WOE( peso de evidencia ) y el IV(Valor de informacion) estas tecnicas para ingenieria de caracteristicas son ampliamente usadas en puntajes crediticios.

el WOE usa la formula de logaritmo natural de la division entre el porcentaje de buenos clientes sobre malos clientes mientras que el IV es una sumatoria de el producto del WOE por la diferencia de porcentaje entre buenos y malos clientes, estas tecnicas las aplicamos a todas nuestras variables predictorias

En la siguiente imagen mostramos un ejemplo usando la variable revol_util

Imagen 09

## Modelo inicial
Una vez obtenido el modelo  , usando regresion logistica y usando validacion cruzada obtenemos un modelo de prediccion de si una persona es buen o no cliente
con esto vemos que tanto el puntaje GINI como AUROC , son bastante buenos por lo tanto se acepta el modelo.

Imagen 10

## Modelo del Scorecard

Por ultimo creamos un Scorecard, para esto usaremos los rangos sugeridos para los puntajes siendo de 300 a 850, con esto creamos coeficientes a partir de la suma de minimos y maximos de los valores obtenidos en cada variable , con los cuales obtendremos una calificacion para cada variable, y luego las aplicamos sobre todo el dataset, usando anteriormente , el WOE , calculamos los puntajes para un set de datos dados y con eso se construye el modelo para la scorecard , al aplicarlo sobre el dataset original nos encontramos que la media de la poblacion ronda el puntaje de 549.198462 , ya como se obtuvo el modelo para prediccion , este se usara para predecir en base a las variables obtenidas , el score de una persona.
