import os


def main():
    lenguaje = os.getenv("LENGUAJE")
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GitHub! Tu lenguaje favorito es {lenguaje}!")


if __name__ == "__main__":
    main()