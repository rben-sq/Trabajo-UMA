class Vehiculo {
    constructor (marca, modelo, año){
        this.marca= marca;
        this.modelo= modelo;
        this.año= año;
    }

    info(){
        return `\n ${this.marca} ${this.modelo} ${this.año}`; 
    }
}

class Coche extends Vehiculo {
    constructor(marca, modelo, año, puertas){
        super(marca, modelo, año);
        this.puertas= puertas;
    }

    info(){
        return `\n${this.marca} ${this.modelo} ${this.año}, ${this.marca}` 
    }
}

const miCoche = new Coche('Toyota', 'Corolla', 2020, 4);
console.log(miCoche.info()); // "Toyota Corolla 2020, 4 puertas"

