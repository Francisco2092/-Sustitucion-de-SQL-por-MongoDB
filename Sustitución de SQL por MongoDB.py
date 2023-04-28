import pymongo

cliente = pymongo.MongoClient("mongodb://usuario:contraseña@servidor:puerto/")
base_de_datos = cliente["nombre_base_de_datos"]
coleccion = base_de_datos["palabras"]

def agregar_palabra():
    palabra = input("Ingresa la palabra: ")
    significado = input("Ingresa el significado: ")
    nueva_palabra = {"palabra": palabra, "significado": significado}
    coleccion.insert_one(nueva_palabra)

def editar_palabra():
    palabra = input("Ingresa la palabra que deseas editar: ")
    nueva_palabra = input("Ingresa la nueva palabra: ")
    nuevo_significado = input("Ingresa el nuevo significado: ")
    palabra_editar = coleccion.find_one({"palabra": palabra})
    if palabra_editar:
        coleccion.update_one({"_id": palabra_editar["_id"]}, {"$set": {"palabra": nueva_palabra, "significado": nuevo_significado}})
    else:
        print("La palabra no fue encontrada en el diccionario.")

def eliminar_palabra():
    palabra = input("Ingresa la palabra que deseas eliminar: ")
    palabra_eliminar = coleccion.find_one({"palabra": palabra})
    if palabra_eliminar:
        coleccion.delete_one({"_id": palabra_eliminar["_id"]})
    else:
        print("La palabra no fue encontrada en el diccionario.")

def ver_palabras():
    palabras = coleccion.find()
    for palabra in palabras:
        print(f"{palabra['palabra']}: {palabra['significado']}")

def buscar_palabra():
    palabra = input("Ingresa la palabra que deseas buscar: ")
    palabra_buscar = coleccion.find_one({"palabra": palabra})
    if palabra_buscar:
        print(palabra_buscar["significado"])
    else:
        print("La palabra no fue encontrada en el diccionario.")

def menu():
    while True:
        print("Seleccione una opción:")
        print("a) Agregar nueva palabra")
        print("b) Editar palabra existente")
        print("c) Eliminar palabra existente")
        print("d) Ver listado de palabras")
        print("e) Buscar significado de palabra")
        print("f) Salir")

        opcion = input("Opción seleccionada: ")

        if opcion == "a":
            agregar_palabra()
        elif opcion == "b":
            editar_palabra()
        elif opcion == "c":
            eliminar_palabra()
        elif opcion == "d":
            ver