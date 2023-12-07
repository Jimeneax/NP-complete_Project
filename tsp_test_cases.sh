#!/bin/bash

Run the approximation solution on different test cases
Test Case 1: Small input
echo "Running Test Case 1: Small input"
python cs412_tsp_exact.py < test1/test1Input.txt > test1/test1Output.txt

Test Case 2: Medium input
echo "Running Test Case 2: Medium input"
python cs412_tsp_exact.py < test2/test2Input.txt > test2/test2Output.txt

Test Case 3: Large input
echo "Running Test Case 3: Large input"
python cs412_tsp_exact.py < test3/test3Input.txt > test3/test3Output.txt

Test Case 4: High complexity input
echo "Running Test Case 4: High complexity input"
python cs412_tsp_exact.py < test4/test4Input.txt > test4/test4Output.txt

Test Case 5: Worst case for approximation (does not achieve optimal answer)
echo "Running Test Case 5: Worst case for approximation"
python cs412_tsp_exact.py < test5/test5Input.txt > test5/test5Output.txt

Add more test cases as needed...
echo "All test cases completed."