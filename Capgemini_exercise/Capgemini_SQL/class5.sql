" ---como pesquisar dados"

SELECT ID, PRECO, DESCRICAO FROM  PRODUTOS

"---OU "

SELECT * FROM PRODUTOS "---(esse produtos é o nome da tabela criada) (e o * significa que ele vai trazer todas as colunas)"



" --- como pegar dados de duas tabelas diferentes:"

ELECT P.ID, P.DESCRICAO, P.PRECO, P.QTDESTOQUE, C.NOME
FROM produtos P INNER JOIN CATEGORIAS C
  ON C. ID = P. CATEGORIAID


SELECT P.ID, P.DESCRICAO, P.PRECO, P.QTDESTOQUE, C.NOME 'Categoria'   " --- (mudando o nome da coluna)"
FROM produtos P INNER JOIN CATEGORIAS C
  ON C. ID = P. CATEGORIAID

SELECT P.ID, P.DESCRICAO, P.PRECO, P.QTDESTOQUE, C.NOME 'Categoria' " ---(mudando o nome da coluna)"
FROM produtos P INNER JOIN CATEGORIAS C
  ON C. ID = P. CATEGORIAID

WHERE P.PRECO < 10   " ---(para colocar algum filtro)"

" ---ex: where p.preco < 10      OR ou AND   p.qtdestoque > 10"
