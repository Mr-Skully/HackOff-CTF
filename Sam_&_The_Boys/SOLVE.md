# Sam And The Boys (150pts)
#### Author: [Emil](https://github.com/TheSkullCrushr)
## Challenge
`Sam used to work as a cyptographer for our Forensics & Cryptanalysis Wing, but he's now retired.`  
`He in a band now! And he can make some pretty cool tunes.. Check it out.`  
`But you know what they say, old habits die hard. Just keep an eye on him.`  

## Solution
When we listen to the given audio file, we hear beeps of varying durations somewhere along the middle of the song.
This is **Morse code**.
If only the Morse code was present in the file, we could've uploaded it to some online decryption site to get the result. But since there is a song playing in the background, we'll have to figure this one out ourselves.

Longer beeps mean dashes and short beeps mean dots.
![Morse](https://github.com/TheSkullCrushr/HackOff-CTF/raw/master/Sam_%26_The_Boys/Screenshots/morse.png)  

For the full table, visit [this page](https://electropeak.com/learn/morse-code-communication-using-arduino/).
After converting all the beeps into Morse code, and then into plaintext, we get `bips-and-beeps`.

### flag : hackoff{bips-and-beeps}
