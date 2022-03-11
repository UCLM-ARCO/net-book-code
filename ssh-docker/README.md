Build container
---------------

```
laptop$ docker-compose up
[console blocked by the container SSH server]
```

Login container
---------------

```
laptop$ ssh user@172.20.0.2
user@172.20.0.2's password: secret
Linux viper 5.15.0-3-amd64 #1 SMP Debian 5.15.15-2 (2022-01-30) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Mar  9 20:27:30 2022 from 172.20.0.1
user@viper:~$
```

Authenticate by public key
---------------------------

```
laptop$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa):
Created directory '/home/user/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/user/.ssh/id_rsa.
Your public key has been saved in /home/user/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:luofEzKkKX0G/mXgXEYIZK5V3SSQJL/aTcadCnEY6fw user@viper
The key's randomart image is:
+---[RSA 2048]----+
|   .=o=*oo.      |
|   o +++...      |
|    +o* +        |
|   = BoO o .     |
|  o = X.S o      |
|   . * %Eo       |
|    . + =        |
|     .   o       |
|      ...        |
+----[SHA256]-----+
```

Create your `~/.ssh/config` file at 'laptop':

```
Host viper
    hostname 172.20.0.2
    User user
```


```
laptop$ ssh-copy-id viper
user@172.20.0.2's password: secret

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'viper'"
and check to make sure that only the key(s) you wanted were added.
```

```
laptop$ ssh user@viper
user@viper:~$
```


Authenticate by certificate
---------------------------

Remove private key at viper:

```
laptop$ ssh viper rm .ssh/authorized_keys
```


Get key and certificates from viper:

```
laptop$ scp user@viper:user_key* ~/.ssh/
user_key                           100% 1679     6.1MB/s   00:00
user_key-cert.pub                  100% 1496     5.8MB/s   00:00
user_key.pub                       100%  399     2.2MB/s   00:00
```

Tune  your `~/.ssh/config` file at 'laptop':

```
Host viper
    hostname 172.20.0.2
    User user
    IdentityFile ~/.ssh/user_key
```

And login in:

```
laptop$ ssh user@viper
user@viper:~$
```
