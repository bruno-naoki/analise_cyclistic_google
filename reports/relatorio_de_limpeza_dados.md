# Relatório de Limpeza e Preparação dos Dados — Cyclistic

## 1. Consolidação dos dados

Foram carregados e combinados 12 arquivos CSV, referentes a janeiro a dezembro de 2025, totalizando inicialmente **5.552.994 registros e 13 colunas**.

## 2. Inspeção e transformação

Foram verificadas a estrutura, as colunas, os valores ausentes e os tipos de dados. As colunas `started_at` e `ended_at` foram convertidas para o formato datetime, e as quatro colunas de coordenadas geográficas foram removidas por não serem necessárias às análises.

## 3. Validação dos registros

Foi realizada uma auditoria de identificadores `ride_id` para verificar duplicidades, sem identificação de registros duplicados nos arquivos verificados. Também foram identificados 29 registros com duração negativa, associados à mudança de horário em novembro de 2025, que receberam tratamento específico.

## 4. Duração das viagens

A coluna `ride_length` foi criada a partir da diferença entre os horários de início e término, em segundos. Também foram identificadas 7.824 viagens com duração superior a 12 horas e 5.585 acima de 24 horas, para avaliação de possíveis valores extremos.

## 5. Resultado final

Após o tratamento dos registros com duração negativa, a base utilizada nas análises passou a conter **5.552.965 registros e 9 colunas originais**. Também foram criadas variáveis temporais, como mês, dia, ano e dia da semana, para possibilitar as análises comparativas e a construção dos gráficos no Tableau.