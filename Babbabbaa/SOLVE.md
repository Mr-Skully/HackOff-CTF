# Babbabbaa (100pts)
#### Author: [Emil](https://github.com/TheSkullCrushr)
## Challenge
`
Seriously, what? I can't make head or tails of this!`  
`Do you think it's some kind of secret language? Or maybe code for something?  
`
## Solution
Bacon's cipher or the Baconian cipher is used in this challenge.
To encode a message, each letter of the plaintext is replaced by a group of five of the letters 'A' or 'B'. This replacement is a 5-bit binary encoding and is done according to the alphabet of the Baconian cipher.

On decoding with an online decoder we get the flag.

##### How to detect bacon's cipher ?
Generally there would be two characters in the text. Each word would have a length of five character.
In this challenge, A is used to denote 0 and B to denote 1 in binary.

##### Reference
[Read more about the Bacon Cipher on Wikipedia.](https://en.wikipedia.org/wiki/Bacon%27s_cipher)

### flag : hackoff{somuchforstrongencryption}
