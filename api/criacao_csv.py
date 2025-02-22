import pandas as pd

funcionarios, cargos, departamentos, historicoSalarial, dependentes, projetos, recursos = [], [], [], [], [], [], []

def addFuncionario(nomeFuncionario, idCargo, idDepartamento, salarioReal, dataNascimento):
    '''
    Esta função adiciona dados de um funcionario para a lista funcionarios.
    
    Args:
        nomeFuncionario(str): Refere-se ao nome do funcionário.
        idCargo(int): Refere-se ao identificador do cargo do funcionário.
        idDepartamento(int): Refere-se ao identificador do departamento do funcionário.
        salarioReal(float): Refere-se ao salario real do funcionário.
        dataNascimento(str): Refere-se à data de nascimento do funcionario.
    '''
    funcionarios.append({'idFuncionario':len(funcionarios)+1, 
                         'nomeFuncionario':nomeFuncionario, 
                         'idCargo': idCargo, 
                         'idDepartamento': idDepartamento, 
                         'salarioReal': salarioReal, 
                         'dataNascimento': dataNascimento})
    
    
def addCargo(nomeCargo, salarioBase, nivelCargo, escala):
    '''
    Esta função adiciona dados de um cargo para a lista cargos.
    
    Args:
        nomeCargo(str): Refere-se ao nome do cargo.
        salarioBase(float): Refere-se ao salário base do cargo.
        nivelCargo(str): Refere-se ao nível do cargo
        escala(str): Refere-se à escala do cargo.
    '''
    cargos.append({'idCargo':len(cargos)+1,
                   'nomeCargo':nomeCargo,
                   'salarioBase':salarioBase,
                   'nivelCargo':nivelCargo,
                   'escala':escala})
    
    
def addDepartamento(nomeDepartamento, idGerente, andarDepartamento, horarioFuncionamento):
    '''
    Esta função adiciona dados de um departamento para a lista `departamentos`.
    
    Args:
        nomeDepartamento(str): Refere-se ao nome do departamento.
        idGerente(int): Refere-se ao identificador do gerente do departamento.
        andarDepartamento(int): Refere-se ao andar do departamento.
        horarioFuncionamento(str): Refere-se ao horário de funcionamento do departamento.
    '''
    departamentos.append({'idDepartamento':len(departamentos)+1,
                          'nomeDepartamento':nomeDepartamento,
                          'idGerente':idGerente,
                          'andarDepartamento':andarDepartamento,
                          'horarioFuncionamento':horarioFuncionamento})
    
    
def addHistoricoSalarial(idFuncionario, data, salario):
    '''
    Esta função adiciona dados de um histórico de salário para a lista `historicoSalarial`.
    
    Args:
        idFuncionario(int): Refere-se ao identificador do funcionário.
        data(str): Refere-se à data que o salário foi pago.
        salario(float): Refere-se ao salário pago para o funcionário.
    '''
    historicoSalarial.append({'idSalarial':len(historicoSalarial)+1,
                              'idFuncionario':idFuncionario,
                              'data':data,
                              'salario':salario})
    
    
def addDependente(idFuncionario, parentesco, nome, idade, genero):
    '''
    Esta função adiciona dados de um dependente para a lista `dependentes`.
    
    Args:
        idFuncionario(int): Refere-se ao identificador do funcionário.
        parentesco(str): Refere-se ao parentesco.
        nome(str): Refere-se ao nome do dependente.
        idade(str): Refere-se à data de nascimento do dependente.
        genero(str): Refere-se ao genero do dependente.
    '''
    dependentes.append({'idDependente':len(dependentes)+1,
                        'idFuncionario':idFuncionario,
                        'parentesco':parentesco,
                        'nome':nome,
                        'idade':idade,
                        'genero':genero})
    
 
