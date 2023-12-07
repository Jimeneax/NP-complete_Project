#!/bin/bash

# Run the approximation solution on different test cases

# Test Case 1: Small input
echo "Running Test Case 1: Small input"
python your_approximation_program.py input_small.txt

# Test Case 2: Medium input
echo "Running Test Case 2: Medium input"
python your_approximation_program.py input_medium.txt

# Test Case 3: Large input
echo "Running Test Case 3: Large input"
python your_approximation_program.py input_large.txt

# Test Case 4: High complexity input
echo "Running Test Case 4: High complexity input"
python your_approximation_program.py input_high_complexity.txt

# Test Case 5: Worst case for approximation (does not achieve optimal answer)
echo "Running Test Case 5: Worst case for approximation"
python your_approximation_program.py input_worst_case.txt

# Add more test cases as needed...

echo "All test cases completed."