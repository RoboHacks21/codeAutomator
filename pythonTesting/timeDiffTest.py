import time
start = time.time()

time.sleep(1.25)  # or do something more productive

done = time.time()

print(done)

elapsed = (done - start) * 4

def roundNum(numFloat):
    rounded = int(numFloat)
    if (numFloat - rounded > 0.5):
        rounded += 1

    return rounded

print(elapsed)
print(roundNum(elapsed))
print(round(elapsed))
