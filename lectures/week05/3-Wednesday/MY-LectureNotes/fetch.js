
const ourFetch = (url) => {

    let promise = new Promise((resolve, reject)=>{

        let xhr = new XMLHttpRequest();

        xhr.open('GET', url) //GET, url

        xhr.send()

        xhr.onreadystatechange = ()=>{ //similar to event listener

            if(xhr.readyState == 4 && xhr.status == 200){
                let data = JSON.parse(xhr.responseText)
                console.log(data);
                resolve(data)
            }
            else{
                reject('error in data')
            }
        }
    })

    return promise;
}

window.ourFetch = ourFetch