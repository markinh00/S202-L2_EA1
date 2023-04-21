from Cuidador import Cuidador


class Habitat:
    def __init__(self, habitat_id: str, nome: str, tipoAmbiente: str, cuidador: Cuidador):
        self.id = habitat_id
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador

    def mostrarInfo(self):
        print(f"id do habitat: {self.id}")
        print(f"nome do habitat: {self.nome}")
        print(f"tipo de ambiente do habitat: {self.tipoAmbiente}")
        self.cuidador.mostrarInfo()