def addProjeto(idResponsavel, nomeProjeto, descricao, inicio, conclusao, custo, status):
    '''
    Esta função adiciona dados de um projeto para a lista `projetos`.
    
    Args:
        idResponsavel(int): Refere-se ao identificador do projeto.
        nomeProjeto(str): Refere-se ao nome do projeto.
        descricao(str): Refere-se à descrição do projeto.
        inicio(str): Refere-se à data de início do projeto.
        conclusao(str): Refere-se à data de conclusão do projeto.
        custo(float): Refere-se ao custo do projeto.
        status(str): Refere-se ao status atual do projeto.
    '''
    projetos.append({'idProjeto':len(projetos)+1,
                     'idResponsavel':idResponsavel,
                     'nomeProjeto':nomeProjeto,
                     'descricaoProjeto':descricao,
                     'inicio':inicio,
                     'conclusao':conclusao,
                     'custo':custo,
                     'status':status})   
    
    
def addRecurso(idProjeto, descricao, tipo, qtd, dataUtilizacao):
    '''
    Esta função adiciona dados de um recurso para a lista `recursos`.
    
    Args:
        idProjeto(int): Refere-se ao identificador do projeto que está relacionado.
        descricao(str): Refere-se ao à descricao sobre o recurso solicitado.
        tipo(str): Refere-se ao tipo do recurso.
        qtd(int): Refere-se à quantidade de recursos solicitados.
        dataUtilizacao(str): Refere-se à data de utilização do recurso.
    '''
    recursos.append({'idRecurso':len(recursos)+1,
                     'idProjeto':idProjeto,
                     'descricaoRecurso':descricao,
                     'tipoRecurso':tipo,
                     'qtdRecurso':qtd,
                     'dataUtilizacao':dataUtilizacao})
    
    
# addFuncionario(idFuncionario, nomeFuncionario, idCargo, idDepartamento, salarioReal, dataNascimento)
addFuncionario('André Xavier', 4, 1, 23000, '1994-03-17')
addFuncionario('Andressa Oliveira', 2, 1, 4200, '2005-06-23')
addFuncionario('Roberto Andrade', 1, 1, 11000, '2005-08-05')
addFuncionario('Laís Gomes', 12, 2, 6000, '2001-06-18')
addFuncionario('Paula Barbosa Queiroz', 12, 2, 9700, '1998-03-12')
addFuncionario('Mateus Schmidt', 12, 2, 9000, '2002-02-11')
addFuncionario('Lauro Alvares', 8, 3, 5300, '2000-01-27')
addFuncionario('Edgar Augusto', 9, 3, 12000, '2003-09-30')
addFuncionario('Amanda Rosa', 10, 4, 5800, '1998-03-12')
addFuncionario('Mario Silva Moreira', 11, 4, 9000, '1985-07-10')
addFuncionario('Gabriela Alencar', 5, 5, 3000, '2006-05-15')
addFuncionario('Alessandro Araújo', 6, 5, 8600, '1975-07-21')
addFuncionario('Mara Sousa', 8, 3, 5100, '1999-06-22')
addFuncionario('Alan Silva', 12, 4, 5600, '2004-02-18')
addFuncionario('Daniel Carmo Almeida', 3, 1, 20000, '1973-03-15')
addFuncionario('Jéssica Borges', 7, 1, 20000, '1993-11-13')
addFuncionario('Antônio Ferraz', 5, 5, 3300, '1999-07-25')
addFuncionario('Priscila Barreto', 5, 5, 3400, '2002-03-11')
addFuncionario('Paloma Lopez', 5, 5, 3300, '2002-11-15')
addFuncionario('Eduardo Lima', 5, 2, 4800, '2001-10-06')
addFuncionario('Josué Ribeiro', 6, 2, 5000, '1989-12-29')

# addCargo(idCargo, nomeCargo, salarioBase, nivelCargo, escala)
addCargo('Desenvolvedor Back-end', 9000, 'Analista', '5x2')
addCargo('Desenvolvedor Front-end', 4000, 'Estagiário', '5x2')
addCargo('Desenvolvedor Fullstack', 18000, 'Diretor', '4x3')
addCargo('Tech Lead', 20000, 'Gerente', '4x3')
addCargo('Atendimento ao Cliente', 3000, 'Estagiário', '6x1')
addCargo('Representante de Atendimento', 8000, 'Gerente', '5x2')
addCargo('CEO', 28000, 'Diretor', '5x2')
addCargo('Contador', 5000, 'Analista', '5x2')
addCargo('Contador', 10000, 'Gerente', '4x3')
addCargo('Recrutador', 5000, 'Analista', '6x1')
addCargo('Tech Recruter', 8000, 'Gerente', '5x2')
addCargo('Vendedor', 5000, 'Analista', '6x1')
addCargo('Marketing Digital', 9000, 'Gerente', '4x3')

