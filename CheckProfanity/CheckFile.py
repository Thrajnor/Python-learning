import urllib

def reads():
    quotes = open("C:\ZamberJR\Programs\GitHubbed\CheckProfanity\Movequotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check(contents)

def check(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

reads()
