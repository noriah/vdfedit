vdfedit
==

Easy and fast Python Valve Data Format (VDF) Reader and Writer

###What is a VDF?
A VDF, or Valve Data Format file, is a file that uses Valve's KeyValues format.

https://developer.valvesoftware.com/wiki/KeyValues#File_Format
####Valve Files that use the KeyValues format
* .vdf (Valve Data Format)
* .acf (Application Cache File)
* .vmt (Valve Material Type)
* Some .cfg (Configuration File), Usually those found in Source Engine bin Folder
* Some .txt (Text File), Usually those found in Source Engine bin Folder
* Some .res (Resource File) [NOT YET IMPLMENTED]


What is vdfedit?
--
vdfedit is a program that makes use of [PyVDF] [1] to create an easy to use VDF editor.
[1]: https://github.com/noriah/PyVDF "PyVDF"

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

To get an example of how to format a file, find a vdf on your computer (Try in your steam folder), and run vdfedit with a `'-g'` after the filename. I dont recomend you do this on a very long file, also you cant uses these statements at command line unless you escape the spaces correctly

####Getting Paths
Inserting a path after the filename will return the value for that path, or nothing if the path was not found

