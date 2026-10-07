Circuits = {
    1: "3RESNETWRK",
    2: "Placeholder",
    3: "Placeholder",
    4: "Placeholder",
    5: "Placeholder"
}

ChooseACircuit = input("Which circuit would you like to choose? Please enter a number from 1 to 5: ")
ChosenCircuit = Circuits.get(int(ChooseACircuit), "Invalid choice. Please select a number between 1 and 5.")



