#1.1.3
def double_letter_ezer(a):
    return a*2

def double_letter(b):
   return "".join(map(double_letter_ezer,b))# לשים לב שניתן להוריד את LIST כנראה שJOIN עובד גם על איטרטורים
def main():
    x="maya"
    print(double_letter(x))
main()

#1.1.4
def four_dividers(a):
   return list(filter(ezer, range(1,a)))

def ezer(b):
    return b % 4 == 0
def main():
    x=40
    print(four_dividers(x))
main()

#1.1.4
import functools
def sum_of_digit(a):
   return functools.reduce(ezer,str(a))

def ezer(m,n):
    return int(m)+int(n)
def main():
    x=1234567
    print(sum_of_digit(x))
main()
#1.3.1
def intersection(x,y):
    return list(set([i for i in x if i in y]))

print((intersection([6,6,5,5,7,7], [1,6,9,5,6])))

#1.3.2
def is_prime(a):
  # return "yes" in (["" if a%i==0 else "yes" for i in range(2,a)])
  # אופציה אחרת:
  return  not list(filter(lambda b: a%b==0 , range(2, a)))# ברשימה יש  את המחלקים של המספר הנבדק
# לכן אם הרשימה ריקה יחזיר TRUE ואם מלאה יחזיר FALS
def main():
    x=11
    print(is_prime(x))
if __name__ == '__main__':
    main()

#1.3.3
def is_funny(a):

  return  not list(filter(lambda i: i!="a" and i!="h",a))
def main():
    x="aahahah"
    print(is_funny(x))
if __name__ == '__main__':
    main()

#1.3.4
def kod(a):
    return "".join(list(map(lambda i: chr(ord(i)+2) ,a)))# ORD- מחזיר מספר אסקי של אות
                                                        # CHR -מחזיר סימן של מספר אסקי
def main():
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    print(kod(password))
if __name__ == '__main__':
 main()

 # אתגר המטבע מקוצר
 def combine_coins(a, b):
     # return ",".join(list(map(lambda i: a + str(i) ,range(b)))) # MAP רגיל
     # return ",".join([ a + str(i) for i in range(b)])# LIST COPERHENSION
     return ', '.join(map(lambda s, n: s + str(n), [a for i in range(b)], range(b)))  # שליחת 2 מערכים ללמבדה של המאפ
     # יש לשים לב !!!! שנשלח כל פעם איבר אחד מכל מערך


 def main():
     x = 10
     c = "$"
     print(combine_coins(c, x))
     print(str(3))


 if __name__ == '__main__':
     main()
def longname(a):
   #1.5.1 return sorted( [i for i in open(a,"r")],key=len)[-1]
   #או:
  # return max([i for i in open(a, "r")], key=len)
   #1.5.2 return len(list(filter(lambda i: ord(i) != 10, open(a, "r").read())))
        # מחזיר אורך הרשימה שנבתנה ע"י דילוג על הסימן "\n"
    #1.5.3
       s=sorted( [i for i in open(a,"r")],key=len)
       t="".join(list(filter( lambda j:len(j)==len(s[0]),s ) ))
       return t



def main():
    x = r"C:\Users\USER001\OneDrive - TEL-AVIV MUNICIPALITI\Desktop\Cil\names.txt"
    print(longname(x))



if __name__ == '__main__':
    main()

def longname(a):
    #1.5.4
    o=open(r"C:\Users\USER001\OneDrive - TEL-AVIV MUNICIPALITI\Desktop\Cil\names_length.txt","w")
    t="".join(list(map(lambda i: str(len(i)-1)+"\n" , open(a, "r"))))
    o.write(t)# יוצר את הקובץ וכותב לתוכו
    return t

def main():
    x = r"C:\Users\USER001\OneDrive - TEL-AVIV MUNICIPALITI\Desktop\Cil\names.txt"
    print(longname(x),)



if __name__ == '__main__':
    main()

#1.5.5
def longname(a,b):

    o=open(a,"r")
    t="".join(list(filter(lambda i: len(i)==b+1 ,o)))
    return t

def main():
    y=6
    x = r"C:\Users\USER001\OneDrive - TEL-AVIV MUNICIPALITI\Desktop\Cil\names.txt"
    print(longname(x,y))



if __name__ == '__main__':
    main()

