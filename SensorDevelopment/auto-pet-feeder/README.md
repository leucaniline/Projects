# Automatic Pet Feeder

A battery-powered automatic pet feeder using Arduino components. This project provides a reliable way to feed your pets on schedule without requiring internet connectivity.

## Features

- Runs on 2x AA batteries
- No internet connectivity required
- LCD display for easy programming
- Up to 6 scheduled feeding times per day
- Simple 3-button interface
- EEPROM storage for saving schedules (persists through power loss)
- Servo-controlled food dispensing mechanism

## Required Components

### Electronics
- Arduino Nano/Uno (recommended for low power consumption)
- SG90 Servo Motor
- 16x2 LCD Display
- 3x Push Buttons
- Battery holder for 2x AA batteries
- Voltage regulator (if using Arduino Uno)
- Jumper wires
- Breadboard or PCB for final assembly

### Mechanical Parts
- Food container (recommended volume: 2L)
- Servo mount (3D printed or constructed)
- Food dispensing mechanism (3D printed or constructed)
- Project enclosure
- Mounting hardware (screws, nuts, etc.)

## Pin Connections

| Component | Arduino Pin |
|-----------|------------|
| Servo     | D9         |
| LCD RS    | D12        |
| LCD EN    | D11        |
| LCD D4    | D5         |
| LCD D5    | D4         |
| LCD D6    | D3         |
| LCD D7    | D2         |
| Set Button| D2         |
| Up Button | D3         |
| Down Button| D4        |

## Assembly Instructions

1. **Prepare the Container**
   - Create an opening for the food dispensing mechanism
   - Mount the servo motor securely
   - Attach the dispensing mechanism to the servo

2. **Electronics Assembly**
   - Connect all components according to the pin connection table
   - Mount the LCD display in an accessible viewing position
   - Install buttons in an ergonomic position
   - Secure battery holder and ensure proper connection

3. **Programming**
   - Upload the provided Arduino code
   - Test all buttons and the display
   - Verify servo movement

## Usage Instructions

1. Power on the device using the battery pack
2. The LCD will display "Pet Feeder Ready"
3. To set feeding times:
   - Press SET button to enter programming mode
   - Use UP/DOWN buttons to adjust time
   - Press SET to confirm each time
   - Can set up to 6 feeding times
4. The device will automatically dispense food at the programmed times

## Power Consumption

The device is designed for low power consumption:
- Sleep mode between feeds
- LCD backlight control
- Efficient servo usage
- Expected battery life: 2-3 months with normal use

## Maintenance

- Replace batteries when LCD display becomes dim
- Clean the food container and dispensing mechanism monthly
- Check for any food blockages regularly
- Verify the servo mechanism moves freely

## Troubleshooting

1. **Display not working**
   - Check battery voltage
   - Verify LCD connections

2. **Servo not moving**
   - Check servo connections
   - Ensure no food is blocking the mechanism
   - Verify power supply is adequate

3. **Schedule not saving**
   - Reset Arduino
   - Check if EEPROM is working properly

## Safety Considerations

- Keep electronics away from moisture
- Ensure proper ventilation
- Use food-safe materials for container
- Secure mounting to prevent tipping

## Customization

The code can be modified to adjust:
- Feed portion size (FEED_AMOUNT constant)
- Maximum feeds per day (MAX_DAILY_FEEDS constant)
- Servo movement parameters
- Display messages and timing

## License

This project is open-source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests!