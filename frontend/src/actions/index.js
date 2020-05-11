import deals from '../api/deals';

export const fetchDeals = () => async dispatch => {
    const response = await deals.get('/')
    dispatch({type:"FETCH_DEALS",payload: response})
}