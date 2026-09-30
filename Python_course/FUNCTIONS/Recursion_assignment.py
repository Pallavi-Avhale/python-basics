'''1. Count digits in a number
 Example: 12345 → output = 5

2.Sum of digits of a number
 Input: 123 → Output: 6

3. Product of digits of a number

 Input: 123 → Output: 6

4. Replace Character 'e' to 'i' in given String
input: 'hello' output:- 'hillo'

5. Reverse a String

6. Check String is pallindrome or not

7. Find largest digit in a number
Example: 5832 → 8'''

# 1. Count digits in a number
#  Example: 12345 → output = 5
def count(num):
    if num==0:
        return 0
    return 1+count(num//10)
print(count(12345))

# 2.Sum of digits of a number
#  Input: 123 → Output: 6
def sum(num):
    if num==0:
        return 0
    return (num%10)+sum(num//10)
print(sum(123))

# 3. Product of digits of a number
#  Input: 123 → Output: 6
def prod(num):
    if num==0:
        return 1
    return (num%10)*prod(num//10)
print(prod(123))


# 4. Replace Character 'e' to 'i' in given String
# input: 'hello' output:- 'hillo'
def replace(st):
    if st=='':
        return ''
    if st[0]=="e":
        return "i"+replace(st[1:])
    return st[0]+replace(st[1:])
print(replace("Hello"))

# 5. Reverse a String
def reverse(s):
    # s="Hello"
    if len(s)==0:
        return s
    return reverse(s[1:])+s[0]
print(reverse("Hello"))

# 6. Check String is pallindrome or not
def palindrome(st):
    if st=='':
        return ''
    if st==st[::-1]:
        print('is palindrome')
    else:
        print('not palindrome')
palindrome('madam')


# 7. Find largest digit in a number
# Example: 5832 → 8'''
def largest(num):
    if num==0:
        return 0
    return max(num%10,largest(num//10))
print(largest(5832))
