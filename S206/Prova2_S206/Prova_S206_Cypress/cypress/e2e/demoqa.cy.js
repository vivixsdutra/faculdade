describe('Testes de Qualidade de Software - Prova S206', () => {
  it('Deve verificar o título da página', () => {
    cy.visit('/')
    cy.title().should('eq', 'DEMOQA') // Altere aqui se usar outro site
  })

  it('Deve navegar para a seção Elements e validar formulário', () => {
    cy.visit('/')
    cy.get('.card-body').contains('Elements').click()
    cy.url().should('include', '/elements')
    cy.get('.main-header').should('contain', 'Elements')
    // Função customizada para verificar seção
    validateElementsSection()
  })

  it('Deve falhar ao tentar preencher email inválido (CASO NEGATIVO)', () => {
    cy.visit('/text-box')
    fillForm({
      fullName: 'Teste Usuário',
      email: 'email-invalido',
      currentAddress: 'Endereço teste',
      permanentAddress: 'Endereço permanente teste'
    })
    // Validação negativa: espera borda vermelha no campo de e-mail
    cy.get('#userEmail').should('have.css', 'border-color', 'rgb(220, 53, 69)')
  })

  it('Deve navegar para a seção Forms e validar o header', () => {
    cy.visit('/')
    cy.get('.card-body').contains('Forms').click()
    cy.get('.main-header').should('contain', 'Forms')
  })
})

// Ignora erros de scripts de terceiros do DemoQA
Cypress.on('uncaught:exception', (err, runnable) => {
  return false;
});

// Função customizada (Requisito 3)
function validateElementsSection() {
  cy.get('.element-group').should('have.length.at.least', 6)
  cy.get('.btn-light').should('exist')
}

function fillForm({fullName, email, currentAddress, permanentAddress}) {
  cy.get('#userName').type(fullName)
  cy.get('#userEmail').type(email)
  cy.get('#currentAddress').type(currentAddress)
  cy.get('#permanentAddress').type(permanentAddress)
  cy.get('#submit').click()
}