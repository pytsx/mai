from dataclasses import dataclass

@dataclass
class Project:
  parent: 'Project' | None
  name: str
  id: str 
  
# simtech = Project(None, 'SimTech', '')
# fluxos = Project(simtech, 'fluxos', '')
# ciclo_de_vida = Project(fluxos, 'ciclo de vida', '')


if __name__ == "__main__":
  # se o arquivo for rodado como main, vamos gerar mapear o servidor e criar os objetos com suas respectivas relações
  ...