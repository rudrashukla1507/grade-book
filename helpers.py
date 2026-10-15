def get_number(prompt):
    while True:
        try:
            return(int(input(prompt)))
        except ValueError:
            print("Please Enter a valid number!")