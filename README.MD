1. docker-compose.yml
Este arquivo configura um cluster Spark com um nó master e quatro nós workers, todos utilizando a imagem Bitnami do Spark. Ele também monta um diretório local para que você possa facilmente compartilhar seus jobs Spark entre o host e os contêineres. As portas são mapeadas para permitir acesso à UI do Spark e comunicação entre o master e os workers.

2. main.py
Esse script inicializa uma sessão do Spark configurada para trabalhar com dados não estruturados armazenados no S3 da AWS, utilizando credenciais específicas para acesso seguro.

3. config.py