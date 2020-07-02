# Breaking Magician Code (200pts)
#### Author: [Emil](https://github.com/TheSkullCrushr)
## Challenge
`
Dr.Evil and his minions launched a cyber attack on our operations base. But by the time we got our defenses back up, he managed to corrupt some of our files. Can you fix it?
`  
`
HINT: All files have magic in the beginning.
`
## Solution
After  doing a Google search for **files** and **magic**, we come across the term *magic numbers.*

Every file begins a set of bits known as [Magic Numbers](https://en.wikipedia.org/wiki/File_format#Magic_number). It is a file format indicator, and for our PNG image file, it is definitely required for an image viewer to recognize it as a valid image file. The file format indicators are the first and last few bytes of a file.

The magic numbers are usually inspected in a hex-editor rather than a text editor (although that too is possible), because some file headers may contain non-printable or non-keyboard characters.

Th hex representation of the PNG file header is `89 50 4E 47`.

Let's open the file in [HexEdit](https://hexed.it/). We can see that the PNG magic numbers are not present at the beginning of the file. This might possibly be the reason the file is corrupted. Let's insert 4 bytes before the first existing byte, and change the default `00 00 00 00` values into `89 50 4E 47`.

![hexedit](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Breaking_The_Magicians_Code/Screenshots/hexedit.png)

Export the new file. Now it can be opened using any image viewer.

When we open the file, we see a QR Code. Scan the code to reveal the flag.
### flag : hackoff{magic_number$}
