---
# These are optional metadata elements. Feel free to remove any of them.
status: "accepted"
date: {2024-10-15}
decision-makers: {Yuke Zhu, Delaware Wade, Shaobo Qu, Kanaad Deshpande}
---

# {ADR: Migration from Bigfoot to a JavaScript/TypeScript-based Solution}

## Context and Problem Statement

We are currently deciding between two legacy frameworks, Bigfoot and Littlefoot, for our project. Bigfoot is more widely adopted but suffers from outdated technologies and poor code organization. Littlefoot, while better organized and using a modern language (TypeScript), would require significant customization to meet our needs. The team needs to select a framework or solution that ensures long-term maintainability and a reasonable learning curve.


## Decision Drivers

### Maintainability: 
- The solution should use widely supported languages like TypeScript and JavaScript, which have large communities, extensive documentation, and are continually updated. This ensures that future developers can easily find resources, libraries, and support when maintaining or expanding the codebase. Using older languages like CoffeeScript could present challenges due to limited community support and diminishing relevance in the ecosystem.
- Risk: Continuing with CoffeeScript or SCSS may require the team to invest significant time learning outdated technologies that are no longer maintained, which could lead to maintainability issues and technical debt in the long term.

### Familiarity: 
- The team is more comfortable with modern languages like TypeScript, which allows for better type safety, tooling support, and familiar syntax. Using CoffeeScript, which no one on the team has experience with, would introduce a steep learning curve, slow down development, and increase the likelihood of bugs or inefficiencies.
- Risk: If we continue using CoffeeScript, the team may struggle with slower progress and more errors due to lack of familiarity. This could delay project delivery and increase costs.

### Code Quality: 
- The goal is to have a clean, modular code structure where different parts of the application are logically separated into components or modules. For example, in Littlefoot (LF), the code is already organized into modules that separate responsibilities (e.g., UI components, business logic, and data handling), making it easier to test, extend, and debug. In contrast, Bigfoot (BF) has code clustered in a single file, which makes it harder to maintain and increases technical debt.
- Risk: Continuing with a monolithic code structure like BF's could lead to significant technical debt, making future modifications or debugging more time-consuming and error-prone.

### Development Speed: 

- We need a working version quickly, but it should not come at the expense of creating long-term technical debt. Customizing Littlefoot with TypeScript allows us to leverage its modular structure, which is easier to maintain and expand upon in the future. Rewriting Bigfoot, while potentially faster in the short term, may lead to delays as we restructure the code for maintainability.
- Risk: Focusing solely on speed (e.g., by trying to quickly refactor BF) without addressing the underlying structural issues may result in a codebase that's harder to manage, reducing scalability and future productivity.

## Considered Options

* Option A: Redesign Bigfoot using JavaScript/TypeScript

Description: In this option, we would refactor Bigfoot by replacing its outdated CoffeeScript and SCSS with modern JavaScript  and CSS. This approach allows us to keep Bigfoot's core logic intact while improving maintainability by adopting more widely used technologies. The goal is to preserve the current functionality of Bigfoot while modernizing the codebase for better future support and scalability.

We would focus on breaking up the monolithic code structure, modularizing key components, and implementing best practices for code organization. This approach would also involve reworking styles to use modern CSS, which are better maintained.


Pros:
- Bigfoot has a wider adoption and more readable comments.
- Less complicated overall architecture than Littlefoot.
- Modernizing Bigfoot to JavaScript/TypeScript allows us to keep the structural simplicity while adopting modern practices.
Cons:
- Requires a full redesign from CoffeeScript/SCSS to JavaScript/TypeScript.
- All code currently clustered in one file will need to be reorganized, which may require substantial refactoring.


* Option B: Customize Littlefoot with TypeScript

Pros:
- Littlefoot already uses TypeScript, a modern language we are eager to learn.
- Well-structured code organization out of the box, which aligns with our goal of maintainable code.
- Sufficient documentation exists for TypeScript, easing the learning curve.
Cons:
- Less widely adopted and may require significant customization to meet our project’s needs.
- Adopting Littlefoot may lead to slower development if customizations are extensive.

## Decision Outcome

>> Chosen Option: Option A - Redesign Bigfoot with JavaScript/TypeScript

We decided to move forward with a complete redesign of Bigfoot using JavaScript/TypeScript. This decision was driven by the need to adopt modern technologies while maintaining Bigfoot’s simple architecture and wider adoption. The redesign will eliminate outdated CoffeeScript and SCSS code, improving maintainability, team familiarity, and code quality. Though the effort will be significant, this approach allows us to build a solution that is scalable and future-proof while aiming for a working version in the short term.