export default (state = [], actions) => {
    switch(actions.type){
        case "FETCH_DEALS":
            return actions.payload;
        default:
            return state
    }
}