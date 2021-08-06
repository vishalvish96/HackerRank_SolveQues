n=int(input('enter any number'))

if n%2==0 and 2>=n<=5:
    print('Not Weird')
elif 6>=n<=20:
    print('Weird')
elif n>20:
    print('Not Weird')
else:
    print('weird')