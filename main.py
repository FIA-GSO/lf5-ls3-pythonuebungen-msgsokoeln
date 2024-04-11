# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#---------------------Aufgabe 1 ------------------------------------
class R2D2:
    def __init__(self, young, adult, old):
        self.young = young
        self.adult = adult
        self.old = old

    def step(self):
        # Aging
        new_adult = self.young // 2
        new_old = self.adult // 3

        # Reproduction
        new_young = self.adult * 4 + self.old * 2

        # Update population
        self.young = new_young
        self.adult = new_adult
        self.old = new_old

    def __str__(self):
        return f"Young: {self.young}, Adult: {self.adult}, Old: {self.old}"


# Initialize population
# r2d2_population = R2D2(100, 50, 25)

# Simulate for 10 steps
# for _ in range(10):
    # print(r2d2_population)
    # r2d2_population.step()

#---------------------Aufgabe 2 Streichholz------------------------------
#IMPLEMENT YOUR SOLUTION FOR THE STEICHHOLZSPIEL HERE

import random

def matchstick_game(human_starts=False, random_starts=False):
    # Initialize the number of matchsticks
    matchsticks = 31

    # If the human player starts, ask them to set the number of matchsticks
    if human_starts:
        matchsticks = int(input("Player B (Human), how many matchsticks do you want to start with? "))

    # If the computer player starts randomly, set a random number of matchsticks
    if random_starts:
        matchsticks = random.randint(10, 50)
        print(f"Player A (Computer) starts with {matchsticks} matchsticks.")

    # Player A (Computer) starts the game by taking 2 matchsticks
    matchsticks -= 2
    print(f"Player A (Computer) takes 2 matchsticks. Remaining matchsticks: {matchsticks}")

    while matchsticks > 1:
        # Player B (Human) takes 1 to 6 matchsticks
        player_b_matchsticks = int(input("Player B (Human), how many matchsticks do you want to take (1-6)? "))
        
        # Check if the input is within the valid range
        while player_b_matchsticks < 1 or player_b_matchsticks > 6:
            print("Invalid input. Please enter a number between 1 and 6.")
            player_b_matchsticks = int(input("Player B (Human), how many matchsticks do you want to take (1-6)? "))
        
        matchsticks -= player_b_matchsticks
        print(f"Player B (Human) takes {player_b_matchsticks} matchsticks. Remaining matchsticks: {matchsticks}")

        # Player A (Computer) takes a complementary number so that a total of 7 are taken
        player_a_matchsticks = 7 - player_b_matchsticks
        matchsticks -= player_a_matchsticks
        print(f"Player A (Computer) takes {player_a_matchsticks} matchsticks. Remaining matchsticks: {matchsticks}")

    # Player B (Human) must take the last matchstick and therefore loses
    print("Player B (Human), you must take the last matchstick. You lose!")

# Call the function with the optional variants
# matchstick_game(human_starts=True, random_starts=True)


#---------------------Aufgabe 3 Heron ------------------------------------
def heron_method(number):
    # Initialisiere a und b
    laenge_a = number
    laenge_b = 1

    # Initialisiere die Abweichung
    abweichung = abs(laenge_a - laenge_b)

    # Iteriere, bis die Abweichung kleiner als 0.01 ist
    while abweichung >= 0.01:
        # Berechne den Mittelwert von a und b
        mittelwert = (laenge_a + laenge_b) / 2

        # Aktualisiere a und b
        laenge_a = mittelwert
        laenge_b = number / laenge_a

        # Aktualisiere die Abweichung
        abweichung = abs(laenge_a - laenge_b)

    # Gib die Näherung der Quadratwurzel zurück
    return laenge_a

# Rufe die Funktion mit einem dynamischen Wert auf
# number = int(input("Geben Sie eine Zahl an von der Sie die Quadratwurzel berechnen möchten: "))
# print(f"Die Quadratwurzel von {number} ist ungefähr {heron_method(number)}")

#---------------------Aufgabe 4 Quersumme------------------------------
#IMPLEMENT, IF NECESSARY, EXERCISE 4 HERE BUT USE A FUNCTION!

def quersumme_berechnen(zahl):
    return sum(int(ziffer) for ziffer in str(zahl))

#zahl = int(input("Geben Sie eine Zahl ein: "))
#print("Die Quersumme der eingegebenen Zahl ist:", quersumme_berechnen(zahl))


#---------------MANAGEMENT----------------------
#-------------COMMENT/UNCOMMENT lines to launch the different exercises
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Aufgabe 1
    if input("Möchten Sie Aufgabe 1 ausführen? (j/n): ").lower() == 'j':
        print()
        r2d2_population = R2D2(100, 50, 25)
        for _ in range(5):
            print(r2d2_population)
            r2d2_population.step()

    # Aufgabe 2
    if input("Möchten Sie Aufgabe 2 ausführen? (j/n): ").lower() == 'j':
        matchstick_game(human_starts=True, random_starts=False)

    # Aufgabe 3
    if input("Möchten Sie Aufgabe 3 ausführen? (j/n): ").lower() == 'j':
        number = int(input("Geben Sie eine Zahl an von der Sie die Quadratwurzel berechnen möchten: "))
        print(f"Die Quadratwurzel von {number} ist ungefähr {heron_method(number)}")

    # Aufgabe 4
    if input("Möchten Sie Aufgabe 4 ausführen? (j/n): ").lower() == 'j':
        zahl = int(input("Geben Sie eine Zahl ein von der  Sie die Quersumme wissen wollen: "))
        print("Die Quersumme der eingegebenen Zahl ist:", quersumme_berechnen(zahl))
