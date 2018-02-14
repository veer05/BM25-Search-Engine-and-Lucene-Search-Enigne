import requests
from bs4 import BeautifulSoup
import re
import time
import os
from string import maketrans
Remove_Punctuation = True
Do_Case_Folding = True


source_location = "C:\Users\Veer\Desktop\Info\Task 3"
destination_folder = "C:\Users\Veer\Desktop\Info\Task_3_parseddoc"

def remove_multiple_space(raw_content):
    content_with_single_space = re.sub("\s\s+", " ", raw_content)
    content_with_no_lines = re.sub("\n", " ",content_with_single_space)
    return content_with_no_lines


def remove_formula(content_with_space_removed):
    remove_formula = re.sub('{[^}]+}', '', content_with_space_removed)
    return remove_formula


def remove_citation(content_with_formula_removed):
    remove_citation = (re.sub('\[[0-9.,]*\]', '', content_with_formula_removed))
    return remove_citation


def remove_punctuation(remove_citation_from_content):
    incoming_exception = "!\"#$%&()*+/:;<=>?@[\]^_`{|}~?"
    cleaned_str = "                             "
    transform = maketrans(incoming_exception, cleaned_str)
    content_without_punctuation = remove_citation_from_content.translate(transform)
    return content_without_punctuation

def remove_special_punctuation(lower_case_content):
    removeexp = r"(?<=\D)[.,']|[.,'](?=\D)"
    cleaned_str = (re.sub(removeexp,'',lower_case_content))
    return cleaned_str

def remove_special_punctuation(lower_case_content):
    removeexp = r"(?<=\D)[.,']|[.,'](?=\D)"
    cleaned_str = (re.sub(removeexp,'',lower_case_content))
    return cleaned_str

def convert_to_lower(punctuation_removed):
    return punctuation_removed.lower()


def write_to_file(name,consider_special_punctuation):
    filename = name.split(".html")
    name = filename[0] + ".txt"
    temp_name = name.translate(maketrans("(),","   "))
    cleaned_name = re.sub('[\s]','',temp_name)
    #print(cleaned_name)
    f = open (destination_folder + '\\' + cleaned_name, 'w')
    f.write(consider_special_punctuation)
    f.close()


def generate_clean_corpus(filename,name):
    text_content = []
    raw_content = " "
    optional_parsing = []
    # Soup to parse the document (the Document has already been stripped of all reference, images etc.
    soup = BeautifulSoup(open (filename), "html.parser")

    #List of tags to consider while parsing
    tags_to_consider = ['h1','p','h2','h3','h4']
    for semantics in soup("semantics"):
        semantics.decompose()
    # GET all Content from body
    for body_content in soup.find_all(tags_to_consider):
            text_content.append(body_content.text)

    #Convert it one String
    for entry in text_content:
        raw_content = " ".join(text_content)

    #Remove extra spaces and new line and remove new line char
    content_with_space_removed = remove_multiple_space(raw_content)

    #Remove Formulas in { }
    content_with_formula_removed = remove_formula(content_with_space_removed)

    #Remove Citations
    remove_citation_from_content = remove_citation(content_with_formula_removed)

    #Right Now remove_citation_from_content is the The content is free of markup notation, URL's, references to image,
    #table formula, navigational components

    #Convert from utf-8 to string
    str_with_punctuation = str(remove_citation_from_content.encode('ascii','ignore').decode('ascii'))

    #Remove all Punctuations other than "." "," and "-" " ' "
    #content_with_formula_removed
    punctuation_removed = remove_punctuation(str_with_punctuation)

    #convert to lower case
    if Do_Case_Folding:
        lower_case_content = convert_to_lower(punctuation_removed)

    #Retain , and . if it is in between number else remove
    if Remove_Punctuation:
        consider_special_punctuation = remove_special_punctuation(lower_case_content)
    #print(consider_special_punctuation)
    # Remove extra spaces and new line and remove new line char
    content_with_no_space = str(remove_multiple_space(consider_special_punctuation))
    print(name)
    write_to_file(name,content_with_no_space)
#    print(len(optional_parsing))



def main():
    folder = os.listdir(source_location)
    for file in folder:
        generate_clean_corpus(source_location + '\\' +file,file)




main()