# addDepartamento(idDepartamento, nomeDepartamento, idGerente, andarDepartamento, horarioFuncionamento)
addDepartamento('TI', 1, 3, '8h até 20h')
addDepartamento('Marketing', 12, 4, '8h até 18h')
addDepartamento('Financeiro', 8, 5, '6h até 16h')
addDepartamento('Recursos Humanos', 10, 2, '8h até 18h')
addDepartamento('Suporte ao Cliente', 12, 1, '7h até 23h')

# addHistoricoSalarial(idSalarial, idFuncionario, data, salario)
addHistoricoSalarial(1, '2024-09-01', 19000)
addHistoricoSalarial(1, '2024-10-01', 19000)
addHistoricoSalarial(1, '2024-11-01', 20000)
addHistoricoSalarial(1, '2024-12-01', 20000)
addHistoricoSalarial(1, '2025-01-01', 23000)
addHistoricoSalarial(1, '2025-02-01', 23000)

addHistoricoSalarial(2, '2024-09-06', 3800)
addHistoricoSalarial(2, '2024-10-06', 3800)
addHistoricoSalarial(2, '2024-11-06', 3800)
addHistoricoSalarial(2, '2024-12-06', 4200)
addHistoricoSalarial(2, '2025-01-06', 4200)
addHistoricoSalarial(2, '2025-02-06', 4200)

addHistoricoSalarial(3, '2024-09-26', 9700)
addHistoricoSalarial(3, '2024-08-26', 9700)
addHistoricoSalarial(3, '2024-10-26', 10000)
addHistoricoSalarial(3, '2024-11-26', 10000)
addHistoricoSalarial(3, '2024-12-26', 11000)
addHistoricoSalarial(3, '2025-01-26', 11000)

addHistoricoSalarial(4, '2024-08-20', 5000)
addHistoricoSalarial(4, '2024-09-20', 5000)
addHistoricoSalarial(4, '2024-10-20', 5500)
addHistoricoSalarial(4, '2024-11-20', 5500)
addHistoricoSalarial(4, '2024-12-20', 6000)
addHistoricoSalarial(4, '2025-01-20', 6000)

addHistoricoSalarial(5, '2024-09-10', 9700)
addHistoricoSalarial(5, '2024-10-10', 9700)
addHistoricoSalarial(5, '2024-11-10', 9700)
addHistoricoSalarial(5, '2024-12-10', 9700)
addHistoricoSalarial(5, '2025-01-10', 9700)
addHistoricoSalarial(5, '2025-02-10', 9700)

addHistoricoSalarial(6, '2024-09-01', 9000)
addHistoricoSalarial(6, '2024-10-01', 9000)
addHistoricoSalarial(6, '2024-11-01', 9000)
addHistoricoSalarial(6, '2024-12-01', 9000)
addHistoricoSalarial(6, '2025-01-01', 9000)
addHistoricoSalarial(6, '2025-02-01', 9000)

addHistoricoSalarial(7, '2024-09-08', 5000)
addHistoricoSalarial(7, '2024-10-08', 5000)
addHistoricoSalarial(7, '2024-11-08', 5000)
addHistoricoSalarial(7, '2024-12-08', 5000)
addHistoricoSalarial(7, '2025-02-08', 5300)
addHistoricoSalarial(7, '2025-01-08', 5300)

addHistoricoSalarial(8, '2024-09-06', 12000)
addHistoricoSalarial(8, '2024-10-06', 12000)
addHistoricoSalarial(8, '2024-11-06', 12000)
addHistoricoSalarial(8, '2024-12-06', 12000)
addHistoricoSalarial(8, '2025-01-06', 12000)
addHistoricoSalarial(8, '2025-02-06', 12000)

