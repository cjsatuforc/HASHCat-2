try:
   from banner import banner,cor
except:
      print(cor[4]+"\n[!]:"+cor[3]+"Error: The [ "+cor[4]+"banner.py"+cor[3]+" ]Tool File Is Missing!!")
      exit(1)

def examples():
	banner()
	print(cor[5]+"""\n
\033[1;33m>EXAMPLES<:

#[MD5]:\033[1;37m ./HASHCat.py -H 5d41402abc4b2a76b9719d911017c592 -W /root/Desktop/wordlist.txt\033[1;32m
======================================================================================\033[1;33m
#[SHA1]:\033[1;37m ./HASHCat.py -H aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d -W /root/Desktop/wordlist.txt\033[1;32m
===============================================================================================\033[1;33m
#[SHA224]: \033[1;37m./HASHCat.py -H ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193 -W /root/wordlist.txt\033[1;32m
=========================================================================================================\033[1;33m
#[SHA256]:\033[1;37m ./HASHCat.py -H 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e7304-... -W /root/wordlist.txt\033[1;32m
=========================================================================================================\033[1;33m
#[SHA384]:\033[1;37m ./HASHCat.py -H 9b71d224bd62f3785d96d46ad3ea3df72519673ca72323c3d99d-... -W /root/wordlist.txt\033[1;32m
=========================================================================================================\033[1;33m
#[SHA512]:\033[1;37m ./HASHCat.py -H 9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2df-... -W /root/wordlist.txt\033[1;32m
=========================================================================================================\033[1;33m

#[Save Result]:\033[1;37m ./HASHCat.py -H aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d -W /root/wordlist.txt -O res.txt\033[1;32m
=========================================================================================================\033[1;33m

#[Try To Crack Online]:\033[1;37m ./HASHCat.py -H aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d --ON\033[1;32m
=====================================================================================\033[1;33m

#[File-HASH-SUM]: \033[1;37m./HASHCat.py -H sha1 -F /root/hashme.txt\033[1;32m
==========================================================\033[1;33m

#[Encode Text]: \033[1;37m./HASHCat.py -H SHA512 -T mypassword\033[1;32m
====================================================\033[1;33m




""")

