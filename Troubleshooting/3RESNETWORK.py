def VoltageCheck():
    InputVoltage = float(input("Enter the input voltage (V): "))
    InputVoltageCheck = input ("You have entered an input voltage of {} V. Is this correct? (Y/N): ".format(InputVoltage))
    if InputVoltageCheck.lower() == 'y':
        print("Input voltage confirmed.")
        return True, InputVoltage
    else:
        print("\nPlease re-enter the input voltage.")
        return VoltageCheck()  # Recursively call the function to re-enter the voltage

def ResistanceCheck():
    resistance_values = []
    for i in range (0, 3):
        while True:
            InputResistance = float(input("\nEnter the resistance value (Ohms): "))
            InputResistanceCheck = input ("You have entered a resistance value of {} Ohms. Is this correct? (Y/N): ".format(InputResistance))
            if InputResistanceCheck.lower() == 'y':
                print("Resistance value confirmed.")
                resistance_values.append(InputResistance)
                break
            else:
                print("\nPlease re-enter the resistance value.")
                #ResistanceCheck()  # Recursively call the function to re-enter the resistance
    return resistance_values
    
def CalculateExpectedTPValues():
    valid, voltage = VoltageCheck()
    Shunt = 100.0 #Shunt resistor value in Ohms
    if valid:
        resistances = ResistanceCheck()
        R1, R2, R3, = resistances
        I = (voltage / (R1 + R2 + R3 + Shunt)) #Current through the circuit in Amperes
        TP1 = I * (R2 + R3 + Shunt)
        TP2 = I * (R3 + Shunt)
        TP3 = I * Shunt
        print("\nExpected Test Point Values (Note: there may be a small margin of error):")
        print("TP1: {} V".format(TP1))
        print("TP2: {} V".format(TP2))
        print("TP3: {} V".format(TP3))
        print("\nPlease check the Serial Monitor and compare the expected values with the actual values.")
        MOECheck = input("Are the expected values within a reasonable margin of error? (Y/N): ")
        if MOECheck.lower() == 'y':
            print("Great! The circuit is functioning as expected.")
            return
        elif MOECheck.lower() == 'n':
            TroubleshootCircuit(voltage, resistances) 
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
            return CalculateExpectedTPValues()  # Recursively call the function to re-enter the input
            ###############################come back to this for a better solution###################################

def TroubleshootCircuit(voltage, resistances):
    print("\nWelcome to the 3RESNETWORK Troubleshooting Tool.")
    

    TP1 = input("\nPlease enter the actual voltage measured at Test Point 1 (TP1) in Volts: ")
    TP2 = input("Please enter the actual voltage measured at Test Point 2 (TP2) in Volts: ")
    TP3 = input("Please enter the actual voltage measured at Test Point 3 (TP3) in Volts: ")

    Current_mA = float(TP3) * 10.0 #Current through the circuit in mA
    I = Current_mA / 1000.0 #Current through the circuit in Amperes

    if TP1 == "0" and TP2 == "0" and TP3 == "0":
        print("\nAll test points are reading 0V. Please check the connection to the power supply.")
    elif TP1 == "5" and TP2 == "5" and TP3 == "5":
        print("\nAll test points are reading 5V. Please check the connection to ground.")
    elif TP1 == "5" and TP2 == "0" and TP3 == "0":
        print("\nTP1 is reading 5V, while TP2 and TP3 are reading 0V. Please check the connection to R2.")
    elif TP1 == "5" and TP2 == "5" and TP3 == "0":
        print("\nTP1 and TP2 are reading 5V, while TP3 is reading 0V. Please check the connection to R3.")
    else:
        print("\nThe test point values indicate an error in resistance values entered. Hang on while we calculate the resistor values based on the actual test point values...")
        
        R1 = (float(voltage) - float(TP1)) / I
        R2 = (float(TP1) - float(TP2)) / I
        R3 = (float(TP2) - float(TP3)) / I

        if abs(R1 - resistances[0]) > 10:
            print("\nThe calculated value of R1 is {} Ohms, which is significantly different from the entered value of {} Ohms. Please check the resistor at R1.".format(R1, resistances[0]))
        if abs(R2 - resistances[1]) > 10:
            print("\nThe calculated value of R2 is {} Ohms, which is significantly different from the entered value of {} Ohms. Please check the resistor at R2.".format(R2, resistances[1]))
        if abs(R3 - resistances[2]) > 10:
            print("\nThe calculated value of R3 is {} Ohms, which is significantly different from the entered value of {} Ohms. Please check the resistor at R3.".format(R3, resistances[2]))



    
        
    
CalculateExpectedTPValues()


    
