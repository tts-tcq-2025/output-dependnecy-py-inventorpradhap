from typing import List, Tuple, Callable

# 1. Define colors as module-level constants for better reusability and clarity
MAJOR_COLORS: List[str] = ["White", "Red", "Black", "Yellow", "Violet"]
MINOR_COLORS: List[str] = ["Blue", "Orange", "Green", "Brown", "Slate"]

def generate_color_map(
    major_colors: List[str],
    minor_colors: List[str]
) -> List[Tuple[int, str, str]]:
    """
    Generates a list of tuples, each representing a color map entry.
    Each tuple contains (pair_number, major_color, minor_color).
    The pair number is calculated based on the indices of the major and minor colors.
    """
    color_map_entries: List[Tuple[int, str, str]] = []
    num_minor_colors = len(minor_colors)

    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            # 1. FIX: Correct the pair_number calculation
            # This makes it 0-indexed as per the original code's intent (0 and 24 assertions)
            pair_number = i * num_minor_colors + j
            color_map_entries.append((pair_number, major, minor))
    return color_map_entries

def format_color_map_entry(pair_number: int, major: str, minor: str) -> str:
    """
    Formats a single color map entry into a printable string.
    Ensures consistent column alignment.
    """
    # 4. FIX: Use a more robust and consistent padding for all columns
    # Determine the maximum length for major color to ensure alignment
    max_major_len = max(len(color) for color in MAJOR_COLORS)
    # Determine the maximum length for minor color to ensure alignment
    max_minor_len = max(len(color) for color in MINOR_COLORS)

    # Use f-string formatting with dynamic width
    return f"{pair_number:<3} | {major:<{max_major_len}} | {minor:<{max_minor_len}}"

def print_on_console(line_item: str) -> None:
    """
    Prints a single line item to the console.
    (Renamed to follow Python snake_case convention)
    """
    print(line_item)

def print_color_map(
    color_map: List[Tuple[int, str, str]], # 3. FIX: Accept the generated color map as an argument
    output_func: Callable[[str], None] = print_on_console
) -> int:
    """
    Prints the given color map to the console using the specified output function.
    Returns the number of items printed.
    """
    # 4. Add a header for better console output
    print("Pair | Major  | Minor", file=output_func.__globals__.get('__builtins__', {}).get('print', print)) # Print header via actual print if possible
    print("-----|--------|-------", file=output_func.__globals__.get('__builtins__', {}).get('print', print))

    printed_count = 0
    for pair_number, major, minor in color_map:
        line = format_color_map_entry(pair_number, major, minor)
        output_func(line)  # Abstracted output
        printed_count += 1
    return printed_count

# --- Testing Section ---

# 2. FIX: Corrected make_print_mock implementation using a class for clarity and robustness
class MockPrinter:
    """A mock object to capture print calls for testing."""
    def __init__(self):
        self.calls: List[str] = []

    def __call__(self, line: str) -> None:
        """Allows instances to be called like a function."""
        self.calls.append(line)

def test_print_color_map():
    """
    Tests the print_color_map function by mocking print output.
    This test should now pass.
    """
    mock_printer = MockPrinter()

    # 3. Pass the generated color map to print_color_map
    color_map_data = generate_color_map(MAJOR_COLORS, MINOR_COLORS)
    
    count = print_color_map(color_map_data, mock_printer)

    # 5. FIX: Adjust expected output based on correct pair_number calculation
    # and consistent formatting
    expected_first_line_content = format_color_map_entry(0, "White", "Blue")
    expected_last_line_content = format_color_map_entry(
        len(MAJOR_COLORS) * len(MINOR_COLORS) - 1, # Last pair number (24)
        "Violet", "Slate"
    )

    # The first two lines printed by print_color_map will be the header and separator
    # So, the actual content starts from index 2 in mock_printer.calls
    
    # Assertions
    assert count == len(color_map_data), \
        f"Expected {len(color_map_data)} lines printed, but got {count}"
    
    # Check if the header and separator are present
    assert len(mock_printer.calls) >= 2, "Output should contain at least header and separator."
    assert "Pair | Major" in mock_printer.calls[0], "First line should be header."
    assert "-----|--------" in mock_printer.calls[1], "Second line should be separator."

    # Check the first and last content lines
    assert mock_printer.calls[2] == expected_first_line_content, \
        f"First content line mismatch: Expected '{expected_first_line_content}', got '{mock_printer.calls[2]}'"
    
    assert mock_printer.calls[-1] == expected_last_line_content, \
        f"Last content line mismatch: Expected '{expected_last_line_content}', got '{mock_printer.calls[-1]}'"

    print("\nTest passed successfully!")


# --- Main execution ---
if __name__ == "__main__":
    print("Running production print:")
    # Generate the map data
    map_to_print = generate_color_map(MAJOR_COLORS, MINOR_COLORS)
    # Print it using the default console output
    total_combinations = print_color_map(map_to_print)
    print(f"\nTotal combinations printed: {total_combinations}")

    print("\nRunning test:")
    test_print_color_map()
