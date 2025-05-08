BINDER_SIZE = 1025
CARDS_PER_PAGE = 64
ROWS = 8
COLS = 8

class pokemonBinder:
    def __init__(self):
        self.cards = []  

    def add_card(self, number):
        if not 1 <= number <= BINDER_SIZE:
            return "Invalid Pokedex number. Must be between 1 and 1025."
        if number in self.cards:
            return f"Pokedex #{number} already exists in the binder."
        self.cards.append(number)
        self.cards.sort()
        index = self.cards.index(number)
        page = (index // CARDS_PER_PAGE) + 1
        pos_in_page = index % CARDS_PER_PAGE
        row = (pos_in_page // COLS) + 1
        col = (pos_in_page % COLS) + 1
        return f"Page: {page}\nPosition: Row {row}, Column {col}\nStatus: Added Pokedex #{number} to binder"

    def reset_binder(self):
        self.cards = []
        return "The binder reset was successful! All cards have been removed."

    def view_cards(self):
        if not self.cards:
            return "The binder is empty.\nTotal cards in binder: 0\n% completion: 0%"
        output = ["Current Binder Contents:\n------------------------"]
        for number in self.cards:
            index = self.cards.index(number)
            page = (index // CARDS_PER_PAGE) + 1
            pos_in_page = index % CARDS_PER_PAGE
            row = (pos_in_page // COLS) + 1
            col = (pos_in_page % COLS) + 1
            output.append(f"Pokedex #{number}:\n  Page: {page}\n  Position: Row {row}, Column {col}")
        total = len(self.cards)
        percent = round((total / BINDER_SIZE) * 100, 1)
        output.append("------------------------")
        output.append(f"Total cards in binder: {total}")
        output.append(f"% completion: {percent}%")
        if total == BINDER_SIZE:
            output.append("You have caught them all!!")
        return "\n".join(output)

def main():
    binder = pokemonBinder()
    while True:
        print("\nWelcome to Pokemon Card Binder Manager!")
        print("Main Menu:")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            try:
                number = int(input("Enter Pokedex number(1-1025): "))
                print(binder.add_card(number))
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            print("WARNING: This will delete ALL Pokemon cards from the binder.")
            print("This action cannot be undone.")
            confirm = input("Type 'CONFIRM' to reset or 'EXIT' to return to the Main Menu: ").strip().upper()
            if confirm == "CONFIRM":
                print(binder.reset_binder())
            elif confirm == "EXIT":
                continue
            else:
                print("Invalid input. Returning to main menu.")
        elif choice == "3":
            print(binder.view_cards())
        elif choice == "4":
            print("Thank you for using Pokemon Card Binder Manager!")
            print(f"Total cards in binder upon exit: {len(binder.cards)}")
            break
        else:
            print("Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    main()
