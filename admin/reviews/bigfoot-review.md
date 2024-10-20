# Bigfoot Review

## Design Decisions
The design and architecture of Bigfoot.js is detailed below in each section.

### Code Organization and Quality
- Excellent documentation, uses proper JSDoc convention format
- Clear comments above each coffescript function explaining its purpose
- Design modularly that would not affect others
- Using Sass which allows more complex and maintainable stylesheets by using variables
- The use of Sass and modular JavaScript enhances the maintainability of the code
- The plugin offers extensive options to customize behavior, such as the ability to trigger footnotes on hover, configure multiple footnotes to be active at the same time, and control timeouts for popover operations.
- Bigfoot focuses on making footnotes more accessible, replacing traditional footnote links with more interactive elements that are easier to manage and use
- The project is well-documented, covers setup, configuration options, and common issues, which aids in reducing the entry barrier for new users and contributes to overall code quality.


### Pattern and Langauge Use
- JavaScript
> JavaScript is a versatile, high-level programming language primarily used for creating dynamic and interactive content on websites. It allows developers to implement complex features like real-time updates, form validations, animations, and more, enhancing the user experience. JavaScript is executed in the browser and works well with HTML and CSS to create fully functional web applications. 
- CoffeeScript
> CoffeeScript is a programming language that compiles into JavaScript, designed to enhance JavaScript's syntax and readability. It simplifies common coding patterns and reduces boilerplate code, allowing developers to write less code while achieving the same functionality. CoffeeScript introduces features such as list comprehensions, destructuring assignment, and a more concise way to define functions. 
- CSS
> CSS is a stylesheet language used to describe the presentation and layout of a web page written in HTML. It allows developers to apply styles such as colors, fonts, spacing, and positioning to elements on the page. CSS enables the separation of content and design, making it easier to maintain and update the look of a website without altering its structure.
- Sass / SCSS
> SCSS is a syntax of Sass (Syntactically Awesome Style Sheets), a preprocessor scripting language that extends CSS with additional features. Sass adds functionalities like variables, nesting, mixins, and functions, allowing for more organized and maintainable code. With Sass, developers can write cleaner stylesheets and create reusable code components, which can be compiled into standard CSS for use in web development.
- jQuery
> jQuery is a fast, lightweight JavaScript library designed to simplify HTML DOM manipulation, event handling, animation, and Ajax interactions. jQuery simplifies tasks such as selecting and modifying elements, handling events, and making asynchronous requests. jQuery also provides cross-browser compatibility, making it easier to develop for various web browsers.


### Repo Organization and Quality
The repo is organized into two main folders: src and dist. The src folder is cleanly organized with coffee/bigfoot.coffee containing the main code for the tool and scss/ containing the base, foundation, and variants for the Sass CSS styling of the bigfoot buttons and elements. The dist/ folder contains the compiled javascript and CSS elements of bigfoot, which are built from bigfoot.coffee and the Sass components.

The overall repo quality is top-notch, and beautifully organized.

### Modules

#### CONSTANTS
In this module, the developer defined some constants to improve the code readability and maintainability. Constants are used to store fixed values that are not intended to change throughout the code execution. By using these contants, the developer ensures that the values are easily identifiable and can managed in one place, and the user or developer can easily modify some of the functions by easily changing the constants. 
#### INIT
In this module, the developer include some key functions and helper functions to help init the bigfoot. For example, the key funtion -  footnoteInit function initializes the footnote buttons and their corresponding content when the document is ready, and the helper function - cleanFootnoteLinks function extracts and groups the ID and HERF of each footnote anchor, and it checks if there's a element associates the footnote links with it, which can help manage the note links more efficiently.
#### ACTIVATE
This module focuses on managing and displaying popover footnotes triggered by click or hover event. The code is designed to ensure popovers are well positioned and correctly displayed while avoid overlap or multiple simultaneous popovers. For example, the key function buttonHover is triggered on hovering over a footnote button. It creates a popover for the hovered button while removing other popovers if the allowMultipleFN setting is disabled.
#### INACTIVE
This module is very similar to ACTIVE module which activates the popover, this module dissolve the poppover, which involves hover and click behaviors. The methods reviewed below handle the appearance and removal of these footnotes, with the focus on events like hovering, mouseout, and keypresses. For example, the key function unhoverFeet handles the behavior when the mouse leaves a footnote or button area. It checks if the deleteOnUnhover and activateOnHover settings are enabled, and if so, schedules the removal of the footnote after a delay.
#### POSITION
This module ensures that footnotes are positioned correctly based on the available space around the button and that they adapt responsively to window resizing. For example, the key function repositionFeet positions each footnote relative to its button depending on the available screen space. Handles positioning of the popover (footnote) above or below the button and also resizes it based on available screen real estate.
#### BREAK
This section manages breakpoints.
#### OTHER
This section defines an 'updateSetting' and 'getSetting' function, to modify the bigfoot settings.
#### BIND
This section sets up the event handlers for the script, and binds certain keypresses to those event handlers for the CSS attributes. The events recognized include "mouseenter", "touchend click", "mouseout", "keyup", "scroll resize", and "gestureend".
#### RETURN 
The final module of the code, returning the created bigfoot variable.



### Tool Quality
- CoffeeScript might be a bit outdated, its github repo shows most recent commits were minor bug fixes around 1 year ago
- Sass was created during a time when native CSS had much less to offer than it does today. As detailed in this [article](https://medium.com/@erennaktas/sass-is-dead-css-vs-sass-2024-a78c65c47a4d), there's no need to use Sass in 2024 when modern CSS is powerful enough to replace all of its unique functionality.
- jQuery is still a popular tool despite being old. It allows for a much simpler developer experience of writing JavaScript code, especially when it comes to selecting and manipulating HTML elements.


## Demo
We created a simple HTML page to show the effect of BigFoot.


## Final Verdict
Due to the outdated tools used including CoffeeScript and Sass, there is no use in adapting or forking Bigfoot.js to create a new modern JavaScript footnote experience. Most of its functionality would have to be completely rewritten or discarded.

Update: It turns out this was a shortsighted conclusion to make. Bigfoot's usefulness lies in its simplicity, so we've decided to adapt it using modern tools, replacing coffeescript and sass with pure JS and CSS.