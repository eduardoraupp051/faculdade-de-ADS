const tarefas = document.getElementById('task')




function adicionar(){
    const nomeTarefa = tarefas.value
    const li = document.createElement('li')
    li.innerText = nomeTarefa
    const ul = document.getElementById('pendentes')
    ul.appendChild(li)
}