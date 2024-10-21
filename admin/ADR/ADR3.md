---
# These are optional metadata elements. Feel free to remove any of them.
status: "accepted"
date: {2024-10-18}
decision-makers: {Yuke Zhu, Delaware Wade, Shaobo Qu, Kanaad Deshpande}
---

# ADR: Modularize the CoffeeScript to Replace Functions with Raw Javascript and Convert SCSS to CSS in LittleFoot

## Context and Problem Statement

We have already decided migrate Bigfoot for our project. To tackle with Bigfoot's outdated tools and codes, like CoffeeScript and SCSS, we proposed to migrate it to JavaScript and CSS. In this meeting, the team is discussing the progress and deciding the next step of migration. 

## Decision Drivers

* Disorganized codes of BigFoot

  After reviewing the code structure of BigFoot, the team noticed it is disorganized. Despite being well-documented and thoroughly commented, all scripts, functions, and types are bundled into a single `bigfoot.coffee` file, making future development difficult.

* Outdated and deprecated tools

 Some team members encountered difficulties running BigFoot on their devices, highlighting that CoffeeScript and SCSS are deprecated and outdated tools for web development. To ensure functionality and stay current with the latest web frameworks, a renovation and update process should be implemented.

* Team members are not experienced with web development


## Considered Options

* Option A: Convert CoffeeScript function one-by-one to JavaScript function

  #### Description:

  This option includes re-writing the CoffeeScript functions manually to JavaScript and then using the converting tool on CoffeeScript website to verify the CoffeeScript function to JavaScript function.

  #### Pros:

  This is the most straightforward method for converting. The results can be tested and verified to make sure the correctness.

  #### Cons:

  This may require some extra tools and advanced knowledge in writing JavaScript codes. Team members are not experienced in programming with JavaScript. Errors may occur in the conversions.
  
* Option B: Modularize the JavaScript files directly from CoffeeScript outputs 

  #### Description:

  This option includes using generated JavaScripts files from the CoffeeScript functions, and manually replace and modularize to JavaScript functions. Then we can use the converting tool on CoffeeScript website to verify the CoffeeScript function to JavaScript function.

  #### Pros:

  This is the most straightforward method for converting and suitable for team members without advanced JavaScript knowledge. The results can also be tested and verified to make sure the correctness.

  #### Cons:

  Errors may occur in the conversions since team members are not experienced with JavaScript.  
  
* Option C: Convert SCSS to CSS

  #### Description:

  This option includes using converting SCSS to CSS one by one. 

  #### Pros:

  The conversion process is straightforward and easy to complete for team members without advanced web development knowledge.


  #### Cons:

  The results cannot be verified since we have some troubles to compile and run it on our machines.


## Decision Outcome

>> Chosen Option: Option B and C

We have chosen Option B for converting CoffeeScript to JavaScript, leveraging the CoffeeScript-generated outputs due to our team's limited JavaScript expertise. This approach also allows for straightforward verification and testing of modularization. For SCSS conversions, we opted for Option C, as it aligns well with the team's skills and is simple to complete.

