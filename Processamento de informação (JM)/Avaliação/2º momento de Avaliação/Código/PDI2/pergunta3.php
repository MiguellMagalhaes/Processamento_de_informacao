<?php

    require "includes/settings.php";
    include "includes/db.php";
    db_connect();

    $query = "SELECT TRIM(f.formacao) as formacao, ROUND((COUNT(h.id_formacao) / (SELECT COUNT(id_docente) FROM habilitacoes))*100,2) AS media FROM `habilitacoes` h INNER JOIN formacao f ON h.id_formacao = f.id GROUP BY h.id_formacao;";

    $arr = db_query($query);

    function generateRandomColor() {
        // Gerar uma cor hexadecimal aleatória
        return '#' . str_pad(dechex(mt_rand(0, 0xFFFFFF)), 6, '0', STR_PAD_LEFT);
    }

    $labels = [];
    $data = [];
    $backgroundColor = [];

    foreach ($arr as $item) {
        $labels[] = $item['formacao'];
        $data[] = $item['media'];
        $backgroundColor[] = generateRandomColor();
    }

?>

<!DOCTYPE html>
<html lang="en" data-bs-theme="white">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Pergunta 3 </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.11.3/font/bootstrap-icons.min.css" integrity="sha512-dPXYcDub/aeb08c63jRq/k6GaKccl256JQy/AnOq7CAnEZ9FzSL9wSbcZkMp4R26vBsMLFYH4kQ67/bbV8XaCQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        .back-button {
            background-color: #3498db; /* Cor igual a dos botões de perguntas */
            color: #fff;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 3px;
            position: absolute;
            top: 10px;
            left: 10px;
        }
    </style>
</head>
<body class="d-flex flex-column min-vh-100">

    <div class="container mb-4" id="graphs">
        <div class="row justify-content-center">
            <div class="col-md-8 mb-4">
                <canvas id="grafico" style="width:100%"></canvas>
            </div>
        </div>
        <a href="index.php" class="back-button">Voltar</a>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script>
        
        // Obtenha o contexto do canvas
        var ctx = document.getElementById('grafico').getContext('2d');

        // Crie um objeto de gráfico de rosquinha
        var doughnutChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: <?php echo json_encode($labels); ?>,
                datasets: [{
                    data: <?php echo json_encode($data); ?>,
                    backgroundColor: <?php echo json_encode($backgroundColor); ?>,
                }],
            },
        });

    </script>

</body>
</html>