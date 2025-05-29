from doc_scrap import doc_scrap

sort_doc = doc_scrap()

def get_val():
    for n in sort_doc:
        print(n[5:11])

print(get_val())