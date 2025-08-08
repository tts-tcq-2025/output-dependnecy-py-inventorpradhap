from typing import List, Tuple

# Constants for better readability and maintainability
MAJOR_COLORS: List[str] = ["White", "Red", "Black", "Yellow", "Violet"]
MINOR_COLORS: List[str] = ["Blue", "Orange", "Green", "Brown", "Slate"]

def generate_color_map_entries(
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
            pair_number = i * num_minor_colors + j + 1 # +1 to make it 1-indexed for user
            color_map_entries.append((pair_number, major, minor))
    return color_map_entries

def print_color_map(
    color_map_entries: List[Tuple[int, str, str]]
) -> None:
    """
    Prints the color map entries to the console in a formatted way.
    """
    print("Pair Number | Major Color | Minor Color")
    print("-------------------------------------")
    for pair_number, major, minor in color_map_entries:
        print(f'{pair_number: <11} | {major: <11} | {minor}')

def get_total_combinations(major_colors: List[str], minor_colors: List[str]) -> int:
    """
    Calculates the total number of unique color combinations.
    """
    return len(major_colors) * len(minor_colors)

def main():
    """
    Main function to orchestrate the color map generation and printing.
    """
    print("Generating and printing color map...")

    # Generate the color map entries
    color_map_entries = generate_color_map_entries(MAJOR_COLORS, MINOR_COLORS)

    # Print the color map
    print_color_map(color_map_entries)

    # Calculate and verify the total number of combinations
    total_combinations = get_total_combinations(MAJOR_COLORS, MINOR_COLORS)
    
    # The original code's pairing started at 0. If you intend for the
    # pairing to be 1-indexed (which is often more user-friendly for "pair numbers"),
    # then the max_pair_number should match the total combinations.
    # If the original 0-indexed was strictly intended, change the `+ 1` in `generate_color_map_entries`.
    expected_max_pair_number = total_combinations
    
    # Assert that the number of entries generated matches the total combinations
    assert len(color_map_entries) == total_combinations, \
        f"Mismatch: Expected {total_combinations} entries, got {len(color_map_entries)}"
    
    # Optional: Verify the last pair number generated (if 1-indexed)
    if color_map_entries:
        last_pair_number = color_map_entries[-1][0]
        assert last_pair_number == expected_max_pair_number, \
            f"Mismatch: Last pair number is {last_pair_number}, expected {expected_max_pair_number}"


    print(f"\nTotal number of combinations: {total_combinations}")
    print("Color map generation and verification complete!")

if __name__ == "__main__":
    main()
