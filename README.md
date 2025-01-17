# Binary Search and Linear Search Implementation

## Overview
This repository contains the implementation of two essential search algorithms: **Binary Search** and **Linear Search**.  
These algorithms are fundamental in computer science and are widely used to locate elements in datasets of varying sizes and structures.

Through this project, we aim to:
- Understand the operational differences between the two algorithms.
- Analyze their performance under various scenarios, including best and worst cases.

---

## Getting Started
Follow these steps to execute the program:

1. **Clone the Repository**  
   Clone this repository to your local system using the following command:
   ```bash
   git clone https://github.com/azankhokhar47/Searching-Algorithm
   ```

2. **Navigate to the Directory**  
   Open a terminal and navigate to the project folder:
   ```bash
   cd Searching-Algorithm
   ```

3. **Run the Program**  
   Execute the program using Python:
   ```bash
   python search_algorithms.py
   ```

4. **Input Data**  
   - Enter a sorted list of integers when prompted.  
   - Provide the target number to be searched.

---

## How the Algorithms Work
### Binary Search
- **Logic:** Splits the search range into halves, progressively narrowing down to the target.  
- **Strength:** Efficient for sorted datasets due to its logarithmic time complexity.  
- **Worst Case:** Occurs when the algorithm has to reduce the range repeatedly without locating the target, resulting in **O(log n)** complexity.

### Linear Search
- **Logic:** Iterates through the dataset element by element until the target is found.  
- **Strength:** Works on unsorted datasets but is less efficient for large datasets.  
- **Worst Case:** When the target is the last element or missing entirely, resulting in **O(n)** complexity.

---

## Sample Output
Below is an example of the program's output:

```
Enter a sorted array of integers: 1 3 5 7 9
Enter the number to search for: 7

Binary Search: Target found at index 3.
Linear Search: Target found at index 3.

Time Complexity:
- Binary Search: O(log n)
- Linear Search: O(n)
```

---

## Key Features
- **Comprehensive Documentation:** Explains both algorithms and their practical implications.  
- **Interactive Input:** Prompts users for custom inputs.  
- **Edge Case Handling:** Includes checks for empty arrays and invalid inputs.  

---

## Learning Outcomes
This project enabled me to:
1. Dive deep into the mechanics of search algorithms.
2. Develop an appreciation for algorithm efficiency and time complexity.
3. Write clean, maintainable, and reusable code.

---

## Contributing
Contributions are welcome! To propose changes:
1. Fork this repository.
2. Create a new branch.
3. Submit a pull request with a description of your updates.
