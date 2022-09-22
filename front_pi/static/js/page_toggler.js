function setNavbarPageActive() {
    let path = window.location.pathname;

    if (path.includes('home')) {
        let link = window.document.getElementById('link-home')
        link.classList.add('active')
    }

    if (path.includes('clientes')) {
        if (path.includes('cadastro')){
            let link = window.document.getElementById('link-cadastrar-clientes')
            link.classList.add('active')
        } else {
            let link = window.document.getElementById('link-clientes')
            link.classList.add('active')
        }    
    }

    if (path.includes('produtos')) {
        if (path.includes('cadastro')){
            let link = window.document.getElementById('link-cadastrar-produtos')
            link.classList.add('active')
        } else {
            let link = window.document.getElementById('link-produtos')
            link.classList.add('active')
        }  
    }
}