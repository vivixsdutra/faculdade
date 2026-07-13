# 🍴 **Neides** 
> Um sistema robusto para controle de cardápio, estoque e pedidos, com foco em boas práticas de programação, escalabilidade e segurança.

---

## 🛠️ **Objetivo do Projeto**  
O **Neides** foi desenvolvido para facilitar a gestão de cantinas, oferecendo recursos como cadastro de itens, controle de estoque, aplicação de descontos e geração de relatórios de vendas. Ele promove organização e flexibilidade com base nos princípios **SOLID**, arquitetura **MVC** e padrões de design modernos.

---

## 📐 **Principais Funcionalidades**
- **Cadastro de Itens:** Adicione, atualize ou remova itens do cardápio.  
- **Controle de Estoque:** Gerencie a disponibilidade de produtos em tempo real.  
- **Relatórios de Vendas:** Geração de relatórios personalizados (ex.: diários, mensais).  
- **Aplicação de Descontos:** Calcule descontos com regras dinâmicas.  
- **Integração com Banco de Dados:** Estrutura robusta em MySQL para escalabilidade.  

---

📐 **Princípios SOLID Aplicados**

**SRP (Single Responsibility Principle)**

Cada classe tem uma responsabilidade única.
'ItemController' gerencia a lógica de controle, separada da manipulação de dados nos modelos.

**OCP (Open/Closed Principle)**

As classes estão abertas para extensão, mas fechadas para modificação.
A classe 'Venda' pode ser estendida para incluir novos tipos de relatórios.

**LSP (Liskov Substitution Principle)**

Subclasses podem ser usadas sem alterar o comportamento do sistema.
Estratégias de desconto podem ser trocadas sem impactar o cálculo total.

**ISP (Interface Segregation Principle)**

Interfaces específicas garantem que classes não implementem métodos desnecessários.
A interface 'DiscountStrategy' define apenas o método 'applyDiscount'.

**DIP (Dependency Inversion Principle)**

Depender de abstrações e não de implementações.
'ItemController' depende de abstrações como 'Item' e 'Venda'.

🧩 **Padrões de Design Implementados**

1. **Observer**  
- **Objetivo:** Notificar automaticamente as **Views** (interface do usuário) sobre mudanças no **Model** (dados).  
- **Aplicação:**  
  - Sempre que o estoque ou preço de um item muda, a interface é atualizada automaticamente.  
  - Atualização de cardápio em tempo real.  

2. **Singleton**  
- **Objetivo:** Garantir que apenas uma instância de certas classes (como conexão com o banco de dados) exista.  
- **Aplicação:**  
  - A classe de conexão com o banco (`DatabaseConnection`) é um Singleton.  
  - A mesma conexão é compartilhada entre controladores para otimizar recursos.  

3. **Strategy**  
- **Objetivo:** Permitir diferentes comportamentos para o cálculo de descontos dinamicamente.  
- **Aplicação:**  
  - Implementação de estratégias como `DescontoFixo` e `DescontoPercentual`.  
  - Aplicar descontos diferentes para estudantes ou clientes regulares.
---

📂 **Principais Componentes**
- **Models:** Define a lógica e a persistência dos dados, como itens do cardápio e informações de estoque.  
- **Views:** Gerencia a interface do usuário (HTML, CSS e templates Django).  
- **Controllers:** Lógica de aplicação, validação e manipulação de dados.  
- **Utils:** Funções utilitárias, como aplicação de descontos e notificações.

---

🛠️ **Tecnologias Utilizadas**
- **Linguagem:** Python 🐍  
- **Framework Web:** Django 🌐  
- **Banco de Dados:** MySQL 💾  
- **Frontend:** HTML + CSS 🎨  

---

## 🚀 **Como Rodar o Projeto**
### Pré-requisitos:
- Python 3.9+  
- MySQL  
- Django 4+  

### Passos:
1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/neides_project.git
   cd neides_project
   ```

2. Crie o ambiente virtual:  
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados no arquivo `settings.py`.  

5. Execute as migrações e rode o servidor:  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

---
## 🛡️ **Segurança e Tratamento de Erros**
1. **Camada de Tratamento de Erros:**  
   - Classe que gerencia erros comuns, como falhas de conexão e validações.  

2. **Controle de Acesso:**  
   - Implementação de autenticação e autorização para proteger operações críticas.  

3. **Validações:**  
   - Uso do padrão **Strategy** para alternar entre diferentes validações de entrada.  
---

👩‍💻 Desenvolvido por Vitória Dutra e Lucca Marcondes. ✨
