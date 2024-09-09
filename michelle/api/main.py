from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Category, SubCategory, SVG, Dish
from schemas import CategoryBase, SubCategoryBase, DishBase, SVGBase, CategoryWithSubCategories
from decouple import config
from typing import List

BASE_URL = config('BASE_URL')

SQLALCHEMY_DATABASE_URL = f"postgresql://sanjik:1@db:5432/michelle_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "https://menu.michelle.kg",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/categories/", response_model=List[CategoryBase])
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).order_by(Category.number).all()
    for category in categories:
        if category.image:
            category.image = BASE_URL + "media/" + category.image
    return categories


@app.get("/categories/{category_id}/subcategories/", response_model=List[SubCategoryBase])
def get_subcategories(category_id: int, db: Session = Depends(get_db)):
    subcategories = db.query(SubCategory).filter(SubCategory.category_id == category_id).all()
    return subcategories


@app.get("/subcategories/", response_model=List[SubCategoryBase])
def get_subcategories(request: Request, db: Session = Depends(get_db)):
    subcategories = db.query(SubCategory).all()
    return subcategories


@app.get("/subcategories/{subcategory_id}/dishes/", response_model=List[DishBase])
def get_dishes(subcategory_id: int, db: Session = Depends(get_db)):
    dishes = db.query(Dish).filter(Dish.subcategory_id == subcategory_id).all()
    for dish in dishes:
        if dish.image:
            dish.image = BASE_URL + "media/" + dish.image
        dish.svg_urls = [{"id": svg.id, "svg": BASE_URL + "media/" + svg.svg} for svg in dish.svgs]
    return dishes


@app.get("/dishes/", response_model=List[DishBase])
def get_dishes(request: Request, db: Session = Depends(get_db)):
    dishes = db.query(Dish).all()
    for dish in dishes:
        if dish.image:
            dish.image = BASE_URL + "media/" + dish.image
    return dishes


@app.get("/svgs/", response_model=List[SVGBase])
def get_svgs(request: Request, db: Session = Depends(get_db)):
    svgs = db.query(SVG).all()
    for svg in svgs:
        if svg.svg:
            svg.svg = BASE_URL + "media/" + svg.svg
    return svgs