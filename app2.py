

# opening and reading the file, assuming the file name and file path are correct 
file = open("protein-matching-PF00023.fasta","r")   
content = file.read()
content = content.split(">")[1:]
new_list = []
for protein in content:
    head = protein.split("\n")[0].split("|")[0]
    body = "".join(protein.split("\n")[1:-1])
    if len(body) >= 50 and len(body) <= 500:
        cleaned = f">{head}\n{body}\n"
        new_list.append(cleaned)
file.close()

# creating and writing a new file with processed data 
file2 = open("proteini_final.txt","a")                
for i in new_list:
    file2.write(i)