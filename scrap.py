with open('scrapped_users.txt', 'r') as f:
    l = f.readlines()
for i in l:
    print(i.split(',')[1].strip())
