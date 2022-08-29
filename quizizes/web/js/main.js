eel.question()((qns) => {
    document.querySelector('.theqns').innerHTML = qns[0]

    const list = qns[1]
    const buttons = document.querySelectorAll('.ans')


buttons.forEach((button, i )=> {
    console.log(i)
    button.innerHTML = list[i]
    
})
})

eel.increaseIndex()((i) => {
    document.querySelector('.btn').addEventListener('click', (e) => {
        console.log(i)
    })
})




console.log(buttons.entries())