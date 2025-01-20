# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2

# Inputs
layers = 3
elapsed_bake_time = 30

# Functions
def calculate_bake_time_remaining(calculate_total_elapsed_time):
    """
    Calculate the remaining baking time.

    Args:
        elapsed_bake_time (int): The time already spent baking, in minutes.

    Returns:
        int: The remaining baking time in minutes.
    """
    return EXPECTED_BAKE_TIME - calculate_total_elapsed_time(layers, elapsed_bake_time)

def calculate_preparation_time(layers):
    """
    Calculate the total preparation time based on the number of layers.

    Args:
        layers (int): The number of lasagna layers.

    Returns:
        int: The total preparation time in minutes.
    """
    return layers * PREPARATION_TIME_PER_LAYER

def calculate_total_elapsed_time(layers, elapsed_bake_time):
    """
    Calculate the total elapsed time, including preparation and baking.

    Args:
        layers (int): The number of lasagna layers.
        elapsed_bake_time (int): The time already spent baking in minutes.

    Returns:
        int: The total elapsed time in minutes.
    """
    return calculate_preparation_time(layers) + elapsed_bake_time

# Calculations
preparation_time = calculate_preparation_time(layers)
total_elapsed_time = calculate_total_elapsed_time(layers, elapsed_bake_time)
bake_time_remaining = calculate_bake_time_remaining(calculate_total_elapsed_time)

# Outputs
print(f"Preparation time: {preparation_time} minutes")
print(f"Total elapsed time: {total_elapsed_time} minutes")
print(f"Remaining bake time: {bake_time_remaining} minutes")
