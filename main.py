import os
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel


DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:Lilika10%23@localhost/dfimoveis_db")
# DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class TipoImovel(Base):
    __tablename__ = "tipo_imovel"
    id = Column(Integer, primary_key=True, index=True)
    nome_tipo_imovel = Column(String(100))
    imoveis = relationship("Imovel", back_populates="tipo_imovel_rel")

class TipoOperacao(Base):
    __tablename__ = "tipo_operacao"
    id = Column(Integer, primary_key=True, index=True)
    nome_operacao = Column(String(100))
    imoveis = relationship("Imovel", back_populates="tipo_operacao_rel")

class Imobiliaria(Base):
    __tablename__ = "imobiliaria"
    id = Column(Integer, primary_key=True, index=True)
    creci = Column(String(50))
    nome_imobiliaria = Column(String(150))
    imoveis = relationship("Imovel", back_populates="imobiliaria_rel")

class Imovel(Base):
    __tablename__ = "imoveis"
    id = Column(Integer, primary_key=True, index=True)
    endereco = Column(String(255))
    preco = Column(Float)
    tamanho_m2 = Column(Float)
    quartos = Column(Integer)
    vagas = Column(Integer)
    suites = Column(Integer)
    
    imobiliaria_id = Column(Integer, ForeignKey("imobiliaria.id"))
    tipo_operacao_id = Column(Integer, ForeignKey("tipo_operacao.id"))
    tipo_imovel_id = Column(Integer, ForeignKey("tipo_imovel.id"))

    imobiliaria_rel = relationship("Imobiliaria", back_populates="imoveis")
    tipo_operacao_rel = relationship("TipoOperacao", back_populates="imoveis")
    tipo_imovel_rel = relationship("TipoImovel", back_populates="imoveis")

Base.metadata.create_all(bind=engine)


class TipoImovelSchema(BaseModel):
    nome_tipo_imovel: str
    class Config:
        from_attributes = True
        orm_mode = True

class TipoOperacaoSchema(BaseModel):
    nome_operacao: str
    class Config:
        from_attributes = True
        orm_mode = True

class ImobiliariaSchema(BaseModel):
    creci: str
    nome_imobiliaria: str
    class Config:
        from_attributes = True
        orm_mode = True

class ImovelSchema(BaseModel):
    endereco: str
    preco: float
    tamanho_m2: float
    quartos: int
    vagas: int
    suites: int
    imobiliaria_id: int
    tipo_operacao_id: int
    tipo_imovel_id: int
    class Config:
        from_attributes = True
        orm_mode = True

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



from fastapi.responses import JSONResponse, RedirectResponse
import traceback

@app.get("/")
def root():
    """Redireciona a raiz do site para a página visual de Documentação da API"""
    return RedirectResponse(url="/docs")

@app.get("/imoveis", response_model=list[ImovelSchema])
def listar_imoveis(db: Session = Depends(get_db)):
    try:
        return db.query(Imovel).all()
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e), "traceback": traceback.format_exc()})

@app.post("/imoveis")
def cadastrar_imovel(imovel_da_requisicao: ImovelSchema, db: Session = Depends(get_db)):
    # O ** transforma o JSON do Postman em um objeto do Banco
    novo_imovel = Imovel(**imovel_da_requisicao.dict())
    db.add(novo_imovel)
    db.commit()
    db.refresh(novo_imovel)
    return novo_imovel

@app.post("/tipo-imovel")
def cadastrar_tipo_imovel(req: TipoImovelSchema, db: Session = Depends(get_db)):
    novo = TipoImovel(**req.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.post("/tipo-operacao")
def cadastrar_tipo_operacao(req: TipoOperacaoSchema, db: Session = Depends(get_db)):
    novo = TipoOperacao(**req.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.post("/imobiliaria")
def cadastrar_imobiliaria(req: ImobiliariaSchema, db: Session = Depends(get_db)):
    novo = Imobiliaria(**req.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo