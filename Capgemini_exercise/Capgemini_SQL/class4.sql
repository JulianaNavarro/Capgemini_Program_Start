

CREATE TABLE ITENS_VENDAS
(
	IDPRODUTO INT NOT NULL, 
    IDVENDA INT NOT NULL,
    VALORPRODUTO FLOAT NOT NULL,
    DESCONTO FLOAT NOT NULL,
    FOREIGN KEY (IDPRODUTO) REFERENCES PRODUTOS(ID),
    FOREIGN KEY (IDVENDA) REFERENCES VENDAS(ID),
    
    
    PRIMARY KEY (IDPRODUTO, IDVENDA) 
    "--- chave primaria composta, vc declara o primary key embaixo apenas referenciando em quais variaveis"
)
