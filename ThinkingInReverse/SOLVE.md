# ThinkingInReverse

## Challenge prompt 
We are given a reverse.pyc file to work with.Lets decode and see what it holds ?
```
lst = list('rv')
s = input('Enter Key:')
if s == '':
    print('hmmm...interesting')
else:
    if len(s) == 10:
        if s[3:7] == '_1s_':
            if s[1] == str(int(3)):
                if s[(-2)] == str(int(0)):
                    if s[0] == lst[0]:
                        if s[2] == lst[1]:
                            if s[7] == chr(102):
                                if ord(s[9]) == 110:
                                    print('hackoff{' + s[::-1] + '}')
                            print('you were nearly there')
                    print('you are getting closer!')
            print("the decimal system isn't the only system out there")
        else:
            print('reading and patience is the key')
    else:
        print('how could that step possibly go wrong :(')
    
```

Now only thing we have to do is build up the flag from the source code.

I have used a python script to build up the flag. But the twist is that you have to revsere the flag and submit to get points

```python
python3 getFlag.py
```

## flag : hackoff{n0f_s1_v3r}