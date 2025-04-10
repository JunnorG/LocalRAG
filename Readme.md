## Install 
1. run 
    
    `pip install -r requirements.txt` 

    If you fail to install the package without vpn, then you should switch the datasource. Like
    
   `pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

## Start

### UploadFiles
upload your files like pdf to generate the embedding vectors for the content. The vector store is local Sqlite3 by default.

### QA
Ask question and generate the answer according to the contents which from uploaded files.