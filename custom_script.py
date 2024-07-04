def custom_function(kwarg_1, kwarg_2):
    # Write your code here
    print(f"First argument: {kwarg_1}")
    print(f"Second argument: {kwarg_2}")

    # Return the output of the function as an object,
    # Matching the Output Args defined in the Form below
    return {
        "output_1": kwarg_1 + " + extra string",
        "output_2": kwarg_2 + 10
    }
