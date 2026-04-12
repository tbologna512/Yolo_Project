from dataclasses import dataclass
from typing import Optional


@dataclass
class BoundingBox:
    x: int
    y: int
    width: int
    height: int


@dataclass
class CandyProduct:
    name: str
    brand: str = ""


@dataclass
class Detection:
    confidence: float
    label: str
    bounding_box: Optional[BoundingBox] = None
    candy_product: Optional[CandyProduct] = None


@dataclass
class TrainingImage:
    file_path: str