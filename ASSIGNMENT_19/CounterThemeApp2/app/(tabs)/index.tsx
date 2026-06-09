import React, { useState } from 'react';
import {
  SafeAreaView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
  StatusBar,
} from 'react-native';

export default function App() {
  const [count, setCount] = useState(0);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const handleIncrement = () => {
    setCount(count + 1);
  };

  const handleDecrement = () => {
    if (count > 0) {
      setCount(count - 1);
    }
  };

  const handleReset = () => {
    setCount(0);
  };

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };

  return (
    <SafeAreaView
      style={[
        styles.container,
        {
          backgroundColor: isDarkMode ? '#121212' : '#F5F5F5',
        },
      ]}
    >
      <StatusBar
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}
      />

      <Text
        style={[
          styles.heading,
          {
            color: isDarkMode ? '#FFFFFF' : '#000000',
          },
        ]}
      >
        Counter App
      </Text>

      <Text
        style={[
          styles.counterText,
          {
            color: isDarkMode ? '#00E5FF' : '#1E3A8A',
          },
        ]}
      >
        {count}
      </Text>

      <View style={styles.buttonRow}>
        <TouchableOpacity
          style={[styles.button, styles.incrementButton]}
          onPress={handleIncrement}
        >
          <Text style={styles.buttonText}>Increment</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.button, styles.decrementButton]}
          onPress={handleDecrement}
        >
          <Text style={styles.buttonText}>Decrement</Text>
        </TouchableOpacity>
      </View>

      <TouchableOpacity
        style={[styles.button, styles.resetButton]}
        onPress={handleReset}
      >
        <Text style={styles.buttonText}>Reset</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={[styles.button, styles.themeButton]}
        onPress={toggleTheme}
      >
        <Text style={styles.buttonText}>
          {isDarkMode
            ? 'Switch to Light Mode'
            : 'Switch to Dark Mode'}
        </Text>
      </TouchableOpacity>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },

  heading: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 30,
  },

  counterText: {
    fontSize: 72,
    fontWeight: 'bold',
    marginBottom: 40,
  },

  buttonRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '100%',
    marginBottom: 20,
  },

  button: {
    paddingVertical: 15,
    paddingHorizontal: 20,
    borderRadius: 12,
    marginHorizontal: 5,
    alignItems: 'center',
  },

  incrementButton: {
    backgroundColor: '#22C55E',
    flex: 1,
  },

  decrementButton: {
    backgroundColor: '#EF4444',
    flex: 1,
  },

  resetButton: {
    backgroundColor: '#F59E0B',
    width: '100%',
    marginBottom: 20,
  },

  themeButton: {
    backgroundColor: '#6366F1',
    width: '100%',
  },

  buttonText: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
});