-----------------------------------------------------------------------
--                         CRIAR AS SÉRIES Antigas
--             Sexta-Feira 13: Coleção VS A Hora do Pesadelo: Coleção

ifelse(
  (contains(titulooriginal, 'Friday')),
  'Sexta Feira 13',
  ''
)

ifelse(
  (contains(titulooriginal, 'Nightmare')), 
  'Hora do Pesadelo',
  null
)
-----------------------------------------------------------------------
--                    Criando o Conjunto das Séries

ifelse(
    {serie jason} = "Sexta Feira 13", "Sexta Feira 13",
    {serie pesadelo} = "Hora do Pesadelo", "Hora do Pesadelo",
    "Nao faz parte da analise"
)
-----------------------------------------------------------------------
--                          Criando valores acumulados
--                                  Receita

runningSum(
    sum({Receita Atualizada}),
    [anolancamento ASC],
    [Series]
)

--                                  Orçamento
runningSum(
    sum({Orcamento Atualizado}),
    [anolancamento ASC],
    [Series]
)

--                                   Lucro 
runningSum(
    sum({Lucro Atualizado}),
    [anolancamento ASC],
    [Series]
)
