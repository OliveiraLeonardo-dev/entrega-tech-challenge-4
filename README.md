# Tech Challenge - Fase 4: Previsão de Ativos Financeiros

Este projeto utiliza uma rede neural **LSTM** (Long Short-Term Memory) para prever o preço de fechamento da ação **ITUB4.SA**, com dados processados via **AWS Glue** e treinados no **Amazon SageMaker**.

## 🚀 Resultados do Modelo
O modelo apresentou uma performance excepcional nos testes:
* **MAPE (Erro Percentual Médio):** 1.94% (Precisão de 98.06%)
* **MAE (Erro Médio Absoluto):** R$ 0.39
* **RMSE:** R$ 0.51

## 🛠️ Tecnologias Utilizadas
* **Ingestão/Limpeza:** AWS Glue (Python Shell)
* **Treinamento:** Amazon SageMaker (TensorFlow/Keras)
* **API:** FastAPI
* **Container:** Docker

## 📦 Como Executar com Docker
1. Construa a imagem:
   `docker build -t tech-challenge-app .`
2. Rode o container:
   `docker run -p 8000:8000 tech-challenge-app`
3. Acesse a documentação da API em: `http://localhost:8000/docs`