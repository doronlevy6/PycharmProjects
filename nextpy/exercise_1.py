# ex 3.4.2

x= input("please enter a word:  ")
l=len(x)
m=l//2

a=x[:m]
y=a.upper()
z=x[m:]
print(y+z)

#4.2.2
x=input("pls:")
length=len(x)
l=length*(-1)
y=x[-1:-length-1:-1]
print(y)

if(x==y):
    print("ok")
else:
    print("not")
print(x,y)

#4.2.4
x=input("pls enter date dd/mm/yyyy")
import calendar
y=calendar.weekday(int(x[6:]),int(x[3:5]),int(x[0:2]))
if(y==0):
    print("monday")
elif(y==1):
    print("tuesday")
elif(y==2):
    print("wednesday")
elif(y==3):
    print("thursday")
elif(y==4):
    print("friday")
elif(y==5):
    print("saturday")
elif(y==6):
    print("sunday")


#5.3.4
def last_early(my_string:str):
    a = my_string[:-1]
    length=len(my_string)

    if(my_string[length-1] in a):
        return True
    else:
        return False



print(last_early("aycdfy"))

#5.3.6
def distance(x,y,z):
    """documantation is here"""
    flag=True
    if( (abs(x-y)<=1 or abs(x-z) <= 1 or abs(z-y)<=1 ) and ( abs(x-y)>=10 or abs(x-z) >=10 or abs(z-y)>=10 )):
               return True

    else:
        return False


print(distance(1,1.5,11))

help(distance)

# 6.1
def shift_left(z=[]):
  #  l=z.len()
    a =[z[1],z[2],z[0]]
   # ???????????????????? למה הקוד למטה לא טוב
   # a[0]=z[1]
   # a[1]=z[2]
    #a[2]=z[0]
    return a


def main():
    x=[1,2,3]

    shifted=shift_left(x)
    print(shifted)
main()

#6.2.1
a=[1,2,3,4]
b=[5,6,7,8]
c=a+b
d=[a+b]
print(c[0])# 1
# כלומר שרשרתי את המערך והרחבתי אותו ל 8 איברים
print(d[0]) #[1, 2, 3, 4, 5, 6, 7, 8]
# כלומר הגדרתי את d כמערך חדש שהאיבר הראשון בו הוא a+b

# 6.2.3
def join_to_string(aa):
    y=aa[:-1]
    z=aa[-1]
    a=",".join(y)
    xx= a+" and "+z
    return xx

def main():
    x="12345"
    print(join_to_string(x))

main()


# 6.2.4
def extand_list_x(a,b):
    a[:0]=b
    return a


def main():
    x=[1,2,3]
    y=[4,5,6]
    print(extand_list_x(x,y))

main()

#6.3.1
def are_lists_equal(a,b):
    a.sort()# משנה באופן קבוע את סדר הרשימה
    b.sort()
    if(a==b):
        return True
    else:
        return False


def main():
    x=[3,2,1]
    y=[3,2]
    print(are_lists_equal(x, y))


main()

#6.3.2
def longest(y):

    a=max(y,key=len)
    return a



def main():
    x=["aaa","bbbbb","ccc"]
    print(longest(x))


main()

#7.1.4
def squard_nombers(start,stop):
    while start<stop:
        print(start**2 , "\n")
        start+=1

def main():
    x=13
    y=19
    squard_nombers(x,y)

main()
# 7.2.1
  for i in listt:
        if i > maxx:
            new_listt.append(i) ## new_listt.insert(j,i) שים לב!!! לשתול ערכים במערך במקומות ריקים גם אפשרי
           # j+=1                       # אי אפשר לשתול לרשימה ריקה כך -> a[1]="xx"
    return new_listt


def main():

    print(is_greater([3,5,7,9,11],9))

main()

#7.2.2
def numbers_letters_count(a):
    numbers_of_words=1
    numbers_of_digits=0
    for i in a:
        if i==" ":
            numbers_of_words+=1
        if i.isdigit()==True:
            numbers_of_digits+=1

    return(numbers_of_words,numbers_of_digits)


def main():
    kelet="doron levy 66"
    x=numbers_letters_count(kelet)
    print("numbers of words = "+str(x[0])+ "\nnumbers of digit = "+ str(x[1]) )# שים לב!!!!! א"א לשרשר INT

main()

#7.2.4
def seven_boom(a):
    b=[]
    for i in range(1,a+1):

        if i%7 ==0 or i%10==7 or i//10==7 or i//100==7:
            b.insert(i-1,"boom")
        else:
            b.insert(i-1,i)

    return b


def main():
    print(seven_boom(22))

main()