addHistoricoSalarial(9, '2024-08-26', 5500)
addHistoricoSalarial(9, '2024-09-26', 5500)
addHistoricoSalarial(9, '2024-10-26', 5500)
addHistoricoSalarial(9, '2024-11-26', 5500)
addHistoricoSalarial(9, '2024-12-26', 5800)
addHistoricoSalarial(9, '2025-01-26', 5800)

addHistoricoSalarial(10, '2024-09-10', 9000)
addHistoricoSalarial(10, '2024-10-10', 9000)
addHistoricoSalarial(10, '2024-11-10', 9000)
addHistoricoSalarial(10, '2024-12-10', 9000)
addHistoricoSalarial(10, '2025-01-10', 9000)
addHistoricoSalarial(10, '2025-02-10', 9000)

addHistoricoSalarial(11, '2024-09-01', 3200)
addHistoricoSalarial(11, '2024-10-01', 3200)
addHistoricoSalarial(11, '2024-11-01', 3400)
addHistoricoSalarial(11, '2024-12-01', 3400)
addHistoricoSalarial(11, '2025-01-01', 3400)
addHistoricoSalarial(11, '2025-02-01', 3400)

addHistoricoSalarial(12, '2024-09-01', 8000)
addHistoricoSalarial(12, '2024-10-01', 8000)
addHistoricoSalarial(12, '2024-11-01', 8000)
addHistoricoSalarial(12, '2024-12-01', 8000)
addHistoricoSalarial(12, '2025-01-01', 8600)
addHistoricoSalarial(12, '2025-02-01', 8600)

addHistoricoSalarial(13, '2024-09-06', 4900)
addHistoricoSalarial(13, '2024-10-06', 4900)
addHistoricoSalarial(13, '2024-11-06', 4900)
addHistoricoSalarial(13, '2024-12-06', 5000)
addHistoricoSalarial(13, '2025-01-06', 5000)
addHistoricoSalarial(13, '2025-02-06', 5100)

addHistoricoSalarial(14, '2024-09-08', 5000)
addHistoricoSalarial(14, '2024-10-08', 5000)
addHistoricoSalarial(14, '2024-11-08', 5000)
addHistoricoSalarial(14, '2024-12-08', 5000)
addHistoricoSalarial(14, '2025-01-08', 5600)
addHistoricoSalarial(14, '2025-02-08', 5600)

addHistoricoSalarial(15, '2024-08-26', 19000)
addHistoricoSalarial(15, '2024-09-26', 19000)
addHistoricoSalarial(15, '2024-10-26', 19000)
addHistoricoSalarial(15, '2024-11-26', 19500)
addHistoricoSalarial(15, '2024-12-26', 19500)
addHistoricoSalarial(15, '2025-01-26', 20000)

addHistoricoSalarial(16, '2024-08-20', 19800)
addHistoricoSalarial(16, '2024-09-20', 19800)
addHistoricoSalarial(16, '2024-10-20', 19800)
addHistoricoSalarial(16, '2024-11-20', 19800)
addHistoricoSalarial(16, '2024-12-20', 19800)
addHistoricoSalarial(16, '2025-01-20', 20000)

addHistoricoSalarial(17, '2024-09-02', 3300)
addHistoricoSalarial(17, '2024-10-02', 3300)
addHistoricoSalarial(17, '2024-11-02', 3300)
addHistoricoSalarial(17, '2024-12-02', 3300)
addHistoricoSalarial(17, '2025-01-02', 3300)
addHistoricoSalarial(17, '2025-02-02', 3300)

addHistoricoSalarial(18, '2024-09-08', 3200)
addHistoricoSalarial(18, '2024-10-08', 3200)
addHistoricoSalarial(18, '2024-11-08', 3200)
addHistoricoSalarial(18, '2024-12-08', 3200)
addHistoricoSalarial(18, '2025-01-08', 3400)
addHistoricoSalarial(18, '2025-02-08', 3400)

