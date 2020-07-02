# Secret Operations Base (150pts)
#### Author: [Emil](https://github.com/TheSkullCrushr)
## Challenge
`
Wanna hear the word on the streets? The aliens are already here!`  
`But we were wrong about their location. It's not Area 51.`  
`There are 5 bases of operation spread around the globe, and the location of the headquarters is hidden in this file.`  

`HINT: It's encoded more than once.
`
## Solution
The clues to be discovered from the question are:
  1. Some form of base-encoding is used
  2. It is encoded more than once using the same or maybe different encoding method.

We will try decoding the text using Base64, as it is one of the most used encoding schemes. And as there **5** *secret bases*, we'll try decoding it 5 times using base64, and presto - we get the flag.

(You could use any online tools for decoding or this [simple script](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Secret_Operations_Base/getFlag.py) by [Ajay](https://github.com/ajaysram))

### flag : hackoff{secret_base_is_in_area64}
