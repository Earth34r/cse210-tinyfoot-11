const fs = require('fs');
const path = require('path');

class PaperReferenceFootnote {
    constructor() {
        this.originalContent = "";
        this.referenceContent = "";
        this.rawReferences = [];
        this.references = Array(1005).fill('');
        this.referPositions = Array(1005).fill().map(() => []);
        this.refPattern = /\[(\d+)\]: (.*)/g;  // Need to change this pattern [1]
        this.refPosPattern = /\{\d+\}/g;  // Need to change this pattern {1}
        this.header = '';
        this.footer = '';
    }

    getContentFromOriginalFile(filePath) {
        this.originalContent = fs.readFileSync(filePath, 'utf8');
        return this.originalContent;
    }

    generateBkupFile(filePath) {
        const content = fs.readFileSync(filePath, 'utf8');
        fs.writeFileSync(`${filePath}.bkup`, content);
    }

    getReferenceContent() {
        this.rawReferences = [...this.originalContent.matchAll(this.refPattern)];
    }

    getReferencePositions() {
        let match;
        while ((match = this.refPosPattern.exec(this.originalContent)) !== null) {
            const index = parseInt(match[0].slice(1, -1));  // Extract the index
            this.referPositions[index].push(match.index);
        }
        return this.referPositions;
    }

    writeContentToFile(filePath) {
        fs.writeFileSync(filePath, this.originalContent);
    }

    restoreFile(filePath) {
        const content = fs.readFileSync(`${filePath}.bkup`, 'utf8');
        fs.writeFileSync(filePath, content);
        fs.unlinkSync(`${filePath}.bkup`);  // Remove the backup file
    }

    getHeaderandFooter(headerPath) {
        const headerAndFooter = fs.readFileSync(headerPath, 'utf8');
        const parts = headerAndFooter.split("HEADEREND");
        this.header = parts[0];
        this.footer = parts[1];
    }
    convertToHTML(outputPath) {
        let contentByLine = this.originalContent.split('\n').filter(line => line !== '');
        contentByLine = contentByLine.map(line => `\t<p>${line}</p>`);
        
        const outputFilePath = path.join(outputPath, 'index.html');
        const writeStream = fs.createWriteStream(outputFilePath);
        
        writeStream.write(this.header + '\n');
        
        contentByLine.forEach(line => {
            let footnoteMatches = [...line.matchAll(this.refPosPattern)]; 
            footnoteMatches.forEach(match => {
                const index = parseInt(match[0].slice(1, -1));
                line = line.replace(match[0], `<a href="#fn${index}" class="footnote">[${index}]</a>`);

                writeStream.write('\t<div class="footnotes">\n');
                writeStream.write('\t\t<ol>\n');
                writeStream.write(`\t\t\t<li id="fn${index}">${this.references[index]}</li>\n`);
                writeStream.write('\t\t</ol>\n');
                writeStream.write('\t</div>\n\n');
            });
            
            writeStream.write(line + '\n'); 
        });
        
        writeStream.write(this.footer + '\n');
        writeStream.end();
    }
    

    matchReferences() {
        this.rawReferences.forEach(ref => {
            const index = parseInt(ref[1]);
            this.references[index] = ref[2];
        });
    }
}

if (require.main === module) {
    const args = process.argv.slice(2);
    const input = args[0] || '/home/commcheck/gredCodings/CSE210/repos/cse210-tinyfoot-11/paperReferenceFootnote/demo';
    const header = args[1] || '/home/commcheck/gredCodings/CSE210/repos/cse210-tinyfoot-11/paperReferenceFootnote/header';
    const output = args[2] || '/home/commcheck/gredCodings/CSE210/repos/cse210-tinyfoot-11/paperReferenceFootnote/';

    const footnote = new PaperReferenceFootnote();
    footnote.getContentFromOriginalFile(input);
    footnote.generateBkupFile(input);
    footnote.getReferenceContent();
    footnote.getReferencePositions();
    footnote.matchReferences();
    footnote.writeContentToFile(input);
    footnote.getHeaderandFooter(header);
    footnote.convertToHTML(output);
    footnote.restoreFile(input);
}
