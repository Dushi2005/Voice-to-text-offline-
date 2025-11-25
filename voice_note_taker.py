import speech_recognition as sr
from datetime import datetime
import os

# Create notes folder if not exists
if not os.path.exists("notes"):
    os.makedirs("notes")

def take_voice_note():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n Listening... Speak now.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print(" Converting speech to text (offline)...")
        text = recognizer.recognize_sphinx(audio)
        print(f"Recognized Text: {text}")

        # Save note
        filename = f"notes/note_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as file:
            file.write(text)

        print(f"Note saved as: {filename}")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except Exception as e:
        print(f"Error: {e}")

def show_all_notes():
    print("\n Saved Notes:")
    for file in os.listdir("notes"):
        print(" -", file)

def read_note():
    fname = input("\nEnter note filename: ")
    path = f"notes/{fname}"

    if not os.path.exists(path):
        print(" File not found.")
        return

    with open(path, "r") as file:
        print("\n Note Content:")
        print(file.read())

def main():
    while True:
        print("\n==== Voice Note Taker ====")
        print("1. Take new voice note")
        print("2. View saved notes")
        print("3. Read a note")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            take_voice_note()
        elif choice == "2":
            show_all_notes()
        elif choice == "3":
            read_note()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
