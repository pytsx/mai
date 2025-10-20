O módulo tableau.map é responsável por mapear o conteúdo do servidor e cria um arquivo com todas as relações e objetos acessíveis por meio de tipagem 

0 - ao chamar o módulo como main, executar o seguinte fluxo:
1 - buscar os dados atuais no servidor 
2 - salvar um arquivo excel ou csv com o conteúdo
3 - parsear o conteúdo 
4 - criar os objetos e as relações 
5 - criar um arquivo .py com os objetos relações acessíveis para o código 


# show case
´´python
@dataclass
class Project:
  parent: 'Project' | None
  name: str
  id: str 
  
prj_simtech = Project(None, 'SimTech', '')
prj_fluxos = Project(simtech, 'fluxos', '')
prj_ciclo_de_vida = Project(fluxos, 'ciclo de vida', '')
´´

