vdfedit
==

Easy and fast Python Valve Data File (VDF) Reader and Writer

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
You need to get [PyVDF] [1]. Place `PyVDF.py` into the root folder vdfedit-master folder.
```
vdfedit
├── vdfedit
├── PyVDF.py
```
You will probably have to make vdfedit executable
```Bash
chmod +x vdfedit
```
Thats it.

What is vdfedit?
--
vdfedit is a program that makes use of [PyVDF] [1] to create an easy to use VDF editor.

Using VDF Edit is simple:
```Bash
usage: vdfedit [-h] [-o FILE] [-g key] [-s key=value] [-d str] FILE
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
