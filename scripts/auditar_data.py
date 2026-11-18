from pathlib import Path
import pandas as pd

# Localiza a pasta principal do projeto
pasta_projeto = Path(__file__).resolve().parent.parent

# Localiza a pasta que contém os arquivos CSV originais
pasta_dados = pasta_projeto / "data" / "raw"

# Encontra todos os arquivos CSV e organiza os nomes
arquivos_csv = sorted(pasta_dados.glob("*.csv"))

# Lista para armazenar os dados de cada mês
dados_mensais = []

# Percorre os 12 arquivos CSV
for arquivo in arquivos_csv:
    dados = pd.read_csv(arquivo)
    dados_mensais.append(dados)

# Une todos os arquivos em um único DataFrame
all_trips = pd.concat(dados_mensais, ignore_index=True)

# Confere a quantidade de arquivos encontrados
print(f"Arquivos CSV encontrados: {len(arquivos_csv)}")

# Confere a dimensão da base consolidada
print(f"Dimensões da base: {all_trips.shape}")

# Exibe as primeiras linhas
print(all_trips.head())

# Exibe informações sobre colunas e tipos de dados
print(all_trips.info())

# Exibe estatísticas descritivas das colunas numéricas
print(all_trips.describe())

# Remove colunas geográficas que não serão utilizadas
all_trips = all_trips.drop(columns=[
    "start_lat",
    "start_lng",
    "end_lat",
    "end_lng"
], errors="ignore")

# Verifica as colunas restantes
print(all_trips.columns.tolist())

# Verifica as dimensões atualizadas
print(all_trips.shape)

print(all_trips["member_casual"].value_counts())

all_trips["started_at"] = pd.to_datetime(all_trips["started_at"])
all_trips["ended_at"] = pd.to_datetime(all_trips["ended_at"])

print(all_trips[["started_at", "ended_at"]].dtypes)

# Extrai informações da data de início da viagem
all_trips["date"] = all_trips["started_at"].dt.date

all_trips["month"] = all_trips["started_at"].dt.month

all_trips["day"] = all_trips["started_at"].dt.day

all_trips["year"] = all_trips["started_at"].dt.year

all_trips["day_of_week"] = all_trips["started_at"].dt.day_name()

# Exibe as novas colunas criadas
print(all_trips[
    ["started_at", "date", "month", "day", "year", "day_of_week"]
].head())

# Calcula a duração de cada viagem em segundos
all_trips["ride_length"] = (
    all_trips["ended_at"] - all_trips["started_at"]
).dt.total_seconds()

# Exibe início, término e duração das primeiras viagens
print(all_trips[
    ["started_at", "ended_at", "ride_length"]
].head())

#LIMPEZA DE DADOS
all_trips_v2 = all_trips[
    (all_trips["start_station_name"] != "HQ QR") &
    (all_trips["ride_length"] >= 0)
].copy()

# Compara a quantidade de registros antes e depois da limpeza
print("Antes da limpeza:", len(all_trips))
print("Depois da limpeza:", len(all_trips_v2))
print("Registros removidos:", len(all_trips) - len(all_trips_v2))

# Estatísticas descritivas da duração das viagens
print(all_trips_v2["ride_length"].describe())

# Calcula as estatísticas descritivas da duração
estatisticas = all_trips_v2["ride_length"].describe()

# Converte segundos para horas, minutos e segundos
estatisticas_formatadas = estatisticas.copy()

estatisticas_formatadas = estatisticas_formatadas.map(
    lambda segundos: (
        f"{int(segundos // 3600):02d}:"
        f"{int((segundos % 3600) // 60):02d}:"
        f"{int(segundos % 60):02d}"
    )
)

# Exibe a análise descritiva em formato de hora
print(estatisticas_formatadas)

print(
    all_trips_v2.groupby("member_casual")["ride_length"].agg(
        ["mean", "median", "max", "min"]
    )
)

# Calcula a duração média das viagens por tipo de usuário e dia da semana
media_dia_semana = all_trips_v2.groupby(
    ["member_casual", "day_of_week"]
)["ride_length"].mean()

print(media_dia_semana)

# Calcula a duração média por tipo de usuário e dia da semana
media_dia_semana = all_trips_v2.groupby(
    ["member_casual", "day_of_week"]
)["ride_length"].mean()

