import glob

labelsperclass=[0,0,0,0,0]

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

for file in glob.glob("./bindweed/*.txt"):
	file1 = open(file, 'r')
	Lines = file1.readlines()
	row=["","","","","","","","","","","","","","","","",""]
	i=0
	for line in Lines:
		if(line[0]=='0'):
			# row[i]=line
			labelsperclass[1]+=1
		elif(line[0]=='1'):
			labelsperclass[1]+=1
		elif(line[0]=='2'):
			row[i]=line
			i+=1
		elif(line[0]=='3'):
			labelsperclass[1]+=1
		elif(line[0]=='4'):
			# row[i]=replacer(line,'3',0)
			labelsperclass[1]+=1
	file2 = open(file, 'w')
	file2.writelines(row)
	file2.close()
print("Done!!!")

