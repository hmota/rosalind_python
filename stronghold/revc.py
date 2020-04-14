s = ''

with open("/home/debit/Downloads/rosalind_revc.txt", 'r') as f:
    s = f.readline()

resp = ''

for bp in reversed(s):
    if bp == 'A':
        resp = resp + 'T'
    elif bp == 'T':
        resp = resp + 'A'
    elif bp == 'C':
        resp = resp + 'G'
    elif bp == 'G':
        resp = resp + 'C'

print(resp)

with open("/home/debit/Downloads/rosalind_revc_resp.txt", 'w') as fw:
    fw.write(resp)

# solucao mais simples, testar velocidade
# st = "AAAACCCGGT"
# st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
# print st
