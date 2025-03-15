# FastAPI-INSS

[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![GitHub issues](https://img.shields.io/github/issues/Kenjibercysec/FastAPI-INSS)](https://github.com/Kenjibercysec/FastAPI-INSS/issues) [![GitHub forks](https://img.shields.io/github/forks/Kenjibercysec/FastAPI-INSS)](https://github.com/Kenjibercysec/FastAPI-INSS/network) [![GitHub stars](https://img.shields.io/github/stars/Kenjibercysec/FastAPI-INSS)](https://github.com/Kenjibercysec/FastAPI-INSS/stargazers)

![Logo do INSS](inss-logo.png)

O **FastAPI-INSS** é um sistema full-stack para gerenciamento de dispositivos integrado ao INSS. Com uma API desenvolvida em FastAPI e uma interface web responsiva construída com HTML, CSS e JavaScript, o projeto visa facilitar a administração e monitoramento de dispositivos, oferecendo uma experiência prática e eficiente.

---

## Sumário

- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
- [Contribuições](#contribuições)
- [Licença](#licença)

---

## Funcionalidades

- **Gerenciamento de Dispositivos:** Cadastro, consulta e administração dos dispositivos.
- **Interface Web Interativa:** Páginas dinâmicas para cadastro e visualização (ex.: `index.html`, `cadother.html`, `cadpc.html`, `selecao.html`).
- **API com FastAPI:** Endpoints para integração e comunicação entre front-end e back-end.
- **Banco de Dados Integrado:** Utiliza MySQL (ou outro SGBD compatível) com scripts e modelo lógico para a criação de tabelas.

---

## Tecnologias Utilizadas

- **Back-end:** FastAPI, Python
- **Front-end:** HTML5, CSS3, JavaScript
- **Banco de Dados:** MySQL (script SQL disponível)
- **Driver de Conexão:** PyMySQL

---

## Estrutura do Projeto

```plaintext
FastAPI-INSS/
├── backend/                              # Código do back-end (API com FastAPI)
├── BANCO DE DADOS DOS DISPOSITIVOS .sql    # Script SQL para criação do banco de dados
├── MODELO LOGICO BD INSS.txt              # Modelo lógico do banco de dados
├── cadother.html                         # Página de cadastro de outros dispositivos
├── cadpc.html                            # Página de cadastro de PCs
├── index.html                            # Página principal
├── selecao.html                          # Página de seleção de opções
├── inss.js                               # Script JavaScript para funcionalidades específicas
├── script.js                             # Outros scripts JavaScript
├── style.css                             # Estilos CSS para a interface
└── requirements.txt                      # Dependências Python (ex.: PyMySQL)
```

## Pré-requisitos

- **Python 3.7+**
- **MySQL** ou outro SGBD compatível
- **Dependências Python:** Listadas em [`requirements.txt`](requirements.txt)

> **Dica:** Se o projeto utilizar outras dependências (por exemplo, FastAPI e Uvicorn), certifique-se de incluí-las no `requirements.txt`.

---

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu_usuario/FastAPI-INSS.git
   cd FastAPI-INSS
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente no arquivo `.env`:
   ```
   DATABASE_URL=mysql+pymysql://seu_usuario:sua_senha@seu_host/nome_do_banco
   ```

## Execução

1. Inicie o servidor FastAPI:
   ```sh
   uvicorn backend.api:app --reload
   ```

2. Acesse a documentação da API em [http://localhost:8000/docs](http://localhost:8000/docs).

## Testes

1. Execute os testes:
   ```sh
   pytest backend/test_api.py
   ```

## Rotas da API

- `POST /items/`: Cria um novo dispositivo.
- `GET /items/`: Retorna uma lista de dispositivos.
- `GET /items/{item_id}`: Retorna um dispositivo pelo ID.
- `PUT /items/{item_id}`: Atualiza um dispositivo pelo ID.
- `GET /items/{item_id}/history`: Retorna o histórico de atualizações de um dispositivo.

## Uso
Executando o Back-end
No diretório backend, localize o arquivo principal (por exemplo, main.py ou app.py) e execute o servidor FastAPI:
```
uvicorn main:app --reload
```

Acessando a Interface Web
Após iniciar o servidor, abra o arquivo index.html ou acesse a URL indicada para interagir com a aplicação via navegador.

## Configuração do Banco de Dados (Complementar)

- **Script SQL:** Utilize o arquivo `BANCO DE DADOS DOS DISPOSITIVOS .sql` para criar as tabelas.
- **Modelo Lógico:** Consulte o arquivo `MODELO LOGICO BD INSS.txt` para entender a estrutura do banco.
- Certifique-se de que as credenciais e configurações do banco de dados no código estejam de acordo com o ambiente utilizado.

---

## Contribuições

Contribuições para aprimorar o **FastAPI-INSS** são sempre bem-vindas! Para colaborar:

1. **Fork** este repositório.
2. Crie uma **branch** para sua feature ou correção:

    ```bash
    git checkout -b minha-feature
    ```

3. Realize os **commits** com suas alterações:

    ```bash
    git commit -m "Descrição da alteração"
    ```

4. Envie sua branch para o repositório remoto:

    ```bash
    git push origin minha-feature
    ```

5. Abra um **Pull Request** detalhando suas mudanças.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Consulte o arquivo LICENSE para mais informações.

## Autores

<table>
  <tr>
     <td align="center">
      <a href="https://github.com/Kenjibercysec" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/105324711?v=4" width="100px;" alt=""/>
      </a>
      <br /><sub><b> Silas Kenji </b></sub>
    </td>
          <td align="center">
      <a href="https://github.com/Vitorhugofsousa" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/104640675?v=4" width="100px;" alt=""/>
      </a>
      <br /><sub><b> Vitor Hugo </b></sub>
    </td>
    <td align="center">
      <a href="https://github.com/boourlet" target="_blank">
        <img src="https://avatars.githubusercontent.com/u/130801222?v=4" width="100px;" alt=""/>
      </a>
      <br /><sub><b> Carla Letícia </b></sub>
    </td>
  </tr>
</table>
