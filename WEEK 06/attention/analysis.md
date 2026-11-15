# Analysis

I could not complete the attention-head observations in this environment. The available interpreter is Python 3.13.9, while the project recommends Python 3.12, and TensorFlow is not installed. Without running the provided BERT model and inspecting its generated diagrams, naming specific layers and heads would be guesswork. I have left the empirical conclusions open rather than present unverified claims as observations.

These are two sentence pairs I would use to investigate relationships beyond the next-token and adverb-to-verb patterns described in the project. After running `mask.py` on each sentence and comparing its diagrams, record a layer and head only if its attention consistently supports the proposed relationship.

## Direct and indirect objects

Compare attention from the verb and its arguments in these sentences:

- The teacher gave the student a book.
- The teacher sent the child a letter.

I would look for a head that directs attention from each verb toward its object or objects across both examples.

## Prepositions and their objects

Compare the preposition with the noun phrase that follows it:

- The keys beside the lamp were missing.
- A cat under the table was sleeping.

I would look for a head that links each preposition to the noun phrase completing it. The relevant layer and head still need to be identified from actual diagrams.
