'''1- masala'''
def count_unique_numbers(a, b, c):
    # To'plam yaratamiz va uchta sonni qo'shamiz
    unique_numbers = {a, b, c}
    
    # To'plamdagi noyob sonlar sonini qaytaramiz
    return len(unique_numbers)

# Kirishni o'qish
input_numbers = input("3 ta sonni kiriting: ").split()
a, b, c = int(input_numbers[0]), int(input_numbers[1]), int(input_numbers[2])

# Natijani chop etish
print(count_unique_numbers(a, b, c))


'''
2 - masala
'''
def is_htts(number):
    # Sonni satr (string) formatiga o'tkazamiz
    num_str = str(number)
    
    # Son uzunligini tekshiramiz
    if len(num_str) % 2 == 0:
        return "NO"
    
    # Har bir raqamni tekshiramiz
    for digit in num_str:
        if int(digit) % 2 == 0:
            return "NO"
    
    return "YES"

# Misol uchun:
NN = 1333
print(is_htts(NN))

'''
3 - masala
'''

def is_valid(s: str) -> bool:
    # Qavslar uchun moslik lug'ati
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack (to'plam)
    stack = []
    
    for char in s:
        # Agar char yopiq qavs bo'lsa
        if char in bracket_map:
            # Stackdan oxirgi elementni olamiz yoki '#' belgisini qo'yamiz
            top_element = stack.pop() if stack else '#'
            # Agar mos kelmasa, false qaytaramiz
            if bracket_map[char] != top_element:
                return False
        else:
            # Ochiq qavsni stackga qo'shamiz
            stack.append(char)
    
    # Stack bo'sh bo'lsa, true qaytaramiz (hamma qavslar mos keldi)
    return not stack

# Misollar
print(is_valid("()"))        # Chiqish: True
print(is_valid("()[]{}"))    # Chiqish: True
print(is_valid("(]"))        # Chiqish: False
print(is_valid("([)]"))      # Chiqish: False
print(is_valid("{[]}"))      # Chiqish: True