#7.2.5
"""עלה בידינו: מחרוזת אי אפשר לדרוס רגיל אלא ליצור מחרוזת חדשה ריקה ולהעביר אליה את המחרוזת המתוקנת"""
def sequenc_del(a):
    new_word=a[0]
    l=len(a)
    for i in range(1,l):

        if a[i]==a[i-1]:
            continue
        else:
           new_word+=a[i]

    return new_word


def main():
    x="aabbccccc"
    print(sequenc_del(x))

main()


# 7.2.6
def makolet(a, b):
    reshima = a.split(",")

    if (b == 1):
        for i in reshima:
            print(i)

    if (b == 2):
        print(len(reshima))
    if (b == 3):
        k = input("is it on the list?")
        print(k in reshima)
    if (b == 4):
        k = input("is it on the list?")
        print(str(reshima.count(k)) + " times at the list")
    if (b == 5):
        k = input("whice product you want to delet?")
        print(reshima.remove(k))
        print(reshima)
    if (b == 6):
        k = input("whice product you want to add?")
        print(reshima.append(k))
        print(reshima)

        ### צריך להמשיך סעיפים 7-9


def main():
    x = "aa,bb,ccc,aa"
    p = 6
    makolet(x, p)


main()

#8.2.2

def MyFn(s):

    return s[-1]

def main():

    x=[("a",7),("b",4),("c",5)]

    print(sorted(x,key=MyFn  )) # print(sorted(x,key=lambda a: a[-1] )) אפשר גם כך ללא הפונקציה


main()

#8.2.3


def mult_tuple(a,b):
    l=[]

    for i in a:
        for j in b:
            t=(i,j)
            l.append(t)

    for j in b:
        for i in a:
            t = (j, i)
            l.append(t)
    return l



def main():

    x=(1,2)
    y=(4,5)

    print(mult_tuple(x,y))

main()
#8.2.4
def sort_anagrams(a):

    in_anagram=[]
    anagram=[]
    ii=0
    for i in a:
       if i not in in_anagram:
           anagram.append([])
           for j in a:
                if(sorted(i)==sorted(j)):
                    if j not in in_anagram:
                       in_anagram.append(j)
                       anagram[ii].append(j)
           ii+=1


    return anagram

#8.3.4
def inverse_dict(a):
    global new_key
    in_dist = []
    ii = 0
    d = {}
    for i in a.keys():# רץ על הKEYS
            new_key=a[i]
            new_value=i
            if new_key not in in_dist:
                d[new_key]=[new_value]
                in_dist.insert(ii,new_key)
                ii+=1
            else:
                d[new_key].append(new_value)

    return d

def main():
    x={"a":1, "b":2 ,"c":1,"d":1,}
    print(inverse_dict(x))

main()




def main():

    x=['deltas', 'retainers', 'desalt', 'pants', 'slated',
       'generating','ternaries',
       'smelters', 'termless', 'salted', 'staled',
       'greatening', 'lasted', 'resmelts']

    print(sort_anagrams(x))

main()

#8.3.2
def milon(a,b):
    if b==1:
        print(a["last_name"])
    if b == 3:
        l=a["hobbies"].split(",")
        ll=len(l)

        print("number of hobies:"+str(ll))
    if b==2:
        print(a["birth_date"][3:5])
    if b==4:
        l = a["hobbies"].split(",")
        print(l[-1])
    if b==5:
        a["hobbies"]+=","+"Cooking"
        print(a["hobbies"])
    if b==6:
        a["birth_date"]=(a["birth_date"][0:2],a["birth_date"][3:5],a["birth_date"][6:])
       # print(t, type(t))
        print(a["birth_date"],type(a["birth_date"]))
    if b==7:
        a["age"]=17
        print(a)

def main():
    x={"first_name":"Mariah","last_name":"Carey",
       "birth_date":"27.03.1970","hobbies":"Sing, Compose, Act"}
    milon(x,7)

main()

#8.3.3
def count_chars(a):
    d={}
    in_dist=[]
    ii=0
    for i in a:
        if i not in in_dist:
            in_dist.insert(ii,i)
            b=a.count(i)
            d[i]=b
            ii+=1

    return d

def main():
    x="doron levy dddd"
    print(count_chars(x))

main()

#9.1.1
def are_file_equal(a,b):
    f1input=open(a,"r")
    f2input=open(b,"r")
    f1=f1input.read()
    f2=f2input.read()
    print(f1, f2)
    if f1==f2:
        return True
    else:
        return False


def main():
    x=r"C:\Users\USER001\Desktop\Cil\file1.txt"
    y=r"C:\Users\USER001\Desktop\Cil\file2.txt"
    print(are_file_equal(x,y))

main()

#9.1.2

