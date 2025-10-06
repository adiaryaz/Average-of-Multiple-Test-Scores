# Average of Multiple Test Scores

A program to calculate the average of a given number of test scores, with immediate validation for each input.

## 📝 Description

This Python program calculates the average of test scores for a specified number of subjects. First, it prompts the user to enter the total number of scores (n). If n is a positive number, the program then asks for each score one by one. Each score is validated to be within the range of 0-100. If at any point an invalid number is entered (either for n or for a score), the program stops immediately and displays an error message.

The core mathematical principle is the factorial, where the total is the result of n! (n being the number of times "RUN" was printed).

## 🎯 Problem Statement

**Input:** 
- The total number of scores to be entered (n), which must be a positive integer.
- n subsequent numbers, each representing a test score.

**Output:** 
- The average of the valid scores, displayed as a float.
- "NoProceed" if the initial number of scores (n) is not positive, or if any entered score is outside the valid range (0-100).

**Rules:**
- The number of subjects (n) must be greater than 0.
- Each test score must be between 0 and 100, inclusive.
- If any input is invalid, the program must terminate the process immediately.

## 💡 Examples

### Example 1
```
Input:
3
80
85
60

Output:
75.0
```
Explanation: All inputs are valid. The average of (80 + 85 + 60) / 3 is 75.0.

### Example 2
```
Input:
5
6
7
-3

Output:
NoProceed
```
Explanation: The third score, -3, is invalid. The program stops immediately.

### Example 3
```
Input:
2
90
101

Output:
NoProceed
```
Explanation: The second score, 101, is outside the 0-100 range. The program stops.

### Example 4
```
Input:
-10

Output:
NoProceed
```
Explanation: The number of subjects, -10, is not a positive number. The program stops.


## 🚀 How to Use

1. Clone this repository
```bash
git clone https://github.com/adiaryaz/average-test-scores.git
cd calculate-circle-area
```

2. Run the program (assuming the file is main.py):
```bash
python main.py
```

3. Follow the prompts to enter the number of scores and then each score.