#2.2.2+2.2.3
class octopus:
    countanimle=0
    def __init__(self,n="octavio",a=0):
        octopus.countanimle+=1
        self._name=n
        self._age=a
    def birthday(self):
        self._age+=1
    def getage(self):
        return self._age
    def setname(self,b):
        self._name=b
    def getname(self):
        return self._name
def main():
    x=5
    t1=octopus()
    t2=octopus("muli",4)
    for i in range(x):
        t1.birthday()
        t2.birthday()
    print(t1._name,t1.getage(),t2._name,t2.getage())
    print( octopus.countanimle)
    t1.setname("doron")
    print(t1.getname())


if __name__ == '__main__':
    main()

#2.3.4
import math
class pixel:
    def __init__(self, x=0,y=0,r=0,g=0,b=0):
        self.red=r
        self.green=g
        self.blue = b
        self.x = x
        self.y = y

    def set_coords(self,x,y):
        self.x=x
        self.y=y
    def set_grayscale(self):
        a=math.floor((self.red+self.green+self.blue)/3)
        self.red=a
        self.green=a
        self.blue=a
    def print_pixel_info(self):
        y=""
        if(self.red==0 and self.green==0):
            y="blue"
        elif(self.blue==0 and self.green==0):
            y="red"
        elif (self.red==0 and self.blue==0):
            y="blue"
        print("x:%s, y:%s color:(%s,%s,%s)" % (self.x,self.y,self.red,self.green,self.blue),y)


def main():
    p1=pixel(5,6,250,0,0)
    p1.print_pixel_info()
    p1.set_grayscale()
    p1.print_pixel_info()


if __name__ == '__main__':
    main()
