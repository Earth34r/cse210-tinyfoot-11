---
# These are optional metadata elements. Feel free to remove any of them.
status: "accepted"
date: {2024-10-17}
decision-makers: {Yuke Zhu, Delaware Wade, Shaobo Qu, Kanaad Deshpande}
---

# {ADR: Migration from Bigfoot to a JavaScript/TypeScript-based Solution}

## Context and Problem Statement
We need a solution to automatically recognize references in academic papers and insert them as footnotes at the appropriate locations. The feature should also generate an HTML file that Bigfoot can process, allowing references to be easily displayed in the final output. The challenge is to efficiently parse references from papers, maintain accurate placement, and ensure compatibility with the Bigfoot system. This will allow for seamless integration of academic content into a footnote-enabled web format.


## Decision Drivers

### Automation: 
Reducing the manual effort required to manage and insert references in academic papers.
### Accuracy: 
Ensuring that all references are correctly identified and placed as footnotes in the document without missing or misplacing any citations.
### Compatibility with Bigfoot: 
The generated output must be in a format that can be processed by Bigfoot, specifically HTML.
### Maintainability: 
The parser should be easy to update and extend to accommodate different citation styles or document formats in the future.

## Considered Options

* Option A: Build a Custom Parser from Scratch

#### Pros:

Full control over how the parser operates, allowing it to be tailored specifically to our project needs.
Flexibility to easily extend and modify the parser to accommodate future citation formats or custom requirements.
Ensures complete compatibility with the Bigfoot system as the output format can be designed specifically for it.

#### Cons:

Requires significant time and development effort to implement from scratch.
Potential for bugs and edge cases that may not be initially covered, such as variations in reference formatting styles across different papers.
Building parsing logic that handles a wide range of citation styles may introduce complexity.


* Option B: Use an Existing Parsing Library

#### Pros:

Saves development time by leveraging existing parsing libraries that are well-tested and widely adopted.
Many existing libraries support various citation formats, reducing the need to implement custom parsing logic from scratch.
Likely to have comprehensive documentation and community support, aiding in quick implementation.

#### Cons:

Less control over how the parser works, which may result in limitations when customizing or extending the parser to handle specific cases required by Bigfoot.
Some libraries may not output in the exact format needed for Bigfoot, requiring additional transformation steps.
Existing libraries may be too generic, leading to inefficiencies or inaccuracies in parsing references for specific paper formats.

#### Examples/Considerations:
- Citation Styles: The parser will initially handle IEEE-style citations (e.g., “[1]”), but should be extensible for other formats like APA or MLA. Handling multiple styles will involve adding new parsing rules as needed.

- Error Handling: The parser must detect and handle inconsistencies, such as missing references or mismatched in-text citations, providing clear logs for debugging.
sizes.

- Output Format: The parser will generate an HTML file with footnotes properly formatted for Bigfoot to recognize, using <footer> or <sup> tags for citations.


## Decision Outcome

>> Chosen Option: Option A - Build a Custom Parser from Scratch

We have decided to build the PaperFootnote parser from scratch. While this option requires more upfront development work, it provides full control over the parsing process and ensures that the output is perfectly compatible with Bigfoot. This flexibility is crucial, as we anticipate needing to extend the parser in the future to handle different citation styles and formats. Furthermore, by developing a custom solution, we can ensure high accuracy in recognizing references and footnote placement, without relying on potentially inflexible or overly generic third-party libraries.

The custom parser will:

- Analyze the structure of the paper to identify references.
- Insert the references as footnotes at the appropriate locations.
- Generate an HTML file that Bigfoot can read, ensuring seamless integration with our existing system.