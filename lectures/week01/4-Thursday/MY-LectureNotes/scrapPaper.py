# list = []

# little_list = 0

# while little_list < 3:
#     each_number = 0
#     list.append([])
#     while each_number < 3:
#         list[little_list].append(each_number)
#         each_number += 1
#     little_list+=1
# print(list)

# outer_index = 0 
# inner_index = 0 

# big_list = []

# while outer_index < 3:
#     temp_list = []
    
#     while inner_index < 3:
#         temp_list.append(inner_index)
#         inner_index+=1
#     big_list.append(temp_list)
#     inner_index = 0
# #     outer_index +=1
# # print(big_list)

# ##########################################################################

# # alphabet = "abcdefghijklmnopqrstuwxyz"
# # i = 0
# # length = len(alphabet)
# # rev_alph = ''
# # while i < len(alphabet):
# #     rev_alph = rev_alph + alphabet[length -1]
# #     length -= 1
# #     i += 1
# # print(rev_alph)

##########################################################################

# number = -8675309

# toString = str(number)
# length = len(toString)
# was_neg = False
# reverse = ""
# i = 0
# while i < len(toString):
#     if toString[length -1] == '-': #? Converts 
#         toString = list(toString)
#         del toString[length - 1]
#         was_neg = True
#         toString = "".join(toString)
#     else:
#         reverse = reverse + toString[length -1]
    
#     length -= 1
#     i += 1

# if was_neg == True :
#     reverse = list(reverse)
#     reverse.insert(0,'-')
#     reverse = ''.join(reverse)
#     reverse = int(reverse)
# print(reverse)



