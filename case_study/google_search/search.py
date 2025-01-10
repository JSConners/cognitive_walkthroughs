from googlesearch import search

query = "Passkeys pros and cons"

links =[]

for i in search(query, num_results=20, lang="en", ssl_verify=False):
    links.append(i)


for i in links:
    print(i)
