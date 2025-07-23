// import React, { useState, useEffect } from 'react';
// import { StyleSheet, Text, View, Button, Dimensions ,Image} from 'react-native';
// import { StatusBar } from 'expo-status-bar';
// import snakeImg from './assets/snake.png';
// import foodImg from './assets/food.png';
// import {
//   GestureDetector,
//   Gesture,
// } from 'react-native-gesture-handler';


// import { Audio } from 'expo-av';





// const CELL_SIZE = 20;
// const GRID_SIZE = 20;
// const INITIAL_SNAKE = [{ x: 5, y: 5 }];
// const INITIAL_DIRECTION = { x: 1, y: 0 };

// export default function App() {
//   const [snake, setSnake] = useState(INITIAL_SNAKE);
//   const [direction, setDirection] = useState(INITIAL_DIRECTION);
//   const [food, setFood] = useState(randomFoodPosition());
//   const [isGameOver, setIsGameOver] = useState(false);
//   const [sound, setSound] = useState();
//   useEffect(() => {
//     const interval = setInterval(() => {
//       if (!isGameOver) moveSnake();
//     }, 500);


   


//     async function playEatSound() {
//   const { sound } = await Audio.Sound.createAsync(require('./assets/eat.mp3'));
//   setSound(sound);
//   await sound.playAsync();
// }

//  const gesture = Gesture.Pan()
//   .onUpdate((e) => {
//     const { translationX, translationY } = e;

//     if (Math.abs(translationX) > Math.abs(translationY)) {
//       if (translationX > 0) {
//         setDirection({ x: 1, y: 0 }); // Right
//       } else {
//         setDirection({ x: -1, y: 0 }); // Left
//       }
//     } else {
//       if (translationY > 0) {
//         setDirection({ x: 0, y: 1 }); // Down
//       } else {
//         setDirection({ x: 0, y: -1 }); // Up
//       }
//     }
//   })
//   .runOnJS(true);


//     return () => clearInterval(interval);
//   }, [snake, direction]);

//   function randomFoodPosition() {
//     return {
//       x: Math.floor(Math.random() * GRID_SIZE),
//       y: Math.floor(Math.random() * GRID_SIZE)
//     };
//   }

//   const moveSnake = () => {
//     const head = { ...snake[0] };
//     head.x += direction.x;
//     head.y += direction.y;

//     // Wall collision
//     if (head.x < 0 || head.x >= GRID_SIZE || head.y < 0 || head.y >= GRID_SIZE) {
//       setIsGameOver(true);
//       return;
//     }

//     // Self collision
//     for (let segment of snake) {
//       if (segment.x === head.x && segment.y === head.y) {
//         setIsGameOver(true);
//         return;
//       }
//     }

//     const newSnake = [head, ...snake];

//     // Eat food
//     if (head.x === food.x && head.y === food.y) {
//       playEatSound();
//       setFood(randomFoodPosition());
//     } else {
//       newSnake.pop(); // no growth
//     }

//     setSnake(newSnake);
//   };

//   return (
//     <View style={{ flex: 1, backgroundColor: '#000' }}>
//       <StatusBar style="light" />
//       <GestureDetector gesture={gesture}>



//       <View style={styles.gameArea}>
    
//  {snake.map((segment, index) => (
  
//   <Image
//     key={index}
//     source={snakeImg}
//     style={{
//       position: 'absolute',
//       width: CELL_SIZE,
//       height: CELL_SIZE,
//       left: segment.x * CELL_SIZE,
//       top: segment.y * CELL_SIZE,
//       resizeMode: 'contain',
//       transform: [{ rotate: index === 0 ? '0deg' : '0deg' }], // Optionally rotate the head
//     }}
//   />
// ))}
 
//  <Image
//       source={foodImg}
//       style={{
//         position: 'absolute',
//         width: CELL_SIZE,
//         height: CELL_SIZE,
//         left: food.x * CELL_SIZE,
//         top: food.y * CELL_SIZE,
//         resizeMode: 'contain',
//       }}
//     />

//         {isGameOver && (
//           <View style={styles.gameOver}>
//             <Text style={{ fontSize: 30, color: 'white' }}>Game Over</Text>
//           </View>
          
//         )}
//       </View>
//       </GestureDetector>

//       <View style={styles.controls}>
//         <Button title="Up" onPress={() => setDirection({ x: 0, y: -1 })} />
//         <Button title="Down" onPress={() => setDirection({ x: 0, y: 1 })} />
//         <Button title="Left" onPress={() => setDirection({ x: -1, y: 0 })} />
//         <Button title="Right" onPress={() => setDirection({ x: 1, y: 0 })} />
//       </View>
//     </View>

//   );
// }

// const styles = StyleSheet.create({
//   gameArea: {
//     width: GRID_SIZE * CELL_SIZE,
//     height: GRID_SIZE * CELL_SIZE,
//     backgroundColor: '#222',
//     position: 'relative',
//     alignSelf: 'center',
//     marginTop: 50
//   },
//   controls: {
//     flexDirection: 'row',
//     justifyContent: 'space-around',
//     marginTop: 30,
//     paddingHorizontal: 10
//   },
//   gameOver: {
//     position: 'absolute',
//     top: '40%',
//     left: 0,
//     right: 0,
//     alignItems: 'center',
//     backgroundColor: 'rgba(0,0,0,0.7)',
//     padding: 20,
//     borderRadius: 10
//   }
// });
import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Button, Image } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import snakeHeadImg from './assets/head.png';
import snakeBodyImg from './assets/body.png';
import snakeTailImg from './assets/tail.png';

