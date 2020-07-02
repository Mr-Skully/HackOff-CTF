# What the F (150pts)
#### Author: [Bichu](https://github.com/ben-jnr)
## Challenge
`Woah! That is so weird! I swear that I saw him use this to display the flag. But I don't know how!`  
`Can you help me? Pretty Please???`  

`HINT: It can be executed somewhere.`
## Solution
We are provided with `weird.txt`.

This is code written in *JSFuck*.

For people hearing about JSFuck for the first time, it is a subset of Javascript that allows you to code using just six characters.

To get the flag, you can decode it using any online tool.

After decoding, we get:
```
console.log('hackoff{d@mn_js}')
```
## Alternate Solution
###### Submitted by [Emil](https://github.com/TheSkullCrushr)
JSFuck is used, as only six special characters make up the whole file.

You can run it on the JS Console of your browser (since it works just like ordinary Javascript code), and the flag is displayed in the output.

### flag : hackoff{d@mn_js}
