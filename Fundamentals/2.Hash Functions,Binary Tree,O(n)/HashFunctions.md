Can refer https://www.pythoncentral.io/hashing-strings-with-python/

## Hash Functions

A hash function is a function that takes input of a variable length sequence of bytes and converts it to a fixed length sequence. It is a one way function. This means if f is the hashing function .This is an irreversible process, once f(x) is created, which is fast and simple, obtaining x again will take long time.The value returned by a hash function is often called a hash, message digest, hash value, or checksum. Most of the time a hash function will produce unique output for a given input. However depending on the algorithm, there is a possibility to find a collision due to the mathematical theory behind these functions.

![alt text](https://s25033.pcdn.co/wp-content/uploads/2013/05/hash1-300x108.png)


Now suppose you want to hash the string "Hello Word" with the SHA1 Function, the result is 0a4d55a8d778e5022fab701977c5d840bbc486d0

![alt text](https://s25033.pcdn.co/wp-content/uploads/2013/05/hash2-300x65.png)


Hash functions are used inside some cryptographic algorithms, in digital signatures, message authentication codes, manipulation detection, fingerprints, checksums (message integrity check), hash tables, password storage and much more. You may need these functions to check for duplicate data or files, to check data integrity when you transmit information over a network, to securely store passwords in databases, or maybe some work related to cryptography.

Hash functions are not cryptographic protocol, they do not encrypt or decrypt information, but they are a fundamental part of many cryptographic protocols and tools.


### Some of the most used hash functions are:

 1)MD5: Message digest algorithm producing a 128 bit hash value. This is widely used to check data integrity. It is not suitable for use in other fields due to the security vulnerabilities of MD5.
 2)SHA: Group of algorithms designed by the U.S's NSA that are part of the U.S Federal Information processing standard. These algorithms are used widely in several cryptographic applications. The message length ranges from 160 bits to 512 bits.

The hashlib module, included in The Python Standard library is a module containing an interface to the most popular hashing algorithms. hashlib implements some of the algorithms, however if you have OpenSSL installed, hashlib is able to use this algorithms as well.

This code is made to work in Python 3.2 and above. If you want to run this examples in Python 2.x, just remove the algorithms_available and algorithms_guaranteed calls.

First, import the hashlib module:

         import hashlib

Now we use algorithms_available or algorithms_guaranteed to list the algorithms available.
	
         print(hashlib.algorithms_available)
         print(hashlib.algorithms_guaranteed)

The algorithms_available method lists all the algorithms available in the system, including the ones available trough OpenSSl. In this case you may see duplicate names in the list. algorithms_guaranteed only lists the algorithms present in the module. md5, sha1, sha224, sha256, sha384, sha512 are always present.
MD5

         import hashlib
         hash_object = hashlib.md5(b'Hello World')
         print(hash_object.hexdigest())

The code above takes the "Hello World" string and prints the HEX digest of that string. hexdigest returns a HEX string representing the hash, in case you need the sequence of bytes you should use digest instead.

It is important to note the "b" preceding the string literal, this converts the string to bytes, because the hashing function only takes a sequence of bytes as a parameter. In previous versions of the library, it used to take a string literal. So, if you need to take some input from the console, and hash this input, do not forget to encode the string in a sequence of bytes:

	
           import hashlib
           mystring = input('Enter String to hash: ')
           # Assumes the default UTF-8
           hash_object = hashlib.md5(mystring.encode())
           print(hash_object.hexdigest())

### SHA1

          import hashlib
          hash_object = hashlib.sha1(b'Hello World')
          hex_dig = hash_object.hexdigest()
          print(hex_dig)

### SHA224

          import hashlib
          hash_object = hashlib.sha224(b'Hello World')
          hex_dig = hash_object.hexdigest()
          print(hex_dig)

### SHA256
	
          import hashlib
          hash_object = hashlib.sha256(b'Hello World')
          hex_dig = hash_object.hexdigest()
          print(hex_dig)

### SHA384
	
          import hashlib
          hash_object = hashlib.sha384(b'Hello World')
          hex_dig = hash_object.hexdigest()
          print(hex_dig)

### SHA512

	
          import hashlib
          hash_object = hashlib.sha512(b'Hello World')
          hex_dig = hash_object.hexdigest()
          print(hex_dig)

### Using OpenSSL Algorithms

Now suppose you need an algorithm provided by OpenSSL. Using algorithms_available, we can find the name of the algorithm you want to use. In this case, "DSA" is available on my computer. You can then use the new and update methods:

	
         import hashlib
         hash_object = hashlib.new('DSA')
         hash_object.update(b'Hello World')
         print(hash_object.hexdigest())
