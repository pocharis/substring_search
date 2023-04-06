import re
import os

class SearchFile:
    """
    A class for searching a file for a given term and formatting the matching lines.

    Args:
    - file_path (str): the path to the input file

    Methods:
    - read_file: read the input file and return its lines
    - get_search_term: extract the search term from the input file's last line
    - clean_line: format a line that contains the search term by removing special characters and numbers
    - match_search_term: find all the lines that contain the search term and format them
    - write_matches_to_file: write the formatted matching lines to an output file
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        """
        Read the input file and return its lines.

        Returns:
        - a list of strings, where each string is a line in the input file
        """
        try:
            if os.stat(self.file_path).st_size == 0 or not self.file_path.endswith('.txt'):
                print(f"Error: The File '{self.file_path}' is empty or not a txt file")
                return []
            else:
                with open(self.file_path, "r") as f:
                    lines = f.readlines()
                return lines
        except FileNotFoundError:
            print(f"Error: The File '{self.file_path}' is not found.")
            return []
        except Exception as e:
            print(f"Error: {e}")
            return []

    def get_search_term(self, lines):
        """
        Extract the search term from the input file's last line.

        Args:
        - lines (list of str): the lines in the input file

        Returns:
        - str, the search term
        """
        if len(lines) == 0:
            return None
        else:
            return lines[-1].strip()

    def clean_line(self, line):
        """
        Format a line that contains the search term by removing special characters and numbers.

        Args:
        - line (str): a line in the input file that contains the search term

        Returns:
        - str, the formatted line
        """
        return re.sub(r"([^a-zA-Z\s]+ ?)", " ", line).strip()
            

    def match_search_term(self, search_term, lines):
        """
        Find all the lines that contain the search term and format them.

        Args:
        - search_term (str): the search term
        - lines (list of str): the lines in the input file

        Returns:
        - a list of strings, where each string is a formatted line that contains the search term
        """
        matches = []
        for line in lines[:-1]:
            if search_term.lower() in line.lower():
                matches.append(self.clean_line(line).strip())
        return matches

    def write_matches_to_file(self, matches, output_file_path):
        """
        Write the formatted matching lines to an output file.

        Args:
        - matches (list of str): the formatted lines that contain the search term
        - output_file_path (str): the path to the output file
        """
        try:
            with open(output_file_path, "w") as f:
                if len(matches) > 0:
                    for i, match in enumerate(matches):
                        if i == len(matches) - 1:
                            f.write(f"[{match.strip()}]")
                        else:
                            f.write(f"[{match.strip()}]\n")
                    print('Search results written to search_results.txt file')
                else:
                    print('No matches found')

        except Exception as e:
            print(f"Error: {e}")