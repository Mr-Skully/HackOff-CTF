# Anche Tu Brutale (100pts)
#### Author: [Emil](https://github.com/TheSkullCrushr)

## Challenge

`Friends, Romans, countrymen, lend me your ears;`  
`I come to bury Caesar, not to praise him.`  
`The evil that men do lives after them;`  
`The good is oft interred with their bones;`   

`And crack away...!!!` 
## Solution
The question name and description points us to Caesar Cipher, also known as the Shift Cipher which is one of the most common ciphers used.

Just by analyzing the ciphertext, we can figure out which part of the ciphertext is actually the encrypted flag.

Flag in ciphertext : `unpxbss{pnrfne_1birq_guvegrra}`

We expect ‘h’ to come first, but it’s ‘u’ in the ciphertext, a shift by 13 characters.
Shift all the alphabets back 13 places and you will get the flag.


### flag : hackoff{caesar_1oved_thirteen}
