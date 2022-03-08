text="abcdabbbbhgy "
char=""
for x in range(0,len(text)):
    count1=1
    for y in range(x+1,len(text)):
     if text[x]==text[y]:
         count1=count1+1
         char=text[y]
         text = text[:y] + '0' + text[y+1:];
    
    if(count1 > 1 and text[x] != '0'):  
        print(text[x]," - ",count1);     
              