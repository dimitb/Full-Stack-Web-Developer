import urllib

def read_text():
    quotes = open("/Users/brandondimit/Desktop/Dr_Who.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("PROFANITY ALERT!!!!!!!")
    elif "false" in output:
        print("This document has no curse words:)!!!HOORAY!!!")
    else:
        print("Could not scan this document:(")

    
read_text()
