import random

class FlashcardQuiz:
    def __init__(self):
        self.flashcards = {
            "Python is a programming language.": "True",
            "The capital of France is Paris.": "True",
            "Water boils at 100 degrees Celsius.": "True",
            "The Earth is flat.": "False",
            "The currency of Japan is the Yuan.": "False"
            # Add more flashcards as needed
        }

    def start_quiz(self):
        print("Welcome to the Flashcard Quiz!")
        print("Answer 'True' or 'False'. Enter 'q' to quit.")

        # Shuffle the flashcards
        flashcard_keys = list(self.flashcards.keys())
        random.shuffle(flashcard_keys)

        # Quiz loop
        for question in flashcard_keys:
            user_answer = input(f"\n{question}\nYour answer: ").lower()

            if user_answer == "q":
                print("\nQuitting the quiz. Goodbye!")
                break
            elif user_answer == self.flashcards[question].lower():
                print("Correct!\n")
            else:
                print(f"Wrong! The correct answer is {self.flashcards[question]}.\n")

        print("Quiz completed.")

if __name__ == "__main__":
    quiz = FlashcardQuiz()
    quiz.start_quiz()
