# We Create Our Own Demons (150pts)
#### Author: [Emil](https://github.com/TheSkullCrushr)
## Challenge
`
There are clues hidden in every nook and corner! All you've got to do is observe..`  
`"Bonne chance."`  

`HINT: Something's French.
`

## Solution
`Something's French` and `there are clues in every corner` are the two important hints for this challenge.

The name of the challenge looks like a quote. A quick Google search reveals that it is a quote by Tony Stark, aka, Iron Man.

After another round of searches for famous ciphers, we come across Vigenère Cipher, which is named after Blaise de Vigenère, a **French** cryptographer.

Using an online tool, we can decode this cipher. Vigenère ciphers require a key to encrypt/decrypt. But it can easily be bruteforced with modern-day computers. But still, to make our lives easier, we can try some possible keywords.

After a bit of trial and error, we can see that `STARK` was the key used to encrypt the text. Decrypting with `STARK` yeilds us the flag.

### flag : hackoff{even_dead_im_th3_her0}
