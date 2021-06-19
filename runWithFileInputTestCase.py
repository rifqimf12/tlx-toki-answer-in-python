#!/usr/bin/env python3
import sys
import os

args = sys.argv
if len(args) > 1:
    codeFilePath = args[1]
else:
    exit("You should provide which code to run on 1st argument")
if len(args) > 2:
    inputFilePath = args[2]
else:
    pathPrefix, fileName = codeFilePath.split("/")
    fileName = f"_{fileName.replace('.py', '.in')}"
    inputFilePath = f"{pathPrefix}/{fileName}"
    if not os.path.isfile(inputFilePath):
        exit(
            "File input should be provided either on 2nd argument or by place the file on the same path and name as code file with '_' prefix and '.in' extension"
        )
os.system(f'python3 "{codeFilePath}" < "{inputFilePath}"')
