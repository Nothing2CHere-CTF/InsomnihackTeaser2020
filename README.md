# Insomni'hack Teaser (2020)
Insomni'hack Teaser - 2020

## Overview

**URL:** https://teaser.insomnihack.ch/ 
**Organisors:** Insomni'hack Team
**Duration:** 24 hours  
**Team mates:** Team Competition  

```
Title                         Category        Points  Flag
----------------------------- --------------- ------- ------------------------------------------------
Welcome                         Warmup          36     INS{Miss me with that fhisy line}
LowDeep                         Web             36     INS{Wh1le_ld_k1nd_0f_forg0t_ab0ut_th3_x_fl4g}

```
## Welcome

* **Category:** Warmup
* **Points:** 36

### Challenge

```
======================================================================
============   Welcome to the Insomni'Hack Teaser 2020!   ============
======================================================================

Give me an input whose md5sum starts with "hhhhhh" and get the flag ;)
```

> This year we added a Proof of Work to some of our challenges.
>
> Just run python pow.py <target>, were target is the value provided by the server and get the flag.
>
> [pow](/InsomnihackTeaser2020/pow.zip)
>
> nc welcome.insomnihack.ch 1337



### Solution

[rock_md5.py](/InsomnihackTeaser2020/rock_md5.py)

Ran rock_md5.py which reads lines from rockyou.txt, hashes them in MD5, and writes them to a new file hash.txt in the format word:md5sum.

grep :hhhhhh hash.txt

Enter the word into the nc shell.

[welcome.png](/InsomnihackTeaser2020/welcome.png)

**Flag**
```
INS{Miss me with that fhisy line}
```

---


## LowDeep

* **Category:** Web
* **Points:** 36

### Challenge

```
## LowDeep Plateform

That's our new plateform to perform ping the easy way.

Enter the IP address to ping:
```

> Try out our new ping platform: lowdeep.insomnihack.ch/(http://lowdeep.insomnihack.ch/)


### Solution

[lowdeep.png](/InsomnihackTeaser2020/lowdeep.png)

Checked if form was vulnerable to improperly formed input validation

Tried:
127.0.0.1 && ls -> Failed
127.0.0.1; ls -> Worked
1; ls -> Worked
1; cat print-flag -> Failed
1; ls -laR -> Found ping.php

Decided to try http://lowdeep.insomnihack.ch/robots.txt(/InsomnihackTeaser2020/robots.png)
As it had the /_res_/iron-fleet path found with the 'ls -laR' command, tried http://lowdeep.insomnihack.ch/print-flag, which downloaded the file (/InsomnihackTeaser2020/print-flag), which turned out to be an ELF file.

Running strings on the file revealed the flag.

**Flag**
```
INS{Wh1le_ld_k1nd_0f_forg0t_ab0ut_th3_x_fl4g}
```
---
