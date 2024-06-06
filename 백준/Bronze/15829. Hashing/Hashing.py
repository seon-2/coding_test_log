import sys
data = sys.stdin.readline

L = int(data())
input_data = data().strip()
mod_number = 1234567891


def modular_pow(base, exponent, modulus):
    result = 1
    base %= modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus

    return result


def make_mod_pow(l, mod_number):
    mod_pow = [0 for _ in range(l)]
    mod_pow[0] = 1
    base = 31

    for i in range(1, l):
        mod_pow[i] = modular_pow(base, i, mod_number)

    return mod_pow


def make_num_list(string):
    num_list = []
    for char in string:
        num_list.append(ord(char) - 96)
    return num_list


def get_hash(mod_pow, num_list):
    answer = 0
    for i in range(L):
        answer += (num_list[i] * mod_pow[i]) % mod_number
    return answer % mod_number


mod_pow = make_mod_pow(L, mod_number)
num_list = make_num_list(input_data)
print(get_hash(mod_pow, num_list))