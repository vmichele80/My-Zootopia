import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)



def main():
    animals_data = load_data('animals_data.json')

    for animal in animals_data:
        characteristics = animal["characteristics"]
        if "type" in characteristics:
            print(f"Name: {animal["name"]} \nDiet: {characteristics["diet"]}\nLocation: {animal["locations"][0]}\nType: {characteristics["type"]}\n")
        else:
            print(f"Name: {animal["name"]} \nDiet: {characteristics["diet"]}\nLocation: {animal["locations"][0]}\n")

if __name__ == '__main__':
    main()