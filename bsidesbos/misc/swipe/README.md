1. Extract the "swipe" file locally. I personally did this:

	i) `` xxd -p swipe ``, copied the entire hex code
	ii) Used cyberchef to transform from hex and download the file

2. ``file output`` will give you that the extracted file is a Vim swap file

3. Rename file to ``output.swp`` and create a directory in ``/tmp/swipe/``

4. Recover vim file ``vim -r output.swp``

5. Use binwalk to extract the png file inside: ``binwalk --dd='.*' output.

6. Open up the PNG file and find the QR code that will eventually give you the flag. 
