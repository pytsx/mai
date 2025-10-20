from datetime import datetime

class TracerCache:
  
  @staticmethod
  def get_active_instance():
    return 
  
  @staticmethod
  def get(key: str):
    return 

class Tracer:
  def __init__(self):
    self.tracer_id = datetime.now().__str__()
    self.spans:list=[]
    
  def _start(self):
    span = {"tracer_id": self.tracer_id, "name": "start", "at": datetime.now()}
    self.spans.append(span)
  
  def span(self, name: str):
    span = {"tracer_id": self.tracer_id,"name": name, "at": datetime.now()}
    self.spans.append(span)
  
  def end(self):
    span = {"tracer_id": self.tracer_id, "name": "end", "at": datetime.now()}
    self.spans.append(span)
    
  
    
  def _generate_trace_id(self):
    return datetime.now().__str__()