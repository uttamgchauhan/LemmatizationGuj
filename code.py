from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tree import *
from getpass import _raw_input
from macpath import split
import sys
from itertools import count
from dharati1 import input_length
from operator import and_
import re

def split(word): 
    return [char for char in word]
a = ['ુ','એ','ે' ,'ન','ી','ો','થ','ા','ત','મ','ં' ,'વ','ઓ','શ','વા','ય','્', 'દ','દા','લ', 'િ']
def miniword(t_l):
            two_flag=0
            l=t_l
            if l==1 or l==2:
                for word in two_letter_words:
                    if word == s:
                        two_flag=1
                        break
                if two_flag == 1:   
                    print(s)
                    count_string.append(s)
                else:   
                    print(x)
                    count_string.append(x)
            else:
                print(s)
                count_string.append(s)
              
count=0
temp_var=0
flag2=0
temp1=0
d=1
ttr=0

k=0
o=0
oo=0
e=0
uu=0
aa=0
f_a=0
h_a=0
#reg_exp1='^[-+]?[0-9]+$'
reg_exp1='\d+'
#reg_exp2='^(?=.*[a-z0-9])[a-z0-9!@#$%&*.]{7,}$/i'
reg_exp3='^[a-zA-Z]*$'
#-----------------------------file-------------------------------------------
f2=open("words.txt","r")
rem_words=f2.read()
f=open("input1.txt","r")
f3=open("ending_n.txt","r")
f4=open("two_letter.txt","r")
f5=open("append_oo.txt","r")
ending_n_file=f3.read()
ending_n_words=word_tokenize(ending_n_file)
two_letter_file=f4.read()
two_letter_words=word_tokenize(two_letter_file)
append_oo_file=f5.read()
append_oo_words=word_tokenize(append_oo_file)
orig_stdout = sys.stdout
f1 = open('output1.txt', 'w')
sys.stdout = f1
input=f.read()
#----------------------------------------------------------------------------
re_check=re.sub('\\\\|\[\[|\]\]|\,|\,|[a-z*A-Z_]+',"",input)
input=re_check
print(input)
count_string=[]
non_discrete_words=[]
discrete_words=[]

