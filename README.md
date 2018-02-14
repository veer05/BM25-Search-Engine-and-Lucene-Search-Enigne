steps to follow :

1) Install Python 2.7.14
2) import requests
3) import from bs4 import BeautifulSoup
4) import re
5) import time
6) import os
7) from string import maketrans

______________________________________________________________________________________________

-> Make sure the python file is present in the working directory
--> To run the program type 
    python Bm25.py
_______________________________________________________________________________________________
MAKE SURE THE DESTINATION AND SOURCE PATH IS CHANGED TO REFLECT THE HOST SOURCE FILE LOCATION AND 
HOST DESTINATION FILE LOCATION

Source Code : Tokenise_doc.py and Inverted_index.py FOR INDEX CREATION 
Source Code : Bm25.py for HW-4(Task 2) Retrieval Model
Source Code : Hw4.java is the Lucene Retrival Model

Hw4.java :
Contains code to index the raw documents from Hw3 Task 3, and using this index, Perform search for all queries provided in 
Task 2 of Hw4

The queries are supplied form Query-Terms.txt
BM25.py  -->
Contains the code for Bm25 retrieval model which provides ranked list of documents for a file with one or more queries.
The queries are supplied form Query-Terms.txt
The info about the flow of program is provided below
The info about BM25 implementation is provided in BM25 Implentation file
(Note the query supplied are case-folded since our index is also case-folded)

Tokenise_doc.py --> 
containts the code to clean the document i.e, remove unwanted sections from the corpus
remove images and other unwanted sections that do not hold relevant information

Inverted_index.py --> 
Contains the code to generate unigram, bigram and trigram inverted index and later use these
index to create unigram-tf,unigram-df,bigram-tf,bigram-df,trigram-tf,trigram-df

NOTE : There is also code to store the filename and the number of words in (unigram,bigram, trigram) the file has
AND The Output of Tokenise should be provided as input for Inverted_index.py

TEXT FILE INFORMATION 
Task 2      : Unigram_inverted_index.txt,Bigram-File-Token-Count.txt, Trigram_inverted_index.txt,
		      Unigram-TF.txt,Unigram-DF.txt,Bigram-TF.txt,Bigram-DF.txt,Trigram-DF.txt,	Trigram-TF.txt,
			  BM25_Unigram_Casefolding_query_res.txt, Query-Terms.txt
			(Optional Files, Unigram-File-Token-Count.txt, Trigram-File-Token-Count.txt,Bigram-File-Token-Count.txt)
Task 1      : Lucene_Result.txt
______________________________________________________________________________________________________________________________________________________
Other Files : Comparision.txt,BM25 Implentation. 


IMPORTANT NOTES BEFORE RUNNING PROGRAM :

 1) Make Sure the DOC FED TO Inverted_index.py ARE FILES GENERATED FORM Tokenise_doc.py,
    Since It may affect the program the type of input file it takes and
    the operation it performs.
 2) "Inverted_index.py" consumes the CORPUS GENERATED FORM Tokenise_doc.py to generate unigram inverted index, bigram inverted index,
    trigram inverted index.
 3) When running Bm25.py program Make sure all the inverted index is present in the same folder, and Query file which I have attached 
    named (Query-Term.txt) is in the same file. Beacuse that file is read for query 
	The query provided is in format 
	QueriId Query
	
IMPORTANT NOTES FOR RUNNING TASK 1 Lucene : 
  1) When you run the java program, you will be prompted to enter the destination folder that you want to create index in 
     (make sure that the foler does not have any previouos index content or make sure the folder is empty)
  2) Then you are prompted to enter the path of folder that has the cleaned corpus. 
  3) After the corpus is tokensised and indexed you will be prompted to enter the querty text file
     Please provide the location provided as Example :Z:\\Info\\Task 4\\Query-Terms.txt
  4) The result will be genreated in "Lucene_Result.txt" in the project source location.

IMPORTANT NOTES FOR RUNNING TASK 2 My_Retrieval_Model(BM25_Unigram_Casefolding)
  1) When you are running the Bm25.py make sure Query-Terms.txt is in the same folder as the 
     python file.
  
  "Tokenise_doc.py" Takes html files --> Generates .txt cleaned corupus that does not contain noise
  "Inverted_index.py" Takes the cleaned documents from Tokenise_doc and generates inverted index and term frequency and document frequency
   for (Unigram, Bigram and Trigram)
   I have made changes to these files from the previous submittion in HW3. 
   Inverted index and document frequency have chaged
   and (ngram-File-Token-Count contains the total length of each document (earlier contained number of tokens each file had)
	Run Tokenise_doc.py -> (Feed this corpus) to Inverted_index.py (which will generate index) -> BM25 -> Ranking
	
Here I have mentioned the changes I have made in the indexer program. 
Detailed information about Bm25.py and Hw.py have been given in the implementation.txt which has further details.
The general info about the flow of logic is provided below 
 
Text FIle description : 

Lucene_Result : Contains the 9 Tables one for each query in format (one for each query for Lucene HW4 Task1) 
"query_id Q0 doc_id rank BM25_score system_name"
One table is associated with one query 
And table is ranked in decreasing order of Bm25 Score (More popular to less popular)
 
BM25_Unigram_Casefolding_query_res : Contains  the 9 table one for each query in the format (one for each query for Lucene HW4 Task2) 
"query_id Q0 doc_id rank BM25_score system_name"
One table is associated with one query 
And table is ranked in decreasing order of Bm25 Score (More popular to less popular)

Uni/Bi/Tri/gram_inverted_index.txt : Contains the inverted index 
Uni/Bi/Tri/gram-DF.txt  : Contains the term and document frequency
Uni/Bi/Tri/gram-TF.txt  : Contains the term and the number of times they appear in the corpus.
Uni/Bi/Tri/gram-File-Token_Count.txt : Contains the filename and their length (document length for each document)

Query-Terms.txt : Contains the 9 queries to be supplied 
The Query entry are of form 
queryid Query 
1 hurricane isabel damage

Comparision.txt : A brief discussion comparing the top 5 results between the two search engines for each query

BM25 Implentation :report describing my implementation of BM25 Formula.
General Flow of Logic in the program ....
 I initially read the query and then if that query has multiple terms I get the list of files 
 that word appears in 
 After looping for each terrm I get a list of file that contain the query words
 Next, I calculate the Bm25 Score for each document containing 
 the query term (The code for calculating BM25 Score is in BM25 Implentation file)
 after the score is calculated for each document then, I get the top score and documents 
 associated with the score.

 