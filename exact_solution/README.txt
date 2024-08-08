=================================
| How to run our exact solution |
=================================

1. Navigate to the exact_solution directory
   
   cd np-project/exact_solution
   


2. Generate test cases

   bash gen_test_cases.sh 26 7

   The first parameter is the number of vertices we want in our graph, we used 26
   The second parameter is for incrementing the edge percentage chance, we used 7 (same as 7%)



3. Run test cases

   bash run_test_cases.sh 26 7



4. Check your output

    The times to run each test can be found in the current directory
    exact_solution/times.txt

    The solutions to each test case can be found within the test_cases directory
    test_cases/expectedOutput.txt

    The final test case runs over 20 minutes