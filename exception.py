def process_number(numbers, divisor):  # Function define kiya numbers aur divisor ko process karne kay liye

    try:
        if (type(divisor) is not int and type(divisor) is not float):  # Check kar raha hai divisor number hai ya nahi
            raise Exception("Divisor must be a number")  # Agar nahi hai to exception throw kara hai
        for num in numbers:  # List mein har number ko process karne ke liye loop
            try:
                result = num / divisor  # Number ko divisor se divide kara hai
            except Exception as ex:  # Agar koi exception aayi to handle kar lega
                print(f"Can't Divide {num} by {divisor}, {ex}")  # Exception ka message print kara hai
            else:  # Agar koi exception nahi aayi
                print(f"{num}/{divisor}={result}")  # Result print

    except ZeroDivisionError:  # Agar divisor zero ho to ye run karega
        print("Can't divide by zero")  # Message print karega
    except Exception as ex:  # Agar koi aur error aayi
        print(ex)  # Error ka message print karega
    finally:  # Ye block hamesha chalega, chahe koi error ho ya na ho
        print()  # Completion ka message de raha hai


# Function ko call kar raha hai aur alag-alag cases test kar raha hai
process_number([10, 20, 30, 0, 50], 5)  # Divisor number hai, sab theek chalega
process_number([10, 20, 30, 0, 50], 0)  # Divisor zero hai, ZeroDivisionError handle karega
process_number([10, 20, 30, 0, 50], "0")  # Divisor string hai, custom exception handle karega
process_number([10, 20, "30", 0, 50], 5)  # List mein ek string hai, runtime error handle karega
