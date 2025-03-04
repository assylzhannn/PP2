f = open("c:\\Users\\mrzha\\Documents\\PP2\\PP2\\lab6\\text.txt")
print(f.read())

def writesome(list_of_elements):
    with open(r"c:\\Users\\mrzha\Documents\\PP2\\PP2\\lab6\sometext.txt", '+a') as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
       
    
 

writesome([12345, 56789, 90987654, "dfghjkl","efrgf",34,34])