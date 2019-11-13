Title: Russell and Norvig, Chapter 1
Date: 2019-11-13
Category: AI
Tags: ai, learning
Slug: russell-norvig-1
Author: Brian Keating
Summary: Chapter 1 of Russel and Norvig's classic AI text.

Chapter 1 is a fairly short introductory chapter that describes the history of AI (going back to Aristotle), and puts this interdisciplinary field in context. Obviously AI owes a lot to computer science, philosophy, mathematical logic, cognitive science, control theory, etc. The authors make clear that the topic of the book is *rational agents*, where "rational" means that the agent makes optimal descisions, as opposed to attempting to imitate humans descionmaking. Note that my edition of the book was printed in 2014, right around the time that [CNNs started crushing ImageNet](https://en.wikipedia.org/wiki/AlexNet). The book identifies the 2010s as the era of big data and a more scientific approach via standardized tasks but they don't mention ImageNet specifically.

[This John McCarthy paper](https://www.cs.cornell.edu/selman/cs672/readings/mccarthy-upd.pdf) is mentioned prominently, as is [Turing's](https://www.csee.umbc.edu/courses/471/papers/turing.pdf).

## Excercises

1. Define in your own words: (a) intelligence, (b) artificial intelligence, (c) agent, (d) rationality, (e) logical reasoning.
2. Read [Turing’s original paper on AI]((https://www.csee.umbc.edu/courses/471/papers/turing.pdf)) (Turing, 1950). In the paper, he discusses several objections to his proposed enterprise and his test for intelligence. Which objections still carry weight? Are his refutations valid? Can you think of new objections arising from developments since he wrote the paper? In the paper, he predicts that, by the year 2000, a computer will have a 30% chance of passing a five-minute Turing Test with an unskilled interrogator. What chance do you think a computer would have today? In another 50 years?
3. Are reflex actions (such as flinching from a hot stove) rational? Are they intelligent?
4. Suppose we extend Evans’s A NALOGY program so that it can score 200 on a standard IQ test. Would we then have a program more intelligent than a human? Explain.
5. The neural structure of the sea slug Aplysia has been widely studied (first by Nobel Laureate Eric Kandel) because it has only about 20,000 neurons, most of them large and easily manipulated. Assuming that the cycle time for an Aplysia neuron is roughly the same as for a human neuron, how does the computational power, in terms of memory updates per second, compare with the high-end computer described in Figure 1.3?
6. How could introspection—reporting on one’s inner thoughts—be inaccurate? Could I be wrong about what I’m thinking? Discuss.
7. To what extent are the following computer systems instances of artificial intelligence:
    * Supermarket bar code scanners.
    * Web search engines.
    * Voice-activated telephone menus.
    * Internet routing algorithms that respond dynamically to the state of the network.
8. Many of the computational models of cognitive activities that have been proposed involve quite complex mathematical operations, such as convolving an image with a Gaussian or finding a minimum of the entropy function. Most humans (and certainly all animals) never learn this kind of mathematics at all, almost no one learns it before college, and almost no one can compute the convolution of a function with a Gaussian in their head. What sense does it make to say that the “vision system” is doing this kind of mathematics, whereas the actual person has no idea how to do it?
9. Why would evolution tend to result in systems that act rationally? What goals are such systems designed to achieve?
10. Is AI a science, or is it engineering? Or neither or both? Explain.
11. “Surely computers cannot be intelligent—they can do only what their programmers tell them.” Is the latter statement true, and does it imply the former?
12. “Surely animals cannot be intelligent—they can do only what their genes tell them.” Is the latter statement true, and does it imply the former?
13. “Surely animals, humans, and computers cannot be intelligent—they can do only what their constituent atoms are told to do by the laws of physics.” Is the latter statement true, and does it imply the former?
14. Examine the AI literature to discover whether the following tasks can currently be solved by computers:
    - Playing a decent game of table tennis (Ping-Pong).
    - Driving in the center of Cairo, Egypt.
    - Driving in Victorville, California.
    - Buying a week’s worth of groceries at the market.
    - Buying a week’s worth of groceries on the Web.
    - Playing a decent game of bridge at a competitive level.
    - Discovering and proving new mathematical theorems.
    - Writing an intentionally funny story.
    - Giving competent legal advice in a specialized area of law.
    - Translating spoken English into spoken Swedish in real time.
    - Performing a complex surgical operation.
  For the currently infeasible tasks, try to find out what the difficulties are and predict when, if
  ever, they will be overcome.
15. Various subfields of AI have held contests by defining a standard task and inviting researchers to do their best. Examples include the DARPA Grand Challenge for robotic cars, The International Planning Competition, the Robocup robotic soccer league, the TREC information retrieval event, and contests in machine translation, speech recognition. Investigate five of these contests, and describe the progress made over the years. To what degree have the contests advanced toe state of the art in AI? Do what degree do they hurt the field by drawing energy away from new ideas?