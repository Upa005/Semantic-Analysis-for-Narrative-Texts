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
The Monkey and the Wedge' from Panchatantra
which is an ancient Indian collection of animal fables.
> There was once a merchant who employed many carpenters and
masons to build a temple in his garden. Regularly, they would
start work in the morning and take a break for the mid-day meals,
and return to resume work till evening. One day, a group of monkey arrived at the site of the building and watched the workers
leaving for their mid-day meals. One of the carpenters was sawing a huge log of wood. Since, it was only half-done; he placed
a wedge in between to prevent the log from closing up. He then
went along with the other workers for his meal. When all
the workers were gone, the monkeys came down from the trees
and started jumping around the site, and playing with the instruments. There was one monkey, who got curious about the
wedge placed between the log. He sat down on the log, and having placed himself in between the half-split log, caught hold of
the wedge and started pulling at it. All of a sudden, the wedge
came out. As a result, the half-split log closed in and the monkey got caught in the gap of the log. As was his destiny, he was
severely wounded.The wise indeed say: One, who interferes in
other's work, surely comes to grief.

### Word frequency
Word frequency is one of the standard approaches used for keyword extractions. In narrative text, important characters and their actions are repeatedly
referred. Using word frequency as one of the features helps the algorithm to
identify key characters and their actions. But frequency alone can't be used
for summarization as in short narrative text relevant words are rarely repeated. Following is the list of keywords when only word frequency is taken
into consideration from the above mentioned Panchatantra Story:

>['log', 'wedge', 'one', 'he', 'workers', 'work', 'placed', 'monkey',
'his', 'started', 'site', 'mid-day', 'meals', 'it', 'half-split', 'caught',
'carpenters', 'came', 'wounded', 'wood', 'wise', 'went', 'watched',
'trees', 'they', 'temple', 'surely', 'sudden', 'start', 'severely', 'say',
'sawing', 'sat', 'return', 'resume', 'result', 'pulling']

It is not easy to formulate the story using the above list of keywords. Also,
there are dangling pronouns i.e he, his, it which are not useful for story
formulation. Hence, frequency alone cant be used for semantic similarity.

### Linguistic knowledge
Linguistic knowledge helps the algorithm to filter out non-relevant words according to their PoS tags. We have used only nouns and verbs as potential
keywords. Nouns in the passage tell us the important characters and hence
are helpful in framing the story. Verbs are also important in telling the task
the nouns are performing in the text. [14], [15] has shown the importance of
linguistic knowledge for identifcation of important keywords. Following is
the list of keywords using word frequency and Pos tags as features :
>['log', 'wedge', 'monkey', 'worker', 'work', 'start', 'place', 'meal',
'come', 'site', 'mid-day', 'half-split', 'caught', 'carpenter', 'wound',
'wood', 'wise', 'watch', 'tree', 'temple', 'say', 'saw', 'sat', 'return',
'resume', 'result', 'pull', 'prevent', 'play', "other's", 'morning',
'merchant', 'mason', 'leave', 'jumping', 'interferes', 'instrument']

Adding linguistic knowledge helps in bringing nouns and verbs from the
story but still the list of keywords is not similar to the story.

### Word co-occurrence
Word co-occurrence brings those words which are not frequently occurring
but are associated with prominent keywords. Hence, word co-occurrence
features recommend relevant word with lower word count as candidate keywords. Following is the list of the keywords when word frequency, PoS tags
> 'work', 'monkey', 'log', 'start', 'worker', 'meal', 'wedge', 'site',
'place', 'mid-day', 'day', 'come', 'build', 'half-split', 'caught', 'carpenter', 'watch', 'leave', 'group', 'building', 'arrive', 'tree', 'play',
'jumping', 'instrument', 'sat', 'return', 'resume', 'pull', 'morning',
'hold', 'break', 'temple', 'result', 'merchant', 'mason', 'garden']

Adding PoS tags, word co-occurrence and word frequency helps in bringing important keywords around which the story is revolving but still the
information presented in the above list is scatterd. Hence, sequencing of
keywords is important. Also, in narrative stories, we have found that certain
sections are more informational than other sections.

### Proposed Features
We have used word frequency, sectional weight, PoS tags, co-occurrence and
sequencing as features to extract keywords that are semantically similar to
the text. Following is the list of the keywords using our proposed features.
and word co-occurrence is taken into consideration
> ['merchant', 'employ', 'carpenter', 'mason', 'build', 'temple', 'garden', 'start', 'work', 'morning', 'break', 'meal', 'return', 'resume',
'day', 'group', 'monkey', 'arrive', 'site', 'building', 'watch', 'worker',
'leave', 'log', 'wood', 'half-done', 'place', 'wedge', 'close', 'come',
'catch', 'result', 'destiny', 'wise', 'say', 'interfere', 'grief']

The above list is semantically similar to the Panchatantra story mentioned
above. Weights are associated with the words according to their PoS tags,
frequency, sectional position and co-occurrence.

### Algorithm used
The algorithm proceeds as follows. First, the text is divided into sections.
Anaphors (pronouns) are resolved with recent antecedent available. Words
are then tokenized after stopwords are filtered. Words are annotated with
parts of speech (PoS) tags. In order to reduce the size of keywords, a syntactical filter is used which filter only nouns and verbs from the lexical unit list.
Weights are assigned to candidate keywords according to their position in the
text and the PoS tags associated with the word. The noun which appears
first in a sentence (dominating noun) is given more weight than the nouns
appearing later in the sentence. Nouns and verbs which are present in the
first and last sections are given more strength then present in other sections.

At the end, weights of the words are added and the word co-occurrence is further evaluated and added in the weights. After nal evaluation of weights,
top 17% of the words are preserved as keywords. The keywords are then
presented in a sequential order which will help the reader to formulate the
information.

![Figure2](https://github.com/Upa005/Semantic-Analysis-for-Narrative-Texts/blob/master/Images/weightvskeyword2.PNG)

This graph represents the weights associated with each keyword. `log', `work',
`monkey', `wedge'are appearing as the top keywords. The above mentioned
Panchatantra story is also revolving around the words monkey, log and wedge.

![Figure3](https://github.com/Upa005/Semantic-Analysis-for-Narrative-Texts/blob/master/Images/sectionvskeyword3.PNG)

This graph represents the co-occurrence of keywords in a sentence. Keywords
are listed sequentially. Different colour symbols are used to depict keywords
weights in different sections. Keywords like log, work, monkey, wedge are
appearing in multiple sections showing their importance in the story. The
graph represents that most of the words are occurring only in one section.
There are only a few words which are occurring in multiple sections showing
their importance in the story.
