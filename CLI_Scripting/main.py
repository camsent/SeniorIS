Circuits = {
    1: "3RESNETWRK",
    2: "Placeholder",
    3: "Placeholder",
    4: "Placeholder",
    5: "Placeholder"
}
from Troubleshooting import three_RESNETWORK

ChooseACircuit = input("Which circuit would you like to choose? Please enter a number from 1 to 5: ")
ChosenCircuit = Circuits.get(int(ChooseACircuit), "Invalid choice. Please select a number between 1 and 5.")



if ChosenCircuit == "3RESNETWRK":
    three_RESNETWORK.CalculateExpectedTPValues()



