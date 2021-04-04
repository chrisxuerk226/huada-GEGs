# First ,  I used csv model to read the csv file ，File path you need according to write your own file
import csv
csv_reader = csv.reader(open('/Users/xrk.study/Desktop/GSE100458/Degs.csv' , encoding='utf-8')) 

# Next, define a dict to save logFC and pvalue 
cutoff_info = {} 
# As you can see , Much of our data is in scientific notation， In the following steps we will perform 
# numerical comparisons, so we need to convert the format， here i define a function for practice 
# You can also use eval() 
def sd_to_float(str_num):
    if "e-" or "e+" in str_num:
        before_e = float(str_num.split('e')[0])
        ind = str_num.split('e')[1][1:]
        sign = str_num.split("e")[1][:1]
        index = int(ind)
        if sign == "+":
            return before_e * math.pow(10, index)
        elif sign == "-":
            return before_e * math.pow(10, -index)
    else :
        return float(str_num) 
 return       
# Create several lists to store information in the same content as the name

symbol = []
logfc = []
pvalue = []
# I'm going to do a pretty rough job here, if to get rid of the header  ：=） 
for row in csv_reader :
   if row[1] == "logFC" :
        continue
   else :
        symbol.append(row[0])
        logfc.append(row[1])
        pvalue.append(row[4])
# Iterate through the table and fill in the information  
for x in logfc :
   if "e" in x  :
        logfc_f.append(sd_to_float(x))
   else :
        logfc_f.append(float(x))
        
# create list to save ID of up-regulated and down-regulated genes  
up_genes = []
down_genes = [] 
# And then it's just going to traverse and extract according to 
# the threshold ， threshold_one refers to the threshold that you set 
# for logfc and threshold_two refers to the threshold that you set for
# pvalue 

for i in range(0,len(symbol)) :
    if Pvalue[i] < 0.05 and logfc_f[i] > 0.5  :
        up_genes.append(symbol[i])
    elif Pvalue[i] < 0.07 and logfc_f[i] < -0.5 :
        down_genes.append(symbol[i])
    else :
        continue
 # Finally , we save up-regulated genes and down-regulated genes in txt file 
 # The file path you should define according to yourself 
 
with open('/Users/xrk.study/Desktop/GSE100458/DEGs.txt' , 'r+') as f :
    f.write('Up Genes: ')
    f.write('\n')
    for x in up_genes :
        f.write(str(x) + '\n')
    f.write('-----------------------' + '\n')
    f.write('Down Genes: ')
    f.write('\n')
    for x in down_genes :
        f.write(str(x) + '\n')
    f.write('-----------------------' + '\n') 
    

 
