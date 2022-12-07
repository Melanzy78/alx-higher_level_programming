#!/usr/bin/python3
# Author -Bamidele Adefolaju

i = 0
for c in range(ord('z'), ord('a') - 1, -1):
<<<<<<< HEAD
print("{}".format(chr(c - i)), end="")
i = 32 if i == 0 else 0
=======
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
>>>>>>> 82b7305138ae38f014f692c5dea7bb74ceb3669d
