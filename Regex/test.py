import re


pattern = r'(\b(_{1})[a-zA-Z/d]+\b)'
text = input()

lst = []
match = re.finditer(pattern,text)

for i in match:
    lst.append(i.group())

final_list = []
for j in lst:
    if '_' in j:
        new_str = j.replace('_','')
        final_list.append(new_str)

print(','.join(final_list))
