import React from 'react';
import {
    ActionSheetIOS,
    StatusBar,
    Button,
    Image,
    StyleSheet,
    Text,
    View,
    TouchableOpacity,
    AsyncStorage
} from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import {NavigationContainer} from '@react-navigation/native';
import {createBottomTabNavigator} from '@react-navigation/bottom-tabs';
import {createStackNavigator} from '@react-navigation/stack';

import {MaterialCommunityIcons} from '@expo/vector-icons';
import {Alert} from "react-native-web";
import * as ImageManipulator from 'expo-image-manipulator';
import {SafeAreaProvider, SafeAreaView} from 'react-native-safe-area-context';
import uploadImage from './assets/upload-image.png';

// Function to save data in AsyncStorage
const _storeData = async (key, value) => {
    try {
        await AsyncStorage.setItem(key, value);
    } catch (error) {
        // Error saving data
        alert('Error while saving data');
    }
}

// Function to get data from AsyncStorage
const _retrieveData = async (key) => {
    try {
        const value = await AsyncStorage.getItem(key);
        if (value !== null) {
            // Our data is fetched successfully
            console.log('_retrieveData return result:');
            console.log(value);
            return value;
        } else {
            console.log('_retrieveData returns NULL:');
            return null;
        }
    } catch (error) {
        // Error retrieving data
        alert('Error while retrieving data')
    }
}

// Function to remove data from AsyncStorage
const _removeItemValue = async (key) => {
    try {
        await AsyncStorage.removeItem(key);
        return true;
    } catch (exception) {
        return false;
    }
}

class Home extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            imageURI: null,
            cameraIsVisible: false,
            cameraPermission: false,
            galleryPermission: false,
            archiveData: null
        }

        _retrieveData('archiveData')
            .catch(error => {
                alert('Error ' + error);
            }).then(response => {
            console.log('CONSTRUCTOR GOT: ')
            if (response !== null) {
                console.log(response);
                const parsedJSON = JSON.parse(response.toString())
                if (parsedJSON) {
                    this.setState({archiveData: parsedJSON})
                } else {
                    this.setState({archiveData: {}});
                }
            } else {
                console.log('Null, set: {}');
                this.setState({archiveData: {}})
            }
        })
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
            this.askPermission("camera");

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
            this.askPermission("gallery");

        ImagePicker.launchImageLibraryAsync({
            mediaTypes: ImagePicker.MediaTypeOptions.All,
            allowsEditing: true,
            base64: true,
            aspect: [4, 3],
            quality: 1,
        }).then(image => {
            if (!image.cancelled) {
                this.setState({imageURI: image.uri});
            }
        })
    }

    uploadImage = () => {
        alert('showActionSheetWithOptions');
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
                    this.openGallery();
                }
            }
        );
    }

    sendRequest = async () => {
        // alert('sendRequest')
        if (this.state.imageURI) {
            ImageManipulator.manipulateAsync(
                this.state.imageURI,
                [{resize: {width: 224, height: 224}}]
            ).then(response => {
                console.log("ImageManipulator.manipulateAsync: ");
                console.log(JSON.stringify(response));
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
                            alert("ERROR " + error);
                        })
                        .then(response => {
                            if (response) {
                                console.log('//////////////////////////////////////////////////');
                                console.log("NEW RESPONSE");
                                console.log('Response Image New: ' + (((new Date()).getTime() - start) / 1000).toString());
                                console.log(response);

                                // Get current archive
                                let curArchiveData = this.state.archiveData;
                                if (curArchiveData !== null) {
                                    console.log('Update storage');
                                    // Add image uri to Object
                                    response['image_uri'] = this.state.imageURI;
                                    const curID = Object.keys(curArchiveData).length;
                                    curArchiveData[curID] = response;

                                    // Save archive to AsyncStorage
                                    _storeData('archiveData', JSON.stringify(curArchiveData));
                                    this.setState({'archiveData': curArchiveData});
                                }
                            }
                        })
                }
            }).catch((error) => {
                    console.log("Error: " + error);
                }
            );

        }
    }
    resetValue = () => {
        // alert('resetValue');
        _removeItemValue('archiveData').then(response => {
            if (response) {
                console.log('REMOVED');
            } else {
                console.log('ERROR while remove');
            }
        })
    }

    printArchive = () => {
        // alert('printArchive')
        console.log('////////////////////////////////////////////////////////');
        console.log('this.state.archiveData:');
        console.log(this.state.archiveData);
        console.log('');

        _retrieveData('archiveData')
            .catch(error => {
                alert('Error retrieving data')
            }).then(response => {
            console.log('CURRENT _retrieveData');
            console.log(response);
            console.log('');
        })
    }

    render() {
        return (
            <SafeAreaView
                style={styles.safeAreaContainer}
            >
                <StatusBar barStyle="dark-content" backgroundColor="#ecf0f1"/>
                <View style={styles.imagePlaceContainer}>
                    <View style={styles.imagePlace}>
                        {!this.state.imageURI &&
                        <Image source={uploadImage} style={styles.imagePlaceholder} resizeMode='contain'/>}
                        {this.state.imageURI &&
                        <Image source={{uri: this.state.imageURI}} style={styles.imageUploaded} resizeMode='cover'/>}
                    </View>
                </View>
                <View style={styles.imagePlaceContainer}>
                    {this.state.imageURI &&
                    <TouchableOpacity
                        style={styles.buttonUpload}
                        onPress={this.sendRequest}
                    >
                        <Text style={styles.textButton}>Process photo</Text>
                    </TouchableOpacity>}
                </View>

                <View style={styles.imagePlaceContainer}>

                    <TouchableOpacity
                        style={styles.buttonUpload}
                        onPress={this.uploadImage}
                    >
                        <Text style={styles.textButton}>Select photo</Text>
                    </TouchableOpacity>
                </View>

                <View style={styles.imagePlaceContainer}>

                    {<TouchableOpacity
                        style={styles.buttonUpload}
                        onPress={this.printArchive}
                    >
                        <Text style={styles.textButton}>Print Archive</Text>
                    </TouchableOpacity>}
                </View>
                <View style={styles.imagePlaceContainer}>

                    {<TouchableOpacity
                        style={styles.buttonUpload}
                        onPress={this.resetValue}
                    >
                        <Text style={styles.textButton}>Remove value</Text>
                    </TouchableOpacity>}
                </View>
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
            galleryPermission: false,
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
                    <StatusBar barStyle="light-content" backgroundColor="#6a51ae"/>
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
        backgroundColor: '#fdfdfd',
        flex: 0.9,
        aspectRatio: 1,
        alignItems: 'center',
        justifyContent: 'center',
        borderRadius: 20,

        shadowColor: '#000000',
        shadowOffset: {width: 0, height: 1},
        shadowOpacity: 0.4,
        shadowRadius: 3,
        elevation: 3,

        marginBottom: 40
    },
    imagePlaceholder: {
        width: '80%',
    },
    imageUploaded: {
        width: "100%",
        height: "100%",
        borderRadius: 20,
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
    buttonUpload: {
        alignItems: "center",
        display: 'flex',
        flexDirection: 'row',
        flex: 0.8,
        height: 50,
        borderRadius: 5,
        justifyContent: 'center',
        alignContent: 'center',
        backgroundColor: '#2AC062',
        shadowColor: '#2AC062',
        shadowOpacity: 0.4,
        marginBottom: 15,
    },
    textButton: {
        fontSize: 16,
        textTransform: 'uppercase',
        color: '#FFFFFF'
    }
});
