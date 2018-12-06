from passlib.hash import md5_crypt


if __name__ == '__main__':

    #give your Hashed MD5+salt password
    codefull = "$1$.rquYmlo$yFWfaSKplZmp1Id2VZ6iT1"
    #give the salt value
    salt = ".rquYmlo"
    #give the path of your wordlist
    file = open('Wordlist.txt', 'r', -1, 'ISO-8859-1')

    with file as fp:
        line = fp.readline()
        cnt = 2
        while line:
            line = (fp.readline()).rstrip("\n")
            line2 = (md5_crypt.using(salt=".rquYmlo").hash(line))
            cnt += 1
            print("{}: {}".format(cnt, line2))
            if line2 == codefull:
                print("GOTTCHA!!! \n the password is: " + line)
                break
