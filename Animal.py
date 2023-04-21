from Habitat import Habitat


class Animal:
    def __init__(self, animal_id: str, nome: str, especie: str, idade: int, habitat: list[Habitat]):
        self.id = animal_id
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = habitat

    def mostrarInfo(self):
        print(f"id do animal: {self.id}")
        print(f"nome do animal: {self.nome}")
        print(f"espécie do animal: {self.especie}")
        print(f"idade do animal: {self.idade}")
        for habitat in self.habitat:
            habitat.mostrarInfo()
