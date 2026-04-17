import os
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

# Mesmo banco do main.py
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:Lilika10%23@localhost/dfimoveis_db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def rodar_scraping():
    print("Iniciando coleta de dados (Simulação de Webscraping)...")
    db = SessionLocal()
    # Mock de dados maiores para o gráfico
    dados_site = [
        {"endereco": "Asa Sul SQS 310", "preco": 1450000.0, "tamanho": 110.0, "vagas": 2},
        {"endereco": "Sudoeste SQSW 105", "preco": 1600000.0, "tamanho": 95.0, "vagas": 2},
        {"endereco": "Noroeste SQNW 311", "preco": 1900000.0, "tamanho": 125.0, "vagas": 3},
        {"endereco": "Águas Claras - Rua 20 Sul", "preco": 850000.0, "tamanho": 75.0, "vagas": 1},
        {"endereco": "Guará II - SQB", "preco": 1100000.0, "tamanho": 90.0, "vagas": 2},
        {"endereco": "Asa Norte SQN 215", "preco": 1250000.0, "tamanho": 105.0, "vagas": 1}
    ]
    
    from main import Imovel
    for item in dados_site:
        novo = Imovel(
            endereco=item['endereco'], 
            preco=item['preco'], 
            tamanho_m2=item['tamanho'],
            imobiliaria_id=1,
            tipo_operacao_id=1,
            tipo_imovel_id=1,
            quartos=3,
            vagas=item['vagas'],
            suites=1
        )
        db.add(novo)
    
    db.commit()
    db.close()
    print("Dados salvos com sucesso!")

if __name__ == "__main__":
    rodar_scraping()