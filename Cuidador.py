class Cuidador:
    def __init__(self, cuidador_id: str, nome: str, documento: str):
        self.id = cuidador_id
        self.nome = nome
        self.documento = documento

    def mostrarInfo(self):
        print(f"id do cuidador: {self.id}")
        print(f"nome do cuidador: {self.nome}")
        print(f"documento do cuidador: {self.documento}")
