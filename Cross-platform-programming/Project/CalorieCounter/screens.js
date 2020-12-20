import React from 'react';
import {ActionSheetIOS, StatusBar, Button, Image, StyleSheet, Text, View, TouchableOpacity} from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import {NavigationContainer} from '@react-navigation/native';
import {createBottomTabNavigator} from '@react-navigation/bottom-tabs';
import {createStackNavigator} from '@react-navigation/stack';

import {MaterialCommunityIcons} from '@expo/vector-icons';
import {Alert} from "react-native-web";
import * as ImageManipulator from 'expo-image-manipulator';
import {SafeAreaProvider, SafeAreaView} from 'react-native-safe-area-context';
import uploadImage from './assets/upload-image.png';

class Home extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            imageURI: null,
            cameraIsVisible: false,
            cameraPermission: false,
            galleryPermission: false
        }
    }

    askPermission = (type) => {
        if (type === "camera") {
            ImagePicker.requestCameraPermissionsAsync().then(permissionResult => {
                if (permissionResult.granted === false) {
                    alert("Permission to access camera roll is required!");
                } else {
                    this.setState({cameraPermission: true});
                }
            })
        } else if (type === "gallery") {
            ImagePicker.requestMediaLibraryPermissionsAsync().then(permissionResult => {
                if (permissionResult.granted === false) {
                    alert("Permission to access camera roll is required!");
                } else {
                    this.setState({galleryPermission: true});
                }
            })
        }
    };

    openCamera = () => {
        if (this.state.cameraPermission === false)
            this.askPermission("camera")

        ImagePicker.launchCameraAsync({
            allowsEditing: true,
            quality: 1,
            base64: true,
            exif: false,
            doNotSave: true
        }).then(image => {
            if (!image.cancelled) {
                this.setState({imageURI: image.uri});
            }
        })
    }


    openGallery = () => {
        if (this.state.galleryPermission === false)
            this.askPermission("gallery")

        ImagePicker.launchImageLibraryAsync({
            mediaTypes: ImagePicker.MediaTypeOptions.All,
            allowsEditing: true,
            base64: true,
            aspect: [4, 3],
            quality: 1,
        }).then(image => {
            if (!image.cancelled) {
                this.setState({imageURI: image.uri})
            }
        })
    }

    onPress = () => {
        ActionSheetIOS.showActionSheetWithOptions(
            {
                options: ["Cancel", "Take photo", "Choose from gallery"],
                cancelButtonIndex: 0
            },
            buttonIndex => {
                if (buttonIndex === 0) {
                    // cancel action
                } else if (buttonIndex === 1) {
                    this.openCamera();
                } else if (buttonIndex === 2) {
                    this.openGallery()
                }
            }
        );
    }

    sendRequest = async () => {
        if (this.state.imageURI) {
            ImageManipulator.manipulateAsync(
                this.state.imageURI,
                [{resize: {width: 224, height: 224}}]
            ).then(response => {
                console.log("ImageManipulator.manipulateAsync: ");
                console.log(JSON.stringify(response))
                const resizedImageURI = response.uri;

                if (resizedImageURI) {
                    let start = (new Date()).getTime();
                    let url = "https://dfd00a2ac464.ngrok.io/analyse"
                    let uploadData = new FormData();
                    uploadData.append('submit', 'ok');
                    uploadData.append('file', {
                        uri: resizedImageURI,
                        type: 'image/jpeg',
                        name: 'photo.jpg',
                    })
                    fetch(url, {
                        method: 'post',
                        body: uploadData
                    }).then(response => response.json())
                        .catch((error) => {
                            alert("ERROR " + error)
                        })
                        .then(response => {
                            console.log('//////////////////////////////////////////////////')
                            console.log("NEW RESPONSE")
                            console.log('Response Image New: ' + (((new Date()).getTime() - start) / 1000).toString())
                            console.log(response)
                            console.log('//////////////////////////////////////////////////')
                        })
                }
            }).catch((error) => {
                    console.log("Error: " + error);
                }
            );

        }
    }


    render() {
        return (
            <SafeAreaView
                style={styles.safeAreaContainer}
            >
                <StatusBar barStyle="dark-content" backgroundColor="#ecf0f1" />
                <View style={styles.imagePlaceContainer}>
                    <View style={[
                        styles.imagePlace,
                        !this.state.imageURI && styles.imagePlaceEmpty
                    ]}>
                        {!this.state.imageURI && <Image source={ uploadImage } style={styles.imagePlaceholder} resizeMode='contain'/>}
                        {this.state.imageURI && <Image source={{uri: this.state.imageURI}} style={styles.imageUploaded} resizeMode='cover'/>}
                    </View>
                </View>
                <TouchableOpacity
                    style={styles.button}
                    onPress={this.onPress}
                >
                    <Text>Select photo</Text>
                </TouchableOpacity>

                {/*<Button onPress={this.onPress} title="Select photo"/>*/}

                {this.state.imageURI && <Button onPress={this.sendRequest} title="Send image"/>}
            </SafeAreaView>
        );
    }

}

