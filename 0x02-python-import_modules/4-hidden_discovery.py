#!/usr/bin/python3
if __name__ == "__main__":
    """Print all hidden diectories"""
    from hidden_4 impory *

    for i in dir(hidden_4) :
        if i[:2] != "__":
            print(i)
