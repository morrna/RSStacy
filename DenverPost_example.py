from RSStacy import *

DPcorpus = FeedCorpus('en')
DPurl = 'http://www.denverpost.com/feed/'
print('Loading feed from '+DPurl)
DPcorpus.from_feed(DPurl)
print(DPcorpus)

print('\nDocument stats:')
for doc in DPcorpus:
    print(doc.metadata['title'])
    print( ('Word count: {}  '\
            +'Flesch-Kincaid level: {:.1f}')\
            .format(doc.readability_stats['n_unique_words'],\
                    doc.readability_stats['flesch_kincaid_grade_level']\
                    )\
        )
