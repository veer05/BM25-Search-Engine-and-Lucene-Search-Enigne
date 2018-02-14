import os
import operator
import re
from string import maketrans

#Dictionary for document frequency table for Unigram
dict_uni_df = dict() #(Key(word) : Value(Docid, Docid, Docid, df)

#Dictionary for frequency table for Unigram
dict_uni_tf = dict()  #(Key(word) : tf)

#Dictionary for Inverted Index for Unigram
dict_uni_index = dict() #(Key (word) : Value (Docid,tf) (Docid, tf)

#Dictionary for document frequency table for Unigram
dict_bi_df = dict() #(Key(word word) : Value(Docid, Docid, Docid, df)

#Dictionary for frequency table for Bigram
dict_bi_tf = dict() #(Key(word word) : tf)

#Dictionary for Inverted Index for Bigram
dict_bi_index = dict() #(Key (word word) : Value (Docid,tf) (Docid, tf)

#Dictionary for document frequency table for Unigram
dict_tri_df = dict() #(Key(word word word) : Value(Docid, Docid, Docid, df)

#Dictionary for frequency table for Trigram
dict_tri_tf = dict() #(Key(word word word) : tf)

#Dictionary for Inverted Index for Trigram
dict_tri_index = dict() #(Key (word word word) : Value (Docid,tf) (Docid, tf)

#Dictionary to hold file and count of token
dict_file_token_count_uni = dict()

#Dictionary to hold file and count of token
dict_file_token_count_bi = dict()
#Dictionary to hold file and count of token

dict_file_token_count_tri = dict()
source_location = "Z:\Info\Task_3_parseddoc"
destination = "Z:\Info\Task 4\Task 4 To Submit"


def getfilename(filenames):
    count = 0
    file_names = []
    remove_start = filenames.strip("(")
    remove_end = remove_start.strip(")")
    to_remove = "();"
    replace_with = " , "
    transform = maketrans(to_remove,replace_with)
    splitstr = remove_end.translate(transform)
    newstr = splitstr.split(",")
    for names in newstr:
        names = names.strip()
        if count % 2 != 1:
            file_names.append(names)
        count += 1
    for entry in file_names:
        filenamestring  = ','.join(file_names)
    return filenamestring

def getcount(filenames):
    count = 0
    counter = 0
    #file_names = []
    remove_start = filenames.strip("(")
    remove_end = remove_start.strip(")")
    to_remove = "()"
    replace_with = " ,"
    transform = maketrans(to_remove,replace_with)
    splitstr = remove_end.translate(transform)
    newstr = splitstr.split(",")
    for names in newstr:
        if count % 2 == 1:
            if names != '':
                counter += int(names)
            else:
                print(newstr)
        count += 1
    return counter


def create_df(dict,df_dict,tf_dict,fname):

    for key in dict.iterkeys():
        df_dict[key] = ""
    for key, value in dict.items():
        temp = getfilename(str(dict[key]))
        df_dict[key] = temp

    for key in dict.iterkeys():
        tf_dict[key] = ""
    for key, value in dict.items():
        #print(key)
        count = getcount(str(dict[key]))
        tf_dict[key] = count

    write_df_freq(df_dict,fname)
    write_term_freq(tf_dict,fname)

##PRINT DOCUMENT FREQUENCY TABLE  (TASK 3.2)
def write_df_freq(dict,fname):
    filename = fname + "-DF.txt"
    f = open(destination + '\\' + filename, 'w')
    for key in sorted(dict.iterkeys()):
        count_number = str(dict[key])
        count_of_file = count_number.split(',');
        row = key + "  -->  " + dict[key] + "(" + str(len(count_of_file)) + ")" +"\n"
        f.write(row)
    f.close()

##PRINT FILE AND TOKEN COUNT
def write_File_token_count(dict,fname):
    f = open(destination + '\\' + fname, 'w')
    for key,value in dict.iteritems():
        row = key + "   -->   "+value + "\n"
        f.write(row)
    f.close()

##PRINT INVERTED INDEX  (TASK 2)
def write_inv_index(dict,fname):
    f = open (destination + '\\' + fname, 'w')
    for key, value in dict.items():
        row = key + "  -->   " + value + "\n"
        f.write(row)
    f.close()

