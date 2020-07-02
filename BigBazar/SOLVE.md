# BigBazar (250pts)
#### Author: [Ajay](https://github.com/ajaysram)
## Challenge
`Canonnically V_Controls everything `
## Solution

Lets unzip and explore:
```bash
tar -xvf BigBazar.tar.gz
```

Moving inside we find a text. Lets read `hacker.txt`
```
Well,well,well............Look at that !, I have the flag and i'll delete it. Hope you could get it before me :C ...
```

Hmmm.. Let's look if anything else have been extracted. Some hints must be there.

In Linux, if you are inside the folder, look all the files, if hidden files are not shown use shortcut Ctrl+H

If you are using terminal  type : 
```bash
ls -la
```

Whoa, there is a `.bzr` directory

Googling `.bzr` we found that it belongs to Bazaar, a version contol system by *Canonical*.

Let's install it first.

```bash
sudo apt install bzr
```

Similar to git, we can revert back to a previous state; just google for the documentation.

  1. Read logs
```
$ bzr log

Output:

revno: 2
committer: webDev <webdev@test.com>
branch nick: files
timestamp: Fri 2020-06-26 17:25:28 +0530
message:
  flag has been deleted
------------------------------------------------------------
revno: 1
committer: webDev <webdev@test.com>
branch nick: files
timestamp: Fri 2020-06-26 17:22:50 +0530
message:
  Flag is created, hope it'll be safe

```
  2. Lets revert back and get the flag

```
bzr revrt -r1

Output:

+N flag.txt
-D hacker.txt
```

So we have our flag, lets read flag.txt

### flag : hackoff{v3rs10n_c0nTr0l5_c@n_d0_mor3_7han_U_kn0w}
