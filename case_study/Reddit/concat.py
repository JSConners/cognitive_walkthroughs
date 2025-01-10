import pandas as pd
import os, glob 

csv_file_path ='reddit_passkeys.csv'

df = pd.read_csv(csv_file_path)


comments = []

path = 'data/'
i=1
for file in glob.glob(os.path.join(path, '*.txt')):
    with open("data/data"+str(i)+".txt", 'r') as f: 
        data = f.read()  
        comments.append(data)
    i+=1
df['COMMENTS'] = comments

df.to_csv(csv_file_path, index=False)