##PRINT TERM FREQUENCY TABLE  (TASK 3.1)
def write_term_freq(dict,fname):
   filename = fname + "-TF.txt"
   f = open(destination + '\\' + filename, 'w')
   for key, value in sorted(dict.iteritems(), key=lambda (k, v): (v, k), reverse=True):
       row = key + "  -->  "+ str(value) + "\n"
       f.write(row)
   f.close()


## ASSIGN VALUE IN DICT (Key (word) : Assign(value))
def assign_value_to_key(dict_source,name,dict_dest):
    fname = name.split('.txt')
    for key in dict_source:
        dict_dest[key] = dict_dest[key] + "("+ fname[0] +", " +str(dict_source[key])+");"

## WRITE IN DICTIONARY TOKEN
def write_token_dic(dict_word_and_count,filename,dest_dict,fcount):
    #dest_dict[filename] = str((len(dict_word_and_count)))
    dest_dict[filename] = str((sum(dict_word_and_count.values())))

##GENERATE INV INDEX
def generate_inv_index(filename,name,fcount):
    dict_word_and_count = dict()
    s = open(filename,'r+')
    stream = s.read()
    individual_string = stream.split()
    filename = name.split('.txt');
    temp = []



    for string in individual_string:
        if string not in dict_word_and_count:
            dict_word_and_count[string] = 1
        else:
            dict_word_and_count[string] = dict_word_and_count[string] + 1
        if string not in dict_uni_index:
            dict_uni_index[string] = ""
    #Generate Filename and Unigram Token Count
    write_token_dic(dict_word_and_count,filename[0],dict_file_token_count_uni,fcount)
    #Generate Unigram Inverted Index
    assign_value_to_key(dict_word_and_count,name,dict_uni_index)
    dict_word_and_count.clear()



    for word in range(len(individual_string) - 1):
        split_bigram = individual_string[word:word+2]
        bigram = " ".join(split_bigram)
        if bigram not in dict_word_and_count:
            dict_word_and_count[bigram] = 1
        else:
            dict_word_and_count[bigram] = dict_word_and_count[bigram] + 1
        if bigram not in dict_bi_index:
            dict_bi_index[bigram] = ""
    # Generate Filename and Bigram Token Count
    write_token_dic(dict_word_and_count, filename[0],dict_file_token_count_bi,fcount)
    #Generate Bigram Inverted Index
    assign_value_to_key(dict_word_and_count, name, dict_bi_index)
    dict_word_and_count.clear()


    for word in range(len(individual_string) - 2):
        split_trigram = individual_string[word:word + 3]
        trigram = " ".join(split_trigram)
        if trigram not in dict_word_and_count:
            dict_word_and_count[trigram] = 1
        else:
            dict_word_and_count[trigram] = dict_word_and_count[trigram] + 1
        if trigram not in dict_tri_index:
            dict_tri_index[trigram] = ""
    # Generate Filename and Trigram Token Count
    write_token_dic(dict_word_and_count, filename[0],dict_file_token_count_tri,fcount)
    #Generate Trigram Inverted Index
    assign_value_to_key(dict_word_and_count, name, dict_tri_index)
    dict_word_and_count.clear()
    print(filename)
    s.close()



def main():
    folder = os.listdir(source_location)
    for file in folder:
        file_count =  len(folder)
        generate_inv_index(source_location + '\\' +file,file,file_count)
    write_inv_index(dict_uni_index,"Unigram_inverted_index.txt")
    write_inv_index(dict_bi_index,"Bigram_inverted_index.txt")
    write_inv_index(dict_tri_index,"Trigram_inverted_index.txt")

    write_File_token_count(dict_file_token_count_uni,"Unigram-File-Token-Count.txt")
    write_File_token_count(dict_file_token_count_bi, "Bigram-File-Token-Count.txt")
    write_File_token_count(dict_file_token_count_tri, "Trigram-File-Token-Count.txt")

    create_df(dict_uni_index,dict_uni_df,dict_uni_tf,"Unigram")
    create_df(dict_bi_index,dict_bi_df,dict_bi_tf,"Bigram")
    create_df(dict_tri_index,dict_tri_df,dict_tri_tf,"Trigram")

main()
