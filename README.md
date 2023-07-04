# CodeAcademy

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Structures section
struct Race {
  int numberOfLaps;
  int currentLap;
  char *firstPlaceDriverName;
  char *firstPlaceRaceCarColor;
};

struct RaceCar {
  char *driverName;
  char *raceCarColor;
  int totalLapTime;
};

// Print functions section
void printIntro(){
  printf("Welcome to our main event digital race fans! I hope everybody has their snacks because we are about to begin!\n");
}
void printCountDown(){
  printf("Racers Ready! In...\n");
  printf("5\n");
  printf("4\n");
  printf("3\n");
  printf("2\n");
  printf("1\n");
  printf("Race!\n");
}
void printFirstPlaceAfterLap(struct Race race){
  printf("After %i laps, %s in the %s car is in the lead!\n", race.currentLap, race.firstPlaceDriverName, race.firstPlaceRaceCarColor);
}
void printCongratulations(struct Race race){

  printf("Let's all congratulate %s in the %s race car for  an amazing performance.\n", race.firstPlaceDriverName, race.firstPlaceRaceCarColor);
  printf("It truly was a great race, everybody have a goodnight!\n");
}
// Logic functions section
int calculateTimeToCompleteLap(){
  int speed = (rand() % 3) + 1;
  int acceleration = (rand() % 3) + 1;
  int nerves = (rand() % 3) + 1;

  return speed + acceleration + nerves;
}
void updateRaceCar(struct RaceCar* raceCar){
  raceCar->totalLapTime += calculateTimeToCompleteLap();
}
void updateFirstPlace(struct Race* race, struct RaceCar* raceCar1, struct RaceCar* raceCar2){
  if(raceCar1->totalLapTime <= raceCar2->totalLapTime){
    race->firstPlaceDriverName = raceCar1->driverName;
    race->firstPlaceRaceCarColor = raceCar1->raceCarColor;
  }
  else(raceCar2->totalLapTime < raceCar1->totalLapTime);{
    race->firstPlaceDriverName = raceCar2->driverName;
    race->firstPlaceRaceCarColor = raceCar2->raceCarColor;
  }
}
void startRace(struct RaceCar* raceCar1, struct RaceCar* raceCar2){
  struct Race race = {5, 1, "", ""};
  for (int i = 1; i <= race.numberOfLaps; i++){
    updateRaceCar(raceCar1);
    updateRaceCar(raceCar2);
    updateFirstPlace(&race, raceCar1, raceCar2);
    printFirstPlaceAfterLap(race);
    race.currentLap++;
  }
  printCongratulations(race);
}

int main() {

	srand(time(0));

  printIntro();
  printCountDown();

  struct RaceCar Car1 = {"Ian", "Silver", 0};
  struct RaceCar Car2 = {"Colm", "Blue", 0};

  startRace(&Car1, &Car2);

};
