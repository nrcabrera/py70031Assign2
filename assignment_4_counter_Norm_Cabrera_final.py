"""
Author: Norm Cabrera
Assignment 4: Number Counter
"""

# Incremental/Decremental counter functions

def band(start, end, step):

    # Validates start, end and step number if procedure will yield a result
    if start < end and step < 0:
        return print("Infinite loop. Start value less than end number with a decremental step value.")
    else:
        while start <= end:
            yield start
            start += step

def band_neg(start, end, step):

    # Validates start, end and step number if procedure will yield a result
    if start > end and step > 0:
        return print("Infinite loop. Start value is greater than end number with a incremental step value.")
    else:
        while end <= start:
            yield start
            start += step

def main():

    # Validate user entry for start value with 0 as default if no value given.
    # User re-prompted if value is not numeric
    print("Hello!")
    while True:
          user_start_value = input("Enter start value (Press Enter for 0): ")
          if user_start_value == "":
              valid_start_value = 0
              break
          try:
              int(user_start_value)
          except ValueError:
              print("Please enter START value as number or press Enter for 0. ")
          else:
               valid_start_value = int(user_start_value)
               break

    # Validate user entry for end value.
    # User re-prompted if value is not numeric
    while True:
          user_end_value = input("Enter end value: ")
          if user_end_value.isdigit() == False:
              print("Please enter END value as number.")
          else:
               valid_end_value = int(user_end_value)
               break

    # Validate user entry for step value with 1 as default if no value entered
    # User re-prompted if value is not numeric
    while True:
          user_step_value = input("Enter step value (Default:1): ")
          if user_step_value == "":
               valid_step_value = 1
               break
          try:
               int(user_step_value)
          except ValueError:
               print("Please enter END value as number or press Enter for 0. ")
          else:
               valid_step_value = int(user_step_value)
               break

    # Counter function applied depends on end and start value
    if valid_end_value > valid_start_value:
          for each_element in band(valid_start_value, valid_end_value, valid_step_value):
               print(each_element, end=' ')
    else:
          for each_element in band_neg(valid_start_value, valid_end_value, valid_step_value):
               print(each_element, end=' ')
main()
