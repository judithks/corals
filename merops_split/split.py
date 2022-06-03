'''
split combined fasta file from merops database into seperate fasta files
'''

content = ""
with open('/Users/roshanklein-seetharaman/projects/pdam_sequences/merops_split/Peptidase_sequences_for_Homo_sapiens.txt') as file:
    for line in file:
        if line == "\n":
            name = content.split()[0]
            new_file = open(f'merops_split/split_sequences/{name[1:]}.fasta', 'w')
            new_file.write(content)
            new_file.close()
            content = ""
        else:
            content += line