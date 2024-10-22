Resumo (Problema, Objetivos, Dificuldades):

O presente projeto visa resolver um dos desafios mais comuns no contexto da gestão de dados heterogéneos: a integração de ficheiros Excel com variações estruturais significativas ao longo do tempo num Sistema de Gestão de Bases de Dados (SGBD). Esta tarefa é especialmente crítica para organizações e académicos que lidam com volumes elevados de dados provenientes de fontes diferentes e não padronizadas, que precisam ser processados e armazenados de forma eficaz e eficiente.

Problema:

A dificuldade central reside na diversidade de estruturas e formatos dos ficheiros MS Excel, que frequentemente sofrem alterações nos campos, nas folhas e nos tipos de dados. Estas variações criam obstáculos substanciais para a normalização dos dados e para a sua integração consistente num SGBD. Um exemplo comum é a alteração de nomes de campos ao longo do tempo ou a introdução de novos campos e folhas de cálculo, o que complica o mapeamento direto para as tabelas de uma base de dados relacional. Estas questões dificultam a automatização da extração e transferência de dados, exigindo soluções adaptativas e robustas.
Além das variações estruturais, é necessário considerar os problemas inerentes à normalização dos dados. Normalizar dados de diferentes fontes, em especial quando os ficheiros apresentam inconsistências ou formatos distintos, é um processo trabalhoso e propenso a erros. O objetivo é garantir que a base de dados final contenha dados limpos, padronizados e confiáveis, que possam ser utilizados de maneira eficiente em sistemas de informação.

Objetivos:

Este projeto tem como principais objetivos:
-> Desenvolver um modelo automatizado de extração e processamento de dados: O modelo deverá ser capaz de ler automaticamente ficheiros MS Excel com diferentes estruturas e adaptar-se às variações, sem a necessidade de reconfigurações manuais constantes. Isto inclui a adaptação a alterações em folhas de cálculo, campos e formatos de dados.

-> Normalizar os dados: Garantir que os dados extraídos sejam normalizados para facilitar a sua inserção numa base de dados relacional. Isto implica resolver problemas como campos duplicados, nomes inconsistentes ou dados ausentes, garantindo a integridade e coerência dos dados ao serem inseridos no SGBD.

-> Transferir os dados para um SGBD: Implementar um sistema que não só extraia e normalize os dados, mas que também automatize a transferência para uma base de dados relacional, mantendo a integridade dos dados durante o processo.

-> Implementar testes de integridade: Para garantir que os dados mantêm a sua fiabilidade e consistência no SGBD, o projeto incluirá a implementação de testes de integridade. Esses testes serão fundamentais para assegurar que os dados transferidos não perdem a sua integridade e permanecem fidedignos após o processo de conversão.

-> Promover a colaboração em equipa: Este projeto é desenvolvido por uma equipa de 2 a 3 estudantes, sendo o trabalho colaborativo um dos pilares centrais. A integração de diferentes competências dos membros da equipa será essencial para o sucesso da abordagem multifacetada necessária para resolver os problemas técnicos complexos envolvidos.

Dificuldades:

O projeto enfrenta uma série de desafios, sendo os mais notáveis os seguintes:
-> Variação nas estruturas dos ficheiros Excel: Esta é a dificuldade mais imediata, uma vez que os ficheiros a serem processados poderão apresentar diferentes layouts de campos, folhas e formatos ao longo do tempo. A adaptação a estas mudanças requer um sistema flexível e dinâmico capaz de lidar com essas variações sem comprometer a integridade dos dados.

-> Normalização de dados: Uma vez extraídos os dados, a sua normalização é um processo complexo que pode ser dificultado por nomes de campos inconsistentes, dados duplicados ou mesmo falta de informações essenciais. O desenvolvimento de regras de normalização robustas será um dos maiores desafios técnicos do projeto.

-> Coordenação entre membros da equipa: Como este projeto será realizado por uma pequena equipa, a coordenação e a distribuição eficaz das tarefas serão cruciais. A integração das diferentes habilidades dos estudantes, como programação, análise de dados e design de bases de dados, será fundamental para assegurar a boa execução do projeto.

-> Implementação de testes de integridade: Para garantir que a transferência de dados do Excel para o SGBD ocorra de maneira precisa e confiável, será necessário desenvolver e executar uma série de testes de integridade. Estes testes têm a finalidade de assegurar que os dados estão corretamente organizados e que a sua migração não introduz erros.


Conclusão:

O sucesso deste projeto terá um impacto significativo não só na resolução de desafios técnicos específicos relacionados à gestão de dados heterogéneos, mas também na melhoria das práticas de gestão de dados em ambientes académicos e profissionais. Ao concluir este trabalho, os estudantes envolvidos ganharão experiência prática em áreas-chave, como processamento de dados, normalização e gestão de bases de dados, habilidades essenciais no campo da engenharia informática e na gestão moderna de informações.
A conclusão bem-sucedida deste projeto contribuirá para estratégias mais eficazes de gestão de dados heterogéneos e servirá como base para trabalhos futuros que lidem com a integração de dados complexos e não padronizados.
