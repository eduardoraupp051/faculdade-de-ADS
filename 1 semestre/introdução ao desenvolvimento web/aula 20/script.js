
//selecionando o elemento pelo id
const meuTitulo = document.getElementById('titulo')
meuTitulo.innerText = 'dom' //alterando id
meuTitulo.style.color = 'green' //alterando a cor do texto
meuTitulo.innerHTML = "manipulando <br> o dom"

const paragrafos = document.getElementsByTagName('p')

//paragrafos[0].innerText = 'paragrafo 1'
//paragrafos[0].style.fontSize = '50px'

//iterando todos os paragrafos do html
//for(let i = 0; paragrafos.length; i++){
//  paragrafos[i].innerText = 'paragrafo' + (i + 1)
//}

const item = document.querySelector('li')
item.textContent = 'texto 1'
item.style.color = 'blue'

const items = document.querySelectorAll("li")
items[1].textContent = 'texto 2'
item[1].style.color = 'blue'

meuTitulo.innerHTML = "manipulando <br> o dom"

function alteraImagem (){
    const img = document.querySelector('img')
    img.src = 'js2.jpg'
}

function voltaImagem (){

    const img = document.querySelector("img")
    img.src = 'js1.png'
}

const link = document.querySelector('a')
link.innerText = 'google'
link.href = 'https://google.com'

const minhaHeader = document.querySelector('header')
minhaHeader.style.backgroundColor = 'black'
minha