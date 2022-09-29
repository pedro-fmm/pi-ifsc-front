window.onload = function () {
    const input_telefone = document.getElementById("cliente-telefone");
    const input_cpf = document.getElementById("cliente-cpf");

    input_cpf.addEventListener("keyup", formatarCPF);
    input_telefone.addEventListener("keyup", formatarTelefone);

    function formatarTelefone(e){

        var v=e.target.value.replace(/\D/g,"");
        
        v=v.replace(/^(\d\d)(\d)/g,"($1) $2"); 
        
        v=v.replace(/(\d{5})(\d)/,"$1-$2");    
        
        e.target.value = v;
        
    }        

    function formatarCPF(e){

        var v=e.target.value.replace(/\D/g,"");
    
        v=v.replace(/(\d{3})(\d)/,"$1.$2");
    
        v=v.replace(/(\d{3})(\d)/,"$1.$2");
    
        v=v.replace(/(\d{3})(\d{1,2})$/,"$1-$2");
    
        e.target.value = v;
    
    } 
}