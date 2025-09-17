const serverURL = 'http://127.0.0.1:5000/'

async function getData(url) {
    let response = await fetch(url);
    let data = await response.json();
    console.log('- data -', data)

    return data
}

let data = await getData(serverURL)
let output = document.querySelector('.output');

output.innerHTML = data.title;