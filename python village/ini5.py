with open("/home/debit/Downloads/rosalind_ini5.txt", 'r') as f:
    with open("/home/debit/Downloads/rosalind_ini5_resp.txt", 'w') as fw:
        fw.write(''.join(f.readlines()[1::2]))
