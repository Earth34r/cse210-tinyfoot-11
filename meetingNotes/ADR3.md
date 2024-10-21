---
# These are optional metadata elements. Feel free to remove any of them.
status: "{proposed | rejected | accepted | deprecated | … | superseded by ADR-0123"
date: {YYYY-MM-DD when the decision was last updated}
decision-makers: {list everyone involved in the decision}
consulted: {list everyone whose opinions are sought (typically subject-matter experts); and with whom there is a two-way communication}
informed: {list everyone who is kept up-to-date on progress; and with whom there is a one-way communication}
---

# ADR: Modularize the CoffeeScript to Replace Functions with Raw Javascript in LittleFoot

## Context and Problem Statement

We have already decided migrate Bigfoot for our project. To tackle with Bigfoot's outdated tools and codes, like CoffeeScript and SCSS, we proposed to migrate it to JavaScript and CSS. In this meeting, the team is discussing the progress and deciding the next step of migration. 

## Decision Drivers

* Disorganized codes of BigFoot

  After reading the code organizations of BigFoot, the team noticed that BigFoot is disorganized. Despite of the well-documented and well-commented codes of BigFoot, all the scripts, functions, and types are packed in the same `bigfoot.coffee` file, which makes further development hard.

* Outdated and deprecated tools

  Some of the team members struggled to run BigFoot on their devices, which reflected that CoffeeScript and SCSS are deprecated and outdated tools for web development. A renovating and updating processing should be performed to make it functional and catch up with the latest web frameworks.


## Considered Options

* Convert CoffeeScript function one-by-one to JavaScript function

  #### Description:

  This option includes re-writing the CoffeeScript functions manually to JavaScript and then using the converting tool on CoffeeScript website to verify the CoffeeScript function to JavaScript function.

  #### Pros:

  This is the most straightforward method for converting. The results can be tested and verified to make sure the correctness.

  #### Cons:

  This may require some extra tools and advanced knowledge in writing JavaScript codes. Team members are not experienced in programming with JavaScript. Errors may occur in the conversions.
  
* Modularize the JavaScript files directly from CoffeeScript outputs 

  #### Description:

  This option includes using generated JavaScripts files from the CoffeeScript functions, and manually replace and modularize to JavaScript functions. Then we can use the converting tool on CoffeeScript website to verify the CoffeeScript function to JavaScript function.

  #### Pros:

  This is the most straightforward method for converting and suitable for team members without advanced JavaScript knowledge. The results can also be tested and verified to make sure the correctness.

  #### Cons:

  Errors may occur in the conversions since team members are not experienced with JavaScript.  
  
* Convert SCSS to CSS

  #### Description:

  This option includes using converting SCSS to CSS one by one. 

  #### Pros:


  #### Cons:


## Decision Outcome

Chosen option: "{title of option 1}", because {justification. e.g., only option, which meets k.o. criterion decision driver | which resolves force {force} | … | comes out best (see below)}.

<!-- This is an optional element. Feel free to remove. -->
### Consequences

* Good, because {positive consequence, e.g., improvement of one or more desired qualities, …}
* Bad, because {negative consequence, e.g., compromising one or more desired qualities, …}
* … <!-- numbers of consequences can vary -->

<!-- This is an optional element. Feel free to remove. -->
### Confirmation

{Describe how the implementation of/compliance with the ADR can/will be confirmed. Is the chosen design and its implementation in line with the decision? E.g., a design/code review or a test with a library such as ArchUnit can help validate this. Note that although we classify this element as optional, it is included in many ADRs.}

<!-- This is an optional element. Feel free to remove. -->
## Pros and Cons of the Options

### {title of option 1}

<!-- This is an optional element. Feel free to remove. -->
{example | description | pointer to more information | …}

* Good, because {argument a}
* Good, because {argument b}
<!-- use "neutral" if the given argument weights neither for good nor bad -->
* Neutral, because {argument c}
* Bad, because {argument d}
* … <!-- numbers of pros and cons can vary -->

### {title of other option}

{example | description | pointer to more information | …}

* Good, because {argument a}
* Good, because {argument b}
* Neutral, because {argument c}
* Bad, because {argument d}
* …

<!-- This is an optional element. Feel free to remove. -->
## More Information

{You might want to provide additional evidence/confidence for the decision outcome here and/or document the team agreement on the decision and/or define when/how this decision the decision should be realized and if/when it should be re-visited. Links to other decisions and resources might appear here as well.}
