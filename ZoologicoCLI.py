import pprint
import uuid
from ZoologicoDAO import ZoologicoDAO
from Animal import Animal
from Habitat import Habitat
from Cuidador import Cuidador


class ZoologicoCLI:
    def __init__(self, database):
        self.database = database
        self.zoologicoDAO = ZoologicoDAO(database)

    def menu(self) -> None:
        print("Bem-vindo ao Zoologico Biruleibe!!")
        while True:
            print("1 ------ criar um animal\n"
                  "2 ------ ver os dados de um animal\n"
                  "3 ------ atualizar um animal\n"
                  "4 ------ excluir um animal\n"
                  "0 ------ sair\n")
            while True:
                user_input = input("Por favor digite uma das opções acima: ")

                if user_input in ["1", "2", "3", "4", "0"]:
                    break

            if user_input in ["1"]:
                self.createAnimal()
            if user_input in ["2"]:
                self.readAnimal()
            if user_input in ["3"]:
                self.updateAnimal()
            if user_input in ["4"]:
                self.deleteAnimal()
            if user_input in ["0"]:
                break

        return None

    def createAnimal(self) -> None:
        new_caregiver_obj = Cuidador(cuidador_id=str(uuid.uuid4()),
                                     nome=input("Digite o nome do cuidador do novo animal: "),
                                     documento=input("Digite o documento do cuidador do novo animal: "))

        while True:
            try:
                habitat_quant = int(input("Digite a quantidade de habitats do novo animal: "))
                break
            except Exception as error:
                print(error)

        new_habitats = []
        for i in range(0, habitat_quant):
            new_habitat_obj = Habitat(habitat_id=str(uuid.uuid4()),
                                      nome=input(f"Digite o nome do habitat {i + 1} do novo animal: "),
                                      tipoAmbiente=input(f"Digite o tipo de ambiente do habitat {i + 1} do novo animal: "),
                                      cuidador=new_caregiver_obj)
            new_habitats.append(new_habitat_obj)
        while True:
            try:
                new_animal_obj = Animal(animal_id=str(uuid.uuid4()),
                                        nome=input("Digite o nome do novo animal: "),
                                        especie=input("Digite a espécie do novo animal: "),
                                        idade=int(input("Digite a idade do novo animal: ")),
                                        habitat=new_habitats)
                break
            except Exception as error:
                print(error)

        new_caregiver = {
            "id": new_caregiver_obj.id,
            "nome": new_caregiver_obj.nome,
            "documento": new_caregiver_obj.documento
        }

        list_of_habitats = []
        for habitat in new_habitats:
            list_of_habitats.append({
                "id": habitat.id,
                "nome": habitat.nome,
                "tipoAmbiente": habitat.tipoAmbiente,
                "cuidador": new_caregiver
            })

        new_animal = {
            "_id": new_animal_obj.id,
            "nome": new_animal_obj.nome,
            "especie": new_animal_obj.especie,
            "idade": new_animal_obj.idade,
            "habitat": list_of_habitats
        }
        self.zoologicoDAO.create_animal(new_animal)

        return None

    def readAnimal(self) -> None:
        animal_id = input("Digite o id do animal desejado: ")
        animal = self.zoologicoDAO.read_animal_by_id(animal_id=animal_id)
        pprint.pprint(animal)
        return None

    def updateAnimal(self) -> None:
        animal_id = input("Digite o id do animal a ser atualizado: ")

        while True:
            user_input = input("O que deseja atualizar, o 'nome', a 'espécie', a 'idade', o 'habitat' ou o 'cuidador'? ")
            if user_input in ["nome", "especie", "espécie", "idade", "habitat", "cuidador"]:
                break

        if user_input in ["nome"]:
            new_name = input("Digite o novo nome do animal: ")
            self.zoologicoDAO.update_animal(animal_id=animal_id, query_filter=None, query={"nome": new_name})

        elif user_input in ["especie", "espécie"]:
            new_species = input("Digite a nova espécie nome do animal: ")
            self.zoologicoDAO.update_animal(animal_id=animal_id, query_filter=None, query={"especie": new_species})

        elif user_input in ["idade"]:
            new_age = input("Digite a nova idade do animal: ")
            self.zoologicoDAO.update_animal(animal_id=animal_id, query_filter=None, query={"idade": new_age})

        elif user_input in ["habitat"]:
            animal = self.zoologicoDAO.read_animal_by_id(animal_id)
            habitats = animal["habitat"]
            pprint.pprint(habitats)

            if len(habitats) > 1:
                habitat_id = input("Digite o id do habitat a ser alterado: ")
            else:
                habitat_id = habitats[0]["id"]

            while True:
                user_input_habitat = input("Deseja mudar o 'nome' ou o 'ambiente'? ")
                if user_input_habitat in ["nome", "ambiente"]:
                    break

            if user_input_habitat in ["nome"]:
                new_habitat_name = input("Digite o novo nome do habitat: ")
                self.zoologicoDAO.update_animal(animal_id=None,
                                                query_filter={"_id": animal_id, "habitat.id": habitat_id},
                                                query={"habitat.$.nome": new_habitat_name})

            if user_input_habitat in ["ambiente"]:
                new_environment_name = input("Digite o novo ambiente do habitat: ")
                self.zoologicoDAO.update_animal(animal_id=None,
                                                query_filter={"_id": animal_id, "habitat.id": habitat_id},
                                                query={"habitat.$.ambiente": new_environment_name})

        elif user_input in ["cuidador"]:
            animal = self.zoologicoDAO.read_animal_by_id(animal_id)
            habitats = animal["habitat"]
            pprint.pprint(habitats)

            cuidador_id = input("Digite o id do cuidador a ser alterado: ")
            while True:
                user_input_cuidador = input("Deseja mudar o 'nome' ou o 'documento' do cuidador? ")
                if user_input_cuidador in ["nome", "documento"]:
                    break

            if user_input_cuidador in ["nome"]:
                new_caregiver_name = input(f"Digite o novo nome do cuidador {cuidador_id}: ")
                self.zoologicoDAO.update_animal(animal_id=None,
                                                query_filter={"_id": animal_id, "habitat.cuidador.id": cuidador_id},
                                                query={"habitat.$.cuidador.nome": new_caregiver_name})

            if user_input_cuidador in ["documento"]:
                new_caregiver_document = input(f"Digite o novo documento do cuidador {cuidador_id}: ")
                self.zoologicoDAO.update_animal(animal_id=None,
                                                query_filter={"_id": animal_id, "habitat.cuidador.id": cuidador_id},
                                                query={"habitat.$.cuidador.documento": new_caregiver_document})
        return None

    def deleteAnimal(self) -> None:
        animal_id = input("Digite o id do animal a ser deletado: ")
        self.zoologicoDAO.delete_animal(animal_id)
        return None
