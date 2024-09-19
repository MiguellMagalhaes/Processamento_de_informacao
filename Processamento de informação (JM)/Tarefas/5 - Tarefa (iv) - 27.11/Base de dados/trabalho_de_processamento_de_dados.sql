-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 20-Nov-2023 às 06:41
-- Versão do servidor: 10.4.28-MariaDB
-- versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `trabalho de processamento de dados`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `carreira_ano`
--

CREATE TABLE `carreira_ano` (
  `id_carreira` int(11) NOT NULL,
  `ano` int(11) DEFAULT NULL,
  `id_docente` int(11) DEFAULT NULL,
  `id_uo` int(11) DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `id_rps` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `categoria`
--

CREATE TABLE `categoria` (
  `Id_categoria` int(11) NOT NULL,
  `codigo` int(11) DEFAULT NULL,
  `Nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `curso`
--

CREATE TABLE `curso` (
  `Id_curso` int(11) NOT NULL,
  `codigo` int(11) DEFAULT NULL,
  `Nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `docente`
--

CREATE TABLE `docente` (
  `Id_docente` int(11) NOT NULL,
  `num_docente_ano` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `ensino`
--

CREATE TABLE `ensino` (
  `Id_ensino` int(11) NOT NULL,
  `codigo` int(11) DEFAULT NULL,
  `Nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `especialidade`
--

CREATE TABLE `especialidade` (
  `Id_especialidade` int(11) NOT NULL,
  `Codigo` int(11) DEFAULT NULL,
  `nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `estabelecimento`
--

CREATE TABLE `estabelecimento` (
  `Id_estabelecimento` int(11) NOT NULL,
  `codigo` int(11) DEFAULT NULL,
  `Nome` varchar(255) DEFAULT NULL,
  `País` varchar(255) DEFAULT NULL,
  `Tipo_faculdade` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `formacao`
--

CREATE TABLE `formacao` (
  `Id_formacao` int(11) NOT NULL,
  `Codigo` int(11) DEFAULT NULL,
  `nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `habilitacoes_ano`
--

CREATE TABLE `habilitacoes_ano` (
  `id` int(11) NOT NULL,
  `Ano` int(11) DEFAULT NULL,
  `id_docente` int(11) DEFAULT NULL,
  `id_ug` int(11) DEFAULT NULL,
  `id_formacao` int(11) DEFAULT NULL,
  `id_curso` int(11) DEFAULT NULL,
  `id_especialidade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `regime_prestacao_servico`
--

CREATE TABLE `regime_prestacao_servico` (
  `Id_regime` int(11) NOT NULL,
  `codigo` int(11) DEFAULT NULL,
  `Nome` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `unidade_organica`
--

CREATE TABLE `unidade_organica` (
  `Id_uo` int(11) NOT NULL,
  `Codigo` int(11) DEFAULT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `id_ensino` int(11) DEFAULT NULL,
  `id_estabelecimento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `carreira_ano`
--
ALTER TABLE `carreira_ano`
  ADD PRIMARY KEY (`id_carreira`),
  ADD KEY `id_docente` (`id_docente`),
  ADD KEY `id_uo` (`id_uo`),
  ADD KEY `id_categoria` (`id_categoria`),
  ADD KEY `id_rps` (`id_rps`);

--
-- Índices para tabela `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`Id_categoria`);

--
-- Índices para tabela `curso`
--
ALTER TABLE `curso`
  ADD PRIMARY KEY (`Id_curso`);

--
-- Índices para tabela `docente`
--
ALTER TABLE `docente`
  ADD PRIMARY KEY (`Id_docente`);

--
-- Índices para tabela `ensino`
--
ALTER TABLE `ensino`
  ADD PRIMARY KEY (`Id_ensino`);

--
-- Índices para tabela `especialidade`
--
ALTER TABLE `especialidade`
  ADD PRIMARY KEY (`Id_especialidade`);

--
-- Índices para tabela `estabelecimento`
--
ALTER TABLE `estabelecimento`
  ADD PRIMARY KEY (`Id_estabelecimento`);

--
-- Índices para tabela `formacao`
--
ALTER TABLE `formacao`
  ADD PRIMARY KEY (`Id_formacao`);

--
-- Índices para tabela `habilitacoes_ano`
--
ALTER TABLE `habilitacoes_ano`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_docente` (`id_docente`),
  ADD KEY `id_ug` (`id_ug`),
  ADD KEY `id_formacao` (`id_formacao`),
  ADD KEY `id_curso` (`id_curso`),
  ADD KEY `id_especialidade` (`id_especialidade`);

--
-- Índices para tabela `regime_prestacao_servico`
--
ALTER TABLE `regime_prestacao_servico`
  ADD PRIMARY KEY (`Id_regime`);

--
-- Índices para tabela `unidade_organica`
--
ALTER TABLE `unidade_organica`
  ADD PRIMARY KEY (`Id_uo`),
  ADD KEY `id_ensino` (`id_ensino`),
  ADD KEY `id_estabelecimento` (`id_estabelecimento`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `carreira_ano`
--
ALTER TABLE `carreira_ano`
  ADD CONSTRAINT `carreira_ano_ibfk_1` FOREIGN KEY (`id_docente`) REFERENCES `docente` (`Id_docente`),
  ADD CONSTRAINT `carreira_ano_ibfk_2` FOREIGN KEY (`id_uo`) REFERENCES `unidade_organica` (`Id_uo`),
  ADD CONSTRAINT `carreira_ano_ibfk_3` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`Id_categoria`),
  ADD CONSTRAINT `carreira_ano_ibfk_4` FOREIGN KEY (`id_rps`) REFERENCES `regime_prestacao_servico` (`Id_regime`);

--
-- Limitadores para a tabela `habilitacoes_ano`
--
ALTER TABLE `habilitacoes_ano`
  ADD CONSTRAINT `habilitacoes_ano_ibfk_1` FOREIGN KEY (`id_docente`) REFERENCES `docente` (`Id_docente`),
  ADD CONSTRAINT `habilitacoes_ano_ibfk_2` FOREIGN KEY (`id_ug`) REFERENCES `unidade_organica` (`Id_uo`),
  ADD CONSTRAINT `habilitacoes_ano_ibfk_3` FOREIGN KEY (`id_formacao`) REFERENCES `formacao` (`Id_formacao`),
  ADD CONSTRAINT `habilitacoes_ano_ibfk_4` FOREIGN KEY (`id_curso`) REFERENCES `curso` (`Id_curso`),
  ADD CONSTRAINT `habilitacoes_ano_ibfk_5` FOREIGN KEY (`id_especialidade`) REFERENCES `especialidade` (`Id_especialidade`);

--
-- Limitadores para a tabela `unidade_organica`
--
ALTER TABLE `unidade_organica`
  ADD CONSTRAINT `unidade_organica_ibfk_1` FOREIGN KEY (`id_ensino`) REFERENCES `ensino` (`Id_ensino`),
  ADD CONSTRAINT `unidade_organica_ibfk_2` FOREIGN KEY (`id_estabelecimento`) REFERENCES `estabelecimento` (`Id_estabelecimento`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
