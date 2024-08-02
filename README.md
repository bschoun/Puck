# Puck.js Experiments

A collection of some of my expirements with [Puck.js](https://www.espruino.com/Puck.js).

## Samples
### [accelerometer.html](https://bschoun.github.io/Puckjs/accelerometer.html)
Connects to a Puck, rotates a cube based on accelerometer and gyroscope data.

Still to do:
  - Could use magnetometer data, but the results seemed worse than just using the accelerometer and gyroscope. Worth exploring more.
  - Experiment with lower sample rates to improve battery life.
  - Display battery life, give warning when below 30% or so.

### [velocity.html](https://bschoun.github.io/Puckjs/velocity.html)
Connects to a Puck, moves a cube up/down based on the accelerometer Z data (Puck's up/down direction).
