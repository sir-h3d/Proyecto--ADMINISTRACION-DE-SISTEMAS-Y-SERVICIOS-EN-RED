Proyecto de Gestión de Conexiones Remotas

Este es un proyecto que utiliza MongoDB, Express.js y Mongoose para gestionar y visualizar las conexiones remotas. Proporciona una interfaz web para realizar operaciones CRUD en una base de datos de direcciones IP y usuarios.

Configuración de MongoDB

Asegúrate de tener MongoDB instalado y en ejecución en tu máquina local. Puedes modificar la configuración de la base de datos en el archivo app.js.

javascript
Copy code
const mongoose = require('mongoose');

mongoose.connect('mongodb://127.0.0.1:27017/connection_ssh', {
    useNewUrlParser: true,
}, (err) => {
    if (!err) {
        console.log('Conexión exitosa a MongoDB');
    } else {
        console.log('Error en la conexión a MongoDB: ' + err);
    }
});
Configuración del Servidor Express
El servidor Express se configura en el archivo app.js. Puedes personalizar el puerto en el que se ejecutará el servidor.

javascript
Copy code
app.listen(3000, () => {
    console.log("Servidor iniciado en el puerto 3000");
});
Rutas y Controladores
El proyecto tiene rutas y controladores para realizar operaciones CRUD en la base de datos. Estas se encuentran en los archivos routes.js y routes_controller.js.

Modelos de Datos
El modelo de datos se define en el archivo routes.model.js utilizando Mongoose. Define la estructura de los datos que se almacenarán en la base de datos.

javascript
Copy code
var routerSchema = new mongoose.Schema({
    username: { type: String, required: 'Este campo es obligatorio' },
    ip: { type: String, required: 'Este campo es obligatorio' },
});

mongoose.model("Routes", routerSchema);
Uso
Asegúrate de tener MongoDB instalado y en ejecución en tu máquina local.
Clona este repositorio.
Ejecuta npm install para instalar las dependencias.
Ejecuta npm start para iniciar el servidor.
Accede a la aplicación en tu navegador web en http://localhost:3000.

