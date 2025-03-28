import json
class Flashcard:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def display_info(self):
        return f"{self.key}{self.value}"
    def to_dict(self):
        return {"key": self.key, "value": self.value}
    
flashcards = [
    Flashcard("key", "value")
]

flashcards_data = [flashcard.to_dict() for flashcard in flashcards]

with open("flashcards.json", "w") as file:
    json.dump(flashcards_data, file, indent=4)

mode = input("Are you a teacher or a student? Please type 'T' or 'S'): ").lower()
teacher = 0
student = 0
if mode in "t":
    teacher += 1
    print("Teacher Mode enabled.")
if mode in "s":
    student += 1
    print("Student Mode enabled.")

while teacher:
    key = input("Insert a key (a term) for the front of the flashcard: ")
    value = input("Insert a value (a definition) for the back of the flashcard: ")
    new_flashcard = Flashcard(key, value)
    # Load existing data
    try:
        with open("flashcards.json", "r") as file:
            flashcards_data = json.load(file)
    except FileNotFoundError:
        flashcards_data = []

    # Append new flashcard
    flashcards_data.append(new_flashcard.to_dict())

    # Save updated data back to file
    with open("flashcards.json", "w") as file:
        json.dump(flashcards_data, file, indent=4)
        print("Flashcard saved!")
    
    cont = input("Would you like to continue adding flashcards? (Yes or no): ")
    if cont in "No" or cont in "no":
        print("Switching to Student mode...")
        student = 1
        teacher = 0
        break
while student:
    try:
        with open("flashcards.json", "r") as file:
            flashcards_data = json.load(file)
    except FileNotFoundError:
        print("No flashcards found. Did your teacher create any yet?")
        exit()
    for flashcard in flashcards_data:
        answer = input(f"What is the definition of {flashcard['key']}? ")
        if answer == flashcard['value']:
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {flashcard['value']}.")
