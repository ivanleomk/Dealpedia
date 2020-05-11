import React from 'react'

const Search = () => {
    return (
        <div className = "relative text-gray-600">
            <input 
                type = "search" 
                name = "search" 
                placeholder = "Search For Deals Today!" 
                className = "rounded-full py-2 px-4 border-2 border-gray-400 outline-none"
                style = {{
                    width: "50vw",
                    padding: "20px 40px",
                    margin:"35px 0"
                }}
            />
            
            <button>
            <i class="fa fa-search"></i>
            </button>
        </div>
    )
}
// style = {{
//     borderRadius: "25px",
//     border: "2px solid #609",
//     padding: "20px",
//     width: "50vw",
//     height: "15px"
// }}

export default Search;

// <div>className = 'bg-white rounded-full py-2 px-4 text-center  text-sm focus:outline' 
//             <div class="relative text-gray-600">
//             <input type="search" name="search" placeholder="Search" class="bg-white h-10 px-5 pr-10 rounded-full text-sm focus:outline-none" />
//                 <button type="submit" class="absolute right-0 top-0 mt-3 mr-4">
//                     <svg class="fill-current">
//                     <path d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z"/>
//                     </svg>
//                 </button>
//             </div>
//         </div>