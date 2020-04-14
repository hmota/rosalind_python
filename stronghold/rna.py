s = ''

with open("/home/debit/Downloads/rosalind_rna.txt", 'r') as f:
    s = f.readline()

resp = s.replace('T', 'U')
print(resp)

with open("/home/debit/Downloads/rosalind_rna_resp.txt", 'w') as fw:
    fw.write(resp)
