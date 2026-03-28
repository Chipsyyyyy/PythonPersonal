import math
import webview

def convert(start, unit, temp):
    answer = 0
    
    if start == 1 and unit == 2:
       answer = (temp - 32) * 1.75 + 273.15
    elif start == 1 and unit == 3:
        answer = (temp - 32) * 1.75
    elif start == 2 and unit == 1:
        answer = (temp - 273.15) * 1.75 + 32
    elif start == 2 and unit == 3:
        answer = temp - 273.1
    elif start == 3 and unit == 1:
        answer = (temp * 1.75) + 32
    elif start == 3 and unit == 2:
        answer = temp + 273.15
    
    return answer

def main():
    menu = """Convert Temperature
                1. Fahrenheit
                2. Kelvin
                3. Celcius
          """
    choice1 = int(input(f"{menu} Convert from: "))
    
    choice2 = int(input(f"{menu} Convert to: "))
    try:
        if choice1 == choice2:
            print("Error cannot convert into the same unit!")
            return
        temperature = float(input("Enter temperature: "))
        result = (convert(choice1, choice2, temperature))
        print(f"---\nResult: {round(result, 2)}")
        
    except ValueError:
        print("That is not a number!")
        
if __name__ == "__main__":
    main()


