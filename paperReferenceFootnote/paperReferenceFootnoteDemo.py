import re
import argparse

class paperReferenceFootnote:

    def __init__(self):
        self.orignalContent = ""
        self.referenceContent = ""
        self.references = []
        self.referPositions = []
        self.refPattern = re.compile(r"\[\d+\]") # Need to change this pattern
        self.refPosPattern = re.compile(r"\[\d+\]") # Need to change this pattern

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
        self.references = references[:]

    def getReferencePositions(self):
        self.referPositions = [m.start() for m in re.finditer(self.refPosPattern, self.orignalContent)]

    def insertFootnote(self):
        assert len(self.referPositions) == len(self.references), "Ref and Pos not match" # Check if the number of references and positions are same
        for i in range(len(self.referPositions)):
            curFootnote = self.references[i] # Need to change this pattern
            curPos = self.referPositions[i]
            self.orignalContent = self.orignalContent[:curPos] + curFootnote + self.orignalContent[curPos:]
        return self.orignalContent
    
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Demo for paper reference footnote')
    parser.add_argument('--input', type=str, help='File path')
    args = parser.parse_args()
    foot = paperReferenceFootnote()
    foot.getContentFromOriginalFile(args.input)
    foot.generateBkupFile(args.input)
    foot.getReferenceContent()
    foot.getReferencePositions()
    foot.insertFootnote()
    foot.writeContentToFile(args.input)

    
        

    
