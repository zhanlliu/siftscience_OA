
# coding: utf-8

# The goals for this challenge are to read a collection of SET cards from standard input and then to:
# 1. find and print the number of possible SETs of three cards in the input, and
# 
# 2. find and print the largest disjoint collection of SETs in the input (any correct answer can be output if there are multiple, maximum-size collections).
# 
# Python version: Python 3.65

# In[1]:


## import the combinations function 
## function attributes, input: a card 
## outputs: a list of four attributes of this card
from itertools import combinations
def attributes(card):
    AttributList = ["a", "s", "h", "A","S","H", "@","$","#"]
    attr_1, attr_rest = card.split()
    pos = AttributList.index(attr_rest[0]) 
    attr_2 = pos%3  
    attr_3 = pos//3
    attr_4 = len(attr_rest)
    return [attr_1, attr_2, attr_3, attr_4]
    


# In[2]:


## function all_same and all_different
## inputs: one specific attribute from three cards
## output (all_same): True when all card has the same value for the attribute
## output (all_different): True when all card has distinguished value for the attribute 
def all_same(card1_attr, card2_attr, card3_attr):
    return card1_attr == card2_attr and card2_attr == card3_attr
def all_different(card1_attr, card2_attr, card3_attr):
    return len(set((card1_attr, card2_attr, card3_attr))) ==3


# In[3]:


## fuction isset 
## input: three cards
## output: True if the three cards is a set
##         Flase if the three cards is not a set
def isset(card1, card2, card3):
    card1_attrs = attributes(card1)
    card2_attrs = attributes(card2)
    card3_attrs = attributes(card3)
    attr_comb = zip(card1_attrs, card2_attrs, card3_attrs)
    attr_comb = list(attr_comb)
    return all(all_same(v0, v1, v2) or all_different(v0, v1, v2)
              for (v0, v1, v2) in attr_comb)
        
            


# In[4]:


## function dis_jointSet
## input: word number and all possibel sets 
## output: all combination of disjoint sets 
## The function iterate through all the possible combinations
## Note the highest combinations depend on the number of the cards of the inputs 
## The longest disjoint set would be the number of the cards divided by 3. 
def dis_jointSet(input_num, allsets):
    if len(allsets) ==1:
        return allsets
    else:
        dis_joint_set = []
        max_dis = input_num//3 
        for i in range(2, max_dis, 1):
            comb = combinations(allsets, i)
            for x in comb:
                s = set(x[0])
                for y in x[1:]:
                    if len(s & set(y))!=0:
                        break
                    else:
                        s.update(y)
                else:
                    dis_joint_set.append(list(x))
        return dis_joint_set
## function longest_disjoint 
## input: all combination of disjoint sets
## output: the longest disjoint sets 
    
def longest_disjoint(dis_joint_set):
    return sorted(dis_joint_set, key=len)[-1]

## function find_set
## input: a text file with cards 
## output: the number of sets, the lenght of the longest disjoint set, and one of the disjoint set 
def find_set(InputText):
    set_res =[]
    input_num = int(open(InputText).read().splitlines()[0])
    lines = open(InputText).read().splitlines()[1:]
    for cards in combinations(lines, 3):
        if(isset(cards[0], cards[1], cards[2]) == True):
            set_res.append(list(cards))
    if(len(set_res) == 0):
        print("There is no set")
    else:
        dis_joint_set = dis_jointSet(input_num, set_res)
        res = longest_disjoint(dis_joint_set)
        return len(set_res), len(res), res


# In[5]:

############################################################################
## The result for the short list input
res = find_set("input_shortlist.txt")
for i in range(2):
    print(res[i])
print('')
for each in res[2]:
    for j in range(3):
        print(each[j])
    print('')


# In[6]:


## The result for the long list input, it takes longer time to execute 
res = find_set("input_longlist.txt")
for i in range(2):
    print(res[i])
print('')
for each in res[2]:
    for j in range(3):
        print(each[j])
    print('')

