#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # Initialize an empty list to store the division results
    result_list = []

    try:
        for i in range(list_length):
            # Try to divide corresponding elements from my_list_1 and my_list_2
            result = my_list_1[i] / my_list_2[i]
            result_list.append(result)

    except ZeroDivisionError:
        # Handle division by zero
        print("division by 0")
        result_list.append(0)

    except (ValueError, TypeError):
        # Handle unexpected value or type errors
        print("wrong type")
        result_list.append(0)

    except IndexError:
        # Handle list index out of range
        print("out of range")

    finally:
        return result_list
