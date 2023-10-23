import org.apache.spark.sql.SparkSession

val spark: SparkSession = SparkSession.builder().appName("Contagem de Palavras").getOrCreate()

val arquivoConteudo: String = scala.io.Source.fromFile("README.md").getLines.mkString
val conteudo = arquivoConteudo.replaceAll("[#*_/:->;\\[\\],()\"\\-`]", " ").toLowerCase
val palavras = conteudo.split("\\s+")

import spark.implicits._
val palavrasDF = palavras.toSeq.toDF("palavras")

palavrasDF.createOrReplaceTempView("palavras")

val consultaSQL =
  """
    SELECT palavras, COUNT(palavras) AS frequencia
    FROM palavras
    GROUP BY palavras
    ORDER BY frequencia DESC
  """

val resultado = spark.sql(consultaSQL)
resultado.show()