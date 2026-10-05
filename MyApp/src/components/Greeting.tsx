import { StyleSheet, Text, useColorScheme } from 'react-native';

type GreetingProps = {
  message: string;
};

function Greeting({ message }: GreetingProps) {
  const isDarkMode = useColorScheme() === 'dark';

  return (
    <Text style={[styles.text, isDarkMode && styles.textDark]}>{message}</Text>
  );
}

const styles = StyleSheet.create({
  text: {
    fontSize: 32,
    fontWeight: '600',
    color: '#000000',
  },
  textDark: {
    color: '#ffffff',
  },
});

export default Greeting;
