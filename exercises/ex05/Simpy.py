"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730386091"


class Simpy:
    values: list[float]
    

    def __init__ (self, values: list[float]):
        self.values = values
    

    def __repr__ (self) -> str:
        return(f"{self.values}")


    def fill (self, val: float, length: int) -> None:
        self.values = [val]
        i: int = 1
        while i < length:
            self.values.append(val)
            i += 1
        

    ### FIX 
    def arange (self, start: float, stop: float, step=1.0) -> None:
        assert step != 0.0
        i = 0
        while i < abs(stop - step):
            self.values.append(start + (i * step))
            i += 1


    def sum (self) -> float:
        length: float = sum(self.values)
        return length


    def __add__ (self, rhs: Union[float, Simpy]) -> Simpy:
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item + rhs)

        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        
        return Simpy(result)


    def __pow__ (self, rhs: Union[float, Simpy]) -> Simpy:
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item ** rhs)

        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        
        return Simpy(result)


    def __mod__ (self, rhs: Union[float, Simpy]) -> Simpy:
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item % rhs)

        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] % rhs.values[i])
        
        return Simpy(result)


    def __eq__ (self, rhs: Union[float, Simpy]) -> list[bool]:
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        
        return result


    def __gt__ (self, rhs: Union[float, Simpy]) -> list[bool]:
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        
        return result


    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        if isinstance(rhs, int):
            result = self.values[rhs]

        else:
            i = 0
            rslt: list[float] = []
            for item in rhs:
                if item == True:
                    rslt.append(self.values[i])
                i += 1
            result = Simpy([])
            result.values = rslt
        return result