addHistoricoSalarial(19, '2024-09-06', 3300)
addHistoricoSalarial(19, '2024-10-06', 3300)
addHistoricoSalarial(19, '2024-11-06', 3300)
addHistoricoSalarial(19, '2024-12-06', 3300)
addHistoricoSalarial(19, '2025-01-06', 3300)
addHistoricoSalarial(19, '2025-02-06', 3300)

addHistoricoSalarial(20, '2024-09-06', 4800)
addHistoricoSalarial(20, '2024-10-06', 4800)
addHistoricoSalarial(20, '2024-11-06', 4800)
addHistoricoSalarial(20, '2024-12-06', 4800)
addHistoricoSalarial(20, '2025-01-06', 4800)
addHistoricoSalarial(20, '2025-02-06', 4800)

addHistoricoSalarial(21, '2024-09-06', 5000)
addHistoricoSalarial(21, '2024-10-06', 5000)
addHistoricoSalarial(21, '2024-11-06', 5000)
addHistoricoSalarial(21, '2024-12-06', 5000)
addHistoricoSalarial(21, '2025-01-06', 5000)
addHistoricoSalarial(21, '2025-02-06', 5000)

# addDependente(idDependente, idFuncionario, parentesco, nome, idade, genero)
addDependente(1, 'Filho', 'Izaac Xavier', '2010-04-14', 'Masculino')
addDependente(1, 'Cônjuge', 'Manuela Silva Xavier', '1996-06-28', 'Feminino')

addDependente(2, 'Mãe', 'Laura Pereira Oliveira', '1979-03-25', 'Feminino')
addDependente(2, 'Pai', 'Sebastião Oliveira', '1976-06-21', 'Masculino')
addDependente(2, 'Filho', 'Juliana Oliveira Soares', '2022-08-15', 'Feminino')

addDependente(3, 'Cônjuge', 'Débora Souza Andrade', '2010-07-14', 'Feminino')
addDependente(3, 'Mãe', 'Amanda Oliveira Andrade', '1974-06-23', 'Feminino')

addDependente(4, 'Pai', 'Anderson Gomes', '1972-01-27', 'Masculino')
addDependente(4, 'Irmão', 'Gabriela Gomes', '2007-03-17', 'Feminino')

addDependente(5, 'Cônjuge', 'Paulo da Silva Queiroz', '1997-05-24', 'Masculino')
addDependente(5, 'Filho', 'Ivana Barbosa Queiroz', '2015-04-15', 'Feminino')

addDependente(6, 'Mãe', 'Manuela Schmidt', '1976-09-29', 'Feminino')
addDependente(6, 'Irmão', 'Mara Schmidt', '2010-12-25', 'Feminino')

addDependente(7, 'Filho', 'Júlia Alvares', '2021-03-05', 'Feminino')
addDependente(7, 'Filho', 'Larissa Alvares', '2018-11-25', 'Feminino')

addDependente(8, 'Cônjuge', 'Luciana Braz Augusto', '2001-10-04', 'Feminino')
addDependente(8, 'Filho', 'Carlos Augusto', '2020-02-16', 'Masculino')

addDependente(9, 'Filho', 'Fabiana Rosa da Silva', '2015-08-19', 'Feminino')
addDependente(9, 'Filho', 'Edgar Rosa da Silva', '2010-02-21', 'Masculino')

addDependente(10, 'Cônjuge', 'Larissa Borbon Moreira', '1986-04-13', 'Feminino')
addDependente(10, 'Filho', 'Wagner Moreira', '2007-09-19', 'Masculino')

addDependente(11, 'Mãe', 'Sandra Albuquerque Alencar', '1979-12-05', 'Feminino')
addDependente(11, 'Pai', 'Leandro Santos Alencar', '1975-11-22', 'Masculino')

addDependente(12, 'Cônjuge', 'Patrícia dos Anjos Araújo', '1972-06-07', 'Feminino')
addDependente(12, 'Filho', 'Thaísa dos Anjos Araújo', '1998-01-20', 'Feminino')

