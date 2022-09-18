cs_subject = {'bengali','english','literature','math'}

# remove duplicates
print(cs_subject)
print('english' in cs_subject)

art_subject = {'art','english','literature','design'}


print(cs_subject.intersection(art_subject))
print(cs_subject.difference(art_subject))
print(cs_subject.union(art_subject))