import React from 'react'

const Describe = () => {
    return (
        <div>
            <h1>How DealPedia Works in the backend (W.I.P) </h1>
            <h3>Tech Stack</h3>
            <p className = "my-5">
                For the backend I used
                <ol className = "list-disc my-2">
                    <li>Scrappy : This helped me to extract the entire database from Eatigo's Singapore listed restaurants</li>
                    <li>Flask : I used this lightweight web framework that would allow me to get the data scrapped by my web crawlers</li>
                </ol>
            </p>
            <p className = 'my-5'>
                For the Frontend I used
                <ol className="list-disc my-2">
                    <li>React : This formed the main view framework I used to render my reusable components</li>
                    <li>React-Router : This allowed for more rapid transition between page views so that I was able to reduce load time for users </li>
                    <li>Redux : This was used to manage global state so that content can be pulled into individual components without relying on component state</li>
                    <li>Thunk : This was used to manage the asynchronous API call to the backend API</li>
                </ol>
            </p>
        </div>
    )
}

export default Describe;
