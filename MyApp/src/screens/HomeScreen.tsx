import { StyleSheet, useColorScheme, View } from 'react-native';
import Greeting from '../components/Greeting';

function HomeScreen() {
  const isDarkMode = useColorScheme() === 'dark';

  return (
    <View style={[styles.container, isDarkMode && styles.containerDark]}>
      <Greeting message="Hello World" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#ffffff',
  },
  containerDark: {
    backgroundColor: '#000000',
  },
});

export default HomeScreen;
