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
    if valid:
        resistances = ResistanceCheck()
        R1, R2, R3 = resistances
        I = voltage / (R1 + R2 + R3)
        TP1 = I * (R1 + R2)
        TP2 = I * R3
        print("\nExpected Test Point Values (Note: there may be a small margin of error):")
        print("TP1: {} V".format(TP1))
        print("TP2: {} V".format(TP2))



    
        
    
CalculateExpectedTPValues()    
