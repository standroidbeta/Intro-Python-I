"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

with open('/home/seek/Documents/GitHub/Intro-Python-I/src/foo.txt', 'r') as f:
    print(f.read())

f.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

with open('/home/seek/Documents/GitHub/Intro-Python-I/src/bar.txt', 'w') as fb:
    arbitrary_lines = ['This is the first arbitrary line.\n', 'This is the second arbitrary line.\n',
                       'This is the third arbitrary line.']
    fb.writelines(arbitrary_lines)
    fb.close()

with open('/home/seek/Documents/GitHub/Intro-Python-I/src/bar.txt', 'r') as fb:
    print(fb.read())

fb.close()