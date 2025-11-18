# 🧠 Predição de Calvície com Regressão Logística

Este projeto desenvolve um modelo de **Regressão Logística** para prever a probabilidade de um indivíduo apresentar **calvície**, utilizando variáveis biométricas e características do conjunto de dados fornecido. O notebook realiza todo o pipeline analítico: carregamento dos dados, tratamento, padronização, treinamento do modelo, avaliação e interpretação dos coeficientes (`odds ratios`).

---

## 📌 Objetivos do Projeto

- Construir um modelo de classificação binária usando **Regressão Logística**.
- Identificar **quais variáveis aumentam ou reduzem** o risco de calvície.
- Avaliar o desempenho do modelo com métricas apropriadas.
- Interpretar coeficientes via **odds ratio**, permitindo explicação clara e objetiva.

---

## 📂 Estrutura do Projeto

´´´
📁 Predicao-Calvicie/
├── Predição_de_Calvice-Regressao_Logistica.ipynb
├── Base_calvice_classificacao.csv
├── README.md
´´´

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **Python 3**
- **Pandas**
- **NumPy**
- **Scikit-learn**
  - train_test_split
  - StandardScaler
  - LogisticRegression
  - Métricas de classificação
- **Matplotlib / Seaborn**

---

## 🧹 Etapas do Processamento

### 1. Carregamento da Base de Dados  
Leitura da base *Base_calvice_classificacao.csv*.

### 2. Análise e Limpeza Inicial  
- Identificação de valores ausentes  
- Imputação via **mediana** nas variáveis numéricas

### 3. Separação entre Features e Target  
- Variável alvo: `Calvicie`

### 4. Padronização  
Padronização dos dados com `StandardScaler`.

### 5. Treinamento do Modelo  
- Divisão treino/teste  
- Regressão Logística como classificador

### 6. Avaliação  
- Acurácia  
- Matriz de confusão  
- Métricas de classificação por classe

### 7. Interpretação dos Coeficientes  
Transformação dos coeficientes em **odds ratios** para identificar impacto das variáveis:

- `odds_ratio > 1` → aumenta a chance de calvície  
- `odds_ratio < 1` → reduz a chance de calvície

---

## 📊 Resultados Obtidos

- **Acurácia aproximada:** ~59%  
- **Conclusões preliminares:**  
  O modelo oferece insights relevantes sobre as variáveis que influenciam o risco de calvície, ainda que o desempenho seja moderado — resultado comum em bases desbalanceadas.

---

## 🚀 Possíveis Melhorias Futuras

- Ajuste do threshold para otimizar sensibilidade/especificidade  
- Aplicação de métodos de balanceamento (ex.: **SMOTE**)  
- Testar algoritmos como Random Forest ou Gradient Boosting  
- Realizar engenharia de atributos  
- Construção de API ou dashboard para disponibilizar o modelo treinado

---

## 📄 Sobre o Projeto

Este notebook foi desenvolvido como parte de estudos de **machine learning aplicado à saúde**, com foco em classificação, pré-processamento e interpretação de modelos.

---
