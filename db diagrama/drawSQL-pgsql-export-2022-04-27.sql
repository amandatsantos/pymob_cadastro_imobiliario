CREATE TABLE "IMOVEL"(
    "id" INTEGER NOT NULL,
    "TITULO IMOVEL" CHAR(255) NOT NULL,
    "logradouro" CHAR(255) NOT NULL,
    "bairro" CHAR(255) NOT NULL,
    "cidade" CHAR(255) NOT NULL,
    "estado" CHAR(255) NOT NULL,
    "descricao" VARCHAR(255) NOT NULL,
    "idCategoria" CHAR(255) NOT NULL,
    "valor aluguel" DOUBLE PRECISION NOT NULL,
    "idProprietario" INTEGER NOT NULL
);
ALTER TABLE
    "IMOVEL" ADD PRIMARY KEY("id");
CREATE TABLE "PROPRIETARIO"(
    "id" INTEGER NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "cpf" VARCHAR(255) NOT NULL,
    "telefone" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "PROPRIETARIO" ADD PRIMARY KEY("id");
ALTER TABLE
    "PROPRIETARIO" ADD CONSTRAINT "proprietario_cpf_unique" UNIQUE("cpf");
ALTER TABLE
    "PROPRIETARIO" ADD CONSTRAINT "proprietario_telefone_unique" UNIQUE("telefone");
ALTER TABLE
    "PROPRIETARIO" ADD CONSTRAINT "proprietario_email_unique" UNIQUE("email");
CREATE TABLE "INQUILINO"(
    "id" INTEGER NOT NULL,
    "nome" INTEGER NOT NULL,
    "cpf" INTEGER NOT NULL,
    "telefone" INTEGER NOT NULL,
    "email" INTEGER NOT NULL
);
ALTER TABLE
    "INQUILINO" ADD PRIMARY KEY("id");
ALTER TABLE
    "INQUILINO" ADD CONSTRAINT "inquilino_cpf_unique" UNIQUE("cpf");
ALTER TABLE
    "INQUILINO" ADD CONSTRAINT "inquilino_telefone_unique" UNIQUE("telefone");
ALTER TABLE
    "INQUILINO" ADD CONSTRAINT "inquilino_email_unique" UNIQUE("email");
CREATE TABLE "CORRETOR"(
    "id" INTEGER NOT NULL,
    "nome" INTEGER NOT NULL,
    "cpf" INTEGER NOT NULL,
    "telefone" INTEGER NOT NULL,
    "email" INTEGER NOT NULL,
    "creci" INTEGER NOT NULL
);
ALTER TABLE
    "CORRETOR" ADD PRIMARY KEY("id");
ALTER TABLE
    "CORRETOR" ADD CONSTRAINT "corretor_cpf_unique" UNIQUE("cpf");
ALTER TABLE
    "CORRETOR" ADD CONSTRAINT "corretor_telefone_unique" UNIQUE("telefone");
ALTER TABLE
    "CORRETOR" ADD CONSTRAINT "corretor_email_unique" UNIQUE("email");
ALTER TABLE
    "CORRETOR" ADD CONSTRAINT "corretor_creci_unique" UNIQUE("creci");
CREATE TABLE "ALUGUEL"(
    "id" INTEGER NOT NULL,
    "id imovel" INTEGER NOT NULL,
    "id proprietário" INTEGER NOT NULL,
    "id inquilino" INTEGER NOT NULL,
    "id corretor" INTEGER NOT NULL,
    "valor aluguel" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "ALUGUEL" ADD PRIMARY KEY("id");
CREATE INDEX "aluguel_id imovel_index" ON
    "ALUGUEL"("id imovel");
CREATE INDEX "aluguel_id proprietário_index" ON
    "ALUGUEL"("id proprietário");
CREATE INDEX "aluguel_id inquilino_index" ON
    "ALUGUEL"("id inquilino");
CREATE INDEX "aluguel_id corretor_index" ON
    "ALUGUEL"("id corretor");
CREATE TABLE "CONTRATO"(
    "id" INTEGER NOT NULL,
    "meses contratados" CHAR(255) NOT NULL,
    "data de inicio" DATE NOT NULL,
    "data de encerramento" DATE NOT NULL,
    "id aluguel" INTEGER NOT NULL
);
ALTER TABLE
    "CONTRATO" ADD PRIMARY KEY("id");
CREATE INDEX "contrato_id aluguel_index" ON
    "CONTRATO"("id aluguel");
CREATE TABLE "CATEGORIA"(
    "id" INTEGER NOT NULL,
    "nomeCategoria" INTEGER NOT NULL
);
ALTER TABLE
    "CATEGORIA" ADD PRIMARY KEY("id");
ALTER TABLE
    "ALUGUEL" ADD CONSTRAINT "aluguel_id imovel_foreign" FOREIGN KEY("id imovel") REFERENCES "IMOVEL"("id");
ALTER TABLE
    "ALUGUEL" ADD CONSTRAINT "aluguel_id inquilino_foreign" FOREIGN KEY("id inquilino") REFERENCES "INQUILINO"("id");
ALTER TABLE
    "ALUGUEL" ADD CONSTRAINT "aluguel_id proprietário_foreign" FOREIGN KEY("id proprietário") REFERENCES "PROPRIETARIO"("id");
ALTER TABLE
    "IMOVEL" ADD CONSTRAINT "imovel_idproprietario_foreign" FOREIGN KEY("idProprietario") REFERENCES "PROPRIETARIO"("id");
ALTER TABLE
    "ALUGUEL" ADD CONSTRAINT "aluguel_id corretor_foreign" FOREIGN KEY("id corretor") REFERENCES "CORRETOR"("id");
ALTER TABLE
    "CONTRATO" ADD CONSTRAINT "contrato_id aluguel_foreign" FOREIGN KEY("id aluguel") REFERENCES "ALUGUEL"("id");
ALTER TABLE
    "IMOVEL" ADD CONSTRAINT "imovel_idcategoria_foreign" FOREIGN KEY("idCategoria") REFERENCES "CATEGORIA"("id");