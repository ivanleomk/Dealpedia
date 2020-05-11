import React from 'react'

const FormatTitle = (title) =>{
    let new_title = []
    for(let i = 0; i< title.length; i++){
        let result = title[i].match('[a-zA-Z]')
        if(result==null){
            new_title.push(title[i])
        }
        else{
            new_title.push(title[i].slice(0,result.index)+title[i][result.index].toUpperCase()+title[i].slice(result.index+1,title[i].length))
        }
    }
    return new_title.join(' ')
}

const FormatInformation = (information) => {
    if(information.length>=200){
        return information.slice(0,197)+'...'
    }
    return information
}

const Card = (props) => {
    const Title = FormatTitle(props.slug.split('/').slice(-1)[0].split('-').slice(0,-1))
    const Information = FormatInformation(props.information.information.bio)
    const post_link = `https://eatigo.com${props.slug}`
    
    
    return (
        <div class="max-w-sm rounded overflow-hidden shadow-lg p-10 flex flex-col items-stretch justify-start">
            
                <div class="font-bold text-xl mb-2">{Title}</div>
                <img class="w-full" src="/img/card-top.jpg" alt="Sunset in the mountains" />
                <br></br>
                <p class="text-gray-700 text-base">
                    {Information}
                </p>
                Address: {props.information.information.restaurant_address.address}
            
            <div className = "my-4">
                <span class="inline-block bg-gray-200 rounded-full m-2  text-sm font-semibold text-gray-700 mr-2">#photography</span>
                <span class="inline-block bg-gray-200 rounded-full m-2  text-sm font-semibold text-gray-700 mr-2">#travel</span>
                <span class="inline-block bg-gray-200 rounded-full m-2 text-sm font-semibold text-gray-700">#winter</span>
            </div>
            <p className="text-gray-700 text-base">
                
            </p>
            <button 
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 my-2 rounded-full outline-none"
            style = {{
                outline: "none"
            }}
            href = {post_link}
            >
            <a href = {post_link}>
            Redeem Deal</a>
            </button>
            
        </div>
    )
}

export default Card