addDependente(13, 'Cônjuge', 'Marcos Ferreira Sousa', '1999-01-22', 'Masculino')
addDependente(13, 'Filho', 'Lucas Sousa', '2020-01-14', 'Masculino')

addDependente(14, 'Mãe', 'Maria Soares Silva', '2011-01-14', 'Feminino')
addDependente(14, 'Filho', 'Daniela Silva', '2024-01-01', 'Feminino')

addDependente(15, 'Cônjuge', 'Carla Gross Almeida', '1984-02-03', 'Feminino')
addDependente(15, 'Filho', 'Roberta Landini Almeida', '2007-05-05', 'Feminino')
addDependente(15, 'Filho', 'Luana Gross Almeida', '1997-07-07', 'Feminino')

addDependente(16, 'Cônjuge', 'Anderson Gonçalves Borges', '1998-01-25', 'Masculino')
addDependente(16, 'Filho', 'Tainara Borges', '2018-07-08', 'Feminino')

addDependente(17, 'Cônjuge', 'Andressa Almeida Ferraz', '1998-09-09', 'Feminino')
addDependente(17, 'Filho', 'Fábia Almeida Ferraz', '2016-10-12', 'Feminino')

addDependente(18, 'Mãe', 'Ana Alves de Souza', '1972-04-05', 'Feminino')
addDependente(18, 'Pai', 'André Barreto', '1972-03-26', 'Masculino')

addDependente(19, 'Pai', 'Alexandre da Silva Lopez', '1970-12-12', 'Masculino')
addDependente(19, 'Irmão', 'Alberto Lopez', '2018-05-14', 'Masculino')

addDependente(20, 'Cônjuge', 'Leila Boaventura Lima', '2010-08-07', 'Feminino')
addDependente(20, 'Filho', 'Fabrício Lima', '2023-01-13', 'Masculino')

addDependente(21, 'Cônjuge', 'Alessandra Lopez Ribeiro', '1994-09-18', 'Feminino')
addDependente(21, 'Filho', 'Caio Ribeiro', '2014-08-21', 'Masculino')


# addProjeto(idProjeto, idResponsavel, nomeProjeto, descricao, inicio, conclusao, custo, status)
addProjeto(1, 'E-commerce de Eletrônicos [Site Institucional]', 'Desenvolvimento de loja virtual de eletrônicos: página inicial, produtos, carrinho de compras, sistema de pagamento, dashboard.', '2025-02-10', '2025-04-10', 8000, 'Em Execução')
addProjeto(15, 'Restaurante [Single page]','Desenvolvimento página única do site de restaurante: banner, sobre, cardápio, formulário de contato.','2025-01-05','2025-01-15', 3000,'Concluído')
addProjeto(1, 'Manutenção de E-commerce de Roupas', 'Correção de erros de funcionalidade.', '2024-11-24', '2024-12-02', 600, 'Concluído')
addProjeto(16, 'Portfólio Advogado [Site Institucional]', 'Desenvolvimento de um site de portfólio: banner, biografia, casos de sucesso e contato.', '2025-02-19', '2025-02-28', 4000, 'Em Planejamento')
addProjeto(21, 'Publicidade Paga I', 'Desenvolvimento de Publicidades em Redes Sociais.', '2024-12-10', '2024-12-16', 450, 'Concluído')
addProjeto(4, 'Publicidade Paga II', 'Desenvolvimento de Publicidades em Redes Sociais.', '2025-02-13', '2025-02-23', 500, 'Em Execução')
addProjeto(8, 'Planejamento Financeiro I', 'Desenvolvimento de ferramentas para o planejamento financeiro da empresa.', '2025-01-10', '2025-01-17', 600, 'Concluído')
addProjeto(8, 'Planejamento Financeiro II', 'Desenvolvimento do planejamento financeiro da empresa.', '2025-02-19', '2025-02-28', 500, 'Em Andamento')
addProjeto(12, 'Planejamento I', 'Desenvolvimento de Estratégias', '2025-02-19', '2025-02-19', 500, 'Cancelado')
addProjeto(16, 'E-commerce de Roupas [Site Institucional]', 'Desenvolvimento de loja virtual de roupas: página inicial, roupas, carrinho de compras, sistema de pagamento, dashboard.', '2025-02-15', '2025-04-15', 8000, 'Em Execução')
addProjeto(1, 'Portfolio Garçom [Single page]','Desenvolvimento página única do site de portfílo: banner, sobre, currículo, formulário de contato.','2025-02-22','2025-03-01', 3000, 'Em Execução')