import foodImg from './assets/food.png';
import { GestureDetector, Gesture } from 'react-native-gesture-handler';
import { Audio } from 'expo-av';

const CELL_SIZE = 20;
const GRID_SIZE = 20;
const INITIAL_SNAKE = [{ x: 5, y: 5 }];
const INITIAL_DIRECTION = { x: 1, y: 0 };

export default function App() {
  const [snake, setSnake] = useState(INITIAL_SNAKE);
  const [direction, setDirection] = useState(INITIAL_DIRECTION);
  const [food, setFood] = useState(randomFoodPosition());
  const [isGameOver, setIsGameOver] = useState(false);
  const [sound, setSound] = useState();

  useEffect(() => {
    const interval = setInterval(() => {
      if (!isGameOver) moveSnake();
    }, 300); // You can adjust speed

    return () => {
      clearInterval(interval);
      if (sound) {
        sound.unloadAsync(); // cleanup audio
      }
    };
  }, [snake, direction]);

  function randomFoodPosition() {
    return {
      x: Math.floor(Math.random() * GRID_SIZE),
      y: Math.floor(Math.random() * GRID_SIZE),
    };
  }

  const playEatSound = async () => {
    try {
      const { sound } = await Audio.Sound.createAsync(
        require('./assets/eat.mp3')
      );
      setSound(sound);
      await sound.playAsync();
    } catch (error) {
      console.log('Error playing sound:', error);
    }
  };

  const moveSnake = () => {
    const head = { ...snake[0] };
    head.x += direction.x;
    head.y += direction.y;
    const newHead = { x: head.x, y: head.y };

  const newSnake = [newHead, ...snake];
    // Wall collision
    if (head.x < 0 || head.x >= GRID_SIZE || head.y < 0 || head.y >= GRID_SIZE) {
      setIsGameOver(true);
      return;
    }

    // Self collision
    for (let segment of snake) {
      if (segment.x === head.x && segment.y === head.y) {
        setIsGameOver(true);
        return;
      }
    }

    // const newSnake = [head, ...snake];

    // Eat food
    if (head.x === food.x && head.y === food.y) {
      playEatSound();
      setFood(randomFoodPosition());
    } else {
      newSnake.pop(); // shrink if no food eaten
    }

    setSnake(newSnake);
  };

  // ✅ Gesture defined outside of useEffect
  const gesture = Gesture.Pan()
    .onUpdate((e) => {
      const { translationX, translationY } = e;
      if (Math.abs(translationX) > Math.abs(translationY)) {
        if (translationX > 0) {
          setDirection({ x: 1, y: 0 });
        } else {
          setDirection({ x: -1, y: 0 });
        }
      } else {
        if (translationY > 0) {
          setDirection({ x: 0, y: 1 });
        } else {
          setDirection({ x: 0, y: -1 });
        }
      }
    })
    .runOnJS(true);

  return (
    <View style={{ flex: 1, backgroundColor: '#000' }}>
      <StatusBar style="light" />
      <GestureDetector gesture={gesture}>
        <View style={styles.gameArea}>
          {snake.map((segment, index) => {
 let img = snakeBodyImg;
if (snake.length === 1) {
  img = snakeHeadImg; // just head
} else if (index === 0) {
  img = snakeHeadImg;
} else if (index === snake.length - 1) {
  img = snakeTailImg;
}


  return (
    <Image
      key={index}
      source={img}
      style={{
        position: 'absolute',
        width: CELL_SIZE,
        height: CELL_SIZE,
        left: segment.x * CELL_SIZE,
        top: segment.y * CELL_SIZE,
        resizeMode: 'contain',
      }}
    />
  );
})}

          <Image
            source={foodImg}
            style={{
              position: 'absolute',
              width: CELL_SIZE,
              height: CELL_SIZE,
              left: food.x * CELL_SIZE,
              top: food.y * CELL_SIZE,
              resizeMode: 'contain',
            }}
          />

          {isGameOver && (
            <View style={styles.gameOver}>
              <Text style={{ fontSize: 30, color: 'white' }}>Game Over</Text>
            </View>
          )}
        </View>
      </GestureDetector>

      <View style={styles.controls}>
        <Button title="Up" onPress={() => setDirection({ x: 0, y: -1 })} />
        <Button title="Down" onPress={() => setDirection({ x: 0, y: 1 })} />
        <Button title="Left" onPress={() => setDirection({ x: -1, y: 0 })} />
        <Button title="Right" onPress={() => setDirection({ x: 1, y: 0 })} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  gameArea: {
    width: GRID_SIZE * CELL_SIZE,
    height: GRID_SIZE * CELL_SIZE,
    backgroundColor: '#222',
    position: 'relative',
    alignSelf: 'center',
    marginTop: 50,
  },
  controls: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginTop: 30,
    paddingHorizontal: 10,
  },
  gameOver: {
    position: 'absolute',
    top: '40%',
    left: 0,
    right: 0,
    alignItems: 'center',
    backgroundColor: 'rgba(0,0,0,0.7)',
    padding: 20,
    borderRadius: 10,
  },
});
