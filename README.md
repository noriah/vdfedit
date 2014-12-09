vdfedit
==

Fast and Easy Python Valve Data File (VDF) Reader and Writer
 
<!-- [![Build Status](https://img.shields.io/travis/noriah/vdfedit.svg?branch=master&style=flat-square)](https://travis-ci.org/noriah/vdfedit)[![Coverage Status](https://img.shields.io/coveralls/noriah/vdfedit.svg?style=flat-square)](https://coveralls.io/r/noriah/vdfedit) -->
[![PyPI version](https://img.shields.io/pypi/v/vdfedit.svg?style=flat-square)](https://pypi.python.org/pypi/vdfedit)[![Downloads](https://img.shields.io/pypi/dm/vdfedit.svg?style=flat-square)](https://pypi.python.org/pypi/vdfedit)

###What is a VDF?
A VDF, or Valve Data File, is a file that uses Valve's KeyValues format.

https://developer.valvesoftware.com/wiki/KeyValues#File_Format
####Valve Files that use the KeyValues format
* .vdf (Valve Data File)
* .acf (Application Cache File)
* .vmt (Valve Material Type)
* Some .cfg (Configuration File), Usually those found in Source Engine bin Folder
* Some .txt (Text File), Usually those found in Source Engine bin Folder
* Some .res (Resource File) [NOT YET IMPLMENTED]

Installation
--

Requires PyVDF
```bash
$ pip install PyVDF
```

You will probably have to make vdfedit executable
```Bash
chmod +x vdfedit
```
Thats it.

What is vdfedit?
--
vdfedit is a program that makes use of [PyVDF] [1] to create an easy to use VDF editor.

Overview

```bash
$ vdfedit -h
usage: vdfedit [-h] [-o FILE] [-p] [-g key] [-s key=value] [-w] [-c]
               [-len int] [-d str] [--indent str] [--spacing str] [--condense]
               [--fast]
               FILE

Read and Write VDF KeyValue Files

positional arguments:
  FILE                  The file to Read

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --out FILE   The file to Write out to Defaults to the infile
  -p, --print           Print the file as groups of Paths.Key=Value
  -g key, --get key     Add a key to Search For
  -s key=value, --set key=value
                        Add/set a key-value pair in the vdf
  -w, --write           Write out the data regardless of setting a value.
  -c, --check           Check the file for validity
  -len int, --token-length int
                        Set the maximum token length. Larger values cause
                        slower searching, however smaller values can result in
                        errors. Defaults to 1200
  -d str, --delim str   Set the string used to separate found values. Defaults
                        to ','
  --indent str          Set the indention used when writing out a file.
                        Defaults to \t
  --spacing str         Set the spacing used when writing out a file. Defaults
                        to \t\t
  --condense, --condensed, --use-condensed
                        Use consensed output when writing a file
  --fast, --faster-reading
                        Use faster reading. **Note** If you write a file while
                        this option is set, your output will not be in the
                        same order as the original file
```

###Paths
Paths are what vdfedit uses to find and retrieve values.

####Reading Paths
Without any get or set options, the output will be a list of Keys and Values

Ex. `PathHead.NextPath.OneMoreLevel.Key Value`

Formatting Keys is a bit tricky
Any key that contains a period `.` must be enclosed by brackets `'[',']'`

####Getting/Setting Values from Paths

For each path that you want to search, place it after a `'-g'`, after the file name.

```Bash
$ vdfedit config.vdf -g Store.Software.apps.240.LastPlayed
16

$ vdfedit config.vdf -gStore.depots.241.CDN.[content1.steampowered.com].Expires
1399694892

$ vdfedit config.vdf -gStore.Software.apps."218_Black Mesa".LastPlayed
1400475046

$ vdfedit config.vdf -g Store.system.EnableGameOverlay \
-gStore.system.JumplistSettings \
-gStore.system.GameOverlayHomePage
1,52976,https://encrypted.google.com
```

You can set the seperator between each returned value by setting the `'-d'` argument

For each value that you want to set, place it and the path to it after a `'-s'`, after the file name.

```Bash
$ vdfedit config.vdf -s Store.Software.apps.240.LastPlayed=0000000000
```

If you want to write the new data to a different file, set the `'-o'` argument.

```Bash
$ vdfedit config.vdf -o config.new.vdf \
-s Store.Software.apps.240.LastPlayed=0000000000
```

[1]: https://github.com/noriah/PyVDF "PyVDF"
