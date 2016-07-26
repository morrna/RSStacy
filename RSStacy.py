import textacy.texts as ttx
import textacy.preprocess as pre
import feedparser as fp

class FeedCorpus(ttx.TextCorpus):
    """
    Extends textacy TextCorpus with methods for feeds
    """
    def from_feed(self, url):
        fdict = fp.parse(url)
        
        for entry in fdict.entries:
            # Each entry may have multiple pieces of content. Here they're just concatenated.
            body = ""
            for c in entry.content:
                body += " " + c.value

            # Preprocessing
            body = pre.preprocess_text(body, no_urls=True, no_emails=True, no_phone_numbers=True)
            
            metadata = {'title': entry.title,
                    'author': entry.author,
                    'date_updated': entry.updated,
                    'publication_title': fdict.feed.title}
            self.add_text(body, metadata = metadata)




