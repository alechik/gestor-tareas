### Requisitos
- Python 3.10 o superior
- Paquetes `requirements.txt` (`flask`)

### Ejecutar consola
```bash
python main.py
```
### Ejecutar API
```bash
python src/api.py
```
`http://localhost:5000`.

### Endpoints
- **GET /**: información básica de la API
- **GET /tareas**: listar las tareas
- **POST /tareas**: crear tarea (`{"descripcion": "texto"}`)
- **GET /tareas/<id>**: obtener tarea por ID
- **PUT /tareas/<id>**: marcar tarea como completada
- **DELETE /tareas/<id>**: eliminar tarea

## Ejecución
```bash
python main.py