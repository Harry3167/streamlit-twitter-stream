import os


class TwitterConfig:
    CONSUMER_KEY = os.environ.get('RZkg6cRcMnAmiw2PKkJ3FTnMY')
    CONSUMER_SECRET = os.environ.get('HCjDaUfRcer5u0bNR1f2BVMHAFl2c2kxhbkKJONqfTF18aNssF')
    ACCESS_TOKEN = os.environ.get('1579194428-bkEqGMTdoqRvsEsobHhLarnYkfa5IjhY9790F4h')
    ACCESS_TOKEN_SECRET = os.environ.get('AUUsnP1GCw7OrCY9qfXaBfflEnGKLT18uv53GxPik0FBq')


class DBConfig:
    USER = os.environ.get('freedb_twitterDB_user')
    PWORD = os.environ.get('m64dD?6Trm6BbGY')
    HOST = os.environ.get('sql.freedb.tech')


if __name__ == '__main__':
    print(type(os.environ.get('RZkg6cRcMnAmiw2PKkJ3FTnMY')))