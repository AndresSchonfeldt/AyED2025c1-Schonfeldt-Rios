# 🐍Nombre del proyecto (darle un nombre significativo) 

Breve descripción del proyecto:
Este código consiste en la implementacion de la estructura de Lista doblemente enlazada. 
Este tipo de estructura de datos nos permite secuenciar datos en forma de nodos los cuales los podemos recorrer y modificar en dos direcciones al mismo tiempo.
En este codigo se implentaron las siguientes funciones: esta_vacia(), agregar_al_final(), agregar_al_inicio(), __len__(), insertar(), extraer(), copia(), invertir(), concatenar() y __add__()
---
## 🏗Arquitectura General

El codigo comienza definiendo las clases Nodo y dentro de esta ListaDobleEnlazada con sus variables = none.
Nodo cuenta con 2 variables que hacen de "puntero" para editar el siguiente o el anterior nodo, caracteristica especial de este tipo de estructura de dato.

funciones:

esta_vacia(): retorna True o False dependiendo si el primer valor de la lista es none o no.
agregar_al_final(valor): Añade al final de la lista el valor deseado.
agregar_al_inicio(valor): Añade al inicio de la lista el valor deseado.
__len__(): Retorna el valor de size, variable relacionada directamente con el tamaño de la lista.
insertar(valor, posicion): Añade en la posicion seleccionada el valor deseado.
extraer(valor, posicion): Elimina el dato de la posicion seleccionada de la lista y lo retorna al usuario.
copia(): Crea una copia de la lista y la retorna al usuario.
invertir(): Invierte el orden de los datos
concatenar(lista): Añade al final de la lista actual la nueva lista ingresada. Esto haciendo uso de la funcion ya mencionada agregar_al_final().
__add__(lista): Crea y retorna al usuario una nueva lista que sería la suma de la lista actual y la nueva lista ingresada.

Las gráficas de los resultados están disponible en la carpeta [data](./data) del proyecto.

El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 📑Dependencias

1. **Python 3.x**
2. **turtle**

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Rios Rodrigo Exequiel
- Schönfeldt Andrés

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