class History extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            image: null,
            cameraIsVisible: false,
            cameraPermission: false,
            galleryPermission: false
        }
    }

    render() {
        return (
            <SafeAreaView
                style={styles.safeAreaContainer}
            >
                <Image source={uploadImage} style={{width: 50, height: 50}}/>
                <Text>There will be a list</Text>
            </SafeAreaView>
        );
    }
}


const Stack = createStackNavigator();
const Tab = createBottomTabNavigator();

export class FullView extends React.Component {
    render() {
        return (
            <SafeAreaProvider>
                <NavigationContainer>
                    <StatusBar barStyle="light-content" backgroundColor="#6a51ae" />
                    <Stack.Navigator initialRouteName="Home">
                        <Stack.Screen name="Calorie Counter">
                            {() => (
                                <Tab.Navigator
                                    initialRouteName="Home"
                                    tabBarOptions={{
                                        activeTintColor: '#6C63FF'
                                    }}
                                >
                                    <Tab.Screen
                                        name="Home"
                                        component={Home}
                                        options={{
                                            tabBarLabel: 'Home',
                                            tabBarIcon: ({color, size}) => (
                                                <MaterialCommunityIcons name="home" color={color} size={34}/>
                                            ),
                                        }}
                                    />
                                    <Tab.Screen
                                        name="History"
                                        component={History}
                                        options={{
                                            tabBarLabel: 'History',
                                            tabBarIcon: ({color, size}) => (
                                                <MaterialCommunityIcons name="history" color={color} size={34}/>
                                            ),
                                            tabBarBadge: 3
                                        }}
                                    />
                                </Tab.Navigator>
                            )}
                        </Stack.Screen>

                    </Stack.Navigator>
                </NavigationContainer>
            </SafeAreaProvider>
        );
    }
}

const styles = StyleSheet.create({
    safeAreaContainer: {
        display: 'flex',
        flex: 1,
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'flex-start',
        backgroundColor: 'white'

    },
    imagePlaceContainer: {
        display: 'flex',
        flexDirection: 'row',
    },
    imagePlace: {
        backgroundColor: '#f1f1f1',
        flex: 0.9,
        aspectRatio: 1,
        alignItems: 'center',
        justifyContent: 'center',
        borderRadius: 20,

    },
    imagePlaceEmpty: {
        borderColor: '#8d8d8d',
        borderWidth: 4,
        borderStyle: 'dashed',
    },
    imagePlaceholder: {
        width: '80%',
    },
    imageUploaded: {
        width:"100%",
        height: "100%",
        borderRadius: 20,
        borderWidth: 4,
        borderColor: '#6C63FF',
    },
    top: {
        flex: 0.3,
        backgroundColor: "grey",
        borderWidth: 5,
        borderTopLeftRadius: 20,
        borderTopRightRadius: 20,
    },
    middle: {
        flex: 0.3,
        backgroundColor: "beige",
        borderWidth: 5,
    },
    button: {
        alignItems: "center",
        backgroundColor: "#DDDDDD",
        padding: 10
    },
});
