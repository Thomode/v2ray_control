import json

ruta_config = "/etc/v2ray/config.json"
user_vend = "tomas.com"

def clients_list():
    try:
        with open("config_br.json", "r") as file_r:
            config = json.load(file_r)
            file_r.close()

            usuarios = config["inbounds"][0]["settings"]["clients"]

        cont_client = 1

        for cliente in usuarios:
            try:
                email = cliente["email"]
                id = cliente["id"]

                nombre, vendedor = email.split("@")

                if vendedor == user_vend:
                    if cont_client > 0 and cont_client < 10:
                        mensaje_cliente = "0" + str(cont_client) + ") " + id + "   "+nombre
                    else:
                        mensaje_cliente = str(cont_client) + ") " + id + "   "+nombre

                    print(mensaje_cliente)

                    cont_client += 1
            except:
                pass
    except NameError:
        print("Archivo no encontrado")

def clients_search(nom_search):
    nom_search = nom_search.lower()
    len_nom_search = len(nom_search)

    try:
        with open("config_br.json", "r") as file_r:
            config = json.load(file_r)
            file_r.close()

            usuarios = config["inbounds"][0]["settings"]["clients"]

        for cliente in usuarios:
            try:
                email = cliente["email"]
                id = cliente["id"]

                nombre, vendedor = email.split("@")

                if vendedor == user_vend:
                    if nombre == nom_search:
                        print(id + " " + nombre)

                    else:
                        nom_reg = ""
                        for i in range(len_nom_search):
                            nom_reg = nom_reg + nombre[i]

                        if nom_search == nom_reg:
                            print(id + " " + nombre)
            except:
                pass

    except NameError:
        print("Archivo no encontrado")

def menu():
    opcion = "1"
    while opcion != "0":
        print("\n1) Mostrar Clientes",
              "\n2) Buscar Cliente",
              "\n0) Salir")
        opcion = input("\nIngresar opcion: ")
        print("")

        if opcion == "1":
            clients_list()
            input("\nPresionar ENTER para continuar")

        elif opcion == "2":
            nombre_seach = input("Ingresar el nombre o iniciales que desea buscar: ")
            clients_search(nombre_seach)
            input("\nPresionar ENTER para continuar")

        else:
            print("Opcion Invalida!")

if __name__ == "__main__":
    menu()


