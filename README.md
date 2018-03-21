# Semantic-Analysis-for-Narrative-Texts
Report of Summer research fellowship program at Indian Academy of Sciences 2017
<br>
[Link to the file](https://github.com/Upa005/Semantic-Analysis-for-Narrative-Texts/blob/master/Semantic%20Analysis%20for%20Narrative%20Texts.pdf)

Semantic analysis is the process of analysing the semantic of a text, i.e. determining the meaning of the text and analysing it. To measure the semantics
of a text, certain semantic measures have been developed. According to
the literature of natural language processing, semantic measure can be
any theoretical tool, mathematical function, algorithm or approach which
enables the comparison of semantic entities according to semantic evidence.
Following are the semantic proxies used for semantic measures:<br>
* Corpora of texts - It consists of unstructured or semi-structured
texts. These texts contain informal evidence of semantic relationships.
For example text, dictionaries, etc.
* Ontologies - It consists of a large range of knowledge models i.e. structured vocabularies, highly formal ontologies, etc.
For semantic analysis of narrative texts, we are extracting a list of keywords
from a text that is semantically similar to that text.<br>
![Similarity](https://github.com/Upa005/Semantic-Analysis-for-Narrative-Texts/blob/master/Images/similarity.PNG)

We are proposing the following five feature for keywords extraction:
* Word frequency
* Sectional weight
* PoS tags
* Co-occurrence
* Sequencing

Following is a story, 
>The Monkey and the Wedge' from Panchatantra
which is an ancient Indian collection of animal fables.
There was once a merchant who employed many carpenters and
masons to build a temple in his garden. Regularly, they would
start work in the morning and take a break for the mid-day meals,
and return to resume work till evening. One day, a group of mon-
key arrived at the site of the building and watched the workers
leaving for their mid-day meals. One of the carpenters was saw-
ing a huge log of wood. Since, it was only half-done; he placed
a wedge in between to prevent the log from closing up. He then
went along with the other workers for his meal. When all
the workers were gone, the monkeys came down from the trees
and started jumping around the site, and playing with the in-
struments. There was one monkey, who got curious about the
wedge placed between the log. He sat down on the log, and hav-
ing placed himself in between the half-split log, caught hold of
the wedge and started pulling at it. All of a sudden, the wedge
came out. As a result, the half-split log closed in and the mon-
key got caught in the gap of the log. As was his destiny, he was
severely wounded.The wise indeed say: One, who interferes in
other's work, surely comes to grief.

### Word frequency
Word frequency is one of the standard approaches used for keyword extrac-
tions. In narrative text, important characters and their actions are repeatedly
referred. Using word frequency as one of the features helps the algorithm to
identify key characters and their actions. But frequency alone can't be used
for summarization as in short narrative text relevant words are rarely re-
peated. Following is the list of keywords when only word frequency is taken
into consideration from the above mentioned Panchatantra Story:

>['log', 'wedge', 'one', 'he', 'workers', 'work', 'placed', 'monkey',
'his', 'started', 'site', 'mid-day', 'meals', 'it', 'half-split', 'caught',
'carpenters', 'came', 'wounded', 'wood', 'wise', 'went', 'watched',
'trees', 'they', 'temple', 'surely', 'sudden', 'start', 'severely', 'say',
'sawing', 'sat', 'return', 'resume', 'result', 'pulling']