# Converte os segundos para HH:MM:SS
media_dia_semana_formatada = media_dia_semana.map(
    lambda segundos: (
        f"{int(segundos // 3600):02d}:"
        f"{int((segundos % 3600) // 60):02d}:"
        f"{int(segundos % 60):02d}"
    )
)

# Exibe os resultados formatados
print(media_dia_semana_formatada)

# Calcula a duração média das viagens por tipo de usuário
media_usuario_segundos = all_trips_v2.groupby(
    "member_casual"
)["ride_length"].mean()

# Formata os resultados em horas, minutos e segundos
media_usuario_formatada = media_usuario_segundos.map(
    lambda segundos: (
        f"{int(round(segundos) // 3600):02d}:"
        f"{int((round(segundos) % 3600) // 60):02d}:"
        f"{int(round(segundos) % 60):02d}"
    )
)

# Exibe os resultados
print(media_usuario_formatada)

# Define a ordem correta dos dias da semana
ordem_dias = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# Calcula a quantidade de viagens por usuário e dia da semana
viagens_dia_semana = all_trips_v2.groupby(
    ["member_casual", "day_of_week"]
)["ride_id"].count()

# Organiza os dias da semana na ordem cronológica
viagens_dia_semana = viagens_dia_semana.reindex(
    pd.MultiIndex.from_product(
        [["casual", "member"], ordem_dias],
        names=["member_casual", "day_of_week"]
    )
)

# Exibe os resultados
print(viagens_dia_semana)

# Conta a quantidade de viagens por tipo de usuário e mês
viagens_mes = all_trips_v2.groupby(
    ["member_casual", "month"]
)["ride_id"].count()

print(viagens_mes)

# Calcula a duração média das viagens por tipo de usuário e mês
media_duracao_mes = all_trips_v2.groupby(
    ["member_casual", "month"]
)["ride_length"].mean()

# Formata os resultados em horas, minutos e segundos
media_duracao_mes_formatada = media_duracao_mes.map(
    lambda segundos: (
        f"{int(round(segundos) // 3600):02d}:"
        f"{int((round(segundos) % 3600) // 60):02d}:"
        f"{int(round(segundos) % 60):02d}"
    )
)

# Exibe os resultados
print(media_duracao_mes_formatada)

# Conta a quantidade de viagens por tipo de usuário e tipo de bicicleta
viagens_tipo_bicicleta = all_trips_v2.groupby(
    ["member_casual", "rideable_type"]
)["ride_id"].count()

# Exibe os resultados
print(viagens_tipo_bicicleta)

# Cria uma tabela-resumo por tipo de usuário e dia da semana
summary_stats = all_trips_v2.groupby(
    ["member_casual", "day_of_week"]
).agg(
    number_of_rides=("ride_id", "count"),
    average_duration=("ride_length", "mean")
).reset_index()

# Exibe a tabela-resumo
print("\nResumo de viagens e duração por tipo de usuário e dia da semana:\n")
print(summary_stats)

# Cria uma tabela com a duração média por tipo de usuário e dia da semana
counts = all_trips_v2.groupby(
    ["member_casual", "day_of_week"]
)["ride_length"].mean().reset_index()

# Exporta os resultados para um arquivo CSV
counts.to_csv("avg_ride_length.csv", index=False)

# Confirma a exportação
print("\nArquivo avg_ride_length.csv exportado com sucesso!")


# ============================================================
# CRIAÇÃO DO RESUMO CONSOLIDADO PARA O TABLEAU
# ============================================================


# 1. FREQUÊNCIA SEMANAL
# Conta a quantidade de viagens por usuário e dia da semana

frequencia_semanal = (
    all_trips_v2
    .groupby(["member_casual", "day_of_week"])
    .agg(
        ride_count=("ride_id", "count")
    )
    .reset_index()
)

frequencia_semanal["period_type"] = "weekly"
frequencia_semanal["period"] = frequencia_semanal["day_of_week"]
frequencia_semanal["metric"] = "ride_count"

frequencia_semanal["value"] = frequencia_semanal["ride_count"]
frequencia_semanal["average_duration_seconds"] = None
frequencia_semanal["average_duration_hhmm"] = None
frequencia_semanal["rideable_type"] = None


# 1.1 DURAÇÃO MÉDIA SEMANAL
# Calcula a duração média por usuário e dia da semana

