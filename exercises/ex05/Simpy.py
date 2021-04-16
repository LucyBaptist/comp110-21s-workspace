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
        i: int = 0
        while i <= length:
            self.values.append(val)
            i += 1
        

    def arange ([self, start: float, stop: float, step: float]) -> None:
        assert step != 0.0
        self.values[0] = start
        i: float = 0
        while i < stop:
            self.values.append(i)
            i *= step


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


    def __pow___ (self, rhs: Union[float, Simpy]) -> Simpy:
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