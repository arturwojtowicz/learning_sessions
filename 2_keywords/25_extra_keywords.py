# any, all

if any([1 == 2, 2 == 2, 3 == 2]): print("Success - Line 3")
if any([1 == 2, 3 == 2]): print("Success - Line 4")

if all([1 == 2, 2 == 2, 3 == 2]): print("Success - Line 6")
if all([2 == 2, 2 == 2, 2 == 2]): print("Success - Line 7")