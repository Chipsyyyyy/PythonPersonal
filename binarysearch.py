class BinarySearchTree:
    
    def search(self, arr, num):
        low = 0
        high = len(arr) - 1
        
        while low <= high:

            mid = low + (high - low)//2

            if arr[mid] == num:
                return num
            
            elif arr[mid] < num:
                low = mid + 1

            else:
                high = mid - 1

        return -1 
    

def main():   
    array = [1, 2, 5, 8, 10, 15, 24]
    x = 1
    b1 = BinarySearchTree()
    result = b1.search(array, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
    

if __name__ == "__main__":
    main()


