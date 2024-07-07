import pytest
from io import StringIO
from unittest.mock import patch
from syntax_error import MyClass, main
from unittest.mock import patch, mock_open

# Test for MyClass.print_info method
def test_print_info(capsys):
    person = MyClass("Alice", 25)
    person.print_info()
    captured = capsys.readouterr()
    assert captured.out == "Name: Alice, Age: 25\n"

# Test for main function
@patch('builtins.open', new=mock_open(read_data="Test file content"))
def test_main(capsys, monkeypatch):
    # Mocking input for file content
    monkeypatch.setattr('builtins.open', mock_open(read_data="Test file content"))

    main()  # Call the main function

    captured = capsys.readouterr()
    expected_output = (
        "Name: Alice, Age: 25\n"
        "Name: Bob, Age: 30\n"
        "Name: Charlie, Age: 35\n"
        "Total people:  3\n"
        "File content:  Test file content\n"
        "Lambda result:  15\n"
    )
    assert captured.out == expected_output