import sys
# sys.stdin = open("input.txt", "rt")
data = sys.stdin.readline

L = int(data())
input_data = data().strip()
mod_number = 1234567891


def make_mod_pow(l):

    mod_pow = [0 for _ in range(l)]

    mod_pow[0] = 1
    mod_pow[1] = 31
    mod_pow[2] = (31 ** 2) % mod_number

    for i in range(3, l):
        mod_pow[i] = (mod_pow[i-1] * mod_pow[1]) % mod_number

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


mod_pow = make_mod_pow(L)
num_list = make_num_list(input_data)
print(get_hash(mod_pow, num_list))