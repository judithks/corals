'''
create a dictionary to find the fasta file information from a given pdam id
then use this to create a combined fasta file for each pdam id
'''

# clear file
file = open("combined_fasta_corals.txt","w")
file.close()

# generate dictionary
pdam_dict = {}
definition = ""
with open("pdam_proteins.fasta") as file:
    for line in file:
        if line[0] == '>':
          pdam_dict[id] = definition
          definition = line
          id = line.split()
          id = id[0]
          id = id[1:]
        else:
          definition = definition + line
    pdam_dict[id] = definition

# write combined fasta
with open("coral_proteins.txt") as file:
  progress = 0
  for line in file:
    if line == "\n":
      pass
    else:
      with open("combined_fasta_corals.txt", "a") as myfile:
        protein = line.split()
        protein = protein[0]
        protein = protein
        definition = pdam_dict[protein]
        myfile.write(definition)
        myfile.write('\n')
        progress += 1
        print(f"Added {progress} sequences")
