def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    print("Welcome to the Celsius to Fahrenheit converter!")
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32

    print(f"{celsius:.2f} degrees Celsius is converted to {fahrenheit:.2f} degrees Fahrenheit.")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
