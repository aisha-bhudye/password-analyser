
import hashlib, bcrypt, time

def brute_force_md5(target_hash, wordlist):
    start = time.time()
    for word in wordlist:
        if hashlib.md5(word.encode()).hexdigest() == target_hash:
            return word, time.time() - start
    return None, time.time() - start

def brute_force_bcrypt(target_hash, wordlist):
    start = time.time()
    for word in wordlist:
        if bcrypt.checkpw(word.encode(), target_hash.encode()):
            return word, time.time() - start
    return None, time.time() - start
