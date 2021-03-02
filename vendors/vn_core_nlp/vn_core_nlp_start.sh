#!/usr/bin/env bash

#load virtual environment
source ././../../../venv/bin/activate
vncorenlp -Xmx2g VnCoreNLP-1.1.1.jar -p 8888 -a "wseg,pos,ner,parse"
