# . char
import re
'''text  = "i love python : ac , ac   , abc , a1!c"
pattern1 = r'a.?c'
pattern2 = r'a.*c'
pattern3 = r'a.c' 
res1 = re.findall(pattern1,text)    #['ac', 'ac', 'abc']  0 or 1 char 
res2 = re.findall(pattern2,text)    #multiple char : 
res3 = re.findall(pattern3,text)    #['abc'] exactly 1 char
print(res1)
print(res2)
print(res3)

# Another Example :
text = 'Hello World'
res = re.search('Hel.o',text)
if res != None:
    print("Match found")
else:
    print(" no found")
only for matching purpouse we shhuld use

# example 3:

sentence = 'i love pyhton'

res = re.search(r'lo.e',sentence)
if res != None:
    print('Match Found,',res)
else :
    print('no found') '''

'''1.\ (backslash)
text1 = 'pi value is : 3.14'
New_pattern = r'3\14'   #re.PatternError: invalid group reference 14 at position 2
New_pattern = r'3\.14'    # <re.Match object; span=(14, 18), match='3.14'>

print(re.search(New_pattern,text1)) '''


'''3. ^ (Caret)  -  -  Starts With'''
s = " i love pyspiders"
res = re.search(r'^ i',s)
print(res)

'''4.dollar
if the sub string ends with the specified str then returns substr in a list.
otherwise empty list.
'''

str = 'I am a student'
res = re.findall(r'&ent',str)
print(res)


'''5.star(*) - It checks all the substr is exitst if exist returns in a list all the char 
and even if not match the subchar shows like '' it can be one or more
['a', '', '', 'a', '', '', 'a', '', '', '', 'a', '', '', '', '', '']
'''

word = 'ab ab abb abbbb'
result = re.findall(r'a*',word)
print(result)

'''+ '''

sub = 'Python is a highlevel programming language'
resolve = re.findall(r'g+a',sub)#[]
resolve = re.findall(r'g+',sub)#['g', 'g', 'g', 'g', 'g']
print(resolve)

''''?
it checks before question mark the immediatly left char becomes optional if optional char is present its fine otherwise also.
'''
new = 'sujay ajay'
print(re.findall(r's.jay',new))

'''Curly baraces {} like between operator in oracle'''

str4 = 's ss sss ssss'
res4 = re.findall('s{2,3}',str4)
print(res4)

''' []'''


