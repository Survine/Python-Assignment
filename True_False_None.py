def check_variable(var):
    if var is True:
        print("The variable is True.")
    elif var is False:
        print("The variable is False.")
    elif var is None:
        print("The variable is None.")
    else:
        print("The variable is neither True, False, nor None.")

check_variable(True)
check_variable(False)
check_variable(None)
check_variable(42)