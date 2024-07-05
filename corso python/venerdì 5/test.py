class Veicolo:
    def __init__(self, anno):
        self.anno = anno

    def mostra_anno(self):
        print(f"L'anno del veicolo è {self.anno}")

class Automobile(Veicolo):
    def __init__(self, anno, marca):
        __init__(self, anno)  # Chiamata esplicita al costruttore della classe base
        self.marca = marca

    def mostra_dettagli(self):
        print(f"Questa automobile è del {self.anno} e della marca {self.marca}")

classe1 = Veicolo(2020)
classe1.mostra_anno()

classe2 = Automobile(2025,"bmx")
classe2.mostra_dettagli()