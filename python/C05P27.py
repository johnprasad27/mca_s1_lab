src=open(r"c:/Users/john27/MCA/mca_s1/lab/python/source.txt","r")
dst=open(r"c:/Users/john27/MCA/mca_s1/lab/python/output.txt","w")

line_no=1

for line in src:
    if line_no%2 !=0:
        dst.write(line)
    line_no+=1

src.close()
dst.close()

print("odd line copied")