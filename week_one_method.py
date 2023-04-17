#문자열 메서드
text = "abcdefgaa"
print(text.count("a")) # 3

try:
    print(text.index("h")) 
except:
    print("문자열 없음")
    
print(text.find("d")) # 3 

print(" / ".join(["상","중","하"])) # 상 / 중 / 하

print("ABCDefgH".upper()) # ABCDEFGH
print("ABCDefgH".lower()) # abcdefgh

print("ABC DEF G".replace("DEF","QWERTY")) # ABC QWERTY G

#리스트 메서드

num_list =[1,2,3,4]

print("1,2,3,4,5,6,7".split(",")) #['1', '2', '3', '4', '5', '6', '7']
print(len(num_list)) # 4

del num_list[1] # [1,3,4]

num_list.append(0) #[1,3,4,0]

print(num_list)

print(sorted(num_list)) # [0,1,3,4]
num_list.reverse()
print(num_list) #[4,3,1,0]

print(num_list.index(4))  #1

num_list.insert(1,100) #[0, 100, 4, 3, 1]

print(num_list) 

num_list.remove(0) # [100,4,3,1]

num_list.pop() # [100,4,3]

print(num_list)

print(num_list.count(1)) # 0

num_list.extend([3,10,7]) #[100, 4, 3, 3, 10, 7]

num_list += [1,2,3] #[100, 4, 3, 3, 10, 7, 1, 2, 3]

print(num_list)

# 딕셔너리

dic = {}
num_dict = dict(zip([1,2,3,4],["a","b","c","d"]))
print(num_dict) #{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

num_dict[5] = "e" #{1: 'a', 2: 'b', 3: 'c', 4: 'd' 5:'e'}
del num_dict[3] #{1: 'a', 2: 'b', 4: 'd' 5:'e'}

print(num_dict[1]) #a
print(num_dict.get(3,0)) #0

print(num_dict.keys()) #[1, 2, 4, 5]

print(num_dict.values()) #['a', 'b', 'd', 'e']

print(num_dict.items()) #[(1, 'a'), (2, 'b'), (4, 'd'), (5, 'e')]

print(3 in num_dict) # 딕셔너리 자체에 In 을 쓰면 키값에서 찾음.  

num_dict.clear() #{}


