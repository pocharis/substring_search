# Coding Test Solution
This is a program that takes a single command-line argument that species a file path which points to a file specifying some source text and a search term. Its job is to search the source text for matches of the search term, and output all the matches after striping unwanted spaces, characters or numbers.

## The following assumptions and considerations were made:

- The search term is always on the last line of the file, so if the last line is not the search term, the function will not work correctly.
- The solution may produce incorrect results if the search term contains special characters or regular expressions, as these can cause problems when matching as no cleaning was done on the search term.
- It handles situations where the input file is empty, by printing a message to indicate so
- The solution produces errors or unexpected results if the input file is very large and causes memory issues.
- .txt is the input file that the solution handles
- Instead of printing, the solution only creates a new file with the search results and overwrites its content if the search results file already exists.
- Only handles special characters and numbers in the input file, but it may not handle other types of special characters, such as accented characters or emojis.
- The solution assumes that the input file is a plain text file and does not handle other file formats such as binary files, images, pdf, mp3, compressed files, or encrypted files.
- The solution assumes that the output file can be created without any issues, but there may be permission or disk space issues that prevent the file from being created.
- In the solution, there is no way to customize the search criteria or the output format, so it may not be suitable for all use cases.

## Understanding the files

- The **search_app.py** file is the entry point for implementing the solution. It searches for where the *search term* occurs in the **source_input_file.txt**. Running the line of code below implements implement the solution. You can change the source input file to any of your choice.
    ```python
       python search_app.py source_input_file.txt 
    ```
- The **_search_results.txt_** file is used to store the formatted lines where the *search term* appeared.
- The **_test_input.txt_** file contains the source text and search term for testing purposes.
- Lastly, the **_test_search_result.py_** file is used to test, checking for the right output for each method contained in **_search_helper_functions.py_**. Run the test file below to test the methods.
  ```python
    python test_search_result.py
  ```