duracao_semanal = (
    all_trips_v2
    .groupby(["member_casual", "day_of_week"])
    .agg(
        average_duration_seconds=("ride_length", "mean")
    )
    .reset_index()
)

duracao_semanal["period_type"] = "weekly"
duracao_semanal["period"] = duracao_semanal["day_of_week"]
duracao_semanal["metric"] = "average_duration"

# Mantém a duração numérica em segundos
duracao_semanal["value"] = duracao_semanal["average_duration_seconds"]

# Converte a duração para HH:MM
duracao_semanal["average_duration_hhmm"] = (
    duracao_semanal["average_duration_seconds"]
    .apply(
        lambda segundos: (
            f"{int(segundos // 3600):02d}:"
            f"{int((segundos % 3600) // 60):02d}"
        )
    )
)

duracao_semanal["ride_count"] = None
duracao_semanal["rideable_type"] = None



# 2. ANÁLISE MENSAL
# Calcula a quantidade de viagens e a duração média por usuário e mês

analise_mensal = (
    all_trips_v2
    .groupby(["member_casual", "month"])
    .agg(
        ride_count=("ride_id", "count"),
        average_duration_seconds=("ride_length", "mean")
    )
    .reset_index()
)

# Converte a duração média para HH:MM
analise_mensal["average_duration_hhmm"] = (
    pd.to_timedelta(
        analise_mensal["average_duration_seconds"],
        unit="s"
    )
    .apply(
        lambda duracao: (
            f"{int(duracao.total_seconds() // 3600):02d}:"
            f"{int((duracao.total_seconds() % 3600) // 60):02d}"
        )
    )
)

# Formata o mês com dois dígitos
analise_mensal["period"] = (
    analise_mensal["month"].astype(str).str.zfill(2)
)

analise_mensal["period_type"] = "monthly"
analise_mensal["metric"] = "ride_count"
analise_mensal["value"] = analise_mensal["ride_count"]
analise_mensal["rideable_type"] = None

# Cria uma segunda linha para cada mês, representando a duração média
duracao_mensal = analise_mensal.copy()

duracao_mensal["metric"] = "average_duration"
duracao_mensal["value"] = duracao_mensal["average_duration_seconds"]


# 3. TIPO DE BICICLETA
# Conta as viagens por usuário e categoria de bicicleta

tipo_bicicleta = (
    all_trips_v2
    .groupby(["member_casual", "rideable_type"])
    .agg(
        ride_count=("ride_id", "count")
    )
    .reset_index()
)

tipo_bicicleta["period_type"] = "bicycle"
tipo_bicicleta["period"] = None
tipo_bicicleta["metric"] = "ride_count"
tipo_bicicleta["value"] = tipo_bicicleta["ride_count"]
tipo_bicicleta["average_duration_seconds"] = None
tipo_bicicleta["average_duration_hhmm"] = None


# 4. CONSOLIDA AS TRÊS ANÁLISES EM UMA ÚNICA TABELA


# 4. CONSOLIDA TODAS AS ANÁLISES EM UMA ÚNICA TABELA

colunas_resumo = [
    "member_casual",
    "period_type",
    "period",
    "metric",
    "value",
    "average_duration_seconds",
    "average_duration_hhmm",
    "rideable_type"
]

summary_tableau = pd.concat(
    [
        frequencia_semanal[colunas_resumo],
        duracao_semanal[colunas_resumo],
        analise_mensal[colunas_resumo],
        duracao_mensal[colunas_resumo],
        tipo_bicicleta[colunas_resumo]
    ],
    ignore_index=True
)


# 5. EXPORTA O ARQUIVO CSV

caminho_exportacao = pasta_projeto / "cyclistic_summary_tableau.csv"

summary_tableau.to_csv(
    caminho_exportacao,
    index=False
)

print("\nResumo consolidado exportado com sucesso!")
print(f"Arquivo: {caminho_exportacao}")
print(f"Dimensões: {summary_tableau.shape}")
print("\nPrévia do resumo:")
print(summary_tableau.head(10))

# 6. EXPORTA UMA CÓPIA DO RESUMO EM EXCEL

caminho_excel = pasta_projeto / "cyclistic_summary_tableau.xlsx"

summary_tableau.to_excel(
    caminho_excel,
    index=False
)

print("\nResumo em Excel exportado com sucesso!")
print(f"Arquivo: {caminho_excel}")
print(f"Dimensões: {summary_tableau.shape}")

