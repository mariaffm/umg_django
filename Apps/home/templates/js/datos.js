
function Iniciar(){
   
    $varBoton = $('#btnAgregar');
    $varBoton.on('click', Presionar);
    $varBotonA= $('btnAgregar');
    $varBotonA.on ('click',Agregar);
    
}

function Presionar(){
    alert("Boton presionado"); 

}