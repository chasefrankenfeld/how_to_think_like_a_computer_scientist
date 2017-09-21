import urllib.request


myfile = open("test.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()

mynewhandle = open("test.txt", "r")
while True:                                 # Keep reading forever
    theline = mynewhandle.readline()        # Try to read next line
    if len(theline) == 0:                   # if there are no more lines
        break                               # Leave the loop
    # Now process the line we'ver just read
    print(theline, end = "")

mynewhandle.close()

#f = open("friends.txt", "r")
#xs = f.readlines()
#f.close()

#xs.sort()

#g = open("sortedfriends.txt", "w")
#for v in xs:
#    g.write(v)
#g.close()


def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if text[0] == "#":
            continue
        # Any other processing logic would be placed here
        outfile.write(text)

    infile.close()
    outfile.close()

the_url = "http://xml.resources.org/public/rfc/txt/rfc793.txt"


def retrieve_page(url):
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.read())
    my_socket.close()
    return dta

#print(retrieve_page("http://www.crossfitmoorabbin.com"))