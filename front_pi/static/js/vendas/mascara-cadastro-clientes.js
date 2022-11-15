window.onload = function () 
{
    const input_cpf = document.getElementById("cpf");

    input_cpf.addEventListener("keyup", formatarCPF);

    function formatarCPF(e){

        var v=e.target.value.replace(/\D/g,"");
    
        v=v.replace(/(\d{3})(\d)/,"$1.$2");
    
        v=v.replace(/(\d{3})(\d)/,"$1.$2");
    
        v=v.replace(/(\d{3})(\d{1,2})$/,"$1-$2");
    
        e.target.value = v;
    
    } 
}