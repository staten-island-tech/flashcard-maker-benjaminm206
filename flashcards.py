import json
key = 0
value = 0
self = 0
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

mode = input("Are you a teacher or a student? Please type 'Teacher' or 'Student'): ")
teacher = 0
student = 0
if mode in "teacher" or mode in "Teacher":
    teacher += 1
    print("Teacher Mode enabled.")
if mode in "student" or mode in "Student":
    student += 1
    print("Student Mode enabled.")

while teacher == 1:
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
        print(flashcards_data)

while student == 1:
    answer = # The input inputted after user recieves front of flashcard (key)
    if answer in Flashcard(value):
        print("Correct!")
    else:
        print("Incorrect!")
