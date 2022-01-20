seq1 = Seq('EEKG')
seq2 = Seq('SSSDEKA')
a = align(seq1, seq2)
result = a[0] == '---EEKG'
