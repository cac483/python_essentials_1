def is_prime(num):
    is_prime_num = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_prime_num = False
    else:
        is_prime_num = False
    return is_prime_num

for i in range(1, 20):
	if is_prime(i + 1):
		print(i + 1, end=" ")
print()
