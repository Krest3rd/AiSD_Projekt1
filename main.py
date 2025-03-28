import sys

from Menu import Menu,AlgSelect


# Checks if the Python script is being run as the main program (not imported as a module)
if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--menu":
        Menu()
        print("Program ended sucessfully")
    elif len(sys.argv) == 3 and sys.argv[1] == "--algorithm":
        algorithm_number = int(sys.argv[2])

        # Read input data from standard input until the end of file (EOF)
        input=sys.stdin.read().split()
        try:
            data = [int(x) for x in input[1:]]
        except EOFError:
            print("Error reading input.")

        # Perform sorting using the specified algorithm (ignored in this example)
        sorted_data = AlgSelect(data, algorithm_number)

        # Print the sorted data
        print("Sorted data:", sorted_data[0:10])
    else:
        print("Usage: python script.py --algorithm <algorithm_number>\n   Or: python script.py --menu")
        sys.exit(1)
    