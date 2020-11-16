# celo_ui_test
This is a repository created to write UI tests for celo staging environment

These tests are automated using elenium webdriver with python and have used pytest framework. 

Technologies used:

1. Python 3.8
2. Selenium WebDriver Python Language binding
3. PyTest - test framework
4. Pytest - html report
5. Pytest-xsld for parallel execution
6. Pycharm IDE

The tests can be run on Chrome and Edge browsers.

# Test_Execution

To execute the tests , go to. your command line and use the following command:

$ pytest Tests -v -n 5 --html=./celo_tests.html 

(The command is running the tests in 5 sessions parallely and gives a html report stored as celo_tests)