# 2.5
#ללא סעיפים 8-9
# להשלים כל פרק חריגות
#4.1.2
def translate(sentence):
    tergum=""
    s=sentence.split()
    words = {'esta': 'is', 'la': 'the', 'en':
        'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    g=(words[n] for n in s )
    for i in g:
       tergum+=i+" "
    return tergum

def main():
    x="esta en casa"
    print(translate(x))
if __name__ == '__main__':
    main()
 #4.1.3
def first_prime_over(n):
    g = (i for i in range(n + 1, 10 ** 10) if is_prime(i))
    return g


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    x = 10
    gg = first_prime_over(x)
    e = enumerate(gg)
    print(e)
    for i, j in e:
        print(j)
        if i == 7:
            break
if __name__ == '__main__':
    main()
###e=dict([["a","b"],["c","d"]])סתם דוגמא לייצר מילון ע"י רשימה של רשימות
###print(e["c"])
# הדוגמא בפרק 4.2 הצנרת גנרטור
x=r"C:\Users\USER001\OneDrive - TEL-AVIV MUNICIPALITI\Desktop\Cil\capitals.txt"
with open(x) as file:
#content = file.readlines()
    single_line_gen = (line for line in file)

    countries_and_capitals = (l.replace("\n", ("")).split(",") for l in single_line_gen)

    capitals_dict = dict(countries_and_capitals)
    print(capitals_dict)
#4.2.2
# ללא גנרטורים
def parse_ranges(s):
    ll=s.split(",")
    l=[]
    sofi=[]
    for u in ll:
        lll=u.split("-")
        l.append(lll)

    for i in l:
        for j in range(int(i[0]),int(i[1])+1):
            sofi.append(j)
    return sofi

def main():
    x="2-5,7-9,11-12,13-15"
    print(parse_ranges(x))

if __name__ == '__main__':
    main()

#4.2.2
def parse_ranges(s):
    g = (u.split("-") for u in s.split(","))

    gg=([str(j) for j in range(int(start),int(stop)+1)] for start,stop in g)
    return gg
def main():
    x = "2-5,7-9,11-12,13-15"
    y = []
    for i in parse_ranges(x):
        y += i
    print(y)
if __name__ == '__main__':
    main()
#4.3.4
def get_fibo():
    x=0
    y=1
    yield 0
    yield 1
    while(True):
        yield x+y
        x,y=y,x+y
def main():
    fibo=get_fibo()
    for i in range(10):
        print(next(fibo))
if __name__ == '__main__':
    main()


#4.4
def sec():
    for a in range(60):
       yield a
def min():
    for b in range(60):
        yield b
def hrs():
    for c in range(24):
        yield c
def time():
    t=sec()
    for i in hrs():
        for j in min():
            for k in sec():
                yield f"{i:02}:{j:02}:{k:02}"

def year(start=2019):
    for i in range(start,2022):
        yield i

def month():
    for i in range(1,13):
        yield i

def day(month,leap_year=True):
    if month not in (2,4,6,9,11):
        yield 31
    elif month != 2:
        yield 30
    elif leap_year:
        yield 29
    else:
        yield 28

def if_leap(x):
    if x%400==0:
        return True
    elif x%4==0 and x%100!=0:
        return True
    else:
        return False

def pday(1,i+1):
    for k in range(i):
        yield k

def date(x):
    t=time()
    for a in year(x):
        for b in month():
           for c in pday(next(day(b,if_leap(a)))):
               for i in time():
                   yield f"{c:02}\{b:02}\{a:04} {i}"

def main():
    d=date(2019)
    x=0
    for i in d:
        if x%1000000==0:
            print(i)
        x+=1
if __name__ == '__main__':
    main()

#5.1.2
import winsound

#winsound.Beep(frequency, duration)
def main():
    freqs = {"la": 220,
             "si": 247,
             "do": 261,
             "re": 293,
             "mi": 329,
             "fa": 349,
             "sol": 392,
             }
    notes = """sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol
            ",250-sol,250-sol,500"""
    x=notes.split("-")
    m=[]

    for i in x:
       m.append(i.split(","))
    for i in m:
        print(i[0],i[1])
        winsound.Beep(freqs[i[0]],int(i[1]))
    print(m)
if __name__ == '__main__':
    main()


#5.2.3
import itertools
numbers = [20,20,20,10,10,10,10,10,5,5,1,1,1,1,1]
check=[]# keep sorting combination with sum=100
for j in range(len(numbers)+1):
    j_digit_combinations = itertools.combinations(numbers, j)#מכניסים לתוך האיטרטור את כל הצרופים האפשרים בעלי  J ספרות מתוך הרשימה
    for combination in j_digit_combinations:
        sum=0
        for sifra in combination:
            sum+=sifra
        if sum == 100:
            l = list(combination)
            l.sort()
            if l not in check:
                check.append(l)
                print(combination)

#5.3.2
class MusicNotes:
    def __init__(self):
        self._note=[55,61.74,65.41,73.42,82.41,87.31,98]
        self._idx=-1
    def __iter__(self):
        return self
    def __next__(self):
        if self._idx>33:
            raise StopIteration()
        self._idx+=1
        return self._note[(self._idx%7)] * (2**((self._idx)//7))


def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)
if __name__ == '__main__':
     main()
#5.4
import functools


class Iditerator:
    def __init__(self, x):
        self._id = x

    def __iter__(self):
        return self

    def __next__(self):
        self._id += 1
        if self._id > 999999999:
            raise StopIteration
        else:
            while not check_id_valid(self._id):
                self._id += 1
            return self._id


def check_id_valid(id_number):
    x = [int(i) for i in str(id_number)]
    y = [i * 2 if (j) % 2 == 0 else i for j, i in enumerate(x, 1)]
    z = [i % 10 + i // 10 if i > 10 else i for i in y]
    sum = functools.reduce(lambda i, j: i + j, z)

    if sum % 10 == 0:
        return True
    else:
        return False


def main():
    x = 111111111

    y = input("it or ge ")
    if y == "it":
        print("going with iterator")
        o = Iditerator(x)
        m = o
    else:
        g = (i for i in range(x, 999999999) if check_id_valid(i))
        m = g
        print("going with genetator")
    t = 0
    for j in m:
        if t < 10:
            print(j)
            t += 1
        else:
            print("end of listttt of", m)
            break


if __name__ == '__main__':
    main()

#6.1.3
from tkinter import *
from PIL import ImageTk, Image
def h():
    print("doron")
    w.title="Levy"
w=Tk()
sw =int( w.winfo_screenwidth()/3)
sh = int(w.winfo_screenheight()/3)
w.title("title Levy")
w.geometry(f"500x300+{sw}+{sh}")
l=Label(w,text = "what my favorite pic", font=30, fg="blue",bg="white")
img = PhotoImage(file=r"C:\Users\USER001\PycharmProjects\pythonProject1\avinoam.jpg")
Label(w,image=img)
b=Button(w,text="press here",image=img, command=h)
b.place(x=150,y=100)
l.pack()


w.mainloop()