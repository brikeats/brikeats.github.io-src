Title: Russell and Norvig, Chapter 2
Date: 2019-
Category: AI
Tags: ai, learning
Slug: russell-norvig-2
Author: Brian Keating
Summary: Chapter 2 of Russel and Norvig's classic AI text.


# Exercises

2.1 Suppose that the performance measure is concerned with just the first T time steps of
the environment and ignores everything thereafter. Show that a rational agent’s action may
depend not just on the state of the environment but also on the time step it has reached.
2.2
Let us examine the rationality of various vacuum-cleaner agent functions.
a. Show that the simple vacuum-cleaner agent function described in Figure 2.3 is indeed
rational under the assumptions listed on page 38.
b. Describe a rational agent function for the case in which each movement costs one point.
Does the corresponding agent program require internal state?
c. Discuss possible agent designs for the cases in which clean squares can become dirty
and the geography of the environment is unknown. Does it make sense for the agent to
learn from its experience in these cases? If so, what should it learn? If not, why not?
2.3 For each of the following assertions, say whether it is true or false and support your
answer with examples or counterexamples where appropriate.
a. An agent that senses only partial information about the state cannot be perfectly rational.62
Chapter
2.
Intelligent Agents
b.
c.
d.
e.
f.
There exist task environments in which no pure reflex agent can behave rationally.
There exists a task environment in which every agent is rational.
The input to an agent program is the same as the input to the agent function.
Every agent function is implementable by some program/machine combination.
Suppose an agent selects its action uniformly at random from the set of possible actions.
There exists a deterministic task environment in which this agent is rational.
g. It is possible for a given agent to be perfectly rational in two distinct task environments.
h. Every agent is rational in an unobservable environment.
i. A perfectly rational poker-playing agent never loses.
2.4 For each of the following activities, give a PEAS description of the task environment
and characterize it in terms of the properties listed in Section 2.3.2.
•
•
•
•
•
•
•
•
Playing soccer.
Exploring the subsurface oceans of Titan.
Shopping for used AI books on the Internet.
Playing a tennis match.
Practicing tennis against a wall.
Performing a high jump.
Knitting a sweater.
Bidding on an item at an auction.
2.5 Define in your own words the following terms: agent, agent function, agent program,
rationality, autonomy, reflex agent, model-based agent, goal-based agent, utility-based agent,
learning agent.
2.6
This exercise explores the differences between agent functions and agent programs.
a. Can there be more than one agent program that implements a given agent function?
Give an example, or show why one is not possible.
b. Are there agent functions that cannot be implemented by any agent program?
c. Given a fixed machine architecture, does each agent program implement exactly one
agent function?
d. Given an architecture with n bits of storage, how many different possible agent pro-
grams are there?
e. Suppose we keep the agent program fixed but speed up the machine by a factor of two.
Does that change the agent function?
2.7
Write pseudocode agent programs for the goal-based and utility-based agents.
The following exercises all concern the implementation of environments and agents for the
vacuum-cleaner world.Exercises
63
2.8 Implement a performance-measuring environment simulator for the vacuum-cleaner
world depicted in Figure 2.2 and specified on page 38. Your implementation should be modu-
lar so that the sensors, actuators, and environment characteristics (size, shape, dirt placement,
etc.) can be changed easily. (Note: for some choices of programming language and operating
system there are already implementations in the online code repository.)
2.9 Implement a simple reflex agent for the vacuum environment in Exercise 2.8. Run the
environment with this agent for all possible initial dirt configurations and agent locations.
Record the performance score for each configuration and the overall average score.
2.10 Consider a modified version of the vacuum environment in Exercise 2.8, in which the
agent is penalized one point for each movement.
a. Can a simple reflex agent be perfectly rational for this environment? Explain.
b. What about a reflex agent with state? Design such an agent.
c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty
status of every square in the environment?
2.11 Consider a modified version of the vacuum environment in Exercise 2.8, in which the
geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the
initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)
a. Can a simple reflex agent be perfectly rational for this environment? Explain.
b. Can a simple reflex agent with a randomized agent function outperform a simple reflex
agent? Design such an agent and measure its performance on several environments.
c. Can you design an environment in which your randomized agent will perform poorly?
Show your results.
d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent
and measure its performance on several environments. Can you design a rational agent
of this type?
2.12 Repeat Exercise 2.11 for the case in which the location sensor is replaced with a
“bump” sensor that detects the agent’s attempts to move into an obstacle or to cross the
boundaries of the environment. Suppose the bump sensor stops working; how should the
agent behave?
2.13 The vacuum environments in the preceding exercises have all been deterministic. Dis-
cuss possible agent programs for each of the following stochastic versions:
a. Murphy’s law: twenty-five percent of the time, the Suck action fails to clean the floor if
it is dirty and deposits dirt onto the floor if the floor is clean. How is your agent program
affected if the dirt sensor gives the wrong answer 10% of the time?
b. Small children: At each time step, each clean square has a 10% chance of becoming
dirty. Can you come up with a rational agent design for this case