# Created by LimerBoy
import core.rot13 as rot13

message = input("[?] Please enter ROT13 encoded message to bruteforce: ")
for char in range(1, 26):
    result = rot13.decode(message, char)
    print(f"[{char}] {result}")
