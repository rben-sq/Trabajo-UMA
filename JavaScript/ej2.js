const readlineSync = require('readline-sync');

class Producto{
    constructor (nombre, precio, cantidad){
        this.nombre = nombre;
        this.precio = precio;
        this.cantidad = cantidad;
    }
    
    toString() {
        return `\nNombre: ${this.nombre}\nPrecio: ${this.precio}\nCantidad: ${this.cantidad}\n`;
      }
}

class Inventario{
    constructor(){
        this.inventario=[];
    }
    
    añadir(producto){
        this.inventario.push(producto);
    }

    eliminar(nombre){
        this.inventario= this.inventario.filter(producto => producto.nombre !== nombre);
    }

    calcularValor(){
        let total=0
        this.inventario.forEach(a => {
            total += a.precio*a.cantidad;
        });

        return total
    }
    mostrar_inventario(){
        console.log(this.inventario.toString());
    }
    
    mostrarMenu() {
        let opcion;
        do {
            console.log("\nGESTIÓN DE USUARIOS");
            console.log("===================");
            console.log("1. Agregar usuario.");
            console.log("2. Modificar su edad.");
            console.log("3. Eliminar usuario.");
            console.log("4. Mostrar usuarios mayores de edad.");
            console.log("5. Mostrar promedio de edad.");
            console.log("6. Salir.");

            opcion = readlineSync.question("Introduce una opcion de 1-6: ");

            switch (opcion) {
                case '1':
                    const nombreNuevo = readlineSync.question("Introduce el nombre del usuario: ");
                    const edadNueva = Number(readlineSync.question("Introduce la edad del usuario: "));
                    this.agregarUsuario(nombreNuevo, edadNueva);
                    break;
                case '2':
                    const nombreModificar = readlineSync.question("Introduce el nombre del usuario a modificar: ");
                    const nuevaEdad = Number(readlineSync.question("Introduce la nueva edad: "));
                    this.modificarSuEdad(nombreModificar, nuevaEdad);
                    break;
                case '3':
                    const nombreEliminar = readlineSync.question("Introduce el nombre del usuario a eliminar: ");
                    this.eliminarUsuario(nombreEliminar);
                    break;
                case '4':
                    this.usuariosMayoresDeEdad();
                    break;
                case '5':
                    this.promedioDeEdad();
                    break;
                case '6':
                    console.log("Saliendo del programa.");
                    break;
                default:
                    console.log("Opción inválida.");
            }
        } while (opcion !== '6');
    }
}

let inventario = new Inventario();
gestion.mostrarMenu();


/* while (opcion!==0){
    console.log("1. Listar")
    console.log("2. Añadir")
    console.log("3. Eliminar")
    console.log("4. Valor total inventario")

    opcion = readlineSync.question("Introduce la opcion: ");

    if (opcion === 1){
        inventario.mostrar_inventario()
    } else if (opcion === 2){
        let nombre = readlineSync.question("Nombre: ")
        let precio = Number(readlineSync.question("Precio: "))
        let cantidad = Number(readlineSync.question("Cantidad: "))

        let producto = Producto(nombre, precio, cantidad)
        inventario.añadir(producto)
    } else if (opcion === 3){
        let nombre = readlineSync.question("Nombre: ")
        inventario.eliminar(nombre)
    } else if (opcion === 4){
        console.log("Valor total del inventario: " + inventario.calcularValor());
    } else { 
        opcion= 0
    }
} */