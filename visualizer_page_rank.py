import os
import json
import nltk
import numpy
from IPython.display import IFrame
from IPython.core.display import display
import document_sum

BLOG_DATA = 'feed.json'

HTML_TEMPLATE = """<html>
    <head>
    <title>%s</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    </head>
    <body>%s</body>
</html>"""

blog_data = json.loads(open(BLOG_DATA).read())

for post in blog_data:
    #Uses previously defined summarize function
    post.update(document_sum.summarize(post['content']))

    # You could also store a version of the full post with key sentences marked up
    # for analysis with simple string replacement ...
    for summary_type in ['top_n_summary', 'mean_scored_summary']:
        post[summary_type + '_marked_up'] = '<p>%s</p>' % (post['content'], )
        for s in post[summary_type]:
            post[summary_type + '_marked_up'] = post[summary_type + '_marked_up'].replace(s, '<strong>%s</strong>' % (s, ))

        filename = post['title'].replace("?", "") + '.summary.' + summary_type + '.html'
        f = open(filename, 'w')
        html = HTML_TEMPLATE % (post['title'] + \
                'Summary', post[summary_type + '_marked_up'],)
        f.write(html.encode('utf-8'))
        f.close()
        print "Data written to", f.name
