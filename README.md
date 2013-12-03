vdfedit
==

Easy and fast Python Valve Data Format (VDF) Reader and Writer

###What is a VDF?
https://developer.valvesoftware.com/wiki/KeyValues#File_Format

What is vdfedit?
--
vdfedit is actually a program that makes use of my PyVDF library to create an easy to use editor.



Using VDF Edit is simple:
`vdfedit (filename)[,file to write to] [path[,nextpath]`

Using it alone will produce usage instructions.

###Paths
Paths are what vdfedit uses to find and retrieve keys.

Think of it like a maze,


####Reading Paths
With a file, it will list out all the key-value pairs in the file.

Ex. `PathHead.NextPath.OneMoreLevel.Key Value`

Formatting Values is a bit tricky
Any value that contains a comma `','` must be enclosed by brackes `'{}'`
To use a bracket in value, you must escape it: `'\{','\}'`

To get an example of how to format a file, find a vdf on your computer (Try in your steam folder), and run vdfedit with a '-g' after the filename. I dont recomend you do this on a very long file, also you cant uses these statements at command line unless you escape the spaces correctly

####Getting Paths
Inserting a path after the filename will return the value for that path, or nothing if the path was not found