sentences= sent_tokenize(input)
for sentence in sentences:
    new_input=[]
    words=word_tokenize(sentence) #empties the previously stored data
    for w in words:
        if w not in rem_words and not re.search(reg_exp1,w) and not re.search(reg_exp3,w):
           # w=re.sub("\d+"," ",w)
            new_input.append(w)
    n_l=len(new_input)      
    
    j=0
    if(j==0):
        x=new_input[j].replace(u'\ufeff', '')
        b=split(x)
        l=len(b) 
        flag1=0
        n_flag=0
        append_oo_flag=0                                                                                                                                                                                       
        s=""
        j=1
        if b[l-1] == a[5]:         #check 'ો'
            o=o+1
            if b[l-2] == a[3]:           #check 'ન'
                if b[l-3]==a[5]:            #check 'ો'
                    flag1=1          
                    i=0                          #મહાપુરુષોનો =મહાપુરુષ
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                          
                elif b[l-3]==a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag1=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓનો =છોકરો      
                            t_l=len(s)
                            miniword(t_l)   
                                    
                    elif b[l-4]!=a[7]:     #  check e
                        flag1=1
                        i=0
                        while i<=l-4:      #છોકરીઓનો  =છોકરી
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l) 
                                 
                    else:
                        print(s)             
                        count_string.append(s)   
                elif flag1!=1:    #સીતાનો =સીતા
                    i=0
                    while i<=l-2:
                        s=s+b[i]
                        i=i+1
                    for ending_n_word in ending_n_words:
                        if(ending_n_word == s):
                            n_flag=1
                            break
                        else:
                            n_flag=0
                    if(n_flag==1):
                        t_l=len(s)
                        miniword(t_l)
                    else:     
                        i=0
                        b=split(s) 
                        s=''
                        l=len(b)
                        while i<=l-2:
                            s=s+b[i]
                            i=i+1  
                        t_l=len(s)
                        miniword(t_l)
    
                else:
                    print(x)  
                    count_string.append(x) 
            else:
                print(x)
                count_string.append(x)
        elif b[l-1] == a[4]:      #check 'ી'
            e=e+1
            if b[l-2] == a[3]:            #check 'ન'
                if b[l-3]==a[5]:                #check 'ો' 
                    i=0                          #મહાપુરુષોની=મહાપુરુષ
                    flag1=1
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3]==a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag1=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓની =છોકરો      
                            t_l=len(s)
                            miniword(t_l)
     
                    elif b[l-4]!=a[7]: 
                        flag1=1
                        i=0
                        while i<=l-4:      #છોકરીઓની  =છોકરી
                            s=s+b[i]
                            i=i+1
                         
                        t_l=len(s)
                        miniword(t_l)                
                     
                    else:
                        print(s)             
                        count_string.append(s)     
                 
                elif flag1 != 1:            
                    i=0
                    while i<=l-3:                    
                        s=s+b[i]                  #સીતાની=સીતા
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:
                    print(x)
                    count_string.append(x)
            elif b[l-2] == a[6]:          #check 'થ'
                if b[l-3]==a[5]:             #check 'ો' 
                    i=0  
                    flag1=1                        #મહાપુરુષોથી=મહાપુરુષ
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3]==a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag1=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓથી =છોકરો
                            t_l=len(s)
                            miniword(t_l)
                    else: 
                        flag1=1
                        i=0
                        while i<=l-4:      #છોકરીઓથી =છોકરી
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)   
                 
                elif flag1!=1:            
                    i=0
                    while i<=l-3:                    
                        s=s+b[i]                  #સીતાથી=સીતા
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:
                    print(x)    
                    count_string.append(x)
            else:
                print(x)
                count_string.append(x)
                 
        elif b[l-1] == a[0]:         #check 'ુ'
            uu=uu+1
            if b[l-2] == a[3]:    #check 'ન'
                if b[l-3]==a[5]:        #check 'ો' 
                    i=0                    #મહાપુરુષોનુ=મહાપુરુષ
                    flag1=1
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
     
                elif b[l-3]==a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag1=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓનુ =છોકરો      
                            t_l=len(s)
                            miniword(t_l)
                    else: 
                        flag1=1
                        i=0
                        while i<=l-4:      #છોકરીઓનુ =છોકરી
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                   
                elif flag1!=1:            
                    i=0
                    while i<=l-3:                    
                        s=s+b[i]                  #સીતાનુ=સીતા
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:
                    print(x) 
                    count_string.append(x)
            else:
                print(x)
                count_string.append(x)
                 
        elif b[l-1] == a[7]:        #check 'ા'
            aa=aa+1
            if b[l-2] == a[3]:     #check 'ન' 
                if b[l-3]==a[5]: #check ' ો' મહાપુરુષોના =મહાપુરુષ
                    i=0
                    flag1=1
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3]==a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag1=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓના=છોકરો      
                            t_l=len(s)
                            miniword(t_l)
                    elif b[l-4]!=a[7]: 
                        flag1=1
                        i=0
                        while i<=l-4:      #છોકરીઓના =છોકરી
                            s=s+b[i]
                            i=i+1
                         
                        t_l=len(s)
                        miniword(t_l)
                    else:
                        print(x)                
                        count_string.append(x)
                elif flag1 != 1:  
                    i=0
                    while i<=l-3:
                        s=s+b[i]                  #સીતાના=સીતા
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                     
                else:
                    print(x)
                    count_string.append(x)
            elif b[l-2] == a[9]:     #check 'મ' 
                if b[l-3]==a[5]: #check ' ો' મહાપુરુષોમા =મહાપુરુષ
                    i=0
                    flag1=1
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3]==a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag1=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓમા =છોકરો      
                            t_l=len(s)
                            miniword(t_l)
                    elif b[l-4]!=a[7]: 
                        flag1=1
                        i=0
                        while i<=l-4:      #છોકરીઓમા  =છોકરી
                            s=s+b[i]
                            i=i+1
                         
                        t_l=len(s)
                        miniword(t_l)
                    else:
                        print(x)                
                        count_string.append(x)
                elif flag1 != 1:  
                    i=0
                    while i<=l-3:
                        s=s+b[i]                  #સીતામા=સીતા
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:
                    print(x)
                    count_string.append(x)
