"""
Adjust the function 'equal_slices' from question_00 to return number of pieces left as well.

Examples:
    equal_slices(11, 5, 2) ➞ (True, 1)
    # 5 people x 2 slices each = 10 slices < 11 slices 

    equal_slices(11, 5, 3) ➞ (False,None)
    # 5 people x 3 slices each = 15 slices > 11 slicess

    equal_slices(8, 3, 2) ➞ (True, 2)

    equal_slices(8, 3, 3) ➞ (False, None)

    equal_slices(24, 12, 2) ➞ (True, 0)

Notes:
 - Return (True, total_slices) if there are zero people.
 - All parameters are integers.

"""
total_slices = int(input('Input Total number of slices :'))
no_recipients = int(input('Input Number of recipients :'))
slices_each = int(input('Input How many slices each person gets'))

no_recipients != 0

def equal_slices(total_slices, no_recipients, slices_each):
    math_total_slices = no_recipients * slices_each 
    if math_total_slices > total_slices:
        return (False, None)
    else:
        reminder_slices = total_slices % no_recipients
        return (True, reminder_slices)
        
print(equal_slices(total_slices, no_recipients, slices_each))