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

Maintainability: The chosen solution should use modern, widely adopted languages and practices, ensuring future support and ease of use.
Familiarity: The team has limited experience with older technologies like CoffeeScript, which could slow development.
Code Quality: The solution should promote clean, modular code structures, reducing technical debt.
Development Speed: A working version is needed quickly, but without sacrificing future scalability or maintainability.

## Considered Options

* Option A: Redesign Bigfoot using JavaScript/TypeScript

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