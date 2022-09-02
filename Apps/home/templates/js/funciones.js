$(document).on('ready', Iniciar);

function Iniciar(){
   
    alert("Boton "); 
    $varBoton = $('#btnAgregar');
    $varBoton.on('click', Presionar);
    $varBotonA= $('btnAgregar');
    $varBotonA.on ('click',Agregar);
    
}

function Presionar(){
    alert("Boton presionado"); 

}