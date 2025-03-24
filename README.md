# Pipeline ETL com Python: Validando Dados e Planilhas de Excel para um Dashboard

Este projeto visa criar um pipeline ETL utilizando Python, focando na validação de dados e na transformação de planilhas de Excel em um dashboard interativo e informativo. O objetivo é acompanhar o desempenho durante as minhas tarefas de atendimento na empresa, garantindo a qualidade e integridade dos dados antes de serem visualizados.

## Funcionalidades do Projeto

### 1. **Profile Report do Pandas Profiling**
A primeira etapa do pipeline consiste em gerar um **relatório de perfil** (Profile Report) utilizando a biblioteca **Pandas Profiling**. Esse relatório fornece uma análise exploratóriado dataset, destacando a distribuição dos dados, valores ausentes, correlações, e outros insights valiosos para entender a qualidade do dataset.

- **Arquivo:** `main.py`
- **Print da funcionalidade:**
  [Análise Exploratória](C:\Users\marip\OneDrive\Documentos\Python_Scripts\etl-python-tma\images\pandas-profiling-ok.png)


### 2. **Contrato de Dados**
Em seguida, utilizamos um **contrato de dados** para garantir que os dados preenchidos estejam dentro de um padrão específico. Este contrato é configurado em um arquivo separado para ser utilizado como referência durante a validação dos dados.

- **Arquivo:** `validador_dados.py`
- **Print da funcionalidade:**
  *Aqui, insira um print do contrato de dados ou do código que define as regras de validação*

### 3. **Validação do Dataset**
A terceira etapa do pipeline envolve a **validação** do dataset. Após preencher o arquivo `.csv`, a aplicação irá verificar se os dados estão dentro das condições aceitas no contrato de dados. Caso um erro seja encontrado, ele será identificado, juntamente com a linha do erro e sugestões de onde procurar a solução.

- **Arquivo:** `aplicacao.py`
- **Print da funcionalidade:**
  *Aqui, insira um print mostrando a interface ou o erro gerado, com as sugestões de correção*

### 4. **Dashboard de Visualização**
Após corrigir os erros e garantir que os dados estão de acordo com o contrato, o último passo do pipeline é enviar os dados para um **dashboard**. O dashboard é projetado para fornecer uma visualização simples, mas fiel ao objetivo de acompanhamento de desempenho. Ele exibe métricas e gráficos baseados no dataset validado.

- **Print da funcionalidade:**
  *Aqui, insira um print do dashboard exibindo os dados finais após a validação e transformação*

## Como Executar

Para rodar este projeto localmente, siga os seguintes passos:

### 1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/pipeline-etl-dashboard.git
cd pipeline-etl-dashboard

Instale as despedências
pip install -r requirements.txt
