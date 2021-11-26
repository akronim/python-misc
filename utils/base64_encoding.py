#!/usr/bin/env python

import base64

# convert bytes that have binary or text data into ASCII characters

def to_base64(str):
    string_bytes = str.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    
    print(base64_string)


def from_base64(b64_str):
    base64_bytes = b64_str.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes)
    str = string_bytes.decode("ascii")
    
    print(str)


to_base64("Lorem ipsum dolor sit amet")

from_base64("TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQ=")