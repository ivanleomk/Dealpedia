import {combineReducers} from 'redux';
import DealsReducers from './DealsReducers';

export default combineReducers({
    Deals: DealsReducers
})