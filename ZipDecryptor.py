#ZipDecrypter
#A tool which find the password of password-protected ZIP files from a custom password list.
#Author - WireBits

import sys
import time
import zipfile
import argparse
import threading

def main():
    try_count = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help="Name of Zip File")
    parser.add_argument('-p', help="Password List")
    args = parser.parse_args()

    if not args.f or not args.p:
        sys.exit()

    zip_file = zipfile.ZipFile(args.f)
    password_list = open(args.p, 'r')

    start_time = time.time()
    print("[+]Please Wait While Extracting...")

    for password in password_list.readlines():
        try_count += 1
        password = password.strip()

        zip_process = threading.Thread(target=extract_zip, args=(zip_file, password))
        zip_process.start()

    for thread in threading.enumerate():
        if thread != threading.main_thread():
            thread.join()

    print("[+]Tried:",try_count)
    end_time = time.time()
    print("[+]Duration:",end_time - start_time)

def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        print("[+]Password Found:",password)
        sys.exit(0)
    except Exception:
        pass

if __name__ == '__main__':
    main()