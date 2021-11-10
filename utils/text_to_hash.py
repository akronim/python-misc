import hashlib
import argparse


def main(text, hash_type):
    encoder = text.encode('utf_8')
    my_hash = ''

    if hash_type.lower() == 'md5':
        my_hash = hashlib.md5(encoder).hexdigest()
    elif hash_type.lower() == 'sha1':
        my_hash = hashlib.sha1(encoder).hexdigest()
    elif hash_type.lower() == 'sha224':
        my_hash = hashlib.sha224(encoder).hexdigest()
    elif hash_type.lower() == 'sha256':
        my_hash = hashlib.sha256(encoder).hexdigest()
    elif hash_type.lower() == 'sha384':
        my_hash = hashlib.sha384(encoder).hexdigest()
    elif hash_type.lower() == 'sha512':
        my_hash = hashlib.sha512(encoder).hexdigest()
    else:
        print('[!] The script does not support this hash type')
        exit(0)
    print("Your hash is: ", my_hash)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert text to hash')
    parser.add_argument('-t', '--text', dest='text', required=True)
    parser.add_argument('-T', '--Type', dest='type', required=True)
    args = parser.parse_args()

    txt = args.text
    hType = args.type
    main(txt, hType)

    # python3 text_to_hash.py -t 'hello' -T 'md5'
