# Digging up the past (150pts)
#### Author: [Emil](https://github.com/TheSkullCrushr)
## Challenge
`
The photographer in this picture, and the one who took it, are both secret agents who work undercover for us in Russia.`  
`They managed to covertly send us this picture. We think it means something, or maybe something was hidden inside.`  
`Can you extract the information? It's a matter of national security!!
`
## Solution
The description about the photographer suggests something interesting might be present in the EXIF data of the image.

EXIF is a standard for storing metadata in the image, like name of the camera, camera settings, photographer name, and so on.

We can see some basic properties by just checking the File Properties of the image file. But it is possible to store much more fields of metadata that what is visible there.  
We can use any online tool to extract the data, but we'll use [ExifTool by Phil Harvey](https://github.com/exiftool/exiftool).
```bash
exiftool photograph.jpg
```
Here is a small section of the output of the exiftool:
```
Y Cb Cr Positioning             : Centered
Preview Settings Name           : hackoff{lots_0f_secrets_in_exiftags}
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
```
## Alternate Solution
###### Submitted by [Ajay](https://github.com/ajaysram/)
We can use `strings` command in Linux or use a text editor to find the solution.
```bash
strings photographer.jpg | grep hackoff{*}
```

### flag : hackoff{lots_0f_secrets_in_exiftags}
