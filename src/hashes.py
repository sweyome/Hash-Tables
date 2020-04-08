import time
import bcrypt

input_string = b"apple"
n = 1000000

print(f"hashing {n}x")

start_time = time.time()
output_hash = hash(input_string)
end_time = time.time()
print(output_hash)
print(f"paython hash runtime : {end_time - start_time} seconds")


def djb2(key):
    '''
    djb2 hash
    '''
    hash_value = 5381
    for char in key:
        hash_value = ((hash_value <<5) + hash_value) + char
        return hash_value

start_time = time.time()
for i in range(n):
    djb2(input_string)
end_time = time.time()
print(djb2(input_string))
print(f"djb2 hash runtime: {end_time - start_time} seconds")


start_time = time.time()
salt = bcrypt.gensalt()
for i in range(5):
    bcrypt.hashpw(input_string, salt)
end_time = time.time()
print(f"bcrypt hash runtime: {end_time - start_time} seconds")