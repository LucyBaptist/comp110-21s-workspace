"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730386091"


class Simpy:
    values: list[float]

    def __init__ (self, values: list[float]):
        self.values = values
    
    def __repr__ (self) -> str:
        