def family(a,b):
    f3input = open(a, "r")
    f3 = f3input.read()
    f3split = f3.split(" ")
    srev=[]
    if b==1:

        for j in range(len(f3split)):
            if "\n" in f3split[j]:
                f3split[j] = f3split[j][:-1]

        output = []
        for i in f3split:
            if i not in output:
                output.append(i)
        output.sort()
        print(output)
    if b==2:
        for i in range(len(f3)-1,0,-1):# לולאה שרצה מהסוף להתחלה
            srev.append(f3[i])
        s="".join(srev)
        print(s,end="")
    if b==3:
        line=[""]
        i=0
        jj=0
        for ch in f3:
            if "\n" not in ch:
                line[i] += ch
            else:
                i+=1
                line.insert(i,"")#  בכדי להוסיף תוים לאחד מרכיבי הרשימה הריקים יש קודם לאתחל אותו ע"י insert ולאתחל כ ""
        num_of_line=2
        for i in range(len(line)-1,len(line)-num_of_line-1,-1): # מדפיס את השורות מהסוף להתחלה מספר מסוים של שורות
            print (line[i])



    if b==4:
        print(type(f3input))
        print(f3input)
        print(type(f3))
        print(f3)
        for i in f3input:
            print (i)


def main():
    x=r"C:\Users\USER001\Desktop\Cil\file3.txt"

    #print(family(x,2))
    family(x,3)

main()
#9.2.2
def copy_file_content(a,b):
    f1=open(a,"r")
    f2=open(b,"w")
    txt=""
    for i in f1:
        txt=txt+i
    f2.write(txt)
    f2.close()
    f2=open(b,"r")
    f22=f2.read()
    print (f22)



def main():
    x=r"C:\Users\USER001\Desktop\Cil\file5.txt"
    y=r"C:\Users\USER001\Desktop\Cil\file6.txt"

    #print(family(x,2))
    copy_file_content(x,y)

main()

#9.2.3
def copy_file_content(a, b):
    f1 = open(a, "r")
    f2 = open(b, "w")
    f1 = f1.read()
    rezef = ""
    ss = ""
    print(f1)  # check
    for i in f1:
        if i != ",":
            rezef += i
    for j in range(1, len(rezef) + 1):
        if str(j) not in rezef:
            ss = str(j)
    print("rezef" + rezef)  # check
    f2.write(ss)
    f2.close()
    f2 = open(b, "r")
    print(f2.read())
    print("".join(sorted(rezef)))


def main():
    x = r"C:\Users\USER001\Desktop\Cil\file6.txt"
    y = r"C:\Users\USER001\Desktop\Cil\file7.txt"

    # print(family(x,2))
    copy_file_content(x, y)


main()

#9.3.1

def my_mp3_playlist(a):

    pticha=open(a,"r")
    kria=pticha.read()
    song_details=kria.split("\n")
    pticha.close()
    l=[]
    t=[]
    for i in song_details:# פיצול כל שיר לרשימה בפני עצמה
        l.append(i.split(";"))
    num_of_songs=len(l)

    orech_shir=0.0
    for j in l: # בדיקת השיר הארוך
        ez=j[2].split(":")
        ezer=".".join(ez)
        y=float(ezer)

        if y>orech_shir:
            orech_shir=y
            shir_aroch=j[0]

    print(shir_aroch,num_of_songs)#
    singers=[]
    for i in l:
        singers.append(i[1])
    print(singers)#
    pop_singers=""
    num_of_pop=0
    for i in singers:
        print(singers.count(i),type (singers.count(i)))#
        if singers.count(i)>num_of_pop:
            num_of_pop=singers.count(i)
            pop_singers=i
    print (pop_singers,num_of_pop)#

    t=(shir_aroch,num_of_songs,pop_singers)
    return t




def main():

    x=r"C:\Users\USER001\Desktop\Cil\file9.txt"


    #print(family(x,2))
    print(my_mp3_playlist(x))

main()

#9.3.2

def my_mp3_playlist(a,b):

    pticha=open(a,"r")
    kria=pticha.read()

    song_details=kria.split(";")
    pticha.close()
    new=[]
    for i in range(0, len(song_details), 3):
        new.append(song_details[i: i + 3])
    z=b.split(";")
    p=new.pop(2)# = del new[2] רק שזה לא שומר את הרכיב שמחקנו

    new.insert(2,z)

    pticha = open(r"C:\Users\USER001\Desktop\Cil\file11.txt", "w") #  כתבתי לקובץ חדש על מנת לא לדרוס נתונים התחלתיים
    details = ""
    print(new)
    for i in new:
        for j in i:
            details += j+";"
    pticha.write(details)





def main():

    x=r"C:\Users\USER001\Desktop\Cil\file10.txt"
    y="my new song;doron;1:30"

    #print(family(x,2))
    print(my_mp3_playlist(x,y))

main()