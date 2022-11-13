
# initialize variables
a=0
b=0
inc=0  # count of increases
dec=0   # count of decreases
noch=0   #count of no changes
# measurement=0  #troubleshooting variable

# determine how long the file is
num_lines = sum(1 for _ in open('/Users/Tik/Downloads/input'))
print (num_lines)


f=open('/Users/Tik/Downloads/input','r')
a=(f.readline())

#for i in range(num_lines):

while a!='':
    b=(f.readline())


# troubleshooting checks to see if reading lines and comparing correctly
    #print(a)
    #print(b)

    if b=='':
        break

    elif b>a:
        inc+=1
        print('increase')
    elif b<a:
        dec+=1
        print('decrease')
    elif a==b:
        noch+=1

# troubleshooting count measurements
    #measurement+=1
    #print('measurement is :',measurement)

    a=b
    continue

print ("increases equals ",inc)
print ("Decreases equals ",dec)
print ("No changes equals ",noch)






  
