
# Table of Contents

1.  [Overview](#orgb313481)
2.  [Administrivia](#org41a1b98)
    1.  [Prerequisites](#org6e9088a)
    2.  [Schedule](#org59bd50b)
    3.  [People](#orga0545c5)
        1.  [Office Hours/Individual Assistance](#org38206d5)
    4.  [Evaluation (Grading)](#orgf5c24d0)
        1.  [Team evaluations](#org6bb5d53)
        2.  [Teammate evaluations](#org1fe9dbc)
        3.  [Quality of evaluation](#org0a9c115)
        4.  [Instructors&rsquo; Evaluation](#org2fbe0ec)
3.  [Projects](#org0205c03)
    1.  [Introduction & Collaboration](#orgbbe8634)
    2.  [Population & Food Supply](#org0d90f33)
        1.  [Readings](#org2937f4e)
    3.  [Subsistence Diets](#org2d3b57b)
        1.  [Readings](#org433c78a)
    4.  [Consumer Food Demand](#orgef30ba3)
        1.  [Readings](#org8a7e325)
    5.  [Estimating Food Demand Systems](#org1cf13ce)
    6.  [Hacking Food & Nutrition](#org2909bbc)
        1.  [Readings](#org4fba24d)



<a id="orgb313481"></a>

# Overview

This course takes a quantitative, hands-on
approach to understanding the challenges of
feeding the human population of the planet
Earth.  We&rsquo;ll discuss topics of nutrition,
subsistence food consumption, and consumer
demand for food to develop our
understanding of the current situation.
We&rsquo;ll then develop both theories and
computer models of population dynamics
taking into account people&rsquo;s decisions
about child-bearing, changes in mortality,
and changes in food supply in order to
learn something about the future of food.
Focus throughout the course will be on
developing practical tools to work with
real-world data.  Those tools will include
linear programs, globally regular demand
systems, and a variety of
econometric tools.  The course will rely on
a knowledge of the programming language
`python`.


<a id="org41a1b98"></a>

# Administrivia


<a id="org6e9088a"></a>

## Prerequisites

Data8, EEP100 or
equivalents required; Math 54
recommended.


<a id="org59bd50b"></a>

## Schedule

Meet two times per week; Tuesdays and Thursdays 10am&#x2013;12pm (Pacific Time).

We&rsquo;ll have a mix of lectures and discussion (typically on Tuesdays)
and tutorials and group work (typically on Thursdays).

We&rsquo;ll meet in person in Social Sciences 110.   Office hours may be in person or virtual.


<a id="orga0545c5"></a>

## People

-   **Instructor:** Ethan Ligon (ligon@berkeley.edu)
-   **GSI:** Scott Kjorlien (scottkjorlien@berkeley.edu)
-   **Tutor:** Faye Fang (ce<sub>fang</sub>@berkeley.edu)


<a id="org38206d5"></a>

### Office Hours/Individual Assistance

-   **Questions/Discussion:** Please use <https://edstem.org> to ask questions of
    the instructor or assistants; we&rsquo;re likely to miss email.  Note
    that you can post anonymously and/or privately.

-   **Instructor&rsquo;s Office Hours:** You may also make an appointment to
    speak with Professor Ligon during his office hours via
    <https://are.berkeley.edu/~ligon/appointment.html>.

-   **Office hours (GSI):** Scott will hold an office hour Thursdays 1&#x2013;2p in Giannini 203, or by appointment.


<a id="orgf5c24d0"></a>

## Evaluation (Grading)

Grading in course depends primarily on *peer evaluation*.  In
particular, every project will lead to you evaluating your
classmates in two main ways, and being evaluated yourself in three.


<a id="org6bb5d53"></a>

### Team evaluations

Everyone will evaluate every team according to several criteria.  For example,

1.  Code

    1.  Did code work as intended?
    2.  How elegant was the team&rsquo;s code?
    3.  How ambitious were design goals?
    4.  How completely were design goals met?

2.  Organization

    In the presentation:
    
    1.  How well did team manage its time?
    2.  How well did the team work together?

3.  Style

    1.  How interesting was the presentation?
    2.  How polished was the presentation?

4.  Overall

    1.  If you were in the position of needing to hire a team to do
        this sort of analysis, would you hire this team?
    2.  Other constructive comments & criticisms.
    3.  Finally, we&rsquo;ll ask you to rank all teams according to your overall
    
    impression of their presentation.


<a id="org1fe9dbc"></a>

### Teammate evaluations

Everyone will also evaluate all of the individuals on their team
according to several criteria:

1.  Quality of work
2.  Could be counted on to complete tasks in a timely fashion?
3.  Helpful to others in group?
4.  Contributed to the smooth working of the team?

In addition, we&rsquo;ll ask you to give some additional information
about each of your teammates, indicating:

-   What were each person&rsquo;s main strengths?
-   Would you like to work with this person again?

And finally, we&rsquo;ll ask you to:

-   Rank each person according to their overall contribution to the project.


<a id="org0a9c115"></a>

### Quality of evaluation

Your own evaluations are an important individual contribution to
the class, and the quality of your evaluations will affect your
grade.  There are three criteria we&rsquo;ll use in judging the quality
of your evaluations.

1.  Prediction of others&rsquo; evaluations of you

    You&rsquo;ll provide evaluations not only of **other** teams, but also of
    your own team.  And you&rsquo;ll evaluate not just your teammates&rsquo;
    contribution to the project, but also your **own** contribution.
    
    Your self-evaluations will affect your grade.  However, the *way*
    in which these will affect your grade will depend **not** on how
    good you say you are, but how accurately you **predict** how others
    evaluate you.  In particular, the closer your guesses about
    others&rsquo; evaluations are to the *average* of what others give you
    the higher your grade.

2.  Information in your own evaluations of others

    The greater the information provided by your evaluations of others
    the higher your grade.  The amount of information will be measured
    partly according to the variation of your evaluation of others, and
    partly according to a (subjective) measure of the quality of your
    comments.
    
    Observation: if you give everyone the *same* scores (e.g.,
    everyone gets top score) there is *no* variation in your
    evaluation.  This would negatively affect your own grade.

3.  Correlation with evaluations of others

    Your evaluations must be honest, in the sense that they are
    attempts to fairly evaluate the efforts of others and of your own
    efforts.  Ideally there will be broad agreement across different
    people&rsquo;s evaluations.  If your evaluations are \`outliers&rsquo; then
    this may *negatively* effect your grade.  Further, if upon
    examination it appears that you&rsquo;ve used your evaluations
    strategically there may be further repercussions, most
    particularly if the manner in which you&rsquo;ve evaluated others
    violates Berkeley&rsquo;s Honor Code (i.e., you must &ldquo;act with
    integrity, honesty, and respect for others&rdquo;).


<a id="org2fbe0ec"></a>

### Instructors&rsquo; Evaluation

For each project, you will also be evaluated in terms of your *engagement*.  This is the one category which will be evaluated solely by instructors and GSIs, rather than by your peers.  Particular things we will look at:

-   Number and quality of comments, etc. on [edstem.org](https://edstem.org).
-   Number and quality  of comments and issues on github repositories (both yours and others).
-   Number and quality of comments or PRs specifically pertaining to issues/bugs in code or material in EEP153 repos, including
    -   <https://github.com/ligonteaching/EEP153_Materials/issues>
    -   <https://github.com/ligonteaching/EEP153_Exercises/issues>
    -   <https://github.com/ligon/Population>
    -   <https://github.com/ligon/MinCostDiet>
    -   <https://github.com/ligon/FoodDemand>
    -   <https://github.com/ligon/HackingFood>


<a id="org0205c03"></a>

# Projects

The course revolves around a sequence of
topics, each exploring a substantive
issue involved in &ldquo;feeding the planet&rdquo;
and each introducing novel tools.
Students will work in small groups to
complete one structured project for each
topic.


<a id="orgbbe8634"></a>

## Introduction & Collaboration

Students will review introductory materials about coding 
(Python and Pandas) and potential ways to collaborate 
(Git, Google Colab, Trello, and Agile). See online posts
for links to resources.


<a id="org0d90f33"></a>

## Population & Food Supply

Students will construct datasets on the
distribution of characteristics in the
world population, including measures of
resources, and the age and sex
composition of the world population.  A
separate dataset allows us to think
about food supply.


<a id="org2937f4e"></a>

### Readings

-   Malthus [An Essay of the Principle of Population (1798)](https://oll.libertyfund.org/titles/malthus-an-essay-on-the-principle-of-population-1798-1st-ed#lf0195_head_002)
-   de Janvry-Sadoulet (2015), [Chapter 11 of Development Economics](https://github.com/ligonteaching/EEP153_Materials/blob/master/Project1/Chapter_11_Population15.pdf)
-   Fuglie (2012), <https://www.ers.usda.gov/amber-waves/2012/september/global-agriculture/>
-   NYTimes &ldquo;What to eat on a burning planet&rdquo; series, especially:
    -   <https://www.nytimes.com/2024/07/28/opinion/food-climate-crisis-prices.html>
    -   <https://www.nytimes.com/2024/12/13/opinion/food-agriculture-factory-farms-climate-change.html>


<a id="org2d3b57b"></a>

## Subsistence Diets

Every living human has some minimal, or subsistence, nutritional
requirements; should these not be satisfied health and even life
may be threatened.  People satisfy these needs by eating various
kinds of food, but there may be many different food diets which
satisfy people&rsquo;s subsistence requirements.  One criterion for
choosing among these diets is *cost*. 

In this topic students use contemporary data on different kinds of
foods available to the US population along with prices to
construct estimates of *minimum cost* subsistence diets.  


<a id="org433c78a"></a>

### Readings

-   [Stigler (1945) &ldquo;The Cost of Subsistence&rdquo;](https://github.com/ligonteaching/EEP153_Materials/blob/master/Project2/stigler45.pdf)
-   [Dantzig (1990) &ldquo;The Diet Problem&rdquo;](https://github.com/ligonteaching/EEP153_Materials/blob/master/Project2/dantzig90.pdf)


<a id="orgef30ba3"></a>

## Consumer Food Demand

In practice, even very poor people seldom choose their diets on
the basis of minimum costs.  Instead, people balance nutritional
requirements against considerations of cost and what we might call
the gastronomical value of different diets.  Here we explore the
theory of demand as it pertains to these diets&#x2014;how does demand
for food depend on income, prices, and other observables?  How
well (or poorly) do these diets serve nutritional ends?


<a id="org8a7e325"></a>

### Readings

-   Review basic demand theory (e.g., Chapters 3&#x2013;5 in Nicholson-Snyder)


<a id="org1cf13ce"></a>

## Estimating Food Demand Systems

Students will use data on household food expenditures for
populations from different countries to estimate systems of food
demand, and relate these demands to the subsistence diets
calculated in the earlier topic.

With these results in hand you will construct aggregate
demand functions that allow one to make predictions regarding how
aggregate demand for different kinds of foods depends on the
distribution of resources and the demographic composition of the
global population. 


<a id="org2909bbc"></a>

## Hacking Food & Nutrition

This project exploits our work on demand for food and is focused on
evaluating what kinds of **policies** might be effective at improving
nutritional outcomes for particular populations.  Our earlier work
addressed the question of how demand for different kinds of food
depends on prices, budgets, and household characteristics, taking as
given prices, budgets, and so on.

One of the take-aways from our earlier project is that the food people
*choose* to eat may be quite different from the foods that people
*should* eat, from a nutritional perspective.   

But if dietary choices respond to prices and budgets, it may be
possible to manipulate nutritional outcomes by changing either prices
or budgets.  We can assess the costs of this kind of manipulation
(e.g., the deadweight cost of a tax or subsidy); where these costs are
large we can also think about the value of innovation in either the
desirability or nutritional content of food.


<a id="org4fba24d"></a>

### Readings

-   Technical change: [Borlaug (2000)](http://www.plantphysiol.org/content/124/2/487?ijkey=c12c5c79e5b11c10820b21877391b978804dc1c5&keytype2=tf_ipsecsha), [Ars Technica (2019)](https://arstechnica.com/science/2019/06/why-havent-genetically-engineered-crops-made-food-better/)
-   Changes in budget: [Deaton-Dreze (2009)](https://www.jstor.org/stable/40278509)
-   Changes in relative prices: [Falbe et al (2016)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5024386/)

