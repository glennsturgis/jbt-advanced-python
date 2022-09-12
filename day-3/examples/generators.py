# iterators
#1
l=list(range(1,21))
print(l)

#2
odd=[x for x in l if x%2!=0]
print(odd)

#3
m10=[x*10 for x in l]
print(m10)

#4
import random
def genx(a,b):
    while True:
        yield random.randint(a,b)

g=genx(10,20)
print(next(g), next(g))

#5
def circ(n):
    i=0
    while True:
        yield i%n
        i+=1

c=circ(4)
for i in range(10):
    print(next(c))

#6
f=open("log.txt")
def get_log(file,severity=""):
        for line in file:
            if line.split('-')[0]==severity:
                yield line

def get_log2(file, num=10, severity=""):
        lines=file.readlines()
        counter=0
        while counter<len(lines):
            yield lines[counter:counter+num]
            counter+=num

#simple
f=open("log.txt")
gl=get_log(f,severity="1")
try:
    print(next(gl))
    print(next(gl))
except StopIteration:
    print("no more lines")
f.close()

f=open("log.txt")

#complicated
gl2=get_log2(f,num=2, severity="1")
print(next(gl2))
print(next(gl2))
f.close()

#nice 
csv_gen = (row for row in open("log.txt") if row.split('-')[0]=="7")

print(next(csv_gen))
print(next(csv_gen))

