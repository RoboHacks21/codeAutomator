total = 100
def func():
    # refer to global variable 'total' inside function
    global total
    if total > 10:
        total = 15
print('Total = ', total)
func()
print('Total = ', total)