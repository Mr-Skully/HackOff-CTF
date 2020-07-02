# The Men Behind The Curtains (200pts)
#### Author: [Emil](https://github.com/TheSkullCrushr)
## Challenge
`"The eye is always caught by light, but the shadows have more to say.."`  
`The last man on Earth sat alone in a room. There was a knock on the door...`  
`If you want see the truth, you must be brave enough to look.`  
`You cannot hide from the Eye of Providence.`  

`HINT: Read up about hiding data in images.`

## Solution
There are a lot of references to the Illuminati.

Upon closer inspection of the image, we can see `empuraan` written on the hand of the character. This will be useful later on.

The *HINT* given suggests that some form of steganography is used.
We will use a steganography tool called [steghide](https://github.com/StefanoDeVuono/steghide) for this challenge.
```
$ steghide extract -sf Illuminati.jpg
Enter passphrase:
  wrote extracted data to "secret.txt".
```
When the tool asks for a password, we can use `empuraan`, which we discovered a while back.  
The flag can be found in the newly extracted file.

### flag : hackoff{5ecret5_hidden_between_th3_1ine5}
