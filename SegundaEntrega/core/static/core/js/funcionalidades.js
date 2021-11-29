function confirmDelete(id){
    Swal.fire({
        icon: 'warning',
        title: '¿Estás seguro?',
        text: 'Luego no podrás deshacer la acción',
        showCancelButton: true,
        cancelButtonColor: "#d33",
        confirmButtonText: "Sí, Eliminar",
        cancelButtonText: "Cancelar",   
    }).then((result)=>{
        if (result.value){
            Swal.fire(
                '¡Eliminando!',
                'Insumo eliminado correctamente',
                'success'
            ).then(function(){
                window.location.href= "/eliminar_insumos/"+id+"/";
            })
        }
    })
}