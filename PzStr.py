from __future__ import annotations

class PzStr(str):
    def __init__(self, string:str):
        super().__init__()
        self.string = string

    def __str__(self):
        return self.string

    def __setitem__(self, index:int, value):
        string = ""
        for i in range(self.length):
            if i == index:
                string += value
                continue
            string += self.string[i]
        self.string = string

    def reverse(self) -> PzStr:
        self.string = self.string[::-1]
        return PzStr(self.string)

    def isEmpty(self) -> bool:
        return self.length == 0

    def isNotEmpty(self) -> bool:
        return self.length != 0

    def asList(self) -> list:
        return list(self.string)

    def substring(self,begin:int,end:int) ->PzStr:
        return PzStr(self.string[begin:end])


    def remove(self,string:str)->PzStr:
        self.string = self.string.replace(string,"")
        return PzStr(self.string)

    def removeWhere(self,condition:lambda item:bool):
        pzString = PzStr(self.string)
        catchCounter = 0
        for i in range(self.length):
            item = self.string[i]
            if condition(item):
                pzString.removeAt(i-catchCounter)
                catchCounter+=1
        self.string = pzString.string

    def removeAt(self,index:int)->PzStr:
        self.__setitem__(index,"")
        return PzStr(self.string)

    def forEach(self,function:lambda item:item):
        for item in self.string:
            function(item)

    def where(self,condition:lambda item:bool,function:lambda item:str):
        pzString = PzStr(self.string)
        for i in range(self.length):
            item = self.string[i]
            if condition(item):
                pzString[i] = function(item)
        self.string = pzString.string

    def whereIndex(self,condition:lambda index:int,function:lambda index,item:item):
        pzString = PzStr(self.string)
        for i in range(self.length):
            item = self.string[i]
            if condition(i):
                pzString[i] = function(i,item)
        self.string = pzString.string




    @property
    def length(self)->int:
        return len(self.string)

    @property
    def first(self)->PzStr:
        if self.length == 0:
            return PzStr("")
        return PzStr(self.string[0])

    @property
    def last(self) -> PzStr:
        if self.length == 0:
            return PzStr("")
        return PzStr(self.string[-1])
