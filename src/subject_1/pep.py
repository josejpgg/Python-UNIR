from typing import Dict, List, Optional

class GestorTareas:
    """Gestiona una colección de tareas pendientes.
    
    Implementa operaciones básicas CRUD para administrar tareas.
    """
    
    def __init__(self) -> None:
        self.tareas: Dict[int, str] = {}
        self.ultimo_id: int = 0
    
    def agregar(self, descripcion: str) -> int:
        """Agrega una nueva tarea y devuelve su ID.
        
        Args:
            descripcion: Texto que describe la tarea
            
        Returns:
            El ID asignado a la nueva tarea
        """
        self.ultimo_id += 1
        self.tareas[self.ultimo_id] = descripcion
        return self.ultimo_id
    
    def obtener(self, id_tarea: int) -> Optional[str]:
        """Recupera una tarea por su ID.
        
        Args:
            id_tarea: El identificador de la tarea
            
        Returns:
            La descripción de la tarea o None si no existe
        """
        return self.tareas.get(id_tarea)
    
    def listar_todas(self) -> List[Dict[str, object]]:
        """Devuelve todas las tareas como una lista de diccionarios.
        
        Returns:
            Lista de tareas con formato {id: n, descripcion: texto}
        """
        return [
            {"id": id_tarea, "descripcion": desc}
            for id_tarea, desc in self.tareas.items()
        ]
