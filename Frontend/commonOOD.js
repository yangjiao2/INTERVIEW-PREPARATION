import Spaceship from './Spaceship.js';

class Astronaut {
  constructor() {
    this.spaceship = new Spaceship();
  }

  // I know what I want and I know how you do it
  goToSpaceNow() {
    if (this.spaceship.fuel < 10) {
      this.spaceship.refuel();
    }

    if (this.spaceship.flightReady) {
      this.spaceship.fly = true;
    } else (
      this.spaceship.preflightMusicCheck();
      this.spaceship.fly = true;
    )
  }
}


 class Astronaut {
      constructor() {
        this.spaceship = new Spaceship();
      }

      // I know what I want and I trust you to do your part
      // Notice the shrinking public API
      goToSpaceNow() {
        this.spaceship.fly({astronaut: this});
      }
    }
