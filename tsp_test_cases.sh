#!/bin/bash

# Assuming your exact solution program is named exact_solution_program.py
PROGRAM="./tsp.py"
TEST_CASES_DIR="./tsp_exact_solution"

# Run the approximation solution on different test cases
for test_case_dir in "$TEST_CASES_DIR"/test*; do
    if [ -d "$test_case_dir" ]; then
        echo "Running test case in $test_case_dir"
        
        test_case_number=$(basename "$test_case_dir" | sed 's/test//')
        input_file="$test_case_dir/test${test_case_number}Input"
        output_file="$test_case_dir/test${test_case_number}Output"
        expected_file="$test_case_dir/test${test_case_number}Expected"
        
        # Run your exact solution program with the input file
        $PROGRAM "$input_file" > "$output_file"
        
        # Compare the actual output with the expected output
        diff "$output_file" "$expected_file"
        
        # You may want to include additional logic based on the exit status of diff
        # to handle cases where there are differences between actual and expected outputs.
    fi
done

echo "All test cases completed."







# # Test Case 1: Small input
# echo "Running Test Case 1: Small input"
# python tsp.py test1Input.txt > test1Output.txt
# # Compare actual output to expected output
# diff test1Output.txt test1Expected.txt

# # Test Case 2: Medium input
# echo "Running Test Case 2: Medium input"
# python tsp.py test2Input.txt > test2Output.txt
# # Compare actual output to expected output
# diff test2Output.txt test2Expected.txt

# # Test Case 3: Large input
# echo "Running Test Case 3: Large input"
# python tsp.py test3Input.txt > test3Output.txt
# # Compare actual output to expected output
# diff test3Output.txt test3Expected.txt

# # Test Case 4: High complexity input
# echo "Running Test Case 4: High complexity input"
# python tsp.py test4Input.txt > test4Output.txt
# # Compare actual output to expected output
# diff test4Output.txt test1Expected.txt

# # Test Case 5: Worst case for approximation (does not achieve optimal answer)
# echo "Running Test Case 5: Worst case for approximation"
# python tsp.py test5Input.txt > test5Output.txt
# # Compare actual output to expected output
# diff test5Output.txt test5Expected.txt

# # Add more test cases as needed...

# echo "All test cases completed."
