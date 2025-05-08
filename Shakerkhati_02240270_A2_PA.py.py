import random

class GameManager:
    def __init__(self):
        self.overall_score = {
            "guess_number": 0,
            "rock_paper_scissors": 0,
            "trivia": 0
        }
        self.games = {
            1: GuessNumberGame(self),
            2: RockPaperScissorsGame(self),
            3: TriviaPursuitGame(self),
            4: PokemonCardBinderManager()
        }

    def display_menu(self):
        print("\nSelect a function (0-5):")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors Game")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Current Overall Score")
        print("0. Exit program")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    print("Exiting the program.")
                    break
                elif choice == 5:
                    print("Current Scores:", self.overall_score)
                elif choice in self.games:
                    self.games[choice].play()
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

class GuessNumberGame:
    def __init__(self, manager):
        self.manager = manager

    def play(self):
        number_to_guess = random.randint(1, 100)
        guess = None
        attempts = 0
        while guess != number_to_guess:
            try:
                guess = int(input("Guess a number between 1 and 100: "))
                attempts += 1
                if guess < number_to_guess:
                    print("Too low!")
                elif guess > number_to_guess:
                    print("Too high!")
            except ValueError:
                print("Please enter a valid number.")
                continue
        score = max(100 - attempts, 0)
        print(f"Congratulations! You guessed the number in {attempts} attempts. (+{score} points)")
        self.manager.overall_score["guess_number"] += score

class RockPaperScissorsGame:
    def __init__(self, manager):
        self.manager = manager

    def play(self):
        choices = ["rock", "paper", "scissors"]
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice.")
            return
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie! (+1 point)")
            self.manager.overall_score["rock_paper_scissors"] += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win! (+3 points)")
            self.manager.overall_score["rock_paper_scissors"] += 3
        else:
            print("You lose! (+0 points)")

class TriviaPursuitGame:
    def __init__(self, manager):
        self.manager = manager

    def play(self):
        print("\n[Trivia Pursuit]")
        questions = {
            "History": [
                ("Who is the first king of Bhutan?", "a", ["Sir Ugyen Wangchuck", "Jigme Singye Wangchuck", "Jigme Dorji Wangchuck"]),
                ("When did Bhutan join the UN?", "b", ["1961", "1971", "1981"]),
                ("Who introduced democracy in Bhutan?", "c", ["Ugyen Wangchuck", "Jigme Dorji Wangchuck", "Jigme Singye Wangchuck"]),
                ("Which dynasty rules Bhutan?", "a", ["Wangchuck", "Namgyal", "Chogyal"])
            ],
            "Science": [
                ("Approximate distance between Earth and Sun?", "c", ["148 million km", "149 million km", "150 million km"]),
                ("Chemical symbol for water?", "a", ["H2O", "CO2", "O2"]),
                ("Speed of light?", "b", ["150,000 km/s", "300,000 km/s", "1,000,000 km/s"]),
                ("Largest human organ?", "c", ["Heart", "Liver", "Skin"])
            ]
        }
        score = 0
        for category, q_list in questions.items():
            print(f"\nCategory: {category}")
            for i, (question, correct, options) in enumerate(q_list):
                print(f"{i+1}. {question}")
                print(f"a) {options[0]}\tb) {options[1]}\tc) {options[2]}")
                ans = input("Your answer (a/b/c): ").lower()
                if ans == correct:
                    print("Correct!")
                    score += 1
                else:
                    print("Wrong.")
        print(f"You got {score} correct answer(s). (+{score} points)")
        self.manager.overall_score["trivia"] += score

class PokemonCardBinderManager:
    CARDS_PER_PAGE = 64
    BINDER_SIZE = 1025  # Maximum Pokedex number

    def __init__(self):
        self.binder = {}

    def play(self):
        while True:
            print("\nWelcome to Pokemon Card Binder Manager!")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. Exit")
            try:
                choice = int(input("Select option: "))
                if choice == 1:
                    self.add_card()
                elif choice == 2:
                    self.reset_binder()
                elif choice == 3:
                    self.view_cards()
                elif choice == 4:
                    print("Exiting the binder manager.")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def add_card(self):
        try:
            number = int(input("Enter Pokedex number (1-1025): "))
            if number < 1 or number > self.BINDER_SIZE:
                print("Invalid Pokedex number. Must be between 1 and 1025.")
                return
            if number in self.binder:
                print("This card is already in the binder.")
            else:
                self.binder[number] = f"Card #{number}"
                print(f"Added Card #{number} to binder.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def reset_binder(self):
        confirm = input("WARNING: Type 'CONFIRM' to reset or anything else to cancel: ")
        if confirm == "CONFIRM":
            self.binder.clear()
            print("Binder has been reset.")
        else:
            print("Reset cancelled.")

    def view_cards(self):
        if not self.binder:
            print("The binder is empty.")
        else:
            output = ["Current Binder Contents:\n------------------------"]
            for number in sorted(self.binder):
                index = list(self.binder.keys()).index(number)
                page = (index // self.CARDS_PER_PAGE) + 1
                pos_in_page = index % self.CARDS_PER_PAGE
                row = (pos_in_page // 8) + 1
                col = (pos_in_page % 8) + 1
                output.append(f"Pokedex #{number}:\n  Page: {page}\n  Position: Row {row}, Column {col}")
            output.append("------------------------")
            total = len(self.binder)
            percent = round((total / self.BINDER_SIZE) * 100, 1)
            output.append(f"Total cards in binder: {total}")
            output.append(f"% completion: {percent}%")
            if total == self.BINDER_SIZE:
                output.append("You have caught them all!!")
            print("\n".join(output))

if __name__ == "__main__":
    GameManager().run()