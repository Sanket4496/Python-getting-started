# How To Run Your Code in VS Code
1. To run the Python script you have open on the editor, select the Run Python File in Terminal play button in the top-right of the editor
2. Select one or more lines, then press Shift+Enter or right-click and select Run Selection/Line in Python Terminal. This command is convenient for testing just a part of a file.
3. From the Command Palette (Shift + ctrl/command + P), select the Python: Start REPL command to open a REPL terminal for the currently selected Python interpreter. In the REPL, you can then enter and run lines of code one at a time.

# How to Debug 
The debugger is a helpful tool that allows you to inspect the flow of your code execution and more easily identify errors, as well as explore how your variables and data change as your program is run. You can start debugging by setting a breakpoint in your Python project by clicking in the gutter next to the line you wish to inspect.

- To start debugging, initialize the debugger by pressing F5. Since this is your first time debugging this file, a configuration menu will open allowing you to select the type of application you want to debug. If it's a Python script, you can select Python File.

- Once your program reaches the breakpoint, it will stop and allow you to track data in the Python Debug console, and progress through your program using the debug toolbar.

# How To Test
The Python extension provides robust testing support for [Unittest](https://docs.python.org/3.3/library/unittest.html) and [pytest](https://pytest.org/en/7.4.x/).

You can configure Python tests through the Testing view on the Activity Bar by selecting Configure Python Tests and selecting your test framework of choice.

You can also create tests for your Python project, which the Python extension will attempt to discover once your framework of choice is configured. The Python extension also allows you to run and debug your tests in the Testing view and inspect the test run output in the Test Results panel.

Ref: [VSCode](https://code.visualstudio.com/docs/python/python-quick-start)