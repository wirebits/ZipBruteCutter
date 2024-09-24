# ZipBruteCutter
A tool which find the password of password-protected ZIP files from a custom password list.

<h1>Setup</h1>
Make sure the python is installed on your system (Windows/Linux/MacOS).<br>

<h1>Tested Systems</h1>
The tool is currently tested on : <br>
1. Windows (10)<br>
The testing is going on different systems.

<h1>Install and Run</h1>
1. Download or Clone the Repository.<br>
2. Open that folder in Terminal (Linux/MacOS) or CMD/Powershell (Windows).<br>
3. Type the following command : <br><br>
<i>

For Windows<br>

```
python zipdecryptor.py -f "name_of_zipfile.zip/path_of_the_zip_file_with_filename.zip" -p "name_of_passsword_list.txt"
```
</i>

<i>
For Linux/MacOS<br><br>

```
./python zipdecryptor.py -f "name_of_zipfile.zip/path_of_the_zip_file_with_filename.zip" -p "name_of_passsword_list.txt"
```
</i><br>
5. Hit enter.<br>
6. After sometimes, the ZIP file password is cracked.

# Includes
There is <b>password_list.txt</b> file which contain some passwords to decrypt ZIP files.<br>
We can add more passwords in this file or create your own password list according to your need.

<h1>Key Features</h1>
<b>1. It works on any password list.</b><br>
<b>2. When it found the password, then it automatically open the ZIP file and extract the files from it.</b><br>
