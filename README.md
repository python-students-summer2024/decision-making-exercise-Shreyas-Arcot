[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15215717&assignment_repo_type=AssignmentRepo)
# Decision-Making Practice

A few boolean expression puzzles to solve. The given code in [solutions.py](./solutions.py) contains several incomplete functions that you must complete to achieve the desired behavior. That is all you must do.

To run the program, run the file named [main.py](./main.py).

## Clone this repository

First, clone this repository to your local computer, using Visual Studio Code's cloning feature.

Helpful video:

- [cloning a code repository from GitHub to your local machine](https://www.youtube.com/watch?v=axcny0o1NYo).

## Set up Visual Studio Code

Once cloned, set Visual Studio Code to be suitable for Python development using the "command palette":

- set the interpreter to a Python 3.x interpreter, such as that by [`Anaconda`](https://www.anaconda.com/).
- set the linter to by `pylint`.
- set the test framework to be `pytest`.

Helpful video:

- [Setting up Visual Studio Code for Python development](https://www.youtube.com/watch?v=xsXMzyK1M4I)

## Modify the code

The file named `solutions.py` contains several functions that must be completed in order for the program to work. Each function contains a description of what it should do.

The only modifications you must make in order to complete this assignment are to these functions definitions in this one file. Do not modify any code outside of these function definitions.

### Run the program

To run any of the problem files in an project, run them directly from the **Run and Debug** panel within Visual Studio Code. When you first open this panel, it will offer an option to "`Create a launch.json file`". Click that option, it may ask what type of file you intend to run - if so, select regular `Python file`. Then, immediately close down the `launch.json` file that pops open, since it is a settings file for Visual Studio Code that we do not need to change.

To run the currently open Python code file, click the green "play" button towards the top of the panel. Note that for some projects, the instructions indicate a specific file to run directly that will in turn execute the code in the other files.

### Verify that the tests pass

Pytest-based tests are included in the `tests` directory that will help you determine whether each function is operating as expected. If the code has been completed correctly, all tests should pass. If not, they will fail. You should not modify any files in the `tests` directory and you should never run the test files directly.

**To run the tests**, open the **Tests** panel in Visual Studio Code and click the _Run All Tests_ button, usually represented as a "play" button icon. This will run all the tests in all the files in the `tests` directory. There are also run buttons next to each individual test that can be clicked to run specific tests. Running the tests will show which tests pass and which fail. Passing tests are generally shown with a green checkmark icon, while failing tests are shown with a red cross icon.

**If the tests pass**, this means that your code is generally correct. These automated tests cannot check the correctness of all features of your code, so you should always verify that the behavior of your program matches the requirements by running the code and trying it yourself manually.

**If the tests fail**, this means there are errors/mistakes in your solution. For those tests that fail, clicking on the test will show an _AssertionError_ message that may be helpful identifying where the error is in your code.

**If the tests never load**, most likely there are major errors in your code that prevent it from working. The tests will not work if your code does not run, so always try running your code first. You can find out why the tests don’t load by opening Visual Studio Code’s **Terminal** panel and running the command `pytest --collect-only` (If your computer says the command, `pytest` is not found, try `python -m pytest --collect-only` instead). This will show error messages explaining why the tests did not load correctly.

- If the command above doesn't show any erorrs yet the editor still doesn't load the tests, you can run the tests entirely from the **Terminal** with the `pytest` command.
- If the command above doesn't show any error and the tests still don't load you can also try to delete any directories in the project named `__pycache__`, `.pytest_cache` and `tests/__pycache__`, close down your code editor window, open it again, and try running the tests again. If that still fails, try running the tests from the **Terminal** with the `pytest` command as indicated above.
- If error messages that show up when running the `pytest --collect-only` command indicate an error in your code files, fix those errors and try to load the tests again. A common error is, "`reading from stdin while output is captured!`" - this is always due to incorrect indentation of your code, where code that is meant to be nested within a function is, in fact, not indented beneath the function definition line and thus not considered by Python to be part of that functino.

**If, for whatever reason, you are not able to get the tests to load**, this should not stop you from completing the work. Carry on and make sure your programs perform as expected the “old fashioned way” - verify they behave correctly yourself by running them and trying them out. In most cases, the instructions are clear and following them exactly will result in a correct program.

## Submit your work

Each student must submit this assignment individually. Use Visual Studio Code to perform git `stage`, `commit` and `push` actions to submit. These actions are all available as menu items in Visual Studio Code's Source Control panel.

1. Type a short note about what you have done to the files in the `Message` area, and then type `Command-Enter` (Mac) or `Control-Enter` (Windows) to perform git `stage` and `commit` actions.
1. Click the `...` icon next to the words, "Source Control" and select "Push" to perform the git `push` action. This will upload your work to your repository on GitHub.com.

![Pushing work in Visual Studio Code](./images/vscode_stage_commit_push.png)
