s = ''

with open("/home/debit/Downloads/rosalind_dna.txt", 'r') as f:
    s = f.readline()

resp = str(s.count('A'))+' '+str(s.count('C'))+' '+str(s.count('G'))+' '+str(s.count('T'))
print(resp)

with open("/home/debit/Downloads/rosalind_dna_resp.txt", 'w') as fw:
    fw.write(resp)
