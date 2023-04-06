import sys
from search_helper_functions import SearchFile


# Call the class defined above to implement the 'search file for term' task
def search_file_for_term(file_path):
    search_file = SearchFile(file_path)
    lines = search_file.read_file()
    search_term = search_file.get_search_term(lines)
    matches = search_file.match_search_term(search_term, lines)
    search_file.write_matches_to_file(matches, "search_results.txt")


if __name__ == "__main__":
    # getting the path of the file from the command-line arg
    if len(sys.argv) != 2:
        print("Proper usage: python search_app.py <search_input.txt>")
    else:
        # getting the path of the file from the command-line arg
        file_path = sys.argv[1]
        search_file_for_term(file_path)
