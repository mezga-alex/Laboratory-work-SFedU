import { StatusBar } from 'expo-status-bar';
import React, { useState, useEffect } from 'react';
import { StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { FullView ,MyTabs, MyComponent } from './screens.js'


export default function App() {
  return (
      <FullView/>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});


// import React, { useState } from "react";
// import { ActionSheetIOS, Button, StyleSheet, Text, View } from "react-native";
//
// const App = () => {
//     const [result, setResult] = useState("🔮");
//
//     const onPress = () =>
//         ActionSheetIOS.showActionSheetWithOptions(
//             {
//                 options: ["Cancel", "Generate nusmber", "Reset"],
//                 destructiveButtonIndex: 2,
//                 cancelButtonIndex: 0
//             },
//             buttonIndex => {
//                 if (buttonIndex === 0) {
//                     // cancel action
//                 } else if (buttonIndex === 1) {
//                     setResult(Math.floor(Math.random() * 100) + 1);
//                 } else if (buttonIndex === 2) {
//                     setResult("🔮");
//                 }
//             }
//         );
//
//     return (
//         <View style={styles.container}>
//             <Text style={styles.result}>{result}</Text>
//             <Button onPress={onPress} title="Show Action Sheet" />
//         </View>
//     );
// };
//
// const styles = StyleSheet.create({
//     container: {
//         flex: 1,
//         justifyContent: "center"
//     },
//     result: {
//         fontSize: 64,
//         textAlign: "center"
//     }
// });
//
// export default App;
