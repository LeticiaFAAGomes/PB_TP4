from api.crud import *
from api.criacao_tabelas import executar_tabelas

funcionarios, cargos, departamentos, salarios, dependentes, projetos, recursos = executar_tabelas()

amarelo = '\x1b[38;5;229m'


print(f'{amarelo}1. Trazer a média dos salários (atual) dos funcionários responsáveis por projetos concluídos, agrupados por departamento.')
tp4_1 = consultar_tabelas("""
    SELECT D.nomeDepartamento AS Departamento, 
    ROUND(AVG(H.salario))     AS Media 
    FROM tb_Funcionario  F
    JOIN (
        SELECT idFuncionario, salario
        FROM tb_HistoricoSalarial H
        WHERE H.data = (
            SELECT MAX(data)
            FROM tb_HistoricoSalarial 
            WHERE idFuncionario = H.idFuncionario
            )
    )                    H  ON H.idFuncionario = F.idFuncionario
    JOIN tb_Projeto      P  ON P.idResponsavel = F.idFuncionario
    JOIN tb_Departamento D  ON D.idDepartamento = F.idDepartamento
    WHERE P.status = 'Concluído'
    GROUP BY D.nomeDepartamento;   
    """,'tp4.1')
print(tp4_1)


print(f'{amarelo}2. Identificar os três recursos materiais mais usados nos projetos, listando a descrição do recurso e a quantidade total usada.')
tp4_2 = consultar_tabelas("""
    SELECT descricaoRecurso AS Recurso, 
    SUM(qtdRecurso)         AS Qtd 
    FROM tb_Recurso
    GROUP BY descricaoRecurso
    ORDER BY qtd DESC LIMIT 3;                      
    """)
print(tp4_2)


print(f'{amarelo}3. Calcular o custo total dos projetos por departamento, considerando apenas os projetos "Concluídos".')
tp4_3 = consultar_tabelas("""
    SELECT D.nomeDepartamento AS Departamento, 
    SUM(P.custo)              AS CustoTotal
    FROM tb_Funcionario  F
    JOIN tb_Departamento D ON D.idDepartamento = F.idDepartamento
    JOIN tb_Projeto      P ON P.idResponsavel = F.idFuncionario
    WHERE P.status = 'Concluído'
    GROUP BY D.nomeDepartamento;                      
    """,'tp4.3')
print(tp4_3)


print(f'{amarelo}4. Listar todos os projetos com seus respectivos nomes, custo, data de início, data de conclusão e o nome do funcionário responsável, que estejam "Em Execução".')
tp4_4 = consultar_tabelas("""
    SELECT P.nomeProjeto AS Projeto, 
    P.custo, 
    P.inicio, 
    P.conclusao, 
    F.nomeFuncionario    AS Funcionario, 
    P.status
    FROM tb_Funcionario F
    JOIN tb_Projeto     P ON P.idResponsavel = F.idFuncionario
    WHERE P.status = 'Em Execução';                      
    """,'tp4.4')
print(tp4_4)


print(f'{amarelo}5. Identificar o projeto com o maior número de dependentes envolvidos, considerando que os dependentes são associados aos funcionários que estão gerenciando os projetos.')
tp4_5 = consultar_tabelas("""
    SELECT P.nomeProjeto  AS Projeto, 
    COUNT(D.idDependente) AS Qtd
    FROM tb_Funcionario F
    JOIN tb_Projeto     P  ON P.idResponsavel = F.idFuncionario
    JOIN tb_Dependente  D  ON D.idFuncionario = F.idFuncionario
    GROUP BY P.nomeProjeto
    ORDER BY Qtd DESC LIMIT 1;                  
    """)
print(tp4_5)

desconectar(conn)
