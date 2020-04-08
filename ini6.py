dic = {}

with open("/home/debit/Downloads/rosalind_ini6.txt", 'r') as f:
    for word in f.read().strip().split(' '):
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

print(dic)

with open("/home/debit/Downloads/rosalind_ini6_resp.txt", 'w') as fw:
    for key, value in dic.items():
        fw.write(key + ' ' + str(value) + '\n')
