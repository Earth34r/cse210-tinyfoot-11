import re
import argparse
import os

class paperReferenceFootnote:

    def __init__(self):
        self.orignalContent = ""
        self.referenceContent = ""
        self.rawReferences = []
        self.references = ['' for _ in range(1005)]
        self.referPositions = [[] for _ in range(1005)]
        self.refPattern = re.compile(r"\[(\d+)\]: (.*)") # Need to change this pattern [1]
        self.refPosPattern = re.compile(r"\{\d+\}") # Need to change this pattern {1}
        self.header = ''
        self.footer = ''

    def getContentFromOriginalFile(self, path):
        with open(path, 'r') as file:
            self.orignalContent = file.read()
        return self.orignalContent
    
    def generateBkupFile(self, path):
        with open(path, 'r') as file:
            content = file.read()
        with open(path + ".bkup", 'w') as file:
            file.write(content)

    def getReferenceContent(self):
        references = self.refPattern.findall(self.orignalContent)
        self.rawReferences = references[:]

    def getReferencePositions(self):
        # self.referPositions = [m.start() for m in re.finditer(self.refPosPattern, self.orignalContent)]
        for m in re.finditer(self.refPosPattern, self.orignalContent):
            index = int(m.group()[1:-1])
            self.referPositions[index].append(m.start())
        return self.referPositions

    def insertFootnote(self):
        # assert len(self.referPositions) == len(self.references), "Ref and Pos not match"
        # for i in range(len(self.referPositions)):
        #     if len(self.referPositions[i]) == 0:
        #         continue
        #     curFootnote = self.references[i] # Need to change this pattern
            # for curPos in self.referPositions[i]:
            #     self.orignalContent = self.orignalContent[:curPos] + curFootnote + self.orignalContent[curPos:]
        # return self.orignalContent
        pass
    
    def writeContentToFile(self, path):
        with open(path, 'w') as file:
            file.write(self.orignalContent)

    def demo(self):
        self.getContentFromOriginalFile("sample.txt")
        self.generateBkupFile("sample.txt")
        self.getReferenceContent()
        self.getReferencePositions()
        self.insertFootnote()
        self.writeContentToFile("sample.txt")

    def restoreFile(self, path):
        with open(path + ".bkup", 'r') as file:
            content = file.read()
        with open(path, 'w') as file:
            file.write(content)
        # Remove the backup file
        os.remove(path + ".bkup")

    def getHeaderandFooter(self, headerPath):
        with open(headerPath, 'r') as file:
            headerAndFooter = file.read()
        self.header = headerAndFooter.split("HEADEREND")[0]
        self.footer = headerAndFooter.split("HEADEREND")[1]

    def convertToHTML(self, outputPath):
        contentByLine = self.orignalContent.split('\n')
        contentByLine = [line for line in contentByLine if line != '']
        contentByLine = ['\t<p>' + line + '</p>' for line in contentByLine]
        with open(outputPath + '/index.html', 'w') as file:
            file.write(self.header + '\n')
            for line in contentByLine:
                match = self.refPosPattern.search(line)
                if match:
                    index = int(match.group()[1:-1])
                    line = line.replace(match.group(), '<a href="#fn{}" class="footnote">[{}]</a>'.format(index, index))
                    file.write(line + '\n')
                    file.write('\t<div class="footnotes">\n')
                    file.write('\t\t<ol>\n')
                    file.write('\t\t\t<li id="fn{}">'.format(index) + self.references[index] + '</li>\n')
                    file.write('\t\t</ol>\n')
                    file.write('\t</div>\n\n')
                else:
                    file.write(line + '\n')
            file.write(self.footer + '\n')


    def matchReferences(self):
        for ref in self.rawReferences:
            self.references[int(ref[0])] = ref[1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Demo for paper reference footnote')
    parser.add_argument('--input', type=str, help='File path', default='/home/commcheck/gredCodings/CSE210/repos/cse210-tinyfoot-11/paperReferenceFootnote/demo')
    parser.add_argument('--header', type=str, help='Header file path', default='/home/commcheck/gredCodings/CSE210/repos/cse210-tinyfoot-11/paperReferenceFootnote/header')
    parser.add_argument('--output', type=str, help='Output file path', default='/home/commcheck/gredCodings/CSE210/repos/cse210-tinyfoot-11/paperReferenceFootnote/')
    args = parser.parse_args()
    foot = paperReferenceFootnote()
    foot.getContentFromOriginalFile(args.input)
    foot.generateBkupFile(args.input)
    foot.getReferenceContent()
    foot.getReferencePositions()
    foot.matchReferences()
    foot.insertFootnote()
    foot.writeContentToFile(args.input)
    foot.getHeaderandFooter(args.header)
    foot.convertToHTML(args.output)
    foot.restoreFile(args.input)

    
        

    
