# Cyclistic — Análise de Dados de Compartilhamento de Bicicletas (2025)

## Sobre o projeto

Este projeto analisa os dados históricos de viagens da Cyclistic, uma empresa fictícia de compartilhamento de bicicletas de Chicago, com o objetivo de identificar diferenças nos padrões de utilização entre usuários casuais e membros anuais.

O estudo busca responder à seguinte pergunta:

**Como os membros anuais e os usuários casuais utilizam as bicicletas da Cyclistic de maneiras diferentes?**

O projeto foi desenvolvido como estudo de caso inspirado no Google Data Analytics Certificate, aplicando conceitos de preparação, validação, análise e visualização de dados.

## Objetivo de negócio

A equipe de marketing da Cyclistic deseja compreender as diferenças de comportamento entre usuários casuais e membros anuais para identificar oportunidades de conversão de usuários casuais em membros com assinaturas anuais.

A análise investiga padrões relacionados a:

- Frequência de utilização das bicicletas.
- Duração média das viagens.
- Distribuição das viagens ao longo dos dias da semana.
- Variações mensais de utilização.
- Preferência por tipos de bicicleta.

## Dados utilizados

Foram utilizados dados históricos públicos de viagens disponibilizados pela Motivate International Inc.

- **Período analisado:** janeiro a dezembro de 2025.
- **Quantidade de arquivos:** 12 arquivos CSV mensais.
- **Registros originais consolidados:** 5.552.994 viagens.
- **Registros após a preparação e limpeza:** 5.552.965 viagens.
- **Fonte:** [Divvy Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html).
- **Licença:** [Divvy Data License Agreement](https://divvybikes.com/data-license-agreement).

Os dados utilizados contêm informações sobre as viagens, como identificadores, datas e horários, tipos de bicicleta e categorias de usuários. Não foram utilizados dados pessoais para identificar diretamente os usuários.

# Cyclistic — Análise de Dados de Compartilhamento de Bicicletas (2025)

## Sobre o projeto

Este projeto analisa os dados históricos de viagens da Cyclistic, uma empresa fictícia de compartilhamento de bicicletas de Chicago, com o objetivo de identificar diferenças nos padrões de utilização entre usuários casuais e membros anuais.

O estudo busca responder à seguinte pergunta:

**Como os membros anuais e os usuários casuais utilizam as bicicletas da Cyclistic de maneiras diferentes?**

O projeto foi desenvolvido como um estudo de caso inspirado no Google Data Analytics Certificate, aplicando conceitos de preparação, validação, análise e visualização de dados.

## Objetivo de negócio

A equipe de marketing da Cyclistic deseja compreender as diferenças de comportamento entre usuários casuais e membros anuais para identificar oportunidades de conversão de usuários casuais em membros com assinaturas anuais.

A análise investiga padrões relacionados a:

- Frequência de utilização das bicicletas;
- Duração média das viagens;
- Distribuição das viagens ao longo dos dias da semana;
- Variações mensais de utilização;
- Preferência por tipos de bicicleta.

## Dados utilizados

Foram utilizados dados históricos públicos de viagens disponibilizados pela Motivate International Inc.

- **Período analisado:** janeiro a dezembro de 2025.
- **Quantidade de arquivos:** 12 arquivos CSV mensais.
- **Registros originais consolidados:** 5.552.994 viagens.
- **Registros após a preparação e limpeza:** 5.552.965 viagens.
- **Fonte:** [Divvy Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html).
- **Licença:** [Divvy Data License Agreement](https://divvybikes.com/data-license-agreement).

Os dados utilizados contêm informações sobre as viagens, como identificadores, datas e horários, tipos de bicicleta e categorias de usuários. Não foram utilizados dados pessoais para identificar diretamente os usuários.

## Ferramentas e tecnologias

- **Python:** utilizado na auditoria, limpeza, transformação e análise dos dados.
- **Pandas:** biblioteca utilizada para manipulação, organização e exploração dos conjuntos de dados.
- **Tableau:** utilizado para desenvolver visualizações e dashboards para apresentação dos resultados.
- **PyCharm:** ambiente de desenvolvimento utilizado para escrever, executar e organizar os scripts Python.
- **ChatGPT (OpenAI):** utilizado como ferramenta de apoio ao aprendizado e desenvolvimento do projeto, auxiliando na compreensão de conceitos, resolução de dúvidas, depuração de código, interpretação de resultados e organização da documentação. As sugestões foram avaliadas e aplicadas conforme a necessidade, mantendo a responsabilidade pela execução e validação das análises.

## Processo de análise

O projeto segue as seis etapas do processo de análise de dados:

1. **Ask:** definição do problema de negócio e da pergunta principal.
2. **Prepare:** obtenção e compreensão das fontes de dados.
3. **Process:** auditoria, validação, limpeza e transformação dos dados.
4. **Analyze:** exploração dos dados e identificação de padrões.
5. **Share:** comunicação dos resultados por meio de visualizações e dashboards.
6. **Act:** elaboração de recomendações baseadas nos resultados.

## Preparação e limpeza dos dados

O processo de preparação incluiu:

- Consolidação dos 12 arquivos mensais;
- Verificação da estrutura e consistência das colunas;
- Verificação de valores ausentes;
- Validação dos formatos de data e hora;
- Auditoria de identificadores duplicados;
- Cálculo da duração das viagens;
- Identificação de durações negativas e viagens de longa duração;
- Criação de variáveis temporais para análise.

Durante a validação, foram identificadas 29 viagens com duração negativa, associadas à transição do horário de verão em Chicago, em novembro de 2025. Essas ocorrências foram tratadas durante a preparação dos dados, resultando em uma base com 5.552.965 registros.

Também foram identificadas viagens com duração superior a 12 e 24 horas, que foram avaliadas durante o processo de validação.

## Análises e visualizações

Foram desenvolvidas cinco análises no Tableau, organizadas em dois dashboards:

1. **Frequência semanal:** comparação do volume de viagens entre membros e usuários casuais ao longo dos dias da semana.
2. **Duração média semanal:** comparação do tempo médio das viagens por dia da semana.
3. **Utilização por tipo de bicicleta:** comparação da utilização de bicicletas clássicas e elétricas.
4. **Frequência mensal:** análise da variação do volume de viagens ao longo de 2025.
5. **Duração média mensal:** comparação da duração média das viagens entre os grupos ao longo dos meses.

## Principais descobertas

- **Volume de viagens:** os membros anuais realizaram aproximadamente 3,55 milhões de viagens, enquanto os usuários casuais realizaram aproximadamente 2 milhões.
- **Frequência semanal:** os membros apresentaram maior volume de viagens durante os dias úteis, com destaque para quinta-feira. Os usuários casuais registraram seu maior volume aos sábados.
- **Duração das viagens:** os usuários casuais apresentaram viagens de maior duração média em todos os dias da semana e em todos os meses analisados.
- **Tipo de bicicleta:** ambos os grupos utilizaram mais bicicletas elétricas. Elas representaram 66,36% das viagens casuais e 64,11% das viagens dos membros.
- **Variação mensal:** agosto registrou o maior volume de viagens, com 790.317 registros somando os dois grupos.
- **Participação dos casuais:** junho apresentou a maior participação de usuários casuais no volume mensal de viagens, com 43,02%.
- **Duração mensal:** junho registrou a maior duração média das viagens casuais, aproximadamente 25 minutos e 23 segundos.

## Conclusão

A análise demonstrou diferenças nos padrões de utilização entre membros anuais e usuários casuais. Os membros realizaram um volume maior de viagens ao longo do ano, enquanto os usuários casuais apresentaram viagens de maior duração média, especialmente aos finais de semana.

Os resultados indicam que a frequência e a duração das viagens são características importantes para diferenciar os dois grupos. Essas informações podem apoiar o desenvolvimento de campanhas direcionadas aos usuários casuais, considerando os períodos de maior utilização e os padrões observados.

## Recomendações de negócio

Com base nos resultados, recomenda-se:

1. **Campanhas aos finais de semana:** direcionar ações de marketing aos períodos em que os usuários casuais apresentam maior volume de viagens.
2. **Ações nos meses de maior utilização:** intensificar campanhas antes e durante o período de maior atividade, especialmente entre junho e agosto.
3. **Comunicação sobre os planos anuais:** destacar os possíveis benefícios da associação anual para usuários que realizam viagens mais longas e frequentes.

As campanhas devem ser testadas e acompanhadas por indicadores de adesão e conversão, permitindo avaliar quais estratégias contribuem efetivamente para o aumento das assinaturas anuais.

## Estrutura do projeto

A estrutura de pastas e arquivos do projeto será apresentada de acordo com a organização utilizada no repositório.

## Limitações

- A análise considera exclusivamente os dados históricos disponibilizados para o período de janeiro a dezembro de 2025.
- Os padrões observados representam comportamentos registrados nas viagens, não necessariamente as motivações pessoais dos usuários.
- Os dados não permitem determinar diretamente por que um usuário casual decidiria contratar uma assinatura anual.
- As recomendações representam oportunidades identificadas a partir dos padrões observados e não garantem resultados de conversão.

## Referências

- **Google Data Analytics Certificate:** estudo de caso Cyclistic e materiais de referência.
- **Motivate International Inc.:** [Divvy Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html).
- **Licença dos dados:** [Divvy Data License Agreement](https://divvybikes.com/data-license-agreement).
*Projeto desenvolvido para fins educacionais e de portfólio.*