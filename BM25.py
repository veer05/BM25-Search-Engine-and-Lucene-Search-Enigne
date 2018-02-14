import os
import math
import operator
import re

k1=1.2
k2=100
b=0.75
N = 1000
#cHANGE HERE IF THE NUMBER OF FILE CHANGES
#SOURCE LOCATION
source_location = "Z:\Info\Task 4\Task 4 To Submit"

#Dictionary for document frequency table for Unigram
dict_term_docname = dict() #(Key(word) : Value(Docid, Docid, Docid)

#Dictionary for document frequency count table for Unigram
dict_term_doccount = dict() #(Key(word) : Value(number of documents the word appears in)

#dictionary for unigram index
dict_unigram_index = dict()

#UNIGRAM DF FILENAME
unigram_df = "Unigram-DF.txt"
unigram_tf = "Unigram-TF.txt"
unigram_inv_index = "Unigram_inverted_index.txt"
unigram_file_word_count = "Unigram-File-Token-Count.txt"

#Populate the term-DocFreq dict
def populate_Doc_freq_dict():
 term = []
 path = source_location + "\\" + unigram_df
 f = open(path, 'r+')
 filecontent = f.readlines()
 for lines in filecontent:
     lines = lines.strip()
     str = lines.split("-->")
     str[0] = str[0].strip()
     str[1] = str[1].strip()
     term.append(str[0])
     dict_term_docname.setdefault(str[0],[])
     term = str[1].split(',')
     count = term[-1].strip('(')
     dict_term_doccount[str[0]] = count.strip(')')
     for i in range(len(term) -1):
         dict_term_docname[str[0]].append(term[i])
 f.close()
 #print(dict_term_docname)
 #print(dict_term_doccount)

#Create index unigram
def createIndex():
    content = []
    path = source_location + "\\" + unigram_inv_index
    f = open(path, 'r+')
    filecontent = f.readlines()
    for lines in filecontent:
        content.append(lines.strip())
    for lines in content:
        get_count = []
        get_count = lines.split("-->")
        tempstr = str(get_count[1])
        filename = str(get_count[0])
        dict_unigram_index[filename.strip()] = tempstr.strip()
    #dict_unigram_index

#Get estimate of how many times the word appears in the document
def count_of_query_in_doc(query,docs):
    filecount = None
    docname = "("+docs
    if query in dict_unigram_index:
        term = dict_unigram_index[query]
        filename = term.split(";")
        join_entries = ",".join(filename)
        document_names = join_entries.split(",")
        for index, value in enumerate(document_names):
            if value == docname:
                filecount = str(document_names[index + 1])
    if filecount != None:
        filecount = filecount.strip()
        count = filecount.strip(")")
        count = count.strip()
        termcount = int(count)
    else:
        termcount = 0
    return termcount

#Get document length
def document_length(docs):
 content = []
 path = source_location + "\\" + unigram_file_word_count
 f = open(path, 'r+')
 filecontent = f.readlines()
 for lines in filecontent:
    content.append(lines.strip())
 for entry in content:
     file_word_count = entry.split("-->")
     fname = str(file_word_count[0])
     if fname.strip() == docs:
        tokencount = str(file_word_count[1])
        count = int(tokencount.strip())
 return count

#Calc score for each document
def Calc_BM25(queryterm,doc,avgdocLen):
    seperate_term = queryterm.split()
    BM25val = 0
    for query in seperate_term:
        count_of_query = count_of_query_in_doc(query, doc)
        doc_len = document_length(doc)
        K = k1 * ((1 - b) + b * (doc_len / avgdocLen))
        ri = 0
        ni = dict_term_doccount[query]
        #print ni
        R = 0
        fi = count_of_query
        qfi = seperate_term.count(query)
        v = (((float(ri) + 0.5) / (float(R) - float(ri) + 0.5)) / (
            (float(ni) - float(ri) + 0.5) / (float(N) - float(ni) - float(R) + float(ri) + 0.5)))
        v1 = math.log(v, 2)
        v2 = (((float(k1) + 1) * float(fi)) / (float(K) + float(fi)))
        v3 = (((float(k2) + 1) * float(qfi)) / (float(k2) + float(qfi)))
        BMval = (v1 * v2 * v3)
        BM25val += BMval
    return BM25val


def calc_scores(eachquery,id,avgdocLen):
 #print eachquery + " "+str(count)
 seperate_term = eachquery.split()
 dict_file_BMScore = dict()
 doc_name_list = []
 for query in seperate_term:
     for docname in dict_term_docname[query]:
         if docname not in doc_name_list:
            doc_name_list.append(docname)
 for docs in doc_name_list:
     dict_file_BMScore.update({docs + '.txt': Calc_BM25(eachquery, docs,avgdocLen)})
 sorted_dict = sorted(dict_file_BMScore.items(), key=operator.itemgetter(1))
 sorted_tuple = sorted_dict[::-1][0:100]
 write_output(sorted_tuple,id,eachquery)

#Write output to a file
def write_output(sortedlist,id,query):
  res = ''
  rank = 0
  doc_name = ''
  BMvalue = ''
  with open(source_location + '\\' + 'BM25_Unigram_Casefolding_query_res.txt', 'a') as f:
    for entry in sortedlist:
        rank +=1
        for subentry in entry:
            if isinstance(subentry, str):
                doc_name = subentry
            else:
                BMvalue = subentry
        res = str(id) + ' Q0 '+ doc_name+' '+ str(rank)+ ' ' +str(BMvalue)+ ' ' + 'BM25_Unigram_Casefolding'
        row = str(res)
        row = row + "\n"
        f.write(row)
  f.close()


#Calc AvgDoc Length
def find_avg_doc_len(unigram_tf):
 content = []
 count = 0
 number_of_doc = 1000
 path = source_location + "\\" + unigram_tf
 f = open(path, 'r+')
 filecontent = f.readlines()
 for lines in filecontent:
     content.append(lines.strip())
 for lines in content:
     get_count = lines.split()
     #countstr = str(get_count[2])
     count += int(get_count[2])
 return (float(count)/float (number_of_doc))


def main(queryfilename):
 content = []
 query_terms = []
 query_key = dict()
 # Open and read the query file
 path = source_location + "\\" +queryfilename
 f = open(path, 'r+')
 filecontent = f.readlines()
 for lines in filecontent:
    content.append(lines.strip())
 count = 1
 #Strip the number and only get the query terms
 for entry in content:
    get_query_term = entry.split()
    query_term = get_query_term[1:]
    query = ' '.join(query_term)
    query_key[get_query_term[0]] = query
    query_terms.append(query)
 #Send Query 1 by 1
 populate_Doc_freq_dict()
 avgDocLen = find_avg_doc_len(unigram_tf)
 createIndex()
 try:
    for key,val in (sorted (query_key.iteritems())):
        calc_scores(val,key,avgDocLen)
 except:
    print "Please make sure you have entered query in the form 1 query term"
 f.close()
main("Query-Terms.txt")











