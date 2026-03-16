import random
import time

class Searcher:
    
    start_time = time.perf_counter() # Time the search started

    def binary_search(self, arr, num):
        
        low = 0
        high = len(arr) - 1
        
        while low <= high:

            mid = low + (high - low)//2

            if arr[mid] == num:
                return mid
            
            elif arr[mid] < num:
                low = mid + 1

            else:
                high = mid - 1
        return -1 
    end_time = time.perf_counter() # Time when the search finished
    
    def createArray(self, num):
        array = []
        for i in range(num):
            array.append((random.randint(1, 100000))) # Create an array with random integers ranging from 1 - 1000
        return sorted(array) # Binary search only works on sorted arrays

def main():       
    b1 = Searcher()

    size = int(input("How many numbers do you want inside the array?: "))
    array = b1.createArray(size)    

    print(f"{array}")

    x = int(input("What number do you want to search for?: "))
    
    result = b1.binary_search(array, x)

    if result != -1:
        print(f"Element is present at index:  {result}")
    else:
        print("Element is not present in array")
    print(f"The time it took to complete was {b1.end_time - b1.start_time:.2f} seconds")
    

if __name__ == "__main__":
    main()


