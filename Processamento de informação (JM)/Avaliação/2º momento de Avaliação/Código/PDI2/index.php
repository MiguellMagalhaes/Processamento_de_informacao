<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> PDI</title>
    <link rel="stylesheet" href="styles.css">

    <style>

    body {
    font-family: Arial, sans-serif;
    background-color: #ccc;
    margin: 0;
}

.container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.question {
    margin-bottom: 20px;
}

.question a {
    display: block;
    padding: 10px;
    margin: 5px 0;
    text-decoration: none;
    background-color: #3498db;
    color: #fff;
    border-radius: 3px;
}

.question h2 {
    color: #333;
}

.footer {
    background-color: black; /* Laranja */
    color: #fff;
    text-align: center;
    padding: 20px;
    position: fixed;
    bottom: 0;
    width: 100%;
}
 </style>
</head>
<body>

    <div class="container">
        <div class="question">
            <h2>Estatísticas Básicas</h2>
            <a href="pergunta1.php">Qual é a média do número de docentes que estao associados ao ispgaya?</a>
            <br>
            <a href="pergunta2.php">Qual é a percentagem de docentes com especialidade e a percentagem de docentes sem especialidade, em relação ao total de docentes?</a>
        </div>
        <br>
        <div class="question">
            <h2>Distribuição de Graus</h2>
            <a href="pergunta3.php">Qual é a porcentagem de docentes para cada grau acadêmico na tabela?</a>
        </div>
        <br>
        <div class="question">
            <h2>Relacionamento entre Dados</h2>
            <a href="pergunta4.php">Qual é a proporção de docentes que possuem uma especialidade em relação ao total de docentes?</a>
        </div>
    </div>

    <div class="footer">
        <h3>Criadores do Projeto</h3>
        <p>Gonçalo Silva, Nº2020101055</p>
        <p>Gonçalo Pereira, Nº2020101880</p>
        <p>Miguel Magalhães, Nº2021103166</p>
        <a href="https://ispgaya.pt/pt" target="_blank">
        <img src="Logo_ispgaya.png" alt="ISPGAYA"style="width: 150px; height: auto;">
    </a>
    </div>

</body>
</html>
