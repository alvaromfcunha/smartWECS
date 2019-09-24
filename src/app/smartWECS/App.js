/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React from 'react';
import {
  StyleSheet,   
} from 'react-native';
import AwsIot from './AwsIot';
var DeviceEventEmitter = require('react-native').DeviceEventEmitter; 

class App extends React.Component {
  constructor(props) {
    super(props);
    AwsIot.init()
    .then((rtn)=>{
      AwsIot.connectAndSubscribe();
      console.log("SUCCESS", rtn); 
    }).catch((e)=>{
      console.log("Error", e); 
    });
  }

  componentDidMount(){
    DeviceEventEmitter.addListener("got-data", (json)=>{
      console.log("GOT DATA:",json);
    });
  }

  render(){
    return(
      null
    );
  }
}

const styles = StyleSheet.create({
  
});

export default App;
