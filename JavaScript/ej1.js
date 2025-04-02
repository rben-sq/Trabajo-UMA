class Estudiante {
    constructor(nombre, edad, curso) {
        this.nombre=nombre;
        this.edad=edad;
        this.curso=curso;
    }
    
    presentarse(){
        console.log("Hola, me llamo "+ this.nombre + " y estoy en " + this.curso)
    }
    

    
    
}
/* antonio= new Estudiante("Antonio", 19, "2º")
manolo= new Estudiante("Manolo", 18, "1º")
paco= new Estudiante("Paco", 23, "1º")
tomas= new Estudiante("Tomás", 39, "2º")

const clase = [antonio, manolo, paco, tomas] */
let clase = [
    new Estudiante("Antonio", 19, "2º"),
    new Estudiante("Manolo", 18, "1º"),
    new Estudiante("Paco", 23, "1º"),
    new Estudiante("Tomás", 39, "2º")
]

clase.forEach(estudiante => {
    estudiante.presentarse();
});