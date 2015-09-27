import json
import re

# a = ["aaaaa","bbbb","Dave"]
# print a
#
# # Example of a list comprehension
# new_list = [x.upper() for x in a]
# print new_list
#
# list1 = ["Dave","George","Steve"]
# new_list1 = [x.upper() for x in list1 if x.find('George')]
# print new_list1
#
# new_dict = {}
# new_dict["key"] = "first"
# print new_dict
#
#
# print new_dict.get("what")
# # Returns None if key not found
# # Returns value of key if found
#
# fh=open("small.txt", 'r')
#x = fh.readlines() # Assumes there are lines of strings
# print x
# # Comprehension that will only returns lines wth the word "should"
# y = [j for j in x if "should" in j]
# print y

# readfile = fh.read()
# file_split = readfile.split()
#
# count_dict = {}
# for c in file_split:
#     if count_dict.has_key(c):
#         count_dict[c] += 1
#     else:
#         count_dict[c] = 1
# print count_dict
# fh.close()
fh = open('michah.json','r')
x = fh.read()
# JSON decode process
decoded_data_dict = json.JSONDecoder().decode(x)
#print decoded_data_dict.keys()
#print decoded_data_dict['data'][0]['location']['latitude']
def length_8(test_string):
    if len(test_string) >8:
        return True
    else:
        return False

#print filter(length_8,test_string)
# When calling a function in filter, don't use parens or the parameter


# for i in range(0,len(decoded_data_dict['data'])):
#     print decoded_data_dict['data'][i]['user']['username']


l = ['This','That','How','When']
for item in l:
    search_func = re.search('T', item)
    print search_func