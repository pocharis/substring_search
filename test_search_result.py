import unittest
import os
from search_helper_functions import SearchFile


class TestMyFunctions(unittest.TestCase):
    def test_read_file(self):
        # Test reading a file that exists
        expected_output = [
            '"Alice was beginning...\n',
            "to_get9_!very\n",
            "1111tired1111of1111sitting1111\n",
            "on9the bank,\n",
            'and""of""having\n',
            "nothing to do!!!\n",
            "by her_sister\n",
            '908^)-234 923this-09her-++-23is./<.";][}"another-=&^5.\n',
            "er",
        ]
        search_file = SearchFile("test_input.txt")
        lines = search_file.read_file()
        self.assertEqual(lines, expected_output)

        # Test reading a file that doesn't exist
        search_file = SearchFile("nonexistent_file.txt")
        lines = search_file.read_file()
        self.assertEqual(lines, [])

    def test_get_search_term(self):
        # Test getting the search term from a list of lines
        search_file = SearchFile("test_input.txt")
        lines = search_file.read_file()
        search_term = search_file.get_search_term(lines)
        self.assertEqual(search_term, "er")

        # Test getting the search term from an empty list
        self.assertIsNone(search_file.get_search_term([]))

    def test_clean_line(self):
        # Test cleaning a line with special characters and numbers
        line = '908^)-234 923this-09her-++-23is./<.";][}"another-=&^5.'
        search_file = SearchFile("test_input.txt")
    
        self.assertEqual(
            search_file.clean_line(line), "this her is another"
        )

        # Test cleaning a line with no special characters or numbers
        line = "characters or numbers\n"
        self.assertEqual(search_file.clean_line(line), line.strip())

    def test_match_search_term(self):
        # Test matching a search term to lines that contain it
        search_file = SearchFile("test_input.txt")
        lines = search_file.read_file()
        search_term = search_file.get_search_term(lines)
        expected_output = ['to get very','by her sister','this her is another']
        self.assertEqual(search_file.match_search_term(search_term, lines), expected_output)

        # Test matching a search term to lines that don't contain it
        search_term = "nonexistent"
        expected_output = []
        self.assertEqual(search_file.match_search_term(search_term, lines), expected_output)

    def test_write_matches_to_file(self):
        # Test writing matches to a file
        search_file = SearchFile("test_input.txt")

        matches = ['to get very','by her sister','this her is another']
        output_file_path = "search_results.txt"
        search_file.write_matches_to_file(matches, output_file_path)
        with open(output_file_path, "r") as f:
            output_contents = f.read()
        expected_output = "[to get very]\n[by her sister]\n[this her is another]"
        self.assertEqual(output_contents.strip(), expected_output)

        # Clean up the test output file
        os.remove(output_file_path)


if __name__ == "__main__":
    unittest.main()
