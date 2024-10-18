# The Littlefoot Review

## Design Decisions


### Code Organization and Quality

#### Code Quality

- Organization: The overall structure and code organization is high-quality for a nodejs-based TypeScript project. However, this repo has only basic level of directory structure, with core modules and DOM-related scripts. Additionally, it doesn't separate different modules in individual TypeScript files and all defined types in an independent script, which makes the maintainance and development difficult. These scripts can be further modularized into smaller units for easy maintainance and developments.

- Code comments: Despite the type, class, and function names are straightforward, **ZERO** code comments make it difficult for developers who are not familiar with this project to understand the functionality and  perform further developments on top of the code. Adding concise comments to explain the purpose of each module and function would greatly improve code readability and make it easier for new developers to contribute.

#### Functionality and Organization

- Entry Point: `src/littlefoot.ts` defines the primary entry point of the application with input arguments on user settings, making it easy to import with developer's customization. 
  
- Logics and Constants: `src/use-cases.ts` and `src/settings.ts` define types `UseCaseSettings`, `Footnote`, and `UseCases`. `UseCaseSettings` is a template for developers to manage footnotes. `Footnote` is the object with methods for activation, dismissal and `UseCases` is for methods for various footnote operations. `src/settings.ts` is for application-specific constants. Overall, this code exhibits high quality in terms of strong typing and providing a single source for the feature implementation and constants, making it easy for maintainability and customizations. 

- The use of strongly typed settings and constants creates a solid foundation for customizations, ensuring future features can be integrated with minimal disruption to the core functionality.”

- DOM Handling:  
  - Document: `dom/document.ts` defines actions performed on footnote document, including activate, dismiss, reposition, resize, toggle, hover, etc. 
  - Footnote Structure: `dom/footnote.ts` defines behaviors of footnote actions. 
  - Events for User Interface: `dom/events.ts` defines footnote-specific events for user interactions, and are listening to the mouse and key input events.
  

#### Styling

- CSS: `src/littlefoot.css`

#### Build and Configuration

- Build Configuration:  
  - `rollup.config.js`
  - `tsconfig.json`

#### Testing

- Unit Tests: the unit tests provided in `test/` allow the developers to easily test the components and functions of LittleFoot by comparing their actual behavior with the expected behavior.

- End-to-End Tests: the end-to-end tests in `cypress/e2e/` provide another level of testing to ensure the correct overall workflow of LittleFoot by simulating real-world user scenarios.

- While unit tests and end-to-end tests are in place, the test coverage could be expanded to cover edge cases and more complex user interactions, particularly for scenarios involving simultaneous footnote actions.

#### Development Tools: 

- Development Config: `biome.json` is included for configuration of Biome module for development.

#### Documentation

- Project Documentation: `README.md` gives developers a clear view and instruction about how to install and use the scripts. 

- Although README.md provides basic usage instructions, adding a 'Contributing Guide' or developer-focused documentation outlining the code structure and typical development workflow would further aid new contributors.

#### Packages

- Package Management: The `package.json` file includes the necessary packages to run LittleFoot in a Node.js environment, and the scripts are well-documented and easy to use. However, it’s important to note that: 1) the scripts only function on Linux or Unix-based systems and are incompatible with Windows, and 2) there is no script available to create a simple demo for testing, which complicates the developer testing process.

#### Modularization

- Modularizing the core modules into smaller, independent TypeScript files would significantly improve maintainability, reduce complexity, and facilitate future feature development or refactoring.


### Pattern and Language Use

- TypeScript is a modern, actively maintained language that enhances JavaScript development. The strong typing of TypeScript guarantees the correct functionality and robustness for JavaScript. 


### Main Modules

#### documents
This module is responsible for setting up and managing footnotes in a document by identifying footnote references, creating interactive footnote buttons and popovers, and handling their lifecycle. It identifies all footnote references (anchor links) within a specified scope using a pattern that matches the links' href attributes. For each identified footnote, it generates a button and a popover using the provided templates, populating them with dynamic content such as the footnote text and reference number. It creates the necessary HTML elements (buttons and popovers) for each footnote and binds event handlers for actions like scrolling. Elements related to footnotes are marked with a special "print-only" class to handle the visibility of the footnotes when printed. The module also recursively hides empty footnote containers. 

#### events
This module is responsible for managing event listeners related to footnote actions in a web application. It gives several different helper functions like closestTarget and hoverHandler. And the main function addListeners sets up various event listeners that respond to user interactions with footnotes: Touch and Click, Escape and Hover.

#### footnotes
This module provides a set of actions for managing the behavior of footnotes on a webpage, including their activation, dismissal, and positioning. It defines how footnote buttons and their associated popovers (tooltips) behave interactively when the user interacts with them. It provides a complete set of actions to handle footnote interactions, including activation, dismissal, repositioning, and resizing, ensuring the footnote remains interactive and properly displayed within the layout.

#### layout
This module manages the positioning and layout of popovers (tooltips) relative to a button element. It handles positioning and repositioning of tooltips and popovers, ensuring they are correctly aligned based on space and element size.



## Final Verdict

Overall, the LittleFoot repository demonstrates that its developer has abundant experience and expertise in handling Node.js-based TypeScript projects. LittleFoot provides well-defined settings functionality that makes customization simple. However, it is clear that the developer did not consider making it easy for other developers to maintain and build upon this project. The lack of comments and poor directory structure obviously prevent others from understanding its code.
While LittleFoot is highly functional and showcases advanced TypeScript usage, improvements in modularity, documentation, and cross-platform support would not only enhance maintainability but also broaden the appeal of the project to a wider developer audience.
