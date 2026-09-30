num=eval(input('enter a no.'))
res=num
rev=0
while num!=0:
    rev=rev*10+num%10
    num=num//10
print(f'reverse no is {rev}')
if res==rev:
    print('palindrome no.')
else:
    print('not a palindrome no.')