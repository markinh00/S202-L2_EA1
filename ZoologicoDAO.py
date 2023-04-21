class ZoologicoDAO:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_animal(self, animal: dict) -> None:
        try:
            result = self.collection.insert_one(animal)
            animal_id = str(result.inserted_id)
            print(f"Animal {animal['nome']} created with id: {animal_id}")
            return None
        except Exception as error:
            print(f"An error occurred while creating animal: {error}")
            return None

    def read_animal_by_id(self, animal_id: str) -> [dict, None]:
        try:
            animal = self.collection.find_one({"_id": animal_id})
            if animal:
                print(f"Animal found: {animal}")
                return animal
            else:
                print(f"No animal found with id {animal_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading animal: {error}")
            return None

    def update_animal(self, animal_id: [str, None], query_filter: [dict, None], query: dict) -> [int, None]:
        try:
            if animal_id is None:
                animal_id = query_filter["_id"]

            if query_filter is None:
                query_filter = {"_id": animal_id}

            result = self.collection.update_one(query_filter, {"$set": query})
            if result.modified_count:
                print(f"Animal {animal_id} updated")
            else:
                print(f"No animal found with id {animal_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating animal: {error}")
            return None

    def delete_animal(self, animal_id: str) -> [int, None]:
        try:
            result = self.collection.delete_one({"_id": animal_id})
            if result.deleted_count:
                print(f"Animal {animal_id} deleted")
            else:
                print(f"No animal found with id {animal_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting animal: {error}")
            return None
