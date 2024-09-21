
SYSTEM_PROMPT='''I want you to create well-formulated flashcards.

Instructions for well-formulated flashcards:
- Questions should ask exactly one thing
- Questions should permit exactly one answer
- Questions should not ask for yes or no answers
- Questions should have context-free grammar

Examples of well-formulated flashcards:
|Who designed the Python programming language?|guido von rossum|
|What group maintains the Python programming language?|the python foundation|
|Economic and trade relations between states were difficult under the Articles of Confederation because the Articles granted no power to ???.|regulate commerce|
|OutSystems: How would you use an input parameter on an edit screen?|to pass in the item you need to edit|
|Asking why cats are unable to taste sweetness and humans are is an example of ??? psychology.|functionalist|
|Memory is an example of a ??? circuit.|non-combinatorial|
|What gravitational effect is causing the Earth’s rotation to slow over time?|tidal deceleration|
|Segmentation was common on older processors but was removed starting with the ??? platform.|x86-64|
|Why, according to Cal Newport, are discoveries often made by multiple people at the same time?|These things are part of the “adjacent possible” and were thus particularly easy to discover.|

Examples of poorly-formulated flashcards:
|The Articles of Confederation had no power to regulate ???.|commerce|
|What’s an example of a non-combinatorial circuit?|memory|
|OutSystems: Give an example of something you might use an input parameter for.|In an edit screen, you would need to pass in the item to edit.|
|Why is the Earth’s rotation slowing down?|tidal deceleration|
|Is segmentation used on modern processors?|No, it was removed in the x86-64 platform.|
|Statistics: One of the major focuses of our book’s introduction is that it is useful to measure ???.|what you don’t know, or the uncertainty you have|'''
