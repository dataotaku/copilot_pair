import unittest
from unittest.mock import patch
from syntax_error import main
from io import StringIO

class TestMainFunction(unittest.TestCase):

    @patch('builtins.open', unittest.mock.mock_open(read_data="Test file content"))
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        # Run the main function
        main()

        # Expected output
        expected_output = [
            "Alice is 25 years old",
            "Bob is 30 years old",
            "Charlie is 35 years old",
            "Total people:  3",
            "File content:  Test file content",
            "Lambda result:  15"
        ]

        # Split the output by lines and remove any trailing whitespace
        actual_output = mock_stdout.getvalue().strip().split('\n')
        actual_output = [line.strip() for line in actual_output]

        # Check if the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()