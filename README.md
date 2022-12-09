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
Ahora manejamos variables con informacion que en la manera que esta , no se puede digitar en un modelo, primero transformamos la variables emp_length ( el cual es años trabajando) , eliminamos toda cadena de texto , y en caso de ser especificamente trabajando menos de un año , eliminamos
Imagen 05
