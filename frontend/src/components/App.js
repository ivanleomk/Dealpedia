import React from 'react'

import Header from './Header';
import CardList from './CardList'
import Search from './Search'

import Describe from '../pages/Describe';

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from 'react-router-dom'


const App = () => {
    return (
        <Router>
            <Header />
                <div className = "flex flex-col items-center justify-center">
                <Switch>
                    <Route exact path = '/'>
                        <Search />
                        <CardList />
                    </Route>
                    <Route exact path = '/about'>
                        <Describe />
                    </Route>

                </Switch>
                </div>
        </Router>
            
    )
}

export default App;
