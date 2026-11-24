import re

# 1. re.search()

sentence  = 'While Ailve eating sleep coding '
# res1 = re.search("While",sentence)  # matched results : <re.Match object; span=(0, 5), match='While'>
# res1 = re.search("while",sentence) #unmatched results Returns : None
# print(res1)

# 2. re.fullmatch()
sentence2 = " i love coding "
res2 = re.fullmatch(' i love coding ',sentence2) #entire string match then return: <re.Match object; span=(0, 15), match=' i love coding '>
rej2 = re.fullmatch('i love coding ',sentence2) # when once he got 1 umatced str it returns : None 
# print(res2,rej2)

# 3. re.sub()

sentence3 = 'There is no way to skip  There the task '

resolveRes = re.sub("There",'Over There',sentence3,count=1)
# returns : Over There is no way to skip  There the task 
print(resolveRes)

# 4.re.findall()
Sentence4 = "Rose is red sky is blue Nobody gonna love you the day the way I do Rose"

result = re.findall('Rose',Sentence4) # ['Rose']
# result = re.findall('z',Sentence4) # if there not present the finding substr it return  : []

print(result)
