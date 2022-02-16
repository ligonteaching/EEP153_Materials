
# Table of Contents

1.  [Overview](#org80cd0cf)
2.  [Administrivia](#orgd6da2ea)
    1.  [Prerequisites](#org2177f56)
    2.  [Schedule](#org85d9bb4)
    3.  [People](#org583fbd8)
        1.  [Office Hours](#orge117704)
    4.  [Evaluation (Grading)](#org34804f6)
        1.  [Team evaluations](#orgc4461fb)
        2.  [Teammate evaluations](#orgb65ce57)
        3.  [Quality of evaluation](#org5627d45)
3.  [Projects](#org84acc93)
    1.  [Introduction & Collaboration](#org369a490)
    2.  [Population & Food Supply](#org78ff8ea)
        1.  [Readings](#orga2db0b2)
    3.  [Subsistence Diets](#org7dbc9e7)
        1.  [Readings](#orgda613c4)
    4.  [Consumer Food Demand](#org9b48771)
        1.  [Readings](#org04ecf24)
    5.  [Estimating Food Demand Systems](#org2c27993)
    6.  [Hacking Food & Nutrition](#org0741ca1)
        1.  [Readings](#orgcbafe88)



<a id="org80cd0cf"></a>

# Overview

This course takes a quantitative, hands-on
approach to understanding the challenges of
feeding the human population of the planet
Earth.  We'll discuss topics of nutrition,
subsistence food consumption, and consumer
demand for food to develop our
understanding of the current situation.
We'll then develop both theories and
computer models of population dynamics
taking into account people's decisions
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


<a id="orgd6da2ea"></a>

# Administrivia


<a id="org2177f56"></a>

## Prerequisites

Data8, EEP100 or
equivalents required; Math 54
recommended.


<a id="org85d9bb4"></a>

## Schedule

Meet two times per week; M 2&#x2013;4pm and W 1&#x2013;3pm (Pacific Time). 

We'll have a mix of lectures and discussion (typically on Mondays)
and tutorials and group work (typically on Wednesdays).  

When we're able to meet in person we'll be in Social Sciences 110;
until then we'll meet via zoom at
<https://berkeley.zoom.us/j/91293178788>.  Note that to join you'll
need to sign-in to zoom using your `berkeley.edu` email.


<a id="org583fbd8"></a>

## People

-   Ethan Ligon (ligon@berkeley.edu)
-   Becky Cardinali
-   Ryan Sandan


<a id="orge117704"></a>

### Office Hours

See announcement on `piazza`


<a id="org34804f6"></a>

## Evaluation (Grading)

Grading in course depends primarily on *peer evaluation*.  In
particular, every project will lead to you evaluating your
classmates in two main ways, and being evaluated yourself in three.


<a id="orgc4461fb"></a>

### Team evaluations

Everyone will evaluate every team according to several criteria:

1.  Code

    1.  Did code work as intended?
    2.  How elegant was the team's code?
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
        population analysis, would you hire this team?
    2.  Other constructive comments & criticisms.

5.  Ranking

    Finally, we'll ask you to rank all teams according to your overall
    impression of their presentation.


<a id="orgb65ce57"></a>

### Teammate evaluations

Everyone will also evaluate all of the individuals on their team
according to several criteria:

1.  Quality of work
2.  Could be counted on to complete tasks in a timely fashion?
3.  Helpful to others in group?
4.  Contributed to the smooth working of the team?

In addition, we'll ask you to give some additional information
about each of your teammates, indicating:

-   What were each person's main strengths?
-   Would you like to work with this person again?

And finally, we'll ask you to:

-   Rank each person according to their overall contribution to the project.


<a id="org5627d45"></a>

### Quality of evaluation

Your own evaluations are an important individual contribution to
the class, and the quality of your evaluations will affect your
grade.  There are three criteria we'll use in judging the quality
of your evaluations.

1.  Prediction of others' evaluations of you

    You'll provide evaluations not only of **other** teams, but also of
    your own team.  And you'll evaluate not just your teammates'
    contribution to the project, but also your **own** contribution.
    
    Your self-evaluations will affect your grade.  However, the *way*
    in which these will affect your grade will depend **not** on how
    good you say you are, but how accurately you **predict** how others
    evaluate you.  In particular, the closer your guesses about
    others' evaluations are to the *average* of what others give you
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
    people's evaluations.  If your evaluations are \`outliers' then
    this will *negatively* effect your grade.  Further, if upon
    examination it appears that you've used your evaluations
    strategically there may be further repercussions, most
    particularly if the manner in which you've evaluated others
    violates Berkeley's Honor Code (i.e., you must "act with
    integrity, honesty, and respect for others").


<a id="org84acc93"></a>

# Projects

The course revolves around a sequence of
topics, each exploring a substantive
issue involved in "feeding the planet"
and each introducing novel tools.
Students will work in small groups to
complete one structured project for each
topic.


<a id="org369a490"></a>

## Introduction & Collaboration

Students will review introductory materials about coding 
(Python and Pandas) and potential ways to collaborate 
(Google Colab, Trello, Git, and Agile). See `piazza` post 
for links to the resources


<a id="org78ff8ea"></a>

## Population & Food Supply

Students will construct datasets on the
distribution of characteristics in the
world population, including measures of
resources, and the age and sex
composition of the world population.  A
separate dataset allows us to think
about food supply.


<a id="orga2db0b2"></a>

### Readings

-   Malthus [An Essay of the Principle of Population (1798)](https://oll.libertyfund.org/titles/malthus-an-essay-on-the-principle-of-population-1798-1st-ed#lf0195_head_002)
-   de Janvry-Sadoulet (2015), [Chapter 11 of Development Economics](https://github.com/ligonteaching/EEP153_Materials/blob/master/Project1/Chapter_11_Population15.pdf)
-   Fuglie (2012), <https://www.ers.usda.gov/amber-waves/2012/september/global-agriculture/>


<a id="org7dbc9e7"></a>

## Subsistence Diets

Every living human has some minimal, or subsistence, nutritional
requirements; should these not be satisfied health and even life
may be threatened.  People satisfy these needs by eating various
kinds of food, but there may be many different food diets which
satisfy people's subsistence requirements.  One criterion for
choosing among these diets is *cost*. 

In this topic students use contemporary data on different kinds of
foods available to the US population along with prices to
construct estimates of *minimum cost* subsistence diets.  


<a id="orgda613c4"></a>

### Readings

-   [Stigler (1945) "The Cost of Subsistence"](https://github.com/ligonteaching/EEP153_Materials/blob/master/Project2/stigler45.pdf)
-   [Dantzig (1990) "The Diet Problem"](https://github.com/ligonteaching/EEP153_Materials/blob/master/Project2/dantzig90.pdf)


<a id="org9b48771"></a>

## Consumer Food Demand

In practice, even very poor people seldom choose their diets on
the basis of minimum costs.  Instead, people balance nutritional
requirements against considerations of cost and what we might call
the gastronomical value of different diets.  Here we explore the
theory of demand as it pertains to these diets&#x2014;how does demand
for food depend on income, prices, and other observables?  How
well (or poorly) do these diets serve nutritional ends?


<a id="org04ecf24"></a>

### Readings

-   Review basic demand theory (e.g., Chapters 3&#x2013;5 in Nicholson-Snyder)


<a id="org2c27993"></a>

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


<a id="org0741ca1"></a>

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


<a id="orgcbafe88"></a>

### Readings

-   Technical change: [Borlaug (2000)](http://www.plantphysiol.org/content/124/2/487?ijkey=c12c5c79e5b11c10820b21877391b978804dc1c5&keytype2=tf_ipsecsha), [Ars Technica (2019)](https://arstechnica.com/science/2019/06/why-havent-genetically-engineered-crops-made-food-better/)
-   Changes in budget: [Deaton-Dreze (2009)](https://www.jstor.org/stable/40278509)
-   Changes in relative prices: [Falbe et al (2016)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5024386/)

