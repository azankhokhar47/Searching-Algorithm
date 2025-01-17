# search_algorithms.py



def binary_search(arr, target):



    left, right = 0, len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:

            return mid

        elif arr[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return -1





def linear_search(arr, target):



    for index, value in enumerate(arr):

        if value == target:

            return index

    return -1





if __name__ == "__main__":

    print("Welcome to the Search Algorithms Program!")

    

    try:

        # Get the array from the user

        arr = list(map(int, input("Enter a sorted array of integers (space-separated): ").split()))

        

        # Get the target number to search for

        target = int(input("Enter the number to search for: "))

    except ValueError:

        print("Invalid input. Please enter integers only.")

        exit()



    # Perform Binary Search

    print("\nPerforming Binary Search...")

    binary_result = binary_search(arr, target)

    if binary_result != -1:

        print(f"Binary Search: Target found at index {binary_result}.")

    else:

        print("Binary Search: Target not found.")



    # Perform Linear Search

    print("\nPerforming Linear Search...")

    linear_result = linear_search(arr, target)

    if linear_result != -1:

        print(f"Linear Search: Target found at index {linear_result}.")

    else:

        print("Linear Search: Target not found.")



    # Display time complexity analysis

    print("\nTime Complexity:")

    print("- Binary Search: O(log n)")

    print("- Linear Search: O(n)")
