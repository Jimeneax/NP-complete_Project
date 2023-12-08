#!/bin/bash

# Function to extract wall clock time from time command output
get_wall_clock_time() {
  awk '/real/ {print $2}'
}

# Run the approximation solution on different test cases

# Test Case 1: Small input
echo "Running Test Case 1: Small input"
{ time python cs412_tsp_approx.py < test1/test1Input.txt; } 2>&1 | get_wall_clock_time | tee -a test1/test1Output.txt

# Test Case 2: Medium input
echo "Running Test Case 2: Medium input"
{ time python cs412_tsp_approx.py < test2/test2Input.txt; } 2>&1 | get_wall_clock_time | tee -a test2/test2Output.txt

# Test Case 3: Large input
echo "Running Test Case 3: Large input"
{ time python cs412_tsp_approx.py < test3/test3Input.txt; } 2>&1 | get_wall_clock_time | tee -a test3/test3Output.txt

# Test Case 4: High complexity input
echo "Running Test Case 4: High complexity input"
{ time python cs412_tsp_approx.py < test4/test4Input.txt; } 2>&1 | get_wall_clock_time | tee -a test4/test4Output.txt

# Test Case 5: Worst case for approximation (does not achieve optimal answer)
echo "Running Test Case 5: Worst case for approximation"
{ time python cs412_tsp_approx.py < test5/test5Input.txt; } 2>&1 | get_wall_clock_time | tee -a test5/test5Output.txt

# Add more test cases as needed...

echo "All test cases completed."