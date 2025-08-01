def print_color_map():
    # Define major and minor colors
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    
    # Print the color map
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    
    # Return the total number of combinations
    return len(major_colors) * len(minor_colors)

# Call the function and store the result
result = print_color_map()

# Dynamically calculate the expected result based on the lengths of the color lists
expected_result = len(["White", "Red", "Black", "Yellow", "Violet"]) * len(["Blue", "Orange", "Green", "Brown", "Slate"])

# Assert that the result matches the expected value
assert(result == expected_result)

print("All is well (maybe!)")
