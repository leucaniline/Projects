/*
 * AutoPetFeeder.ino
 * An automated pet feeder using Arduino and servo motors
 * Powered by 2x AA batteries
 * No internet connectivity required
 */

#include <Servo.h>
#include <EEPROM.h>
#include <LiquidCrystal.h>

// Pin definitions
#define SERVO_PIN 9
#define BUTTON_SET 2
#define BUTTON_UP 3
#define BUTTON_DOWN 4
#define LCD_RS 12
#define LCD_EN 11
#define LCD_D4 5
#define LCD_D5 4
#define LCD_D6 3
#define LCD_D7 2

// Constants
#define FEED_AMOUNT 240        // Degrees to rotate for one portion
#define MAX_DAILY_FEEDS 6     // Maximum number of feeds per day
#define EEPROM_ADDR_START 0   // Starting address for EEPROM storage

// Global variables
Servo feedServo;
LiquidCrystal lcd(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7);
unsigned long lastFeedTime = 0;
int feedTimes[MAX_DAILY_FEEDS] = {-1};  // Store feeding times in minutes since midnight
int numberOfFeeds = 0;

void setup() {
  // Initialize servo
  feedServo.attach(SERVO_PIN);
  feedServo.write(0);  // Initial position
  
  // Initialize LCD
  lcd.begin(16, 2);
  lcd.print("Pet Feeder Ready");
  
  // Initialize buttons
  pinMode(BUTTON_SET, INPUT_PULLUP);
  pinMode(BUTTON_UP, INPUT_PULLUP);
  pinMode(BUTTON_DOWN, INPUT_PULLUP);
  
  // Load saved feeding schedule from EEPROM
  loadSchedule();
}

void loop() {
  // Check buttons for user input
  checkButtons();
  
  // Check if it's time to feed
  checkFeedingSchedule();
  
  // Update display
  updateDisplay();
  
  delay(100);  // Small delay to prevent excessive CPU usage
}

void checkButtons() {
  static bool setPressed = false;
  static bool upPressed = false;
  static bool downPressed = false;
  static bool inMenu = false;
  static int menuPosition = 0;
  static int tempHour = 0;
  static int tempMinute = 0;
  
  // Check SET button
  if (!digitalRead(BUTTON_SET) && !setPressed) {
    setPressed = true;
    if (!inMenu) {
      inMenu = true;
      menuPosition = 0;
      lcd.clear();
      lcd.print("Set Feed Time");
    } else {
      // Save current time setting
      if (numberOfFeeds < MAX_DAILY_FEEDS) {
        feedTimes[numberOfFeeds] = tempHour * 60 + tempMinute;
        numberOfFeeds++;
        saveSchedule();
      }
      inMenu = false;
      lcd.clear();
    }
    delay(50);  // Debounce
  }
  setPressed = !digitalRead(BUTTON_SET);
  
  // In menu mode
  if (inMenu) {
    // UP button
    if (!digitalRead(BUTTON_UP) && !upPressed) {
      upPressed = true;
      if (menuPosition == 0) {
        tempHour = (tempHour + 1) % 24;
      } else {
        tempMinute = (tempMinute + 1) % 60;
      }
      delay(50);  // Debounce
    }
    upPressed = !digitalRead(BUTTON_UP);
    
    // DOWN button
    if (!digitalRead(BUTTON_DOWN) && !downPressed) {
      downPressed = true;
      if (menuPosition == 0) {
        tempHour = (tempHour - 1 + 24) % 24;
      } else {
        tempMinute = (tempMinute - 1 + 60) % 60;
      }
      delay(50);  // Debounce
    }
    downPressed = !digitalRead(BUTTON_DOWN);
  }
}

void checkFeedingSchedule() {
  // Get current time in minutes since midnight
  int currentMinutes = (millis() / 60000) % 1440;  // 24 hours = 1440 minutes
  
  // Check each feeding time
  for (int i = 0; i < numberOfFeeds; i++) {
    if (feedTimes[i] == currentMinutes) {
      dispenseFeed();
      break;
    }
  }
}

void updateDisplay() {
  static unsigned long lastUpdate = 0;
  static bool showColon = true;
  
  // Update display every 500ms
  if (millis() - lastUpdate >= 500) {
    lastUpdate = millis();
    showColon = !showColon;
    
    lcd.clear();
    int currentMinutes = (millis() / 60000) % 1440;
    int hours = currentMinutes / 60;
    int minutes = currentMinutes % 60;
    
    // First line: Current time
    lcd.setCursor(0, 0);
    if (hours < 10) lcd.print("0");
    lcd.print(hours);
    lcd.print(showColon ? ":" : " ");
    if (minutes < 10) lcd.print("0");
    lcd.print(minutes);
    
    // Second line: Next feed time or menu
    lcd.setCursor(0, 1);
    if (!inMenu) {
      lcd.print("Next: ");
      int nextFeed = -1;
      for (int i = 0; i < numberOfFeeds; i++) {
        if (feedTimes[i] > currentMinutes) {
          nextFeed = feedTimes[i];
          break;
        }
      }
      if (nextFeed != -1) {
        int nextHours = nextFeed / 60;
        int nextMinutes = nextFeed % 60;
        if (nextHours < 10) lcd.print("0");
        lcd.print(nextHours);
        lcd.print(":");
        if (nextMinutes < 10) lcd.print("0");
        lcd.print(nextMinutes);
      } else {
        lcd.print("--:--");
      }
    }
  }
}

void dispenseFeed() {
  feedServo.write(FEED_AMOUNT);
  delay(1000);
  feedServo.write(0);
  lastFeedTime = millis();
  
  // Display feeding confirmation
  lcd.clear();
  lcd.print("Feeding...");
  delay(2000);
}

void loadSchedule() {
  numberOfFeeds = EEPROM.read(EEPROM_ADDR_START);
  if (numberOfFeeds > MAX_DAILY_FEEDS) {
    numberOfFeeds = 0;  // Invalid data in EEPROM
    return;
  }
  
  for (int i = 0; i < numberOfFeeds; i++) {
    int addr = EEPROM_ADDR_START + 1 + (i * 2);
    feedTimes[i] = (EEPROM.read(addr) << 8) | EEPROM.read(addr + 1);
  }
}

void saveSchedule() {
  EEPROM.write(EEPROM_ADDR_START, numberOfFeeds);
  for (int i = 0; i < numberOfFeeds; i++) {
    int addr = EEPROM_ADDR_START + 1 + (i * 2);
    EEPROM.write(addr, feedTimes[i] >> 8);
    EEPROM.write(addr + 1, feedTimes[i] & 0xFF);
  }
}