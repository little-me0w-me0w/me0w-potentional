def hash(s):
    s=s[1]
    p=67
    m=10**9+9
    h=0
    for i in range(len(s)):
        h+=A.find(s[i])*p**i
    h=h%m
    return str(h)
A='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЧЧШЩЪЫЬЭЮЯ'
a=A.lower()
A='*'+A+a+' '
f=open('C:\\Users\\student\\Desktop\\students.csv', encoding='utf8')
a=f.readlines()
shapka=a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')
f=open('students_with_hash.csv','w', encoding='utf8')
f.write(shapka)
for x in a:
    x[0]=hash(x)
    f.write(','.join(x) + '\n')