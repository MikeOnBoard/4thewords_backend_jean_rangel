from fastapi import FastAPI, HTTPException, UploadFile, File, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional, List
from datetime import datetime
import os
import aiofiles
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/4thewords_prueba_jean_rangel"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

class LegendBase(SQLModel):
    title: str
    description: str
    category: str
    province: str
    canton: str
    district: str
    
class Legend(LegendBase, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    image_url: str
    created_at: datetime = Field(default_factory=datetime.now)

class LegendCreate(LegendBase):
    pass

class LegendRead(LegendBase):
    id: int
    image_url: str
    created_at: datetime

class LegendUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    province: Optional[str] = None
    canton: Optional[str] = None
    district: Optional[str] = None

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

UPLOAD_DIRECTORY = "uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/uploads", StaticFiles(directory=UPLOAD_DIRECTORY), name="uploads")

@app.post("/api/legends", response_model=LegendRead)
async def create_legend(
    title: str = Form(...),
    description: str = Form(...),
    category: str = Form(...),
    province: str = Form(...),
    canton: str = Form(...),
    district: str = Form(...),
    image: UploadFile = File(...),
    session: Session = Depends(get_session)
):
    file_location = os.path.join(UPLOAD_DIRECTORY, image.filename)
    async with aiofiles.open(file_location, "wb") as buffer:
        await buffer.write(await image.read())
    
    image_url = f"/uploads/{image.filename}"
    legend = Legend(
        title=title, description=description, category=category,
        province=province, canton=canton, district=district,
        image_url=image_url
    )
    session.add(legend)
    session.commit()
    session.refresh(legend)
    return legend

@app.get("/api/legends", response_model=List[LegendRead])
def get_legends(
    session: Session = Depends(get_session)
):
    legends = session.scalars(select(Legend)).all()
    return legends

@app.get("/api/legends/{legend_id}", response_model=LegendRead)
def get_legend(legend_id: int, session: Session = Depends(get_session)):
    legend = session.get(Legend, legend_id)
    if not legend:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return legend

@app.put("/api/legends/{legend_id}", response_model=LegendRead)
async def update_legend(
    legend_id: int,
    title: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    category: Optional[str] = Form(None),
    province: Optional[str] = Form(None),
    canton: Optional[str] = Form(None),
    district: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
    session: Session = Depends(get_session)
):
    legend = session.get(Legend, legend_id)
    if not legend:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    
    legend.title = title or legend.title
    legend.description = description or legend.description
    legend.category = category or legend.category
    legend.province = province or legend.province
    legend.canton = canton or legend.canton
    legend.district = district or legend.district
    
    if image:
        file_location = os.path.join(UPLOAD_DIRECTORY, image.filename)
        async with aiofiles.open(file_location, "wb") as buffer:
            await buffer.write(await image.read())
        legend.image_url = f"/uploads/{image.filename}"
    
    session.commit()
    session.refresh(legend)
    return legend

@app.delete("/api/legends/{legend_id}")
def delete_legend(legend_id: int, session: Session = Depends(get_session)):
    legend = session.get(Legend, legend_id)
    if not legend:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    session.delete(legend)
    session.commit()
    return {"message": "Leyenda eliminada correctamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