#             elif b[l-2] == a[17]:  #check 'દ'  ઈરાદા=ઈરાદો
#                 i=0
#                 while i<=l-2:
#                     s=s+b[i]
#                     i=i+1
#                 s=s+a[5]    
#                 t_l=len(s)
#                 miniword(t_l)            
            else:
                for append_oo_word in append_oo_words:
                    if(append_oo_word == x):
                        append_oo_flag=1
                        break
                    else:
                        append_oo_flag=0
                if(append_oo_flag==0):
                            print(x)
                            count_string.append(x)
                else:     
                    i=0
                    b=split(x) 
                    s=''
                    l=len(b)
                    while i<=l-2:
                        s=s+b[i]
                        i=i+1
                    s=s+a[5]          #ઈરાદા=ઈરાદો
                    print(s)
                    count_string.append(s)        
                
                 
        elif b[l-1] == a[1]:    #check 'એ' સીતાએ=સીતા
            f_a=f_a+1
            if b[l-2]==a[12]:       #check 'ઓ'
                if b[l-3]==a[7]:        #check 'ા ' 
                    flag1=1
                    i=0
                    while i<=l-3:
                        s=s+b[i]
                        i=i+1
                    for append_oo_word in append_oo_words:
                        if(append_oo_word == s):
                            append_oo_flag=1
                            break
                        else:
                            append_oo_flag=0
                    if(append_oo_flag==0):
                        t_l=len(s)
                        miniword(t_l)
                    else:     
                        i=0
                        b=split(s) 
                        s=''
                        l=len(b)
                        while i<=l-2:
                            s=s+b[i]
                            i=i+1
                        s=s+a[5]          #છોકરાઓએ =છોકરો      
                        t_l=len(s)
                        miniword(t_l)
                elif b[l-3]!=a[7]: 
                    flag1=1
                    i=0
                    while i<=l-3:      #છોકરીઓએ  =છોકરી
                        s=s+b[i]       #પરસજાતિઓએ  =પરસજાતિ
                        i=i+1
                    t_l=len(s)
                    miniword(t_l) 
                else:
                    print(x)     
                    count_string.append(x)
            elif b[l-2] == a[5]:    #check 'ો'  મહાપુરુષોએ =મહાપુરુષ    
                i=0
                flag1=1
                while i<=l-3:
                    s=s+b[i]
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            elif flag1 != 1:  
                i=0                     #remove only 'એ'
                while i<=l-2:
                    s=s+b[i]
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            else:
                print(x)
                count_string.append(x)
                  
        elif b[l-1] == a[2]:        #check 'ે'
            h_a=h_a+1
            if b[l-2] == a[3]:        #check 'ન'
                if b[l-3] == a[5]:    #check 'ો'  મહાપુરુષોને =મહાપુરુષ    
                    i=0
                    flag1=1
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3]==a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag1=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓને =છોકરો     
                            t_l=len(s)
                            miniword(t_l)
                    elif b[l-4]!=a[7]: 
                        flag1=1
                        i=0
                        while i<=l-4:      #છોકરીઓને   =છોકરી
                            s=s+b[i]
                            i=i+1
                         
                        t_l=len(s)
                        miniword(t_l)
                    else:
                        print(x)           
                        count_string.append(x)
                elif flag1 != 1:              
                    i=0
                    while i<=l-3:
                        s=s+b[i]                 #સીતાને=સીતા
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:
                    print(s)        
                    count_string.append(s)
            elif b[l-2] != a[3]:                 # રમે=રમ
                i=0
                while i<=l-2:
                    s=s+b[i]
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            else: 
                print(x)  
                count_string.append(x)
        elif b[l-1] == a[12]: #check 'ઓ'
            oo=oo+1
            i=0
            while i<=l-2:     #કેરીઓ=કેરી
                s=s+b[i]
                i=i+1
            print(s) 
            count_string.append(s)   
                 
        elif b[l-1] == a[10]:        #check anusvar 'ં'
            if b[l-2] == a[0]:      #check 'ુ' 
                if b[l-3] == a[3]:    #check 'ન'
                    if b[l-4]==a[5]:        #check 'ો' 
                        i=0                    #મહાપુરુષોનું=મહાપુરુષ
                        flag1=1
                        while i<=l-5:
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    elif b[l-4]==a[12]:       #check 'ઓ'
                        if b[l-5]==a[7]:        #check 'ા ' 
                            flag1=1
                            i=0
                            while i<=l-5:
                                s=s+b[i]
                                i=i+1
                            for append_oo_word in append_oo_words:
                                if(append_oo_word == s):
                                    append_oo_flag=1
                                    break
                                else:
                                    append_oo_flag=0
                            if(append_oo_flag==0):
                                t_l=len(s)
                                miniword(t_l)
                            else:     
                                i=0
                                b=split(s) 
                                s=''
                                l=len(b)
                                while i<=l-2:
                                    s=s+b[i]
                                    i=i+1
                                s=s+a[5]          #છોકરાઓનું =છોકરો      
                                t_l=len(s)
                                miniword(t_l)
                        else: 
                            flag1=1
                            i=0
                            while i<=l-5:      #છોકરીઓનું=છોકરી
                                s=s+b[i]
                                i=i+1
                            t_l=len(s)
                            miniword(t_l)
                              
                    elif flag1!=1:            
                        i=0
                        while i<=l-4:                    
                            s=s+b[i]                  #સીતાનું=સીતા
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    else:
                        print(x) 
                        count_string.append(x)
                else:
                    print(x)
                    count_string.append(x)
                 
              
            elif b[l-2] == a[7]:     #check 'ા'
                if b[l-3] == a[3]:    #check 'ન'
                    if b[l-4]==a[5]:        #check 'ો' 
                        i=0                    #મહાપુરુષોનાં=મહાપુરુષ
                        flag1=1
                        while i<=l-5:
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    elif b[l-4]==a[12]:       #check 'ઓ'
                        if b[l-5]==a[7]:        #check 'ા ' 
                            flag1=1
                            i=0
                            while i<=l-5:
                                s=s+b[i]
                                i=i+1
                            for append_oo_word in append_oo_words:
                                if(append_oo_word == s):
                                    append_oo_flag=1
                                    break
                                else:
                                    append_oo_flag=0
                            if(append_oo_flag==0):
                                t_l=len(s)
                                miniword(t_l)
                            else:     
                                i=0
                                b=split(s) 
                                s=''
                                l=len(b)
                                while i<=l-2:
                                    s=s+b[i]
                                    i=i+1
                                s=s+a[5]          #છોકરાઓનાં =છોકરો      
                                t_l=len(s)
                                miniword(t_l)
                        elif b[l-5]!=a[7]: 
                            flag1=1
                            i=0
                            while i<=l-5:      #છોકરીઓનાં=છોકરી
                                s=s+b[i]
                                i=i+1
                            t_l=len(s)
                            miniword(t_l)
                        else:
                            print(x)                
                            count_string.append(x)
                    elif flag1!=1:            
                        i=0
                        while i<=l-4:                    
                            s=s+b[i]                  # સીતાનાં=સીતા
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    else:
                        print(x) 
                        count_string.append(x)
                elif b[l-3] == a[9]:    #check 'મ'
                    if b[l-4]==a[5]:        #check 'ો' 
                        i=0                    #મહાપુરુષોમાં=મહાપુરુષ
                        flag1=1
                        while i<=l-5:
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    elif b[l-4]==a[12]:       #check 'ઓ'
                        if b[l-5]==a[7]:        #check 'ા ' 
                            flag1=1
                            i=0
                            while i<=l-5:
                                s=s+b[i]
                                i=i+1
                            for append_oo_word in append_oo_words:
                                if(append_oo_word == s):
                                    append_oo_flag=1
                                    break
                                else:
                                    append_oo_flag=0
                            if(append_oo_flag==0):
                                t_l=len(s)
                                miniword(t_l)
                            else:     
                                i=0
                                b=split(s) 
                                s=''
                                l=len(b)
                                while i<=l-2:
                                    s=s+b[i]
                                    i=i+1
                                s=s+a[5]          #છોકરાઓમાં =છોકરો      
                                t_l=len(s)
                                miniword(t_l)
                        elif b[l-5]!=a[7]: 
                            flag1=1
                            i=0
                            while i<=l-5:      #છોકરીઓમાં=છોકરી
                                s=s+b[i]
                                i=i+1
                            t_l=len(s)
                            miniword(t_l)
                        else:
                            print(x)                
                            count_string.append(x)
                    elif flag1!=1:            
                        i=0
                        while i<=l-4:                    
                            s=s+b[i]                  # સીતામાં =સીતા
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    else:
                        print(x) 
                        count_string.append(x)
                else:
                    print(x)
                    count_string.append(x)
            else:
                print(x)                 
                count_string.append(x)
        else: 
            print(x)  
            count_string.append(x)
#-------------------------------For second word onwards-------------------------------------------------------------------------------------------------------------------
    while j<=n_l-1:
        x=new_input[j]
        #print(x)
        b=split(x)
        l=len(b)
        flag=0    
        n_flag=0
        append_oo_flag=0
        s=""
        if b[l-1] == a[0]:            #check 'ુ'
            uu=uu+1
            if b[l-2] == a[15]:       #check 'યુ'
                if b[l-3] == a[16]:     #check '્'
                    i=0                  #બન્યુ = બનવુ
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    s=s+a[11]+a[0]    
                    print(s)
                    count_string.append(s)  
                else:
                    print(x)
                    count_string.append(x)  
                     
                    #t_l=len(s)
                    #miniword(t_l)  
                    
            elif b[l-2] == a[19]:       #check 'લ'
                if b[l-3] == a[2]:       #check 'ે'
                    if b[l-4] == a[15]:     #check 'ય'
                        if b[l-5] == a[7]:    #check 'ા'
                            i=0                 # સંતાડાયેલુ = સંતાડવુ
                            while i<=l-6:
                                s=s+b[i]
                                i=i+1
                            s=s+a[11]+a[0]    
                            t_l=len(s)
                            miniword(t_l)  
                        else:
                            print(x)
                            count_string.append(x)          
                    else:
                        print(x)
                        count_string.append(x) 
                else:
                    print(x)
                    count_string.append(x)         
            elif b[l-2] == a[11]:       #check 'વ'
                i=0                   # રમવુ= રમ
                while i<=l-3:
                    s=s+b[i]
                    i=i+1
                t_l=len(s)
                miniword(t_l)
             
            elif b[l-2] == a[8]:
                if(x == 'પરંતુ'  or x == 'હેતુ' or x=='વસ્તુ'):
                    print(x)
                    count_string.append(x)
                else:    
                    i=0                   #check 'ત' રમતુ = રમ
                    while i<=l-3:
                        s=s+b[i]
                        i=i+1
                    print(s)
                    count_string.append(s)
            elif b[l-2] == a[9]:
                i=0                   #check 'મ' પાંચમુ=પાંચ
                while i<=l-3:
                    s=s+b[i]
                    i=i+1
                t_l=len(s)
                miniword(t_l) 
            elif b[l-2] == a[13]:       #check 'શ' 
                if b[l-3] == a[4]:      #check 'ી '
                    i=0                   #check 'શ' આવીશુ=આવ
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)   
                else:
                    print(x)
                    count_string.append(x)             
            elif b[l-2] == a[3]:    #check 'ન'
                if b[l-3]==a[5]:        #check 'ો' 
                    i=0                    #મહાપુરુષોનુ=મહાપુરુષ
                    flag=1
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)   
                elif b[l-3]==a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag1=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓનુ =છોકરો      
                            t_l=len(s)
                            miniword(t_l)
                    else: 
                        flag=1
                        i=0
                        while i<=l-4:      #છોકરીઓનુ =છોકરી
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)    
                        
                elif flag!=1:            
                    i=0    
                    while i<=l-3:                    
                        s=s+b[i]                  #સીતાનુ=સીતા
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:
                    print(x)  
                    count_string.append(x)
            else:
                print(x)
                count_string.append(x)
     
             
        elif b[l-1] == a[1]:            #check 'એ'
            f_a=f_a+1
            if b[l-2]==a[12]:       #check 'ઓ'
                if b[l-3]==a[7]:        #check 'ા ' 
                    flag=1
                    i=0
                    while i<=l-3:
                        s=s+b[i]
                        i=i+1
                    for append_oo_word in append_oo_words:
                        if(append_oo_word == s):
                            append_oo_flag=1
                            break
                        else:
                            append_oo_flag=0
                    if(append_oo_flag==0):
                        t_l=len(s)
                        miniword(t_l)
                    else:     
                        i=0
                        b=split(s) 
                        s=''
                        l=len(b)
                        while i<=l-2:
                            s=s+b[i]
                            i=i+1
                        s=s+a[5]          #છોકરાઓએ=છોકરો      
                        t_l=len(s)
                        miniword(t_l)
                elif b[l-3]!=a[7]:
                    flag=1
                    i=0
                    while i<=l-3:      #છોકરીઓએ  =છોકરી or other e 
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:
                    print(x)     
                    count_string.append(x)
            elif b[l-2] == a[5]:    #check 'ો'  મહાપુરુષોએ =મહાપુરુષ    
                i=0
                flag1=1
                while i<=l-3:
                    s=s+b[i]
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            elif flag1 != 1:  
                i=0                     #remove only 'એ'
                while i<=l-2:
                    s=s+b[i]
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            else:
                print(x)
                count_string.append(x)
                  
        elif b[l-1] == a[2]:          #check 'ે' 
            h_a=h_a+1
            if b[l-2] == a[3]:        #check 'ન'
                if b[l-3] == a[5]:    #check 'ો'  મહાપુરુષોને =મહાપુરુષ    
                    i=0
                    flag=1
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3] == a[12]:         #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓને =છોકરો      
                            t_l=len(s)
                            miniword(t_l)
                    elif b[l-4] == a[4]:
                        i=0
                        while i<=l-4:                    
                            s=s+b[i]                  #છોકરાઓને=છોકરો
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    else: 
                        print(s)
                        count_string.append(s)         
                    
                elif flag != 1:    #સીતાને=સીતા
                    i=0
                    flag=1
                    while i<=l-3:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else: 
                    print(s)
                    count_string.append(s)
            elif b[l-2] == a[13]:        #check 'શ'
                if b[l-3]== a[7]:
                    i=0                    #check 'શ' કરાશે=કર
                    flag=1
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:  
                    i=0                    #check 'શ' કરશે=કર
                    flag=1
                    while i<=l-3:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
            elif flag != 1:                   # રમે=રમ
                i=0
                while i<=l-2:
                    s=s+b[i]
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            else:
                print(x)
                count_string.append(x)
            
        elif b[l-1] == a[4]:          #check 'ી'  
            e=e+1
            if b[l-2] == a[6]:          #check 'થ'
                if b[l-3]==a[5]:             #check 'ો' 
                    flag=1
                    i=0                          #મહાપુરુષોથી=મહાપુરુષ
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3]==a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓથી=છોકરો      
                            t_l=len(s)
                            miniword(t_l)
                    else: 
                        flag=1
                        i=0
                        while i<=l-4:      #છોકરીઓથી =છોકરી
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    
                elif flag!=1:            
                    flag=1
                    i=0
                    while i<=l-3:                    
                        s=s+b[i]                  #સીતાથી=સીતા
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:
                    print(x) 
                    count_string.append(x)   
            elif b[l-2] == a[3]:            #check 'ન'
                if b[l-3]==a[5]:                #check 'ો' 
                    i=0                          #મહાપુરુષોની=મહાપુરુષ
                    flag=1
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3]==a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓની =છોકરો      
                            t_l=len(s)
                            miniword(t_l)
     
                    elif b[l-4]!=a[7]: 
                        flag1=1
                        i=0
                        while i<=l-4:      #છોકરીઓની  =છોકરી
                            s=s+b[i]
                            i=i+1
                         
                        t_l=len(s)
                        miniword(t_l)                
                     
                    else:
                        print(s)             
                        count_string.append(s)     
        
                elif b[l-3] == a[7] and b[l-4] == a[11]:      #check 'ા' and 'વ'    
                    i=0
                    while i<=l-5:                    
                        s=s+b[i]                  #લાવવાની  = લાવ
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)    
                elif flag!=1:            
                    i=0
                    flag=1
                    while i<=l-3:                    
                        s=s+b[i]                  #સીતાની=સીતા
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:
                    print(x)        
                    count_string.append(x)
                           
            elif b[l-2] == a[8]:      #check 'ત'
                i=0
                while i<=l-3:                    
                    s=s+b[i]        #રમતી=રમ
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            elif b[l-2] == a[9]:     #check 'મ'                      
                i=0
                while i<=l-2:
                    s=s+b[i]      #રમી=રમ    
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            else:
                print(x)
                count_string.append(x)
     
        elif b[l-1] == a[5]:         #check 'ો'
            o=o+1
            if b[l-2] == a[3]:           #check 'ન'
                if b[l-3]==a[5]:            #check 'ો'
                    flag=1
                    i=0                          #મહાપુરુષોનો =મહાપુરુષ
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3] == a[12]:         #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓનો =છોકરો      
                            t_l=len(s)
                            miniword(t_l)   
                                    
                    elif b[l-4]!=a[7]:     #  check e
                        flag=1
                        i=0
                        while i<=l-4:      #છોકરીઓનો  =છોકરી
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l) 
                                 
                    else:
                        print(s)             
                        count_string.append(s)
                              
                elif flag!=1:    #સીતાનો =સીતા
                    i=0
                    while i<=l-2:
                        s=s+b[i]
                        i=i+1
                    for ending_n_word in ending_n_words:
                        if(ending_n_word == s):
                            n_flag=1
                            break
                        else:
                            n_flag=0
                    if(n_flag==1):
                        t_l=len(s)
                        miniword(t_l)
                    else:     
                        i=0
                        b=split(s) 
                        s=''
                        l=len(b)
                        while i<=l-2:
                            s=s+b[i]
                            i=i+1  
                        t_l=len(s)
                        miniword(t_l)
                else:
                    print(x)    
                    count_string.append(x)
            elif b[l-2] == a[8]:     #રમતો =રમ
                i=0
                flag=1
                while i<=l-3:
                    s=s+b[i]
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            elif b[l-2] == a[9]:     #પાંચમો=પાંચ
                i=0
                flag=1
                while i<=l-3:
                    s=s+b[i]
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            elif flag != 1:                  #દોડો =દોડ
                i=0
                while i<=l-2:
                    s=s+b[i]
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            else:
                print(x)
                count_string.append(x)
          
        elif b[l-1] == a[7]:        #check 'ા'  
            aa=aa+1
            if b[l-2] == a[3]:     #check 'ન' 
                if b[l-3]==a[5]: #check ' ો' મહાપુરુષોના =મહાપુરુષ
                    i=0
                    flag=1
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3]==a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓના =છોકરો      
                            t_l=len(s)
                            miniword(t_l)
                    elif b[l-4]!=a[7]: 
                        flag1=1
                        i=0
                        while i<=l-4:      #છોકરીઓના =છોકરી
                            s=s+b[i]
                            i=i+1
                         
                        t_l=len(s)
                        miniword(t_l)
                    else:
                        print(x)                
                        count_string.append(x)    
                elif b[l-3] == a[7] and b[l-4] == a[11]:         #check 'ા' and 'વ'
                    i=0
                    flag=1
                    while i<=l-5:                    
                        s=s+b[i]                  #લાવવાના = લાવ
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif flag!=1:
                    i=0
                    while i<=l-3:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:
                     
                    print(x)    
                    count_string.append(x)
                    
            elif b[l-2] == a[8]:  #check 'ત' રમતા=રમ
                if b[l-3] == a[16]: #check '્'
                    i=0
                    while i<=l-1:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:    
                    i=0
                    while i<=l-3:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
