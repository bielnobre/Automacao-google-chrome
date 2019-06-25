@given(u'que o google chrome esta aberto')
def step_impl(context):
    context.chrome.valida_abertura()


@when(u'navego ate o menu sobre')
def step_impl(context):
    context.chrome.navega_menu_sobre()


@then(u'devo receber informacoes sobre o chrome')
def step_impl(context):
    context.chrome.valida_tela_final()
    