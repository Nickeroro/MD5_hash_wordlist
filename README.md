# MD5_hash_wordlist
## MD5_wordlist will try to find the salted MD5 hashed messages you've given <3

Exemple of salted + MD5 hashed messages can be found there:
> /etc/shadow
(Linux password storage)

You should have something like:
> smithj:Ep6mckrOLChF.:10063:0:99999:7:::

As with the passwd file, each field in the shadow file is also separated with ":" colon characters, and are as follows:

* Username, up to 8 characters. Case-sensitive, usually all lowercase. A direct match to the username in the /etc/passwd file.

* Password, 13 character encrypted. A blank entry (eg. ::) indicates a password is not required to log in (usually a bad idea), and a "*" entry (eg. :*:) indicates the account has been disabled.

* The number of days (since January 1, 1970) since the password was last changed.

* The number of days before password may be changed (0 indicates it may be changed at any time)

* The number of days after which password must be changed (99999 indicates user can keep his or her password unchanged for many, many years)

* The number of days to warn user of an expiring password (7 for a full week)

* The number of days after password expires that account is disabled

* The number of days since January 1, 1970 that an account has been disabled

* A reserved field for possible future use
