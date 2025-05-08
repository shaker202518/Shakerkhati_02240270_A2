class PokemonCardBinderManager:
    CARDS_PER_PAGE = 64
    BINDER_SIZE = 1025  

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
        if confirm.strip().upper() == "CONFIRM":
            self.binder.clear()
            print("Binder has been reset.")
        else:
            print("Reset cancelled.")

    def view_cards(self):
        if not self.binder:
            print("The binder is empty.")
        else:
            output = ["\nCurrent Binder Contents:\n------------------------"]
            sorted_cards = sorted(self.binder.keys())
            for index, number in enumerate(sorted_cards):
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
    manager = PokemonCardBinderManager()
    manager.play()
