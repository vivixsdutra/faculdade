const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://demoqa.com', // baseUrl para acessar o site real
    setupNodeEvents(on, config) {
      // Você pode configurar eventos aqui se necessário
    },
    supportFile: 'cypress/support/e2e.js', // caminho correto do arquivo de suporte
    specPattern: 'cypress/e2e/**/*.cy.js' // onde estão os testes
  }
});