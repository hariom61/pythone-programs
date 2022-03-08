#dictionary1 = {
#    "Play" : "Doing some activity",
#    "Food" : "123",
#    "Python" : "Language",
#}
#
##print(dictionary1[0])
#print(len(dictionary1))
#n=12345
#rvs=0
#while n != 0:
#    rvs=n%10+rvs*10
#    print(rvs)
#    n=n/10
#
#print(rvs)
#

#count=[1,1,1,1,12,3,4,5,6,7,8,"d"]
#
#print(count)
#from audioop import add
#from pickle import APPEND
#
#
#count=[1,2,3,3,4,5,66,66]
#count.append(66)
#count.insert(-1,"ram")
#print(count)

#from itertools import count
#from operator import length_hint
#from pickle import TRUE
#from re import T
#from turtle import update


#count=["ram","jijus","mohomad","goutam","7"]
#if "ram" in count:
#    print("yes ,ram in the list")
#    if "jijus" in count:
#        count[0:3]="bheem","ram","shyam","devid","om","asa","sdsd"
#        print("hey jijus")
#    else:
#        print("yes")
##count.remove(7)
##print(count)
#y = list(count)
#y.append("hey")
#count=tuple(y)
#print(count
#import re 
#
#text=" 0	12.1.2.8	toyota	cruiser	2008	clean vehicle	274117	black	  jtezu11f88k007763	159348797	new jersey	 usa	10 days left 1	2899	ford	se	2011	clean vehicle	190552	silver	  2fmdk3gc4bbb02217	166951262	tennessee	 usa	6 days left2	5350	dodge	mpv	2018	clean vehicle	39590	silver	  3c4pdcgg5jt346413	167655728	georgia	 usa	2 days left 3	25000	ford	door	2014	clean vehicle	64146	blue	  1ftfw1et4efc23745	167753855	virginia	 usa	22 hours left 4	27700	chevrolet	1500	2018	clean vehicle	6654	red	  3gcpcrec2jg473991	167763266	florida	 usa	22 hours left 5	5700	dodge	mpv	2018	clean vehicle	45561	white	  2c4rdgeg9jr237989	167655771	texas	 usa	2 days left 6	7300	chevrolet	pk	2010	clean vehicle	149050	black	  1gcsksea1az121133	167753872	georgia	 usa	22 hours left 7	13350	gmc	door	2017	clean vehicle	23525	gray	  1gks2gkc3hr326762	167692494	california	 usa	20 hours left 8	14600	chevrolet	malibu	2018	clean vehicle	9371	silver	  1g1zd5st5jf191860	167763267	florida	 usa	22 hours left 9	5250	ford	mpv	2017	clean vehicle	63418	black	  2fmpk3j92hbc12542	167656121	texas	 usa	2 days left 10	10400	dodge	coupe	2009	clean vehicle	107856	orange	  2b3lj54t49h509675	167753874	georgia	 usa	22 hours left "
#x= re.findall("(\d.\d\.\d\.\d)", text)
#print(x)
#[ print(x) for x in count]
#count=("ram","jijus","mohomad","goutam","7")
#(r,t,y,u,i)=count
#for x in range(len(count)):
# print(count[4])
#listcount={count}
#print(listcount)
#listcount.add("asasas")
#print(listcount)
#print(listcount)
#count=tuple(listcount)
##for x in range(len(count)):
##count.sort(reverse=True)
#print(count.type)
#count={"ram","jijus","mohomad","goutam","7","7"}
#count2={"time","date","DBD","abc","xyz"}
#count.update(count2)
#print(count)
#count.add("shiyam")
#count.remove("shiyam")
#print(count)

#name = {'World',"hey","hi"}
#program = 'Python'
#print(f'Hello {name}! This is {program}')
#number=2
#number1=4
##print(f'{number+number1}')
#
#
#list1=[1,2,3,4,5,6,7,"eer"]
##print(type(list1))
#list1.reverse()
#reversedlist= list1
#print(reversedlist)

#find the count in sting
#       text="sssdfgffgvvbfhjkk "
#       char=""
#       for x in range(0,len(text)):
#           count1=1
#           for y in range(x+1,len(text)):
#            if text[x]==text[y]:
#                count1=count1+1
#                char=text[y]
#                text = text[:y] + '0' + text[y+1:];
#           
#           if(count1 > 1 and text[x] != '0'):  
#               print(text[x]," - ",count1);     
#               

#l=["asas","asas",3,4,5,2,3,4,7,9,5]
#l1=[]
#for i in l:
#    if i not in l1:
#        l1.append(i)
#    else:
#        print(i,end=' ')
#        print("duplicate value is",i)

#MyList = ["aa", "b", "a", "c", "c", "a", "c"]
#my_dict = {i:MyList.count(i) for i in MyList}
#print()
#print(my_dict)

#from collections import Counter
#list1 = ('x','y','z','x','x','x','y', 'z')
#print(Counter(list1))
#
#
import requests
try:
   api_url = input('Enter your api:')
   response = requests.get(f"{api_url}")
   print("",response.json)
except:
    print("handle exception")



