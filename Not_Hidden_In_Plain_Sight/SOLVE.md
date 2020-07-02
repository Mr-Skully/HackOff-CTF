# Not Hidden In Plain Sight (150pts)
#### Author: [Emil](https://github.com/TheSkullCrushr)
## Challenge
`All she said was, "There are some easter eggs hidden inside". I don't think she meant it literally.`

## Solution

We are provided with *broken_eggs.jpg.*

We will perform our primary analysis of the image file by opening it in a text-editor or using the `strings` command in Linux:
```
$ strings broken_eggs.jpg
```
We see `pass.txt` among the contents of *broken_eggs.jpg*.

Embedding the code of a zip file in an image is one of the most easy and primitive methods of steganography, so we'll start with that.

Rename *broken_eggs.__jpg__* to _broken_eggs.**zip**_.

Now upon opening the zip file using any archiver/compression tool, we can find that it actually was a **zip** file, and *pass.txt* is present inside the archive.
The flag is inside *pass.txt*.
### flag : hackoff{just_an0ther_easter_egg}
