# Automatic Pet Feeder

A battery-powered automatic pet feeder using Arduino components. This project provides a reliable way to feed your pets on schedule without requiring internet connectivity.

## Features

- Runs on 2x AA batteries or a 9V or a 6V or a 4.5V
- No internet connectivity required
- LCD display for easy programming
- Up to 6 scheduled feeding times per day
- Simple interface
- EEPROM storage for saving schedules (persists through power loss)
- Servo-controlled food dispensing mechanism

## Required Components

### Electronics
- Arduino Nano
- SG90 Servo Motor
- 16x2 LCD Display
- 3x Push Buttons
- Battery holder for chosen batteries
- Voltage regulator
- Wires
- Breadboard or PCB for assembly
- USBC Charging Circuit (see other project)
- Rechargeable batteries

### Mechanical Parts
- Food container
- Servo mount
- Food dispensing mechanism
- Enclosure
- Mounting hardware

## Pin Connections

| Necessary component connections |
|-----------|
| Servo 
| LCD RS
| LCD EN
| LCD D4 
| LCD D5 
| LCD D6 
| LCD D7   
| Set Button
| Up Button 
| Down Button


## Usage Instructions

1. Power on the device using the battery pack
2. Set feeding times:
   - Press SET button to enter programming mode
   - Use UP/DOWN buttons to adjust time
   - Press SET to confirm each time
   - Can set up to 6 feeding times
3. The device will automatically dispense food at the programmed times

## Power Consumption

The device is designed for low power consumption:
- Sleep mode
- LCD backlight control
- Efficient servo usage
- Expected battery life: 2-3 months with normal use

## Safety Considerations

- Electronic atmospheric isolation
- Ensure proper ventilation
- Use food-safe materials for container
- Secure mounting to prevent tipping or tampering by pet

## Customization

Variables:
- Maximum feeds per day (MAX_DAILY_FEEDS constant)
- Servo movement parameters
- Display messages and timing

## License

This project is open-source and available under the MIT License.
