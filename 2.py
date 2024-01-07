from collections import deque

d = deque()

def palindrome(str: str) -> bool:
    for char in str:
        if char != ' ':
            d.append(char.lower())

    for i in range(0, (round(len(d) / 2))):
        if len(d) > 1:
            a = d.pop()
            b = d.popleft()

            if a != b:
                print('Is not palindrome')
                return
    print('Is palindrome')
    
palindrome('abba')
