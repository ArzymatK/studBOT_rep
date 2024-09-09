from pydantic import BaseModel
from typing import List, Optional

class SVGBase(BaseModel):
    id: int
    svg: str

    class Config:
        orm_mode = True

class DishBase(BaseModel):
    id: int
    title_ru: str
    title_kg: str
    title_tu: str
    title_en: str
    image: Optional[str] = None
    subcategory_id: int
    text_ru: str
    text_kg: str
    text_tu: str
    text_en: str

    advice_ru: Optional[str] = None
    advice_kg: Optional[str] = None
    advice_tu: Optional[str] = None
    advice_en: Optional[str] = None

    price: float
    weight: Optional[int] = None
    svg_urls: List[SVGBase] = []

    class Config:
        orm_mode = True

class SubCategoryBase(BaseModel):
    id: int
    title_ru: str
    title_kg: str
    title_tu: str
    title_en: str
    category_id: int

    custom_orange_ru: Optional[str] = None
    custom_orange_kg: Optional[str] = None
    custom_orange_tu: Optional[str] = None
    custom_orange_en: Optional[str] = None
    custom_black_ru: Optional[str] = None
    custom_black_kg: Optional[str] = None
    custom_black_tu: Optional[str] = None
    custom_black_en: Optional[str] = None
    main_title_ru: Optional[str] = None
    main_title_kg: Optional[str] = None
    main_title_tu: Optional[str] = None
    main_title_en: Optional[str] = None



    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    id: int
    title_ru: str
    title_kg: str
    title_tu: str
    title_en: str
    image: Optional[str] = None
    link: str
    is_about: bool
    is_constructr: bool
    is_collagen: bool
    is_coffe: bool
    is_tea: bool
    is_drink: bool
    is_bar: bool
    is_smuzi: bool
    is_wine: bool
    is_sale: bool
    number: Optional[int] = None

    class Config:
        orm_mode = True


class CategoryWithSubCategories(BaseModel):
    category: CategoryBase
    subcategories: List[SubCategoryBase]