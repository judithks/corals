''' 
for each pdam id, give the number of matches 
that are also contained in the olfactory_gcprs file given
'''

# reformat strangely formatted input file
new_file = open("simplified_pdam.txt", "w")
pdam_dict = {}
with open("pdam_to_gpcr.txt") as file:
    for line in file:
        if line[0] == ',':
            pass
        else:
            new_file.write(line)
            
new_file.close()

# generate list of matches for each pdam id
with open("simplified_pdam.txt") as file:
    for line in file:
        gpcr_list = []
        words = line.split()
        for count, value in enumerate(words):
            if '[' in value:
                # specific to how the input was formatted
                prot_name = words[count + 11]

                # read until the species name
                protein = ""
                for char in prot_name:
                    if char == '_':
                        break
                    else:
                        protein += char
                gpcr_list.append(protein)
        pdam_dict[words[0]] = gpcr_list

#print(pdam_dict['pdam_00017423-RA'])

# reformat it to get rid of the "HUMAN" ending
olfactory_gcprs = []
with open("olfactory_gpcrs.txt") as file:
    for line in file:
        olfactory_gcprs.append(line[:-1])

# print the info we want
for pdam in pdam_dict.keys():
    count = 0
    for gpcr in pdam_dict[pdam]:
        if gpcr in olfactory_gcprs:
            count += 1
        else:
            pass
    print(f"{pdam} has {count} olfactory matches")

#print(pdam_dict['pdam_00017423-RA'])

