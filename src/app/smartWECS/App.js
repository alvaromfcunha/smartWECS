/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React from 'react';
import {
  View,
  Text,
  Image
 } from 'react-native';

 import {Header} from 'react-native-elements';
 import {Card} from 'react-native-shadow-cards';


import AwsIot from './AwsIot';
var DeviceEventEmitter = require('react-native').DeviceEventEmitter; 

export default class App extends React.Component {

  constructor(props) {
    super(props);
    AwsIot.init()
    .then((rtn)=>{
      AwsIot.connectAndSubscribe()
      .then((rtn)=>{
        console.log("SUCCESS SUB", rtn); 
      })
      .catch((e)=>{
        console.log("Error sub BUT WORKS????", e);
      })
      console.log("SUCCESS CON", rtn); 
    }).catch((e)=>{
      console.log("Error con", e); 
    });
    this.state = {
      json : undefined
    };
  }

  componentDidMount(){
    DeviceEventEmitter.addListener("got-data", (jsonStr)=>{
      console.log("GOT DATA:",jsonStr);
      this.setState({
        json : JSON.parse(jsonStr['value'])
      })
      //console.log("GOT JSON:",json);
    });
  }

  render() {

    

    if (this.state.json !== undefined){
      return(
        <View style={{flex: 1, flexDirection: 'column'}}>

          <Header
            backgroundColor="#1F6FB2"
            statusBarProps={{ backgroundColor:'#1F6FB2'}}
            centerComponent={<Text style={{fontWeight: "bold", color: '#fff', fontSize: 25, fontFamily: 'Helvetica'}}>SmartWECS</Text>}
          />

          <Card style={{padding: 20, margin: 20, backgroundColor: '#B8D0E5', flexDirection: 'row', justifyContent: 'space-between'}}>
            <Image source={require('./icons/t.png')} style={{width: 150, height: 150}}/>
            <View
              style={{
              borderLeftWidth: 1,
              borderLeftColor: 'black',
              marginLeft: 5,
              marginRight: 15
              }}
            />
            <View style={{flex: 1, flexDirection: 'column', justifyContent: 'space-around', alignContent: 'center'}}>
              <Text style={{fontWeight: "normal", fontSize: 25}}>
                Consumo: {this.state.json["electricity"].toFixed(2)} kWh
              </Text>
              <Text style={{fontWeight: "normal", fontSize: 25}}>
              Tarifa: {this.state.json['money']["electricity"].toFixed(2)} R$
              </Text>
            </View>
          </Card>
          

          <Card style={{padding: 20, margin: 20, backgroundColor: '#B8D0E5', flexDirection: 'row', justifyContent: 'space-between'}}>
            <Image source={require('./icons/w.png')} style={{width: 150, height: 150}}/>
            <View
              style={{
              borderLeftWidth: 1,
              borderLeftColor: 'black',
              marginLeft: 5,
              marginRight: 15
              }}
            />
            <View style={{flex: 1, flexDirection: 'column', justifyContent: 'space-around', alignContent: 'center'}}>
              <Text style={{fontWeight: "normal", fontSize: 25}}>
                Consumo: {this.state.json["water"].toFixed(2)} m3
              </Text>
              <Text style={{fontWeight: "normal", fontSize: 25}}>
              Tarifa: {this.state.json['money']["water"].toFixed(2)} R$
              </Text>
            </View>
          </Card>

          {/* <View style={{flex: 1, flexDirection: 'column'}}>

            <Card style={{padding: 150, margin: 20, alignContent: 'center', backgroundColor: '#B8D0E5'}}>
                <View style={{flex: 1, flexDirection: 'row', justifyContent: 'space-evenly'}}>
                  <View>
                    <Image source={require('./icons/t.png')} />
                  </View>
                  <View>
                    <Text style={{fontWeight: "normal", fontSize: 25}}>
                      Consumo: {this.state.json["electricity"]}kWh
                    </Text>
                    <Text style={{fontWeight: "normal", fontSize: 25}}>
                    Tarifa: {this.state.json['money']["electricity"]}R$
                    </Text>
                  </View>
                </View> 
            </Card>
            <Card style={{padding: 50, margin: 20, alignContent: 'center', backgroundColor: '#B8D0E5'}}>

              <Text style={{fontWeight: "normal", fontSize: 25}}>
                Consumo de Agua: {this.state.json["water"]}
              </Text>
              <Text style={{fontWeight: "normal", fontSize: 25}}>
                Conta de Agua: {this.state.json['money']["water"]}
              </Text>

            </Card>
          </View> 
          */}
        </View> 
      )
    } else {
      return(
        <View>
          <Header
            backgroundColor="#1F6FB2"
            statusBarProps={{ backgroundColor:'#1F6FB2'}}
            centerComponent={<Text style={{fontWeight: "bold", color: '#fff', fontSize: 25, fontFamily: 'Helvetica'}}>SmartWECS</Text>}
          />
          <View style={{alignContent: 'center'}}>
            <Card style={{padding: 50, margin: 20, alignContent: 'center', backgroundColor: '#B8D0E5'}}>
              <Text style={{fontWeight: "normal", fontSize: 25}}>Carregando...</Text>
            </Card>
          </View>
        </View>
      )
    }
  }
}