# addRecurso(idRecurso, idProjeto, descricao, qtd, dataUtilizacao)
addRecurso(1, 'Desenvolvedor de Software', 'Humano', 4, '2025-02-13')
addRecurso(1, 'Designer', 'Humano', 1, '2025-02-12')
addRecurso(1, 'Servidor de Hospedagem', 'Material', 1, '2025-02-25')
addRecurso(2, 'Desenvolvedor de Software', 'Humano', 1, '2025-01-06')
addRecurso(2, 'Servidor de Hospedagem', 'Material', 1, '2025-01-13')
addRecurso(3, 'Desenvolvedor de Software', 'Humano', 2, '2024-11-25')
addRecurso(3, 'Servidor de Hospedagem', 'Material', 1, '2024-12-01')
addRecurso(4, 'Desenvolvedor de Software', 'Humano', 2, '2025-02-20')
addRecurso(5, 'Anúncio no Google Ads', 'Financeiro', 1, '2024-12-14')
addRecurso(6, 'Anúncio no Google Ads', 'Financeiro', 1, '2024-12-14')
addRecurso(7, 'Desenvolvedor de Software', 'Humano', 2, '2025-01-11')
addRecurso(7, 'Assinatura Power BI Premium', 'Financeiro', 4, '2025-01-11')
addRecurso(8, 'Orçamento para Treinamento', 'Financeiro', 1, '2025-02-19')
addRecurso(9, 'Desenvolvedor de Software', 'Humano', 4, '2025-02-16')
addRecurso(9, 'Designer', 'Humano', 1, '2025-02-15')
addRecurso(10, 'Desenvolvedor de Software', 'Humano', 1, '2025-02-23')



def inserirDadosCsv(nomeArquivo, lista, *campos):
    '''
    Esta função cria um arquivo .CSV personalizado como base no nome do arquivo, lista e os campos.
    
    Args:
        nomeArquivo(str): Refere-se ao nome do arquivo que irá ser gerado.
        lista(list[obj]): Refere-se à uma lista de dados criada nas funções anteriores.
        campos(*Args): Refere-se aos campos que a tabela .CSV terá.
    '''
    df = pd.DataFrame(lista)
    df.to_csv(f'api/tabelas/tb_{nomeArquivo}.csv', encoding='UTF-8', index=False)
    print(f'{nomeArquivo.title()}s adicionados com sucesso!\n')  
          
          
# inserirDadosCsv(nomeArquivo, lista, *campos)
inserirDadosCsv('funcionario', funcionarios, 'idFuncionario', 'nomeFuncionario', 'idCargo', 'idDepartamento', 'salarioReal', 'dataNascimento')
inserirDadosCsv('cargo', cargos, 'idCargo', 'nomeCargo', 'salarioBase', 'nivelCargo', 'escala')    
inserirDadosCsv('departamento', departamentos, 'idDepartamento', 'nomeDepartamento', 'idGerente', 'andarDepartamento', 'horarioFuncionamento')      
inserirDadosCsv('historicoSalarial', historicoSalarial, 'idSalarial', 'idFuncionario', 'data', 'salario')        
inserirDadosCsv('dependente', dependentes, 'idDependente', 'idFuncionario', 'parentesco', 'nome', 'idade', 'genero') 
inserirDadosCsv('projeto', projetos, 'idResponsavel', 'nomeProjeto', 'descricao', 'inicio', 'conclusao', 'custo', 'status')
inserirDadosCsv('recurso', recursos, 'idRecurso', 'idProjeto', 'descricao', 'tipo','qtd', 'dataUtilizacao')
            