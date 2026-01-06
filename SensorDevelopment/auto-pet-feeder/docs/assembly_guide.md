# Detailed Assembly Instructions

## 1. Prepare the Tools

Required tools:
- Soldering iron and solder
- Wire strippers
- Small Phillips screwdriver
- Hot glue gun
- Drill with various bits (if modifying enclosure)
- Small pliers
- Multimeter (for testing)

## 2. Electronics Assembly

### 2.1 Power Supply Setup
1. Install batteries in the battery holder
2. Connect battery holder to voltage regulator:
   - Red wire to input positive
   - Black wire to input negative
3. Connect voltage regulator output:
   - Positive to Arduino VIN
   - Negative to Arduino GND

### 2.2 LCD Display
1. Solder header pins to LCD if needed
2. Connect LCD to Arduino:
   ```
   LCD Pin -> Arduino Pin
   RS -> D12
   EN -> D11
   D4 -> D5
   D5 -> D4
   D6 -> D3
   D7 -> D2
   VSS -> GND
   VDD -> 5V
   V0 -> 10K potentiometer middle pin
   ```
3. Connect potentiometer:
   - Left pin to GND
   - Right pin to 5V
   - Middle pin to LCD V0

### 2.3 Buttons
1. Mount buttons on the enclosure
2. Connect one terminal of each button to GND
3. Connect other terminals to Arduino:
   ```
   SET button -> D2
   UP button -> D3
   DOWN button -> D4
   ```

### 2.4 Servo Motor
1. Extend servo wires if needed
2. Connect servo:
   ```
   Red wire -> 5V
   Brown/Black wire -> GND
   Orange/Yellow wire -> D9
   ```

## 3. Mechanical Assembly

### 3.1 Food Container
1. Clean container thoroughly
2. Mark and cut opening for food dispensing:
   - Size: 40mm x 20mm
   - Position: 20mm from bottom
3. Sand edges smooth

### 3.2 Servo Mount
1. Position servo mount at 45° angle
2. Mark mounting holes
3. Drill pilot holes
4. Secure servo using provided screws
5. Test servo movement clearance

### 3.3 Dispensing Mechanism
1. Attach paddle wheel to servo arm
2. Verify free rotation
3. Adjust servo position if needed
4. Test manual rotation

## 4. Final Assembly

### 4.1 Electronics Housing
1. Mount Arduino in enclosure
2. Secure LCD in viewing window
3. Route wires neatly
4. Add strain relief where needed
5. Mount buttons in designated holes

### 4.2 Food Container Integration
1. Attach container to base
2. Verify alignment with servo
3. Test feed mechanism
4. Secure all components

### 4.3 Power System
1. Create battery compartment access
2. Install power switch if using
3. Secure all connections
4. Test voltage at key points

## 5. Testing and Calibration

### 5.1 Initial Power-Up
1. Install fresh batteries
2. Power on system
3. Verify LCD display
4. Test all buttons

### 5.2 Servo Calibration
1. Upload code
2. Test servo movement
3. Adjust FEED_AMOUNT if needed
4. Verify portion size

### 5.3 Schedule Setup
1. Set current time
2. Program test feeding times
3. Verify EEPROM saving
4. Test full feeding cycle

## 6. Troubleshooting

### 6.1 Display Issues
- Adjust contrast potentiometer
- Check all connections
- Verify power supply voltage

### 6.2 Servo Problems
- Check for binding
- Verify power supply
- Test with basic servo sketch

### 6.3 Button Issues
- Check soldered connections
- Verify pull-up resistors
- Test continuity with multimeter

## 7. Maintenance Access

### 7.1 Regular Access Points
1. Battery compartment
2. Food container
3. Dispensing mechanism

### 7.2 Service Points
1. Servo mounting screws
2. Electronics enclosure
3. Button access

## 8. Final Checks

### 8.1 Safety
- No exposed wires
- All sharp edges covered
- Stable mounting
- Proper ventilation

### 8.2 Functionality
- Reliable feeding
- Clear display
- Responsive buttons
- Proper portion size
- Schedule retention

### 8.3 Documentation
- Record any modifications
- Note calibration settings
- Document feeding schedule