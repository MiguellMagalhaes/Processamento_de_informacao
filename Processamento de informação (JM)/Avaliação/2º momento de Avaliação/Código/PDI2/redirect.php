<?php
$questionNumber = isset($_GET['question']) ? $_GET['question'] : 1;

// Aqui você pode adicionar lógica específica para cada pergunta se necessário

// Exemplo de redirecionamento genérico
header("Location: http://seusite.com/resposta.php?question=$questionNumber");
exit();
?>
