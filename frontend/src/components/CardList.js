import React, { Component } from 'react'
import Card from './Card'

import {connect} from 'react-redux';
import {fetchDeals} from '../actions'


class CardList extends Component {
    
    componentDidMount(){
        this.props.fetchDeals()
    }
    render() {
        if(this.props.deals.data){
            console.log(Object.keys(this.props.deals.data).slice(0,3))
            console.log(this.props.deals.data)
        }
        return (
            <div className="grid grid-cols-3 gap-4 p-6">
            {this.props.deals.data && Object.keys(this.props.deals.data).slice(0,3).map((item)=>
                <Card slug = {item} information = {this.props.deals.data[item]} />
            )}
            </div>
        )
    }
}

const mapStateToProps = state =>{
    return {
        deals: state.Deals
    }
}

export default connect(mapStateToProps,{
    fetchDeals
})(CardList);
