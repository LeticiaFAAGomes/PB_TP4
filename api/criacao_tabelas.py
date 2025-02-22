from api.crud import *

def executar_tabelas():
    '''
    Esta função cria todas as tabelas armazenadas nos arquivos .CSV na pasta tabelas e depois insere os dados nelas.
    
    Returns:
        lists:
            funcionarios(list[dict]): Refere-se aos dados de funcionarios que estavam armazenados em tb_funcionario.csv;
            cargos(list[dict]): Refere-se aos dados de cargos que estavam armazenados em tb_cargo.csv;
            departamentos(list[dict]): Refere-se aos dados de departamentos que estavam armazenados em tb_departamento.csv;
            salarios(list[dict]): Refere-se aos dados de salários que estavam armazenados em tb_historicoSalarial.csv;
            dependentes(list[dict]): Refere-se aos dados de dependentes que estavam armazenados em tb_dependente.csv;
            projetos(list[dict]): Refere-se aos dados de projetos que estavam armazenados em tb_projeto.csv
            recursos(list[dict]): Refere-se aos dados de recursos que estavam armazenados em tb_recurso.csv
    ''' 
    cursor.execute("PRAGMA foreign_keys = OFF")
    
    criar_tabelas('''
        CREATE TABLE IF NOT EXISTS tb_Cargo (
            
            idCargo      INTEGER PRIMARY KEY AUTOINCREMENT,
            nomeCargo    VARCHAR(30),
            salarioBase  REAL,
            nivelCargo   VARCHAR(30),
            escala       VARCHAR(30)
        );
    ''')
    
    criar_tabelas("""
        CREATE TABLE IF NOT EXISTS tb_Departamento (
            
            idDepartamento        INTEGER  PRIMARY KEY AUTOINCREMENT,
            nomeDepartamento      VARCHAR(30),
            idGerente             INTEGER,
            andarDepartamento     INTEGER,
            horarioFuncionamento  VARCHAR(30),
            
            FOREIGN KEY (idGerente) REFERENCES tb_Funcionario(idFuncionario)
        );    
    """)
    
    criar_tabelas('''
        CREATE TABLE IF NOT EXISTS tb_Funcionario (
            
            idFuncionario    INTEGER  PRIMARY KEY AUTOINCREMENT,
            nomeFuncionario  VARCHAR(50),
            idCargo          INTEGER,
            idDepartamento   INTEGER,
            salarioReal      REAL,
            dataNascimento   TEXT,
            
            FOREIGN KEY (idCargo) REFERENCES tb_Cargo(idCargo),
            FOREIGN KEY (idDepartamento) REFERENCES tb_Departamento(idDepartamento)
        );
    ''')
    

    criar_tabelas('''
        CREATE TABLE IF NOT EXISTS tb_historicoSalarial (
            
            idSalarial     INTEGER  PRIMARY KEY AUTOINCREMENT,
            idFuncionario  INTEGER,
            data           TEXT,
            salario        REAL,
            
            FOREIGN KEY (idFuncionario) REFERENCES tb_Funcionario(idFuncionario)
        );
    ''')

    criar_tabelas('''
        CREATE TABLE IF NOT EXISTS tb_Dependente (
        
            idDependente   INTEGER  PRIMARY KEY AUTOINCREMENT,
            idFuncionario  INTEGER,
            parentesco     VARCHAR(10),
            nome           VARCHAR(50),
            idade          TEXT,
            genero         VARCHAR(15),
            
            FOREIGN KEY (idFuncionario) REFERENCES tb_Funcionario(idFuncionario)
        );
    ''')
    
    criar_tabelas('''
        CREATE TABLE IF NOT EXISTS tb_Projeto (
            
            idProjeto        INTEGER  PRIMARY KEY AUTOINCREMENT,
            idResponsavel    INTEGER,
            nomeProjeto      VARCHAR(50),
            descricaoProjeto VARCHAR(150),
            inicio           TEXT,
            conclusao        TEXT,
            custo            REAL(10,2),
            status           VARCHAR(15),
            
            FOREIGN KEY (idResponsavel) REFERENCES tb_Funcionario(idFuncionario)
        );
    ''')

    criar_tabelas('''
        CREATE TABLE IF NOT EXISTS tb_Recurso (
        
            idRecurso         INTEGER  PRIMARY KEY AUTOINCREMENT,
            idProjeto         INTEGER,
            descricaoRecurso  VARCHAR(40),
            tipoRecurso       VARCHAR(15),
            qtdRecurso        INTEGER,
            dataUtilizacao    TEXT,    
            
            FOREIGN KEY (idProjeto) REFERENCES tb_Projeto(idProjeto)
        );
    ''')
    
             
    funcionarios = lerDadosCsv('tb_funcionario.csv')
    cargos = lerDadosCsv('tb_cargo.csv')
    departamentos = lerDadosCsv('tb_departamento.csv')
    salarios = lerDadosCsv('tb_historicoSalarial.csv')
    dependentes = lerDadosCsv('tb_dependente.csv')
    projetos = lerDadosCsv('tb_projeto.csv')
    recursos = lerDadosCsv('tb_recurso.csv')


    criar_insert('INSERT OR IGNORE INTO tb_Cargo(idCargo, nomeCargo, salarioBase, nivelCargo, escala) VALUES(:idCargo, :nomeCargo, :salarioBase, :nivelCargo, :escala);', 
                        [{'idCargo':cargo['idCargo'],
                        'nomeCargo':cargo['nomeCargo'], 
                        'salarioBase':cargo['salarioBase'], 
                        'nivelCargo':cargo['nivelCargo'], 
                        'escala':cargo['escala']} for cargo in cargos])

    criar_insert('''INSERT OR IGNORE INTO tb_Departamento(idDepartamento, nomeDepartamento, idGerente, andarDepartamento, horarioFuncionamento) 
                    VALUES(:idDepartamento, :nomeDepartamento, :idGerente, :andarDepartamento, :horarioFuncionamento);''', 
                        [{'idDepartamento':departamento['idDepartamento'],
                        'nomeDepartamento':departamento['nomeDepartamento'], 
                        'idGerente':departamento['idGerente'], 
                        'andarDepartamento':departamento['andarDepartamento'], 
                        'horarioFuncionamento':departamento['horarioFuncionamento']} for departamento in departamentos])

    criar_insert('''INSERT OR IGNORE INTO tb_Funcionario(idFuncionario, nomeFuncionario, idCargo, idDepartamento, salarioReal, dataNascimento) 
                    VALUES(:idFuncionario, :nomeFuncionario, :idCargo, :idDepartamento, :salarioReal, :dataNascimento);''', 
                        [{'idFuncionario':funcionario['idFuncionario'],
                        'nomeFuncionario':funcionario['nomeFuncionario'], 
                        'idCargo':funcionario['idCargo'], 
                        'idDepartamento':funcionario['idDepartamento'], 
                        'salarioReal':funcionario['salarioReal'], 
                        'dataNascimento':funcionario['dataNascimento']} for funcionario in funcionarios])

    criar_insert('''INSERT OR IGNORE INTO tb_historicoSalarial(idSalarial, idFuncionario, data, salario) 
                    VALUES(:idSalarial, :idFuncionario, :data, :salario);''', 
                        [{'idSalarial':historicoSalarial['idSalarial'],
                        'idFuncionario':historicoSalarial['idFuncionario'], 
                        'data':historicoSalarial['data'], 
                        'salario':historicoSalarial['salario']} for historicoSalarial in salarios])

    criar_insert('''INSERT OR IGNORE INTO tb_Dependente(idDependente, idFuncionario, parentesco, nome, idade, genero) 
                    VALUES(:idDependente, :idFuncionario, :parentesco, :nome, :idade, :genero);''', 
                        [{'idDependente':dependente['idDependente'],
                        'idFuncionario':dependente['idFuncionario'], 
                        'parentesco':dependente['parentesco'], 
                        'nome':dependente['nome'], 
                        'idade':dependente['idade'],
                        'genero':dependente['genero']} for dependente in dependentes])
    
    criar_insert('''INSERT OR IGNORE INTO tb_Projeto(idProjeto, idResponsavel, nomeProjeto, descricaoProjeto, inicio, conclusao, custo, status) 
                    VALUES(:idProjeto, :idResponsavel, :nomeProjeto, :descricaoProjeto, :inicio, :conclusao, :custo, :status);''', 
                       [{'idProjeto':projeto['idProjeto'],
                        'idResponsavel':projeto['idResponsavel'], 
                        'nomeProjeto':projeto['nomeProjeto'], 
                        'descricaoProjeto':projeto['descricaoProjeto'], 
                        'inicio':projeto['inicio'],
                        'conclusao':projeto['conclusao'],
                        'custo':projeto['custo'],
                        'status':projeto['status']}  for projeto in projetos])
    
    criar_insert('''INSERT OR IGNORE INTO tb_Recurso(idRecurso, idProjeto, descricaoRecurso, tipoRecurso, qtdRecurso, dataUtilizacao) 
                    VALUES(:idRecurso, :idProjeto, :descricaoRecurso, :tipoRecurso, :qtdRecurso, :dataUtilizacao);''', 
                        [{'idRecurso':recurso['idRecurso'],
                        'idProjeto':recurso['idProjeto'], 
                        'descricaoRecurso':recurso['descricaoRecurso'], 
                        'tipoRecurso':recurso['tipoRecurso'], 
                        'qtdRecurso':recurso['qtdRecurso'],
                        'dataUtilizacao':recurso['dataUtilizacao']} for recurso in recursos])
    
    cursor.execute("PRAGMA foreign_keys = ON")
    
    return funcionarios, cargos, departamentos, salarios, dependentes, projetos, recursos
