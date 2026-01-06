# Hardware Documentation

## Component List

1. **Microcontroller**
   - Arduino Nano 
   - Operating voltage: 5V
   - Power consumption: ~15mA (normal operation), ~5mA (sleep mode)

2. **Power Supply**
   - 2x 1.5V AA Batteries 
   - Total voltage: 3V
   - Capacity: ~2000-2500mAh (typical alkaline)
   - Expected battery life: 2-3 months with normal use
   
3. **Servo Motor**
   - Model: SG90 or equivalent
   - Operating voltage: 4.8-6V (~5V)
   - Current draw: ~100mA (during operation)
   - Torque: 1.8 kg/cm
   - Rotation: 180 degrees
   
4. **LCD Display**
   - Type: 16x2 character LCD
   - Operating voltage: 5V
   - Current draw: ~20mA (without backlight)
   
5. **Buttons**
   - 3x push buttons
   - Operating voltage: 5V
   - Current: negligible (using internal pull-up)

## Power Management

### Battery Configuration
```
2x AA (3V) --> 5V Step-Up Converter --> System
```

### Power Consumption Analysis
1. **Idle State**
   - Arduino (sleep mode): 5mA
   - LCD (active): 20mA
   - Total: ~25mA

2. **During Feed**
   - Arduino (active): 15mA
   - LCD (active): 20mA
   - Servo (active): 100mA
   - Total: ~135mA for ~2 seconds

### Battery Life Calculation
- Average consumption: ~30mA
- Battery capacity: 2000mAh
- Theoretical life: 66.67 hours continuous
- With sleep modes and intermittent servo use:
  - Estimated 2-3 months of normal operation

## Mechanical Specifications

### Food Container
- Volume: 2L
- Material: Food-safe plastic (HDPE or PET)
- Opening: 80mm diameter minimum

### Servo Mounting
- Mount angle: 45 degrees from vertical
- Clearance: 30mm minimum from container bottom
- Support structure: 3mm thick minimum

### Dispensing Mechanism
- Type: Rotating paddle wheel
- Material: Food-safe PLA or PETG
- Portion size: ~1/4 cup per rotation
- Paddle dimensions: 
  - Length: 50mm
  - Width: 20mm
  - Height: 15mm

## Environmental Considerations

1. **Operating Temperature**
   - Range: 0°C to 40°C
   - Optimal: 15°C to 25°C (alkaline AA batteries)

2. **Humidity**
   - Maximum: 80% (non-condensing)
   - Recommended: Below 60%

3. **Protection Requirements**
   - IP20 rating (touch-safe, not water-resistant)

## Assembly Tolerances

- Servo arm clearance: 2mm minimum
- Container sealing: 0.5mm gap maximum
- Button travel: 1.5mm ±0.5mm
- LCD viewing angle: 15° above horizontal

## Maintenance Access

1. **Battery Compartment**
   - Tool-free access
   - Secured with snap-fit or magnetic closure
   
2. **Food Container**
   - Removable for cleaning
   - Twist-lock mechanism recommended
   
3. **Electronics Enclosure**
   - Secured with 4x M3 screws
   - Separate from food compartment

## Safety Features

1. **Electrical**
   - Reverse polarity protection
   - Current limiting for servo
   - Fuse or PTC for overcurrent protection

2. **Mechanical**
   - Anti-jam detection (software)
   - Emergency manual feed option
   - No sharp edges (minimum 1mm radius)

## Future Improvement Considerations

1. **Power Optimization**
   - Solar charging option
   - More efficient voltage regulation
   - Backlight control

2. **Mechanical Upgrades**
   - Multiple food type support
   - Moisture control system
   - Enhanced portion control

3. **User Interface**
   - Feeding confirmation LED
   - Low battery indicator
   - Portion size adjustment