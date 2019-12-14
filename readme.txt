Este juego del tateti es para la evaluacion tecnica se desarrollo en python 3

Para hacerlo andar crear un ambiente virtual para independizar el ambiente
  python3 -m venv tutorial-env

activar el ambiente:
  source bin/activate

instalar requiriments.txt de la siquiente manera
  pip install -r requiriments.txt

 el mismo esta vacio ya que el unico paquete que utilice fue "random"

 el diagrama de casillero para el juego tiene la siguiente disposicion

                 6   |  7  |  8
               _________________
                 3   |  4  |  5
               _________________
                 0   |  1  |  2

Al iniciar se elije aleatoriamente quien empieza, si la maquina o el jugador.
La maquina no tiene ninguna inteligencia, esta selecciona aleatoriamente casillas vacias
