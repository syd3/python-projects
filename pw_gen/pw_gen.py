#!/usr/bin/env python3

import random
import string
import sys

try:
	pwLength = int(sys.argv[1])
except ValueError:
	exit("Please input the proper data type")
except IndexError:
	pw = random.choices(string.ascii_letters + string.digits, k=14)
else:
	pw = random.choices(string.ascii_letters + string.digits, k=pwLength)

print(''.join(pw))