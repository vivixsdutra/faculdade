def pytest_html_report_title(report):
    report.title = "Relatório de testes — Gerenciador de Tarefas Acadêmicas"


def pytest_html_results_summary(prefix, summary, postfix, session):
    prefix.append(
        '<div class="report-brand">'
        '<div class="report-brand__row">'
        '<span class="report-badge">pytest · relatório HTML</span>'
        '<a class="report-brand__back" href="index.html">← Página do projeto</a>'
        "</div>"
        '<h2 class="report-summary-title">Resumo</h2>'
        "</div>"
    )
