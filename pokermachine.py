import random
from collections import Counter



def main():
    money = 100
    symbols = ["🍒", "🍌", "⭐", "🪙", "🍀", "💎", "7️⃣" ]
    weights = [30, 30, 15, 12, 8, 4, 1]
    
    print("--- Welcome to the Python Slots ---")
    print(f"Your starting balance is ${money}")
    
    while money > 0:  
    
        bet_input = input("Bet Amount (Please enter 1 or a multiple of 5 or q to Quit): ").lower()
        
        if bet_input == "q":
            break
        
        if not bet_input.isdigit():
            print("Invalid input, enter a number or q")
            continue
        
        bet = int(bet_input)
        
        if not bet == 1 and not bet % 5 == 0:
            print("Enter 1 or a multiple of 5!")
            continue
        
        if bet > money:
            print(f"You only have ${money} left!")
            continue
        
        money -= bet
        
        spinresult = random.choices(symbols, weights=weights, k=3)
        
        print(" | ".join(spinresult))
        
        count = Counter(spinresult)

        if any(symbol == 3 for symbol in count.values()):
            if count["🍒"] == 3 or count["🍌"] == 3:
                win_amount = bet * 3
            elif count["⭐"] == 3:
                win_amount = bet * 5
            elif count["🪙"] == 3:
                win_amount = bet * 20
            elif count["🍀"] == 3:
                win_amount = bet * 50
            elif count["💎"] == 3:
                win_amount = bet * 100
            elif count["7️⃣"] == 3:
                win_amount = bet * 1000
            
            money += win_amount
            print(f"JACKPOT! You won ${win_amount}!")
            print(f"Balance: ${money}")
        else:
            print("No match. Try again!")
            print(f"Balance: ${money}")
            continue
    
    print(f"Thanks for playing! Final balance: ${money}")

if __name__ == "__main__":
    main()