# Secret Operation Base

## Challenge prompt
```
Wanna hear the word on the streets? The aliens are already here! But we were wrong about their location. It's not Area 51. There are 5 bases of operation spread around the globe, and the location of the headquarters is hidden in this file. HINT: It's encoded more than once.
```
## **Solution**
```
We are provided with secretbaselocation.txt

So we are looking at some base encoded form.....

If you think too deep, you will be in a rabbit hole.
```
Valuable hint
```
There are 5 bases
```
Of course there is Base32,Base58,Base62,Base64 and Base85 ;total of 5 : but don't go there

```
Just base64 decode the text five times to get the flag.
You could use any online tools or simple script would do the trick
```
## I have made a python script to get the flag , please feel free to use it

```
python3 getFlag.py
```
Keep the python file and secretbaselocation.txt in same folder

## flag : hackoff{secret_base_is_in_area64}
