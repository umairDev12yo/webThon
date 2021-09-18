class document:
    def createParagraph(ides="",classs="",text="hello world"):
        index=open("template/index.html","a")
        index.write(f'\n <p class="{classs}" id="{ides}">{text}</p>')
        index.close()
    def createInput(ides="",classs=""):
        index=open("template/index.html","a")
        index.write(f'\n <input type="text" class="{classs} id="{ides}>')
        index.close()
    def createHeading(size="",text="",ides="",classs=""):
        index=open("template/index.html","a")
        index.write(f'\n <h{size} id="{ides}" class="{classs}">{text}</h{size}>')
        index.close()
    def mainClassHtml():
        index=open("template/index.html","w")
        index.write("")
        index.close()
    def startDiv(classs="",ides=""):
        index=open("template/index.html","a")
        index.write(f'\n<div class="{classs}" id="{ides}">')
        index.close()
    def endDiv():
        index=open("template/index.html","a")
        index.write(f'\n</div>')
        index.close()
    def createHeadingIn(size="",text="",ides="",classs=""):
        index=open("template/index.html","a")
        index.write(f'\n    <h{size} id="{ides}" class="{classs}">{text}</h{size}>')
        index.close()
    def addImage(name="",classs="",ides=""):
        index=open("template/index.html","a")
        index.write(f'\n<img src="images/{name}" alt="unable to show" class="{classs}" id="{ides}">')
        index.close()
    def startList(classs="",ides=""):
        index=open("template/index.html","a")
        index.write(f'\n<ul class="{classs}" id="{ides}">')
        index.close()
    def endList(classs="",ides=""):
        index=open("template/index.html","a")
        index.write(f'\n</ul>')
        index.close()
    def createContent(contents=""):
        index=open("template/index.html","a")
        index.write(f'\n    <li>{contents}</li>')
    def createButton(text="",classs="",ides=""):
        index=open("template/index.html","a")
        index.write(f'\n<button class="{classs}" id="{ides}">')
        index.close()
    def mix(type=""):
        if(type=="style"):
            index=open("template/index.html","a")
            index.write(f'<link rel="stylesheet" href="style.css">')
            index.close()
class style:
    def __init__(self,property,propertyValue):
        self.property=property
        self.propertyValue=propertyValue
        
    def mix():
        index=open("template/index.html","a")
        index.write('<link rel="stylesheet" href="style.css">')
        index.close()
    def addPropertyForClass(property,propertyValue,classsName):
        stylish=open("template/style.css","a")
        stylish.write(f'.{classsName}')
        stylish.write('\n{')
        stylish.write(f'\n    {property}:{propertyValue}')
        stylish.write('\n}')
        stylish.close()
    def mainClassCSS():
        stylish=open('template/style.css','w')
        stylish.write("")
        stylish.close()