#             elif b[l-2] == a[17]:  #check 'દ'  ઈરાદા=ઈરાદો
#                 i=0
#                 while i<=l-2:
#                     s=s+b[i]
#                     i=i+1
#                 s=s+a[5]    
#                 t_l=len(s)
#                 miniword(t_l)    
            elif b[l-2] == a[9]:  #check 'મ' સીતામા=સીતા
                if b[l-3] == a[7] and b[l-4] == a[11]:                 #check 'ા' and 'વ'         
                    i=0
                    while i<=l-5:                                      #વિચારવામા= વિચાર
                        s=s+b[i] 
                        i=i+1                         
                    t_l=len(s)
                    miniword(t_l)    
                elif b[l-3]==a[5]: #check ' ો' મહાપુરુષોમા =મહાપુરુષ
                    i=0
                    flag1=1
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)    
                elif b[l-3] == a[12]:       #check 'ઓ'
                    if b[l-4]==a[7]:        #check 'ા ' 
                        flag=1
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1
                        for append_oo_word in append_oo_words:
                            if(append_oo_word == s):
                                append_oo_flag=1
                                break
                            else:
                                append_oo_flag=0
                        if(append_oo_flag==0):
                            t_l=len(s)
                            miniword(t_l)
                        else:     
                            i=0
                            b=split(s) 
                            s=''
                            l=len(b)
                            while i<=l-2:
                                s=s+b[i]
                                i=i+1
                            s=s+a[5]          #છોકરાઓમા =છોકરો      
                            t_l=len(s)
                            miniword(t_l)
                    elif b[l-4]!=a[7]: 
                        flag1=1
                        i=0
                        while i<=l-4:      #છોકરીઓમા=છોકરી
                            s=s+b[i]
                            i=i+1
                         
                        t_l=len(s)
                        miniword(t_l)
                    else:
                        print(x)                
                        count_string.append(x)       
                else:
                    i=0
                    while i<=l-3:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
            elif b[l-2] == a[11]:  #check 'વ' રમવા=રમ
                i=0
                while i<=l-3:
                    s=s+b[i]
                    i=i+1 
                t_l=len(s)
                miniword(t_l)
            else:
                for append_oo_word in append_oo_words:
                    if(append_oo_word == x):
                        append_oo_flag=1
                        break
                    else:
                        append_oo_flag=0
                if(append_oo_flag==0):
                            print(x)
                            count_string.append(x)
                else:     
                    i=0
                    b=split(x) 
                    s=''
                    l=len(b)
                    while i<=l-2:
                        s=s+b[i]
                        i=i+1
                    s=s+a[5]          #ઈરાદા=ઈરાદો
                    print(s)
                    count_string.append(s)
                 
        elif b[l-1] == a[12]: #check 'ઓ'
            oo=oo+1
            i=0
            while i<=l-2:     #કેરીઓ=કેરી
                s=s+b[i]
                i=i+1
            print(s) 
            count_string.append(s)          
                 
        elif b[l-1] == a[10]:        #check anusvar 'ં'
            if b[l-2] == a[0]:      #check 'ુ' 
                if b[l-3] == a[15]:       #check 'ય'
                    if b[l-4] == a[16]:     #check '્'
                        i=0                 #check બન્યું = બનવું
                        while i<=l-5:
                            s=s+b[i]
                            i=i+1
                        s=s+a[11]+a[0]+a[10]   
                        print(s)
                        count_string.append(s)  
                    else:
                        print(x)
                        count_string.append(x)  
                
                elif b[l-3] == a[19]:       #check 'લ'
                    if b[l-4] == a[2]:       #check 'ે'
                        if b[l-5] == a[15]:     #check 'ય'
                            if b[l-6] == a[7]:    #check 'ા'
                                i=0                   # સંતાડાયેલું = સંતાડવું
                                while i<=l-7:
                                    s=s+b[i]
                                    i=i+1
                                s=s+a[11]+a[0]+a[10]    
                                t_l=len(s)
                                miniword(t_l)  
                            else:
                                print(x)
                                count_string.append(x)          
                        else:
                            print(x)
                            count_string.append(x) 
                    else:
                        print(x)
                        count_string.append(x)         
                        
                elif b[l-3] == a[11]: #check 'વ' રમવું=રમ 
                    i=0                  
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3] == a[3]:    #check 'ન'
                    if b[l-4]==a[5]:        #check 'ો' 
                        i=0                    #મહાપુરુષોનું=મહાપુરુષ
                        flag=1
                        while i<=l-5:
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    elif b[l-4]==a[12]:       #check 'ઓ'
                        if b[l-5]==a[7]:        #check 'ા ' 
                            flag=1
                            i=0
                            while i<=l-5:
                                s=s+b[i]
                                i=i+1
                            for append_oo_word in append_oo_words:
                                if(append_oo_word == s):
                                    append_oo_flag=1
                                    break
                                else:
                                    append_oo_flag=0
                            if(append_oo_flag==0):
                                t_l=len(s)
                                miniword(t_l)
                            else:     
                                i=0
                                b=split(s) 
                                s=''
                                l=len(b)
                                while i<=l-2:
                                    s=s+b[i]
                                    i=i+1
                                s=s+a[5]          #છોકરાઓનું =છોકરો      
                                t_l=len(s)
                                miniword(t_l)
                        else: 
                            flag=1
                            i=0
                            while i<=l-5:      #છોકરીઓનું=છોકરી
                                s=s+b[i]
                                i=i+1
                            t_l=len(s)
                            miniword(t_l)    
                            
                    elif flag!=1:            
                        i=0
                        while i<=l-4:                    
                            s=s+b[i]                  #સીતાનું=સીતા
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    else:
                        print(x) 
                        count_string.append(x)
                elif b[l-3] == a[9]:  #check 'મ'  પાંચમું =પાંચ
                    i=0
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3] == a[8]:  #check 'ત' રમતું=રમ
                    if(x == 'ખાતું'  or x == 'અપૂરતું'):
                        print(x)
                        count_string.append(x)
                    else:    
                        i=0
                        while i<=l-4:
                            s=s+b[i]
                            i=i+1 
                        print(s)
                        count_string.append(s)
                else:
                    print(x)
                    count_string.append(x)
                 
              
            elif b[l-2] == a[7]:     #check 'ા'
                if b[l-3] == a[9]:   #check 'મ'
                    if b[l-4] == a[7] and b[l-5] == a[11]:                 #check 'ા' and 'વ'         
                        i=0
                        while i<=l-6:                                      #વિચારવામાં= વિચાર
                            s=s+b[i] 
                            i=i+1                         
                        t_l=len(s)
                        miniword(t_l)  
                    elif b[l-4]==a[12]:       #check 'ઓ'
                        if b[l-5]==a[7]:        #check 'ા ' 
                            flag=1
                            i=0
                            while i<=l-5:
                                s=s+b[i]
                                i=i+1
                            for append_oo_word in append_oo_words:
                                if(append_oo_word == s):
                                    append_oo_flag=1
                                    break
                                else:
                                    append_oo_flag=0
                            if(append_oo_flag==0):
                                t_l=len(s)
                                miniword(t_l)
                            else:     
                                i=0
                                b=split(s) 
                                s=''
                                l=len(b)
                                while i<=l-2:
                                    s=s+b[i]
                                    i=i+1
                                s=s+a[5]          #છોકરાઓમાં =છોકરો      
                                t_l=len(s)
                                miniword(t_l)
                        elif b[l-5]!=a[7]: 
                            i=0
                            while i<=l-5:      #છોકરીઓમાં=છોકરી
                                s=s+b[i]
                                i=i+1
                            t_l=len(s)
                            miniword(t_l)
                        else:
                            print(x)            
                            count_string.append(x)    
                    elif b[l-4] == a[5]:                                #check 'ો'
                        i=0
                        while i<=l-5:                                      #સંગઠનોમાં=સંગઠન
                            s=s+b[i] 
                            i=i+1                      
                        t_l=len(s)
                        miniword(t_l)    
                    else:
                        i=0       
                        while i<=l-4:                                      #check 'મ' સીતામાં =સીતા
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                elif b[l-3] == a[3]:    #check 'ન'
                    if b[l-4]==a[5]:        #check 'ો' 
                        i=0                    #મહાપુરુષોનાં=મહાપુરુષ
                        while i<=l-5:
                            s=s+b[i]
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    elif b[l-4] == a[12]:   #check 'ઓ'
                        if b[l-5]==a[7]:        #check 'ા ' 
                            flag=1
                            i=0
                            while i<=l-5:
                                s=s+b[i]
                                i=i+1
                            for append_oo_word in append_oo_words:
                                if(append_oo_word == s):
                                    append_oo_flag=1
                                    break
                                else:
                                    append_oo_flag=0
                            if(append_oo_flag==0):
                                t_l=len(s)
                                miniword(t_l)
                            else:     
                                i=0
                                b=split(s) 
                                s=''
                                l=len(b)
                                while i<=l-2:
                                    s=s+b[i]
                                    i=i+1
                                s=s+a[5]          #છોકરાઓનાં =છોકરો  
                                t_l=len(s)
                                miniword(t_l)
                        elif b[l-5]!=a[7]: 
                            i=0
                            while i<=l-5:      #છોકરીઓનાં=છોકરી
                                s=s+b[i]
                                i=i+1
                            t_l=len(s)
                            miniword(t_l)
                        else:
                            print(x)            
                            count_string.append(x)
                    elif b[l-4]!=a[5]:            
                        i=0
                        while i<=l-4:                    
                            s=s+b[i]                  # સીતાનાં=સીતા
                            i=i+1
                        t_l=len(s)
                        miniword(t_l)
                    else:
                        print(x) 
                        count_string.append(x)
                elif b[l-3] == a[11]: #check 'વ' રમવાં =રમ
                    i=0
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                elif b[l-3] == a[8]: #check 'ત' રમતાં =રમ
                    i=0
                    while i<=l-4:
                        s=s+b[i]
                        i=i+1
                    t_l=len(s)
                    miniword(t_l)
                else:
                    print(x)
                    count_string.append(x)
            else:
                print(x)           
                count_string.append(x)
        elif b[l-1] == a[13]:   #check 'શ'
            if b[l-2] == a[4]:   #check 'ી' 
                i=0
                while i<=l-3:
                    s=s+b[i]   #કરીશ=કર
                    i=i+1
                t_l=len(s)
                miniword(t_l)
            else:
                print(x)
                count_string.append(x)
                            
                     
        else: 
             
            print(x)                  
            count_string.append(x) 
        j=j+1
            
count=len(count_string)
count_string[0] = count_string[0].replace(u'\ufeff', '')
print("Non-Discrete output words count=", count)
print(count_string)
#--------------------------discrete words code--------------------------------------------------
for c in count_string:
    non_discrete_words=count_string
     
discrete_words.append(non_discrete_words[0])
 
while d<count:
    temp_var=non_discrete_words[d]
    flag2=0
    for w in discrete_words:
        if temp_var==w:
            flag2=1
    if(flag2==0):
        discrete_words.append(temp_var)
    else:
        d+=1
output_length=len(discrete_words)
print("Discrete output words count=", output_length)    
print(discrete_words)

#*************************************discrete words code****************************************************************

print("Number of words ending with 'ો'",o)
print("Number of words ending with 'ઓ'",oo)
print("Number of words ending with 'ી'",e)
print("Number of words ending with 'ા'",aa)
print("Number of words ending with 'ુ'",uu)
print("Number of words ending with 'એ'",f_a)  
print("Number of words ending with 'ે'",h_a)
ttr=output_length/input_length
print("Type to token ratio=",ttr)
f1.close()
          
sys.stdout = orig_stdout
  
          
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      