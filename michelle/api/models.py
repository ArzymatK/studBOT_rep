from sqlalchemy import Column, Integer, String, ForeignKey, Text, DECIMAL, Table, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

dish_svg_association = Table(
    'dishes_svgs',
    Base.metadata,
    Column('dish_id', Integer, ForeignKey('dishes.id')),
    Column('svg_id', Integer, ForeignKey('svgs.id'))
)


class Category(Base):
    tablename = 'categories'

    id = Column(Integer, primary_key=True)
    title_ru = Column(String(120))
    title_kg = Column(String(120))
    title_tu = Column(String(120))
    title_en = Column(String(120))
    image = Column(String(255))
    link = Column(String(100))

    is_about = Column(Boolean, default=False)
    is_constructr = Column(Boolean, default=False)
    is_collagen = Column(Boolean, default=False)
    is_coffe = Column(Boolean, default=False)
    is_tea = Column(Boolean, default=False)
    is_drink = Column(Boolean, default=False)
    is_bar = Column(Boolean, default=False)
    is_smuzi = Column(Boolean, default=False)
    is_wine = Column(Boolean, default=False)
    is_sale = Column(Boolean, default=False)
    number = Column(Integer, default=0, nullable=True)

    subcategories = relationship("SubCategory", back_populates="category")


class SubCategory(Base):
    tablename = 'subcategories'

    id = Column(Integer, primary_key=True)
    title_ru = Column(String(120))
    title_kg = Column(String(120))
    title_tu = Column(String(120))
    title_en = Column(String(120))
    category_id = Column(Integer, ForeignKey('categories.id'))

    custom_orange_ru = Column(String(120), nullable=True)
    custom_orange_kg = Column(String(120), nullable=True)
    custom_orange_tu = Column(String(120), nullable=True)
    custom_orange_en = Column(String(120), nullable=True)
    custom_black_ru = Column(String(120), nullable=True)
    custom_black_kg = Column(String(120), nullable=True)
    custom_black_tu = Column(String(120), nullable=True)
    custom_black_en = Column(String(120), nullable=True)
    main_title_ru = Column(String(120), nullable=True)
    main_title_kg = Column(String(120), nullable=True)
    main_title_tu = Column(String(120), nullable=True)
    main_title_en = Column(String(120), nullable=True)
    category = relationship("Category", back_populates="subcategories")


class SVG(Base):
    tablename = 'svgs'

    id = Column(Integer, primary_key=True)
    svg = Column(String(255))


class Dish(Base):
    tablename = 'dishes'

    id = Column(Integer, primary_key=True)
    title_ru = Column(String(120))
    title_kg = Column(String(120))
    title_tu = Column(String(120))
    title_en = Column(String(120))
    image = Column(String(255))
    subcategory_id = Column(Integer, ForeignKey('subcategories.id'))
    text_ru = Column(Text)
    text_kg = Column(Text)
    text_tu = Column(Text)
    text_en = Column(Text)

    advice_ru = Column(Text)
    advice_kg = Column(Text)
    advice_tu = Column(Text)
    advice_en = Column(Text)

    price = Column(DECIMAL(10, 2), default=0)
    weight = Column(Integer, default=0, nullable=True)

    subcategory = relationship("SubCategory", back_populates="dishes")
    svgs = relationship("SVG", secondary=dish_svg_association, backref="dishes")


SubCategory.dishes = relationship("Dish", back_populates="subcategory")
Category.subcategories = relationship("SubCategory", back